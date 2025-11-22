#!/usr/bin/env python3
"""
从训练数据中提取热词并生成热词文件
用于提升 ONNX 模型推理准确率
"""

import json
from pathlib import Path
from collections import Counter
import jieba
import re


def load_jsonl(jsonl_path):
    """加载JSONL数据"""
    data = []
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            item = json.loads(line.strip())
            data.append(item)
    return data


def extract_words_and_phrases(data, min_freq=2, max_length=10):
    """
    从数据中提取高频词汇和短语
    
    Args:
        data: 数据列表
        min_freq: 最小出现频率
        max_length: 最大热词长度
    
    Returns:
        热词列表及其频率
    """
    # 统计所有目标文本
    all_texts = []
    for item in data:
        text = item.get('target', '')
        if text:
            all_texts.append(text)
    
    # 统计完整短语的频率
    phrase_counter = Counter()
    for text in all_texts:
        # 按空格分割成短语
        phrases = text.split()
        for phrase in phrases:
            if len(phrase) <= max_length and len(phrase) > 0:
                phrase_counter[phrase] += 1
    
    # 统计分词后的词语频率
    word_counter = Counter()
    for text in all_texts:
        # 使用jieba分词
        words = jieba.lcut(text)
        for word in words:
            # 过滤长度
            if 1 < len(word) <= max_length:
                word_counter[word] += 1
    
    # 合并短语和词语
    combined_counter = phrase_counter + word_counter
    
    # 过滤低频词
    hotwords = {word: freq for word, freq in combined_counter.items() if freq >= min_freq}
    
    return hotwords


def calculate_hotword_weight(freq, max_freq, min_weight=20, max_weight=100):
    """
    根据频率计算热词权重
    
    Args:
        freq: 当前词频
        max_freq: 最大词频
        min_weight: 最小权重
        max_weight: 最大权重
    
    Returns:
        权重值
    """
    if max_freq == 0:
        return min_weight
    
    # 使用对数scale避免权重差异过大
    import math
    log_freq = math.log(freq + 1)
    log_max = math.log(max_freq + 1)
    
    normalized = log_freq / log_max
    weight = min_weight + (max_weight - min_weight) * normalized
    
    return int(weight)


def generate_hotword_file(hotwords, output_path, top_k=100):
    """
    生成热词文件
    
    Args:
        hotwords: {词: 频率} 字典
        output_path: 输出文件路径
        top_k: 保留前K个高频词
    """
    # 按频率排序
    sorted_hotwords = sorted(hotwords.items(), key=lambda x: x[1], reverse=True)
    
    # 取前top_k个
    top_hotwords = sorted_hotwords[:top_k]
    
    # 计算权重
    max_freq = top_hotwords[0][1] if top_hotwords else 1
    
    # 写入文件
    with open(output_path, 'w', encoding='utf-8') as f:
        for word, freq in top_hotwords:
            weight = calculate_hotword_weight(freq, max_freq)
            f.write(f"{word} {weight}\n")
    
    print(f"\n✓ 生成热词文件: {output_path}")
    print(f"  热词数量: {len(top_hotwords)}")
    print(f"\n前10个高频热词:")
    for i, (word, freq) in enumerate(top_hotwords[:10], 1):
        weight = calculate_hotword_weight(freq, max_freq)
        print(f"  {i:2d}. {word:15s} (频率: {freq:3d}, 权重: {weight:3d})")


def analyze_error_patterns(comparison_report_path):
    """
    分析模型错误模式，提取容易识别错误的词
    
    Args:
        comparison_report_path: 对比报告路径
    
    Returns:
        容易出错的词列表
    """
    error_words = set()
    
    try:
        with open(comparison_report_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 查找错误样本
        # 示例: | 9 | 2025_11_17_13_30_57.wav | 红灯跟车 | 红灯奔车 | ✗ 错误 |
        pattern = r'\| \d+ \| .+? \| (.+?) \| (.+?) \| ✗ 错误 \|'
        matches = re.findall(pattern, content)
        
        for ground_truth, recognized in matches:
            # 提取ground_truth中的词，这些是容易被识别错的
            words = jieba.lcut(ground_truth.strip())
            for word in words:
                if len(word) > 1:
                    error_words.add(word)
        
        print(f"\n从错误样本中提取了 {len(error_words)} 个容易出错的词")
        print(f"示例: {list(error_words)[:10]}")
    
    except FileNotFoundError:
        print(f"\n警告: 未找到对比报告 {comparison_report_path}")
    
    return error_words


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='从训练数据生成热词文件')
    parser.add_argument('--train_data', type=str, default='../../data/list/train_from_excel.jsonl',
                        help='训练数据JSONL文件')
    parser.add_argument('--val_data', type=str, default='../../data/list/val_from_excel.jsonl',
                        help='验证数据JSONL文件')
    parser.add_argument('--output', type=str, default='../../exp_svs_onnx/hotwords.txt',
                        help='热词输出文件')
    parser.add_argument('--top_k', type=int, default=100,
                        help='保留前K个高频词 (建议不超过1000)')
    parser.add_argument('--min_freq', type=int, default=2,
                        help='最小词频')
    parser.add_argument('--comparison_report', type=str, default=None,
                        help='模型对比报告路径,用于提取容易出错的词')
    
    args = parser.parse_args()
    
    print(f"\n{'='*80}")
    print("生成 ONNX 热词文件")
    print(f"{'='*80}\n")
    
    # 加载训练数据
    all_data = []
    
    if Path(args.train_data).exists():
        print(f"加载训练数据: {args.train_data}")
        train_data = load_jsonl(args.train_data)
        all_data.extend(train_data)
        print(f"  ✓ 训练样本: {len(train_data)}")
    
    if Path(args.val_data).exists():
        print(f"加载验证数据: {args.val_data}")
        val_data = load_jsonl(args.val_data)
        all_data.extend(val_data)
        print(f"  ✓ 验证样本: {len(val_data)}")
    
    if not all_data:
        print("错误: 未找到任何数据文件")
        return
    
    print(f"\n总样本数: {len(all_data)}")
    
    # 提取热词
    print(f"\n提取热词 (最小频率: {args.min_freq}, 最大长度: 10)...")
    hotwords = extract_words_and_phrases(all_data, min_freq=args.min_freq)
    print(f"  ✓ 提取了 {len(hotwords)} 个候选热词")
    
    # 分析错误模式(如果提供了对比报告)
    error_words = set()
    if args.comparison_report and Path(args.comparison_report).exists():
        print(f"\n分析错误模式: {args.comparison_report}")
        error_words = analyze_error_patterns(args.comparison_report)
        
        # 提升容易出错词的权重
        for word in error_words:
            if word in hotwords:
                hotwords[word] = hotwords[word] * 2  # 加倍权重
    
    # 生成热词文件
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    generate_hotword_file(hotwords, output_path, top_k=args.top_k)
    
    # 生成使用说明
    print(f"\n{'='*80}")
    print("使用说明")
    print(f"{'='*80}\n")
    
    print("⚠️  注意事项:")
    print("  1. SenseVoice-ONNX 对热词的支持有限")
    print("  2. 建议热词数量不超过1000个")
    print("  3. 建议热词长度不超过10个字符")
    print("  4. 权重范围: 1-100 (数值越大,优先级越高)\n")
    
    print("📝 热词文件格式:")
    print("  每行一个热词,格式: 热词 权重")
    print("  示例: 红灯跟车 80\n")
    
    print("🚀 在funasr-onnx中使用热词:")
    print("  目前funasr-onnx的SenseVoiceSmall类不支持hotword参数")
    print("  如需使用热词,建议:")
    print("  1. 使用支持热词的模型(如Paraformer)")
    print("  2. 或通过服务端部署方式使用热词\n")
    
    print("🔍 验证热词效果:")
    print("  重新运行模型对比测试,观察准确率是否提升")
    print("  特别关注之前识别错误的样本\n")
    
    print(f"{'='*80}")
    print("热词生成完成!")
    print(f"{'='*80}\n")


if __name__ == '__main__':
    main()
