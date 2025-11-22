# SenseVoice 微调工具集

本目录包含 SenseVoice 模型微调的完整工具链，已精简为最核心的脚本。

## 📁 目录结构

```
my-tool/
├── 1-data-preparation/      # 数据准备阶段
├── 2-training/              # 模型训练阶段
├── 3-model-evaluation/      # 模型评估与对比阶段
├── 4-model-export/          # 模型导出阶段
├── 5-optimization/          # 模型优化阶段
└── README.md               # 本文件
```

---

## 🔧 各阶段脚本说明

### 1️⃣ 数据准备阶段 (1-data-preparation)

**`generate_sensevoice_data_v2.py`**
- 从 Excel 文件生成 SenseVoice 训练数据
- 包含完整的数据验证和格式转换
- 自动生成 train/val 数据集
- 支持自定义分割比例

**使用方法:**
```bash
python my-tool/1-data-preparation/generate_sensevoice_data_v2.py \
  --excel_file "your_data.xlsx" \
  --audio_dir "./data/Audio" \
  --output_dir "./data/list"
```

---

### 2️⃣ 训练阶段 (2-training)

**`finetune_sensevoice_fixed.ps1`**
- SenseVoice 微调启动脚本（PowerShell）
- 已修复所有已知 bug
- 包含完整的训练参数配置
- 支持断点续训

**使用方法:**
```powershell
# 在 PowerShell 中执行
.\my-tool\2-training\finetune_sensevoice_fixed.ps1
```

---

### 3️⃣ 模型评估与对比阶段 (3-model-evaluation)

#### **`compare_models.py`**
对比微调模型与原始模型的性能差异

**功能:**
- 在验证集上测试两个模型
- 计算准确率、错误率
- 生成详细的对比报告（Markdown 格式）
- 标注差异样本

**使用方法:**
```bash
python my-tool/3-model-evaluation/compare_models.py \
  --original_model_dir "models/SenseVoiceSmall" \
  --finetuned_model_dir "exp_svs" \
  --val_data "./data/list/val_from_excel.jsonl" \
  --batch_size 10
```

#### **`view_checkpoint.py`**
查看训练 checkpoint 的详细信息

**功能:**
- 显示 checkpoint 中的所有键
- 查看模型参数维度
- 检查训练状态信息

**使用方法:**
```bash
python my-tool/3-model-evaluation/view_checkpoint.py \
  --checkpoint_path "exp_svs/model.pt"
```

#### **`generate_training_report.py`**
生成训练过程的详细报告

**功能:**
- 解析 TensorBoard 日志
- 生成损失曲线分析
- 统计训练指标
- 输出 Markdown 报告

**使用方法:**
```bash
python my-tool/3-model-evaluation/generate_training_report.py \
  --tensorboard_dir "exp_svs/tensorboard" \
  --output "training_report.md"
```

---

### 4️⃣ 模型导出阶段 (4-model-export)

#### **`export_to_onnx.py`**
将 PyTorch 模型导出为 ONNX 格式

**功能:**
- 导出完整精度 ONNX 模型
- 导出量化 ONNX 模型
- 自动生成必需的配置文件
- 复制 tokens.txt 等依赖文件

**使用方法:**
```bash
python my-tool/4-model-export/export_to_onnx.py \
  --model_dir "exp_svs" \
  --output_dir "exp_svs_onnx"
```

#### **`check_onnx_metadata.py`**
检查 ONNX 模型的元数据

**功能:**
- 验证 ONNX 模型是否有效
- 显示所有元数据键值对
- 检查必需的配置项
- 验证模型完整性

**使用方法:**
```bash
python my-tool/4-model-export/check_onnx_metadata.py \
  --model_path "exp_svs_onnx/model.onnx"
```

#### **`compare_onnx_models.py`**
对比 ONNX 完整精度模型与量化模型

**功能:**
- 在验证集上测试两个 ONNX 模型
- 对比准确率差异
- 分析识别结果差异
- 生成详细对比报告

**使用方法:**
```bash
python my-tool/4-model-export/compare_onnx_models.py \
  --onnx_model_dir "exp_svs_onnx" \
  --val_data "./data/list/val_from_excel.jsonl" \
  --batch_size 10
```

---

### 5️⃣ 优化阶段 (5-optimization)

#### **`generate_hotwords.py`**
从训练数据生成热词文件

**功能:**
- 提取高频词汇和短语
- 使用 jieba 分词统计
- 根据频率计算权重
- 分析错误模式加权
- 生成标准格式热词文件

**使用方法:**
```bash
python my-tool/5-optimization/generate_hotwords.py \
  --train_data "./data/list/train_from_excel.jsonl" \
  --val_data "./data/list/val_from_excel.jsonl" \
  --output "exp_svs_onnx/hotwords.txt" \
  --top_k 100 \
  --comparison_report "onnx_comparison_xxx.md"
```

---

## 🚀 完整工作流程

### 步骤 1: 准备数据
```bash
python my-tool/1-data-preparation/generate_sensevoice_data_v2.py \
  --excel_file "data.xlsx" \
  --audio_dir "./data/Audio" \
  --output_dir "./data/list"
```

### 步骤 2: 开始训练
```powershell
.\my-tool\2-training\finetune_sensevoice_fixed.ps1
```

### 步骤 3: 评估模型
```bash
# 对比原始模型与微调模型
python my-tool/3-model-evaluation/compare_models.py \
  --original_model_dir "models/SenseVoiceSmall" \
  --finetuned_model_dir "exp_svs" \
  --val_data "./data/list/val_from_excel.jsonl"

# 生成训练报告
python my-tool/3-model-evaluation/generate_training_report.py \
  --tensorboard_dir "exp_svs/tensorboard"
```

### 步骤 4: 导出 ONNX
```bash
# 导出模型
python my-tool/4-model-export/export_to_onnx.py \
  --model_dir "exp_svs" \
  --output_dir "exp_svs_onnx"

# 检查元数据
python my-tool/4-model-export/check_onnx_metadata.py \
  --model_path "exp_svs_onnx/model.onnx"

# 对比完整精度与量化模型
python my-tool/4-model-export/compare_onnx_models.py \
  --onnx_model_dir "exp_svs_onnx" \
  --val_data "./data/list/val_from_excel.jsonl"
```

### 步骤 5: 生成热词（可选）
```bash
python my-tool/5-optimization/generate_hotwords.py \
  --train_data "./data/list/train_from_excel.jsonl" \
  --val_data "./data/list/val_from_excel.jsonl" \
  --output "exp_svs_onnx/hotwords.txt"
```

---

## 📊 脚本统计

| 阶段 | 脚本数量 | 说明 |
|------|---------|------|
| 数据准备 | 1 | 完整无 bug 的数据处理流程 |
| 训练 | 1 | 修复所有已知问题的训练脚本 |
| 评估 | 3 | 模型对比、checkpoint 查看、报告生成 |
| 导出 | 3 | ONNX 导出、元数据检查、模型对比 |
| 优化 | 1 | 热词生成工具 |
| **总计** | **9** | 精简后的核心工具集 |

---

## ⚠️ 注意事项

1. **依赖环境**: 所有脚本需要在 FunASR 虚拟环境中运行
   ```bash
   .venv\Scripts\Activate.ps1  # Windows
   ```

2. **路径配置**: 脚本中的路径均为相对于项目根目录，请在项目根目录执行

3. **数据格式**: 确保 Excel 数据包含 `file_name` 和 `text` 列

4. **模型版本**: 适用于 SenseVoiceSmall 模型

---

## 📝 更新日志

- **2025-11-21**: 精简脚本，从 31 个减少到 9 个核心工具
- **2025-11-19**: 添加热词生成工具
- **2025-11-18**: 完成 ONNX 导出和对比功能
- **2025-11-17**: 修复所有数据处理和训练 bug

---

## 🔗 相关文档

- `FINETUNE_GUIDE.md` - 微调详细指南
- `FINETUNE_SENSEVOICE.md` - SenseVoice 微调说明
- `BATCHSIZE_GUIDE.md` - Batch Size 配置指南

---

**维护者**: AI Assistant  
**最后更新**: 2025年11月21日
