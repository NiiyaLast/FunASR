"""
生成 SenseVoice 训练报告

功能：
1. 分析训练配置和检查点
2. 统计训练数据集信息
3. 检查 TensorBoard 日志
4. 生成带时间戳的训练报告

依赖：pip install pyyaml
"""

import os
import json
import yaml
from pathlib import Path
from datetime import datetime


def get_file_size_mb(file_path):
    """获取文件大小（MB）"""
    if os.path.exists(file_path):
        return os.path.getsize(file_path) / (1024 * 1024)
    return 0


def analyze_checkpoints(output_dir):
    """分析模型检查点"""
    checkpoints = []
    for file in Path(output_dir).glob("model.pt*"):
        checkpoints.append({
            'name': file.name,
            'size_mb': round(get_file_size_mb(file), 2),
            'modified': datetime.fromtimestamp(file.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        })
    
    # 按修改时间排序
    checkpoints.sort(key=lambda x: x['modified'], reverse=True)
    return checkpoints


def count_samples(jsonl_path):
    """统计 JSONL 文件样本数"""
    try:
        with open(jsonl_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
            return len(lines)
    except FileNotFoundError:
        return 0


def analyze_data_distribution(jsonl_path, sample_limit=5):
    """分析数据分布"""
    try:
        with open(jsonl_path, 'r', encoding='utf-8') as f:
            samples = []
            for line in f:
                line = line.strip()
                if line:
                    try:
                        data = json.loads(line)
                        samples.append({
                            'key': data.get('key', 'N/A'),
                            'target_len': data.get('target_len', 0),
                            'target': data.get('target', '')[:50]  # 前50字符
                        })
                    except json.JSONDecodeError:
                        continue
            
            if samples:
                avg_len = sum(s['target_len'] for s in samples) / len(samples)
                return {
                    'total': len(samples),
                    'avg_target_len': round(avg_len, 2),
                    'samples': samples[:sample_limit]
                }
    except FileNotFoundError:
        pass
    
    return {'total': 0, 'avg_target_len': 0, 'samples': []}


def load_config(config_path):
    """加载训练配置"""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return {}


def generate_report(output_dir="../../exp_svs", train_data="../../data/list/train_from_excel.jsonl", 
                   val_data="../../data/list/val_from_excel.jsonl"):
    """生成训练报告"""
    
    # 生成报告文件名（时间戳，输出到项目根目录）
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = f"../../training_report_{timestamp}.md"
    
    # 收集信息
    config = load_config(os.path.join(output_dir, "config.yaml"))
    checkpoints = analyze_checkpoints(output_dir)
    train_info = analyze_data_distribution(train_data)
    val_info = analyze_data_distribution(val_data)
    
    # 生成报告内容
    report = f"""# SenseVoice 训练报告

**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 训练概览

### 数据集统计

| 类型 | 样本数 | 平均文本长度 |
|------|--------|--------------|
| 训练集 | {train_info['total']} | {train_info['avg_target_len']} 字符 |
| 验证集 | {val_info['total']} | {val_info['avg_target_len']} 字符 |
| **总计** | **{train_info['total'] + val_info['total']}** | - |

### 训练配置

"""
    
    # 添加训练配置
    if config:
        train_conf = config.get('train_conf', {})
        dataset_conf = config.get('dataset_conf', {})
        optim_conf = config.get('optim_conf', {})
        
        report += f"""| 参数 | 值 |
|------|-----|
| 最大轮数 (max_epoch) | {train_conf.get('max_epoch', 'N/A')} |
| 批次大小 (batch_size) | {dataset_conf.get('batch_size', 'N/A')} |
| 批次类型 (batch_type) | {dataset_conf.get('batch_type', 'N/A')} |
| 学习率 (lr) | {optim_conf.get('lr', 'N/A')} |
| 优化器 | {config.get('optim', 'N/A')} |
| 调度器 | {config.get('scheduler', 'N/A')} |
| 验证间隔 | {train_conf.get('validate_interval', 'N/A')} 步 |
| 保存间隔 | {train_conf.get('save_checkpoint_interval', 'N/A')} 步 |
| 保留最佳模型数 | {train_conf.get('keep_nbest_models', 'N/A')} |

"""
    
    # 模型检查点
    report += f"""---

## 🎯 模型检查点

共 {len(checkpoints)} 个检查点文件：

| 文件名 | 大小 (MB) | 修改时间 |
|--------|-----------|----------|
"""
    
    for ckpt in checkpoints[:15]:  # 只显示前15个
        report += f"| {ckpt['name']} | {ckpt['size_mb']} | {ckpt['modified']} |\n"
    
    if len(checkpoints) > 15:
        report += f"\n*...还有 {len(checkpoints) - 15} 个检查点未显示*\n"
    
    # 训练样本示例
    if train_info['samples']:
        report += f"""
---

## 📝 训练数据样例

前 {len(train_info['samples'])} 个训练样本：

| 编号 | Key | 文本长度 | 文本内容 |
|------|-----|----------|----------|
"""
        for i, sample in enumerate(train_info['samples'], 1):
            report += f"| {i} | {sample['key']} | {sample['target_len']} | {sample['target'][:40]}... |\n"
    
    # 问题诊断
    report += """
---

## ⚠️ 训练诊断

### 潜在问题

"""
    
    issues = []
    
    # 检查数据量
    if train_info['total'] < 100:
        issues.append("- ⚠️ **训练样本过少** - 仅 {} 个样本，建议至少 1000+ 样本以获得更好效果".format(train_info['total']))
    
    # 检查检查点更新
    if checkpoints:
        latest_time = datetime.strptime(checkpoints[0]['modified'], '%Y-%m-%d %H:%M:%S')
        time_diff = datetime.now() - latest_time
        if time_diff.total_seconds() > 3600:  # 超过1小时
            issues.append(f"- ⚠️ **检查点未更新** - 最新检查点于 {checkpoints[0]['modified']} 生成（{round(time_diff.total_seconds()/3600, 1)} 小时前）")
    
    # 检查模型大小变化
    if len(checkpoints) >= 2:
        size_diff = abs(checkpoints[0]['size_mb'] - checkpoints[1]['size_mb'])
        if size_diff < 1:  # 大小几乎无变化
            issues.append("- ⚠️ **模型大小无明显变化** - 可能训练未真正进行或已收敛")
    
    if not issues:
        report += "✅ 未发现明显问题\n"
    else:
        report += "\n".join(issues) + "\n"
    
    # 建议
    report += """
### 改进建议

1. **数据质量**
   - 确保音频文件存在且可访问
   - 检查文本标注的准确性
   - 验证数据编码格式（UTF-8）

2. **训练参数**
   - 样本数较少时，降低 batch_size（如 2000-3000）
   - 增加训练轮数（max_epoch 20-50）
   - 调整学习率（0.0001-0.0002）

3. **监控训练**
   - 使用 TensorBoard 查看 loss 曲线：`.\start_tensorboard.ps1`
   - 检查 GPU 利用率是否正常
   - 观察验证集指标变化

4. **数据增强**
   - 收集更多训练数据
   - 使用数据增强技术（如语速变化、噪声添加）
   - 确保训练集和验证集分布一致

---

## 📁 文件位置

- **输出目录**: `{output_dir}`
- **训练数据**: `{train_data}`
- **验证数据**: `{val_data}`
- **配置文件**: `{os.path.join(output_dir, 'config.yaml')}`
- **TensorBoard**: `{os.path.join(output_dir, 'tensorboard')}`

---

## 🔗 相关命令

```powershell
# 查看 TensorBoard
.\start_tensorboard.ps1

# 继续训练
.\finetune_sensevoice_fixed.ps1 -MaxEpoch 20

# 清除旧检查点重新训练
Remove-Item {output_dir}\model.pt* -Force
.\finetune_sensevoice_fixed.ps1
```

---

*报告生成于: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    # 写入报告
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ 训练报告已生成: {report_path}")
    print(f"📊 训练样本: {train_info['total']} | 验证样本: {val_info['total']}")
    print(f"📁 检查点文件: {len(checkpoints)} 个")
    
    return report_path


if __name__ == "__main__":
    generate_report()
