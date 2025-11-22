# Copyright FunASR - Windows PowerShell 微调脚本（修复 Windows 兼容性问题）
# 基于官方 finetune.sh，适配 Windows 环境

param(
    # 训练和验证数据（相对于项目根目录）
    [string]$TrainData = "data\list\train_from_excel.jsonl",
    [string]$ValData = "data\list\val_from_excel.jsonl",
    
    # 模型路径（本地目录）
    [string]$ModelDir = "models\SenseVoiceSmall",
    
    # 输出目录
    [string]$OutputDir = "exp_svs",
    
    # GPU 设置
    [string]$CudaDevices = "0",
    
    # 训练配置
    [int]$BatchSize = 5000,        # token-based batch size (RTX 3080 12GB 限制)
    [string]$BatchType = "token",  # "token" or "example"
    [int]$SortSize = 1024,
    [int]$NumWorkers = 0,          # Windows 建议设为 0
    [int]$MaxEpoch = 100,
    [int]$LogInterval = 1,
    [int]$ValidateInterval = 100,
    [int]$SaveInterval = 100,
    [int]$KeepNbest = 3,
    [int]$AvgNbest = 3,
    [double]$LearningRate = 2e-5,  # 实际由 config.yaml 控制 (2e-5)
    [int]$WarmupSteps = 50,           # 小数据集降低 warmup steps (原 25000)
    
    # 可选：使用多 GPU 训练（需要 torchrun）
    [switch]$UseDistributed = $false
)

$ErrorActionPreference = "Stop"

Write-Host "=== SenseVoice Fine-tuning ===" -ForegroundColor Cyan

# 0. 获取项目根目录（脚本在 my-tool/2-training/ 下，向上两级）
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = (Get-Item (Join-Path $ScriptDir "..\..")).FullName
Write-Host "Project root: $ProjectRoot" -ForegroundColor Cyan

# 将相对路径转换为绝对路径
$VenvPath = Join-Path $ProjectRoot ".venv\Scripts\Activate.ps1"
$TrainDataPath = Join-Path $ProjectRoot $TrainData.TrimStart(".\")
$ValDataPath = Join-Path $ProjectRoot $ValData.TrimStart(".\")
$ModelDirPath = Join-Path $ProjectRoot $ModelDir.TrimStart(".\")
$OutputDirPath = Join-Path $ProjectRoot $OutputDir.TrimStart(".\")
$TrainScriptPath = Join-Path $ProjectRoot "funasr\bin\train_ds.py"

# 1. Activate virtual environment
if (Test-Path $VenvPath) {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & $VenvPath
} else {
    Write-Warning "Virtual environment not found at $VenvPath, ensure PyTorch with CUDA is installed"
}

# 2. Check data files
Write-Host "Checking data files..." -ForegroundColor Yellow
if (-not (Test-Path $TrainDataPath)) {
    Write-Error "Training data not found: $TrainDataPath"
}
if (-not (Test-Path $ValDataPath)) {
    Write-Error "Validation data not found: $ValDataPath"
}
Write-Host "Data files OK" -ForegroundColor Green

# 3. Check model directory
Write-Host "Checking model directory..." -ForegroundColor Yellow
if (-not (Test-Path $ModelDirPath)) {
    Write-Error "Model directory not found: $ModelDirPath"
}
Write-Host "Model directory: $ModelDirPath" -ForegroundColor Green

# 4. Create output directory
New-Item -ItemType Directory -Force -Path $OutputDirPath | Out-Null
Write-Host "Output directory: $OutputDirPath" -ForegroundColor Green

# 5. Setup CUDA environment
$env:CUDA_VISIBLE_DEVICES = $CudaDevices
Write-Host "CUDA devices: $CudaDevices" -ForegroundColor Green

# 6. Build training arguments
$train_args = @(
    "++model=$ModelDirPath",
    "++train_data_set_list=$TrainDataPath",
    "++valid_data_set_list=$ValDataPath",
    "++dataset_conf.data_split_num=1",
    "++dataset_conf.batch_sampler=BatchSampler",
    "++dataset_conf.batch_size=$BatchSize",
    "++dataset_conf.sort_size=$SortSize",
    "++dataset_conf.batch_type=$BatchType",
    "++dataset_conf.num_workers=$NumWorkers",
    "++dataset_conf.max_source_length=500",    # 最大 source_len=355，留余量设为 500
    "++dataset_conf.max_token_length=500",     # 同上
    "++train_conf.max_epoch=$MaxEpoch",
    "++train_conf.log_interval=$LogInterval",
    "++train_conf.resume=true",
    "++train_conf.validate_interval=$ValidateInterval",
    "++train_conf.save_checkpoint_interval=$SaveInterval",
    "++train_conf.keep_nbest_models=$KeepNbest",
    "++train_conf.avg_nbest_model=$AvgNbest",
    "++optim_conf.lr=$LearningRate",
    "++scheduler_conf.warmup_steps=$WarmupSteps",
    "++device=cuda",
    "++output_dir=$OutputDirPath"
)

# 7. Start TensorBoard before training
$tensorboard_dir = Join-Path $OutputDirPath "tensorboard"
Write-Host "`nStarting TensorBoard..." -ForegroundColor Cyan
Write-Host "TensorBoard directory: $tensorboard_dir" -ForegroundColor Gray
Write-Host "TensorBoard UI: http://localhost:6006" -ForegroundColor Yellow

# Create tensorboard directory if not exists
New-Item -ItemType Directory -Force -Path $tensorboard_dir | Out-Null

# Start TensorBoard in background
$tensorboard_process = Start-Process powershell -ArgumentList "-NoExit", "-Command", "tensorboard --logdir `"$tensorboard_dir`" --port 6006" -PassThru -WindowStyle Minimized

# Wait for TensorBoard to start
Start-Sleep -Seconds 3

# Open browser
Start-Process "http://localhost:6006"

Write-Host "TensorBoard started (PID: $($tensorboard_process.Id))" -ForegroundColor Green

# 8. Start training
Write-Host "`nStarting training..." -ForegroundColor Green
Write-Host "Training script: $TrainScriptPath" -ForegroundColor Gray

if ($UseDistributed) {
    # Use torchrun for distributed training
    Write-Host "Mode: Distributed training (torchrun)" -ForegroundColor Cyan
    
    # Set USE_LIBUV=0 for Windows
    $env:USE_LIBUV = "0"
    
    $gpu_num = ($CudaDevices -split ",").Count
    $dist_args = @(
        "--nnodes", "1",
        "--nproc_per_node", "$gpu_num",
        "--master_addr", "127.0.0.1",
        "--master_port", "26669",
        $TrainScriptPath
    ) + $train_args
    
    Write-Host "Command: torchrun $($dist_args -join ' ')`n" -ForegroundColor Gray
    & torchrun @dist_args
    
} else {
    # Use python directly (single GPU, avoids Windows torchrun issues)
    Write-Host "Mode: Single GPU training (python)" -ForegroundColor Cyan
    
    $py_args = @($TrainScriptPath) + $train_args
    
    Write-Host "Command: python $($py_args -join ' ')`n" -ForegroundColor Gray
    & python @py_args
}

# 9. Clean up intermediate checkpoints (keep only last N and best)
Write-Host "`nCleaning up intermediate checkpoints..." -ForegroundColor Cyan

# Get all epoch checkpoint files (excluding model.pt and model.pt.best)
$all_checkpoints = Get-ChildItem -Path $OutputDirPath -Filter "model.pt.ep*" | Sort-Object Name

if ($all_checkpoints.Count -gt $KeepNbest) {
    Write-Host "Found $($all_checkpoints.Count) epoch checkpoints, keeping last $KeepNbest" -ForegroundColor Yellow
    
    # Keep only the last N checkpoints
    $to_delete = $all_checkpoints | Select-Object -First ($all_checkpoints.Count - $KeepNbest)
    
    foreach ($file in $to_delete) {
        Write-Host "  Deleting: $($file.Name) ($(([math]::Round($file.Length/1GB, 2))) GB)" -ForegroundColor Gray
        Remove-Item -Path $file.FullName -Force
    }
    
    $freed_space = ($to_delete | Measure-Object -Property Length -Sum).Sum / 1GB
    Write-Host "Freed up $([math]::Round($freed_space, 2)) GB of disk space" -ForegroundColor Green
} else {
    Write-Host "Only $($all_checkpoints.Count) checkpoints found, no cleanup needed" -ForegroundColor Green
}

# 10. Check training results
if ($LASTEXITCODE -eq 0) {
    Write-Host "`nTraining completed successfully!" -ForegroundColor Green
    Write-Host "Output directory: $OutputDirPath" -ForegroundColor Cyan
    
    # Show remaining checkpoints
    $remaining = Get-ChildItem -Path $OutputDirPath -Filter "model.pt*" | Sort-Object Name
    Write-Host "`nFinal checkpoints:" -ForegroundColor Cyan
    foreach ($file in $remaining) {
        $size_gb = [math]::Round($file.Length/1GB, 2)
        Write-Host "  $($file.Name) - $size_gb GB" -ForegroundColor White
    }
    
    Write-Host "`nTensorBoard is still running at: http://localhost:6006" -ForegroundColor Yellow
    Write-Host "Close the TensorBoard window when done" -ForegroundColor Gray
} else {
    Write-Host "`nTraining exited with code: $LASTEXITCODE" -ForegroundColor Red
    Write-Host "Please check logs in output directory: $OutputDirPath" -ForegroundColor Yellow
    Write-Host "`nTensorBoard is still running at: http://localhost:6006" -ForegroundColor Yellow
}

Write-Host "`nTo stop TensorBoard, close its window or run:" -ForegroundColor Cyan
Write-Host "  Stop-Process -Id $($tensorboard_process.Id)" -ForegroundColor Gray
