#!/usr/bin/env python3
"""
生成 SenseVoice 训练数据 - 使用空格分词统计 target_len
策略: 将标点符号替换为空格,按空格统计词意单元数量
"""

import pandas as pd
from pathlib import Path
import json
import re
import torch
import soundfile as sf
import random
from funasr.frontends.wav_frontend import WavFrontend

def replace_punctuation_with_space(text):
    """
    将所有中英文标点符号替换为空格
    
    Args:
        text: 原始文本
    
    Returns:
        替换后的文本
    """
    # 中文标点符号
    chinese_punctuation = '，。！？；：、（）【】《》""''……—·'
    # 英文标点符号
    english_punctuation = ',.!?;:()[]<>"\'-'
    
    # 所有标点符号
    all_punctuation = chinese_punctuation + english_punctuation
    
    # 替换为空格
    result = text
    for punct in all_punctuation:
        result = result.replace(punct, ' ')
    
    # 多个连续空格合并为一个
    result = ' '.join(result.split())
    
    return result


def calculate_target_len(text):
    """
    计算 target_len: 按空格分词统计词意单元数量
    
    规则:
    1. 纯中文: 字符数
    2. 纯英文: 单词数
    3. 中英混搭: 空格分词数(词意单元数)
    
    Args:
        text: 已替换标点为空格的文本
    
    Returns:
        target_len 数值
    """
    # 去除首尾空格
    text = text.strip()
    
    # 按空格分词
    words = text.split()
    
    # 统计词意单元数
    return len(words)


def generate_jsonl_data(
    data_sources,
    output_dir="./data/list",
    train_ratio=0.8
):
    """
    从多个 Excel 文件生成 JSONL 训练数据
    
    Args:
        data_sources: 数据源列表，每个元素为 {"excel": "path/to/excel.xlsx", "audio": "path/to/audio/"}
        output_dir: 输出目录
        train_ratio: 训练集比例
    """
    # 创建输出目录
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # 初始化 WavFrontend
    wav_frontend = WavFrontend(
        cmvn_file=None,
        fs=16000,
        window='hamming',
        n_mels=80,
        frame_length=25,
        frame_shift=10,
        lfr_m=7,
        lfr_n=6,
        dither=0.0
    )
    
    # 收集所有数据源的数据
    all_data = []
    
    print(f"\n{'='*60}")
    print(f"开始处理 {len(data_sources)} 个数据源")
    print(f"{'='*60}\n")
    
    for source_idx, data_source in enumerate(data_sources, 1):
        excel_path = data_source['excel']
        audio_dir = data_source['audio']
        
        print(f"[{source_idx}/{len(data_sources)}] 处理数据源:")
        print(f"  Excel: {excel_path}")
        print(f"  Audio: {audio_dir}")
        
        # 读取 Excel
        try:
            df = pd.read_excel(excel_path)
            print(f"  ✓ 读取成功，共 {len(df)} 行")
        except Exception as e:
            print(f"  ✗ 读取失败: {e}")
            continue
        
        # 准备数据
        audio_dir_path = Path(audio_dir)
        if not audio_dir_path.exists():
            print(f"  ✗ 音频目录不存在: {audio_dir}")
            continue
        
        source_data_count = 0
        
        for idx, row in df.iterrows():
            # 格式化时间戳
            time_str = str(row['time'])
            formatted_time = time_str.replace(':', '_').replace('-', '_').replace(' ', '_')
            
            # 构建音频文件路径
            audio_filename = f"{formatted_time}.wav"
            audio_path = audio_dir_path / audio_filename
            
            # 检查音频文件是否存在
            if not audio_path.exists():
                continue
            
            # 获取原始文本
            original_text = str(row['result']).strip()
            
            # 替换标点符号为空格
            target_text = replace_punctuation_with_space(original_text)
            
            # 计算 target_len (空格分词数)
            target_len = calculate_target_len(target_text)
            
            # 计算 source_len (使用 WavFrontend)
            try:
                # 读取音频数据
                audio_data, samplerate = sf.read(str(audio_path))
                num_samples = len(audio_data)
                
                # 使用 WavFrontend 提取特征
                audio_tensor = torch.from_numpy(audio_data).float()
                with torch.no_grad():
                    fbank, fbank_len = wav_frontend(
                        audio_tensor.unsqueeze(0),
                        torch.tensor([num_samples])
                    )
                
                # 返回降采样后的帧数
                source_len = fbank_len.item()
            except Exception as e:
                continue
            
            # 检测语言 (简单规则: 包含中文字符就是中文)
            has_chinese = bool(re.search(r'[\u4e00-\u9fff]', target_text))
            text_language = "<|zh|>" if has_chinese else "<|en|>"
            
            # 构建 JSONL 数据条目
            entry = {
                "key": formatted_time,
                "source": str(audio_path.absolute()),
                "source_len": int(source_len),
                "target": target_text,
                "target_len": target_len,
                "text_language": text_language,
                "emo_target": "<|NEUTRAL|>",
                "event_target": "<|Speech|>",
                "with_or_wo_itn": "<|woitn|>"  # 已去除标点
            }
            
            all_data.append(entry)
            source_data_count += 1
        
        print(f"  ✓ 成功处理 {source_data_count} 条数据\n")
    
    # 打乱数据顺序（确保训练集和验证集的随机性）
    print(f"正在打乱数据...")
    random.shuffle(all_data)
    print(f"✓ 数据已打乱\n")
    
    # 数据分割
    split_idx = int(len(all_data) * train_ratio)
    train_data = all_data[:split_idx]
    val_data = all_data[split_idx:]
    
    print(f"\n{'='*60}")
    print(f"数据统计:")
    print(f"  总数据: {len(all_data)} 条")
    print(f"  训练集: {len(train_data)} 条")
    print(f"  验证集: {len(val_data)} 条")
    print(f"{'='*60}\n")
    
    # 写入训练集 JSONL
    train_jsonl = output_path / "train_from_excel.jsonl"
    with open(train_jsonl, 'w', encoding='utf-8') as f:
        for entry in train_data:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    
    print(f"✓ 训练集已生成: {train_jsonl}")
    
    # 写入验证集 JSONL
    val_jsonl = output_path / "val_from_excel.jsonl"
    with open(val_jsonl, 'w', encoding='utf-8') as f:
        for entry in val_data:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    
    print(f"✓ 验证集已生成: {val_jsonl}")
    
    # 显示前3条数据示例
    print(f"\n{'='*60}")
    print(f"数据示例 (前3条):")
    print(f"{'='*60}\n")
    
    for i, entry in enumerate(train_data[:3], 1):
        print(f"样本 {i}:")
        print(f"  处理后文本: {entry['target']}")
        print(f"  Source_len: {entry['source_len']}")
        print(f"  Target_len: {entry['target_len']} (空格分词数)")
        print(f"  语言: {entry['text_language']}")
        print()
    
    return len(train_data), len(val_data)


if __name__ == "__main__":
    # 获取项目根目录（脚本在 my-tool/1-data-preparation/ 下，需要向上两级）
    from pathlib import Path
    script_dir = Path(__file__).parent  # my-tool/1-data-preparation/
    project_root = script_dir.parent.parent  # 项目根目录
    
    # 配置数据源（使用绝对路径）
    # 支持多个Excel文件和对应的音频文件夹
    data_sources = [
        {
            "excel": str(project_root / "data/test_data/2025_11_17_13_29_11/asr_results.xlsx"),
            "audio": str(project_root / "data/test_data/2025_11_17_13_29_11/Audio")
        },
        {
            "excel": str(project_root / "data/test_data/2025_11_20_19_34_10/asr_results_2025_11_20_19_34_10.xlsx"),
            "audio": str(project_root / "data/test_data/2025_11_20_19_34_10/Audio")
        },
        {
            "excel": str(project_root / "data/test_data/2025_11_20_22_49_07/asr_results_2025_11_20_22_49_07.xlsx"),
            "audio": str(project_root / "data/test_data/2025_11_20_22_49_07/Audio")
        },
        {
            "excel": str(project_root / "data/test_data/2025_11_21_10_09_06/asr_results_2025_11_21_10_09_06.xlsx"),
            "audio": str(project_root / "data/test_data/2025_11_21_10_09_06/Audio")
        },
        {
            "excel": str(project_root / "data/test_data/2025_11_21_10_36_51/asr_results_2025_11_21_10_36_51.xlsx"),
            "audio": str(project_root / "data/test_data/2025_11_21_10_36_51/Audio")
        },
        {
            "excel": str(project_root / "data/test_data/2025_11_21_13_58_30/asr_results_2025_11_21_13_58_30.xlsx"),
            "audio": str(project_root / "data/test_data/2025_11_21_13_58_30/Audio")
        },
        {
            "excel": str(project_root / "data/test_data/2025_11_21_14_49_13/asr_results_2025_11_21_14_49_13.xlsx"),
            "audio": str(project_root / "data/test_data/2025_11_21_14_49_13/Audio")
        },
        {
            "excel": str(project_root / "data/test_data/2025_11_21_14_53_40/asr_results_2025_11_21_14_53_40.xlsx"),
            "audio": str(project_root / "data/test_data/2025_11_21_14_53_40/Audio")
        },
        {
            "excel": str(project_root / "data/test_data/2025_11_21_21_52_57/asr_results_2025_11_21_21_52_57.xlsx"),
            "audio": str(project_root / "data/test_data/2025_11_21_21_52_57/Audio")
        },
        # 可以添加更多数据源
        # {
        #     "excel": str(project_root / "data/asr_results_2.xlsx"),
        #     "audio": str(project_root / "data/Audio2")
        # },
    ]
    
    print(f"\n{'='*60}")
    print(f"生成 SenseVoice 训练数据 (空格分词版本)")
    print(f"{'='*60}\n")
    
    # 生成数据
    train_count, val_count = generate_jsonl_data(
        data_sources=data_sources,
        output_dir=str(project_root / "data/list"),
        train_ratio=0.8
    )
    
    print(f"\n{'='*60}")
    print(f"数据生成完成!")
    print(f"  训练集: {train_count} 条")
    print(f"  验证集: {val_count} 条")
    print(f"{'='*60}\n")
