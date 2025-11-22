"""
SenseVoice 微调模型导出为 ONNX 格式

功能：
1. 加载微调后的模型 (model.pt.best)
2. 从模型权重中自动检测 vocab_size
3. 导出为 ONNX 格式
4. 在 ONNX 模型元数据中添加 vocab_size
5. 测试导出的 ONNX 模型推理

依赖：pip install -U funasr funasr-onnx pyyaml torch onnx
"""

import os
import glob
import yaml
import torch
from pathlib import Path
from funasr import AutoModel


def export_finetuned_model_to_onnx(
    finetuned_model_dir="../../exp_svs",
    output_dir="../../exp_svs_onnx",
    base_model="iic/SenseVoiceSmall",
    batch_size=10,
    quantize=True
):
    """
    将微调后的 SenseVoice 模型导出为 ONNX 格式
    
    Args:
        finetuned_model_dir: 微调模型目录 (包含 model.pt.best)
        output_dir: ONNX 模型输出目录
        base_model: 基础模型名称或路径
        batch_size: 导出时的批处理大小
        quantize: 是否量化模型
    """
    print("=" * 60)
    print("SenseVoice 微调模型导出为 ONNX 格式")
    print("=" * 60)
    
    # 1. 查找微调后的 checkpoint
    finetuned_model_dir = Path(finetuned_model_dir)
    checkpoint_path = finetuned_model_dir / "model.pt.best"
    
    if not checkpoint_path.exists():
        print(f"⚠️  未找到 model.pt.best，尝试查找最新的 checkpoint...")
        checkpoints = sorted(glob.glob(str(finetuned_model_dir / "model.pt.ep*")))
        if not checkpoints:
            raise FileNotFoundError(f"在 {finetuned_model_dir} 中未找到任何 checkpoint 文件")
        checkpoint_path = Path(checkpoints[-1])
        print(f"✓ 找到 checkpoint: {checkpoint_path.name}")
    else:
        print(f"✓ 找到 model.pt.best")
    
    # 2. 准备输出目录
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n输出目录: {output_dir}")
    
    # 3. 复制微调模型到输出目录
    # ONNX 导出需要完整的模型目录结构
    import shutil
    
    # 复制 config 文件
    base_model_path = Path.home() / ".cache/modelscope/hub" / base_model
    if not base_model_path.exists():
        # 尝试从本地模型目录
        base_model_path = Path("./models/SenseVoiceSmall")
    
    if not base_model_path.exists():
        raise FileNotFoundError(f"未找到基础模型: {base_model_path}")
    
    print(f"\n复制配置文件从: {base_model_path}")
    
    # 复制必要的配置文件和模型文件
    config_files = [
        "config.yaml",
        "configuration.json",
        "am.mvn",
        "chn_jpn_yue_eng_ko_spectok.bpe.model"  # 分词模型文件
    ]
    for config_file in config_files:
        src = base_model_path / config_file
        dst = output_dir / config_file
        if src.exists():
            shutil.copy2(src, dst)
            print(f"  ✓ 复制: {config_file}")
        else:
            print(f"  ⚠️  未找到: {config_file}")
    
    # 复制微调后的模型权重
    shutil.copy2(checkpoint_path, output_dir / "model.pt")
    print(f"  ✓ 复制: {checkpoint_path.name} -> model.pt")
    
    # 4. 生成 tokens.txt 文件 (sherpa-onnx 需要)
    print(f"\n生成 tokens.txt...")
    try:
        import sentencepiece as spm
        bpe_model_path = output_dir / "chn_jpn_yue_eng_ko_spectok.bpe.model"
        if bpe_model_path.exists():
            sp = spm.SentencePieceProcessor()
            sp.load(str(bpe_model_path))
            
            tokens_file = output_dir / "tokens.txt"
            with open(tokens_file, 'w', encoding='utf-8') as f:
                for i in range(sp.vocab_size()):
                    token = sp.id_to_piece(i)
                    f.write(f"{token} {i}\n")
            
            print(f"  ✓ 生成 tokens.txt ({sp.vocab_size()} tokens)")
            print(f"     前5个: {[sp.id_to_piece(i) for i in range(5)]}")
            print(f"     后5个: {[sp.id_to_piece(i) for i in range(sp.vocab_size()-5, sp.vocab_size())]}")
        else:
            print(f"  ⚠️  未找到 BPE 模型文件，跳过 tokens.txt 生成")
    except ImportError:
        print(f"  ⚠️  sentencepiece 未安装，跳过 tokens.txt 生成")
        print(f"     建议运行: pip install sentencepiece")
    except Exception as e:
        print(f"  ⚠️  生成 tokens.txt 失败: {e}")
    
    # 5. 从训练好的模型中读取 vocab_size
    print(f"\n读取模型信息...")
    import torch
    
    # 加载 checkpoint
    checkpoint = torch.load(checkpoint_path, map_location='cpu')
    
    # 从模型状态中获取 vocab_size
    vocab_size = None
    
    # 方法1: 从 model 字典中的权重获取
    if 'model' in checkpoint:
        model_state = checkpoint['model']
        # 打印所有包含 output 或 embed 的键
        relevant_keys = [k for k in model_state.keys() if 'output' in k.lower() or 'embed' in k.lower()]
        print(f"  检测到的相关层: {relevant_keys[:5]}...")  # 显示前5个
        
        # SenseVoice 的输出层
        for key in model_state.keys():
            if 'decoder.output_layer.weight' in key or 'decoder.embed.weight' in key:
                vocab_size = model_state[key].shape[0]
                print(f"  ✓ 从模型权重中检测到 vocab_size: {vocab_size} (来自 {key})")
                break
    
    # 方法2: 尝试其他可能的键名
    if vocab_size is None and 'model' in checkpoint:
        for key in model_state.keys():
            # 查找任何输出层或嵌入层
            if key.endswith('.weight') and ('output' in key or 'embed' in key):
                shape = model_state[key].shape
                if len(shape) == 2 and shape[0] > 1000:  # 词表通常很大
                    vocab_size = shape[0]
                    print(f"  ✓ 从模型权重推断 vocab_size: {vocab_size} (来自 {key}, shape={shape})")
                    break
    
    # 方法3: 从训练配置中获取
    train_config_path = finetuned_model_dir / "config.yaml"
    if train_config_path.exists() and vocab_size is None:
        with open(train_config_path, 'r', encoding='utf-8') as f:
            train_config = yaml.safe_load(f)
            if 'model_conf' in train_config and 'vocab_size' in train_config['model_conf']:
                vocab_size = train_config['model_conf']['vocab_size']
                print(f"  ✓ 从训练配置中读取 vocab_size: {vocab_size}")
    
    # 如果还是没有找到，使用默认值
    if vocab_size is None:
        vocab_size = 25055  # SenseVoiceSmall 默认词表大小
        print(f"  ⚠️  未能自动检测 vocab_size，使用默认值: {vocab_size}")
    
    # 更新 config.yaml
    config_path = output_dir / "config.yaml"
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    # 添加 vocab_size
    if 'model_conf' not in config:
        config['model_conf'] = {}
    config['model_conf']['vocab_size'] = vocab_size
    
    # 写回配置文件
    with open(config_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, allow_unicode=True, default_flow_style=False)
    
    print(f"  ✓ 更新 config.yaml，设置 vocab_size: {vocab_size}")
    
    # 清理 checkpoint 占用的内存
    del checkpoint
    if 'model_state' in locals():
        del model_state
    torch.cuda.empty_cache() if torch.cuda.is_available() else None
    
    # 4. 导出为 ONNX
    print(f"\n开始导出 ONNX 模型...")
    print(f"  batch_size: {batch_size}")
    print(f"  quantize: {quantize}")
    
    try:
        from funasr_onnx import SenseVoiceSmall
        
        # 加载并导出
        model = SenseVoiceSmall(
            str(output_dir),
            batch_size=batch_size,
            quantize=quantize
        )
        
        print(f"\n✓ ONNX 模型导出成功!")
        print(f"  输出目录: {output_dir}")
        
        # 4.5. 修改 ONNX 模型元数据,添加必要的参数
        print(f"\n添加 ONNX 模型元数据...")
        try:
            import onnx
            
            # 从 config.yaml 读取所有需要的参数
            with open(output_dir / "config.yaml", 'r', encoding='utf-8') as f:
                config_data = yaml.safe_load(f)
            
            # 提取参数
            frontend_conf = config_data.get('frontend_conf', {})
            model_conf = config_data.get('model_conf', {})
            
            # 读取 CMVN 参数 (am.mvn 是文本格式)
            cmvn_file = output_dir / "am.mvn"
            neg_mean = []
            inv_stddev = []
            if cmvn_file.exists():
                with open(cmvn_file, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                means_list = []
                vars_list = []
                for i in range(len(lines)):
                    line_item = lines[i].split()
                    if line_item[0] == "<AddShift>":
                        line_item = lines[i + 1].split()
                        if line_item[0] == "<LearnRateCoef>":
                            add_shift_line = line_item[3 : (len(line_item) - 1)]
                            means_list = list(add_shift_line)
                            continue
                    elif line_item[0] == "<Rescale>":
                        line_item = lines[i + 1].split()
                        if line_item[0] == "<LearnRateCoef>":
                            rescale_line = line_item[3 : (len(line_item) - 1)]
                            vars_list = list(rescale_line)
                            continue
                
                if means_list and vars_list:
                    means = [float(x) for x in means_list]
                    vars = [float(x) for x in vars_list]
                    neg_mean = [-m for m in means]
                    inv_stddev = [1.0 / (v ** 0.5) for v in vars]
            
            # 准备元数据字典 (参考 sherpa-onnx 源码和官方导出脚本)
            # 参考: https://github.com/k2-fsa/sherpa-onnx/blob/master/scripts/sense-voice/export-onnx.py
            metadata = {
                # 必需的基本参数
                'vocab_size': str(vocab_size),
                'lfr_window_size': str(frontend_conf.get('lfr_m', 7)),
                'lfr_window_shift': str(frontend_conf.get('lfr_n', 6)),
                'normalize_samples': '0',  # 0: 输入范围 [-32768, 32767]
                
                # ITN 相关
                'with_itn': '14',
                'without_itn': '15',
                
                # 语言ID (SenseVoice 官方默认值)
                # 参考: model.lid_dict 的默认值
                'lang_auto': '0',      # auto
                'lang_zh': '3',        # Chinese
                'lang_en': '4',        # English
                'lang_yue': '7',       # Cantonese (粤语)
                'lang_ja': '11',       # Japanese
                'lang_ko': '12',       # Korean
                'lang_nospeech': '13', # No speech (静音/背景噪音)
                
                # CMVN 参数 (如果有)
                'neg_mean': ','.join(map(str, neg_mean)) if neg_mean else '',
                'inv_stddev': ','.join(map(str, inv_stddev)) if inv_stddev else '',
                
                # 模型类型和版本
                'model_type': 'sense_voice_ctc',
                'version': '2',  # version 2: Use QUInt8
                'model_author': 'iic',
                'maintainer': 'k2-fsa',
                'url': 'https://huggingface.co/FunAudioLLM/SenseVoiceSmall',
            }
            
            print(f"  元数据:")
            for key, value in metadata.items():
                print(f"    {key}: {value}")
            
            # 加载并修改 ONNX 模型
            onnx_model_path = output_dir / "model.onnx"
            if onnx_model_path.exists():
                onnx_model = onnx.load(str(onnx_model_path))
                
                # 添加所有元数据
                for key, value in metadata.items():
                    meta = onnx_model.metadata_props.add()
                    meta.key = key
                    meta.value = value
                
                # 保存修改后的模型
                onnx.save(onnx_model, str(onnx_model_path))
                print(f"  ✓ 已添加元数据到 model.onnx")
                
                # 如果有量化模型，也添加元数据
                onnx_quant_path = output_dir / "model_quant.onnx"
                if onnx_quant_path.exists():
                    onnx_quant = onnx.load(str(onnx_quant_path))
                    for key, value in metadata.items():
                        meta_quant = onnx_quant.metadata_props.add()
                        meta_quant.key = key
                        meta_quant.value = value
                    onnx.save(onnx_quant, str(onnx_quant_path))
                    print(f"  ✓ 已添加元数据到 model_quant.onnx")
            else:
                print(f"  ⚠️  未找到 model.onnx，跳过元数据添加")
                
        except ImportError:
            print(f"  ⚠️  onnx 包未安装，跳过元数据添加")
            print(f"     建议运行: pip install onnx")
        except Exception as e:
            print(f"  ⚠️  添加元数据失败: {e}")
            import traceback
            traceback.print_exc()
        
        # 列出导出的文件
        print(f"\n导出的文件:")
        for file in sorted(output_dir.iterdir()):
            if file.is_file():
                size_mb = file.stat().st_size / 1024 / 1024
                print(f"  - {file.name} ({size_mb:.2f} MB)")
        
        return str(output_dir), model
        
    except ImportError:
        print("\n❌ 错误: funasr-onnx 未安装")
        print("请运行: pip install -U funasr-onnx")
        raise
    except Exception as e:
        print(f"\n❌ 导出失败: {e}")
        import traceback
        traceback.print_exc()
        raise


def test_onnx_model(
    onnx_model_dir,
    test_audio_path=None
):
    """
    测试导出的 ONNX 模型
    
    Args:
        onnx_model_dir: ONNX 模型目录
        test_audio_path: 测试音频文件路径
    """
    print("\n" + "=" * 60)
    print("测试 ONNX 模型推理")
    print("=" * 60)
    
    from funasr_onnx import SenseVoiceSmall
    from funasr_onnx.utils.postprocess_utils import rich_transcription_postprocess
    
    # 加载 ONNX 模型
    model = SenseVoiceSmall(onnx_model_dir, batch_size=10, quantize=True)
    print(f"✓ ONNX 模型加载成功: {onnx_model_dir}")
    
    # 准备测试音频
    if test_audio_path is None:
        # 使用验证集中的第一个音频
        import json
        val_jsonl = Path("./data/list/val_from_excel.jsonl")
        if val_jsonl.exists():
            with open(val_jsonl, 'r', encoding='utf-8') as f:
                first_line = f.readline()
                data = json.loads(first_line)
                test_audio_path = data['source']
                ground_truth = data['target']
                print(f"\n测试音频: {Path(test_audio_path).name}")
                print(f"真实文本: {ground_truth}")
        else:
            print("⚠️  未找到验证集文件，跳过测试")
            return
    
    # 推理
    print(f"\n执行推理...")
    res = model([test_audio_path], language="auto", use_itn=True)
    
    # 输出结果
    result_text = rich_transcription_postprocess(res[0])
    print(f"\n识别结果: {result_text}")
    
    if 'ground_truth' in locals():
        is_correct = result_text.strip() == ground_truth.strip()
        print(f"结果对比: {'✅ 正确' if is_correct else '❌ 错误'}")
    
    return result_text


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="导出 SenseVoice 微调模型为 ONNX 格式")
    parser.add_argument(
        "--finetuned_model_dir",
        type=str,
        default="./exp_svs",
        help="微调模型目录"
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="./exp_svs_onnx",
        help="ONNX 模型输出目录"
    )
    parser.add_argument(
        "--base_model",
        type=str,
        default="iic/SenseVoiceSmall",
        help="基础模型名称或路径"
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=10,
        help="导出时的批处理大小"
    )
    parser.add_argument(
        "--quantize",
        action="store_true",
        default=True,
        help="是否量化模型"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="导出后测试模型"
    )
    parser.add_argument(
        "--test_audio",
        type=str,
        default=None,
        help="测试音频文件路径"
    )
    
    args = parser.parse_args()
    
    try:
        # 导出模型
        onnx_model_dir, model = export_finetuned_model_to_onnx(
            finetuned_model_dir=args.finetuned_model_dir,
            output_dir=args.output_dir,
            base_model=args.base_model,
            batch_size=args.batch_size,
            quantize=args.quantize
        )
        
        # 测试模型
        if args.test:
            test_onnx_model(
                onnx_model_dir=onnx_model_dir,
                test_audio_path=args.test_audio
            )
        
        print("\n" + "=" * 60)
        print("导出完成!")
        print("=" * 60)
        print(f"\nONNX 模型位置: {onnx_model_dir}")
        print(f"\n使用方法:")
        print(f"```python")
        print(f"from funasr_onnx import SenseVoiceSmall")
        print(f"from funasr_onnx.utils.postprocess_utils import rich_transcription_postprocess")
        print(f"")
        print(f"model = SenseVoiceSmall('{onnx_model_dir}', batch_size=10, quantize=True)")
        print(f"res = model(['audio.wav'], language='auto', use_itn=True)")
        print(f"print(rich_transcription_postprocess(res[0]))")
        print(f"```")
        
    except Exception as e:
        print(f"\n❌ 导出失败: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
