"""检查ONNX模型的元数据"""
import onnx
import sys
from pathlib import Path

# 默认模型路径（相对于项目根目录）
default_model_path = '../../exp_svs_onnx/model_quant.onnx'

# 支持命令行参数
model_path = sys.argv[1] if len(sys.argv) > 1 else default_model_path

if not Path(model_path).exists():
    print(f"错误: 模型文件不存在 - {model_path}")
    sys.exit(1)

model = onnx.load(model_path)
print(f'模型路径: {model_path}')
print(f'元数据数量: {len(model.metadata_props)}')
print('\n元数据列表:')
for m in model.metadata_props:
    if len(m.value) > 100:
        print(f'  {m.key}: {m.value[:50]}... (长度: {len(m.value)})')
    else:
        print(f'  {m.key}: {m.value}')
