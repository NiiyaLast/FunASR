#!/usr/bin/env python3
"""
对比 ONNX 模型和量化 ONNX 模型的推理差异
"""

import json
import re
from pathlib import Path
from datetime import datetime
from funasr_onnx import SenseVoiceSmall
from funasr_onnx.utils.postprocess_utils import rich_transcription_postprocess


def load_validation_data(jsonl_path):
    """
    加载验证集数据
    
    Args:
        jsonl_path: JSONL 文件路径
    
    Returns:
        数据列表
    """
    data = []
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            item = json.loads(line.strip())
            data.append(item)
    return data


def clean_text(text):
    """
    清理识别文本，去除标签
    
    Args:
        text: 原始文本
    
    Returns:
        清理后的文本
    """
    # 去除标签前缀 (如 <|zh|><|NEUTRAL|><|Speech|><|woitn|>)
    cleaned = re.sub(r'<\|[^|]+\|>', '', text).strip()
    return cleaned


def test_model(model_path, data, model_name, batch_size=10, quantize=False):
    """
    测试 ONNX 模型并返回详细结果
    
    Args:
        model_path: 模型路径
        data: 验证数据列表
        model_name: 模型名称
        batch_size: 批处理大小
        quantize: 是否为量化模型
    
    Returns:
        测试结果字典列表和统计信息
    """
    print(f"\n{'='*80}")
    print(f"{model_name} - ONNX 推理测试中...")
    print(f"{'='*80}\n")
    
    # 加载模型
    try:
        model = SenseVoiceSmall(
            model_path,
            batch_size=batch_size,
            quantize=quantize
        )
        print(f"✓ 成功加载模型: {model_path}")
    except Exception as e:
        print(f"✗ 加载模型失败: {e}")
        return [], {'error': str(e)}
    
    results = []
    correct_count = 0
    total_count = 0
    
    for idx, item in enumerate(data, 1):
        audio_path = item['source']
        ground_truth = item['target']
        
        # 执行识别
        try:
            result = model(
                [audio_path],
                language='auto',
                use_itn=False
            )
            
            # 提取识别文本
            if result and len(result) > 0:
                raw_text = result[0]['text'] if isinstance(result[0], dict) else str(result[0])
                
                # 清理文本
                recognized_text = clean_text(raw_text)
                
                # 去除空格进行比对
                recognized_clean = recognized_text.replace(" ", "")
                ground_truth_clean = ground_truth.replace(" ", "")
                
                # 判断是否正确
                is_correct = recognized_clean == ground_truth_clean
                if is_correct:
                    correct_count += 1
                total_count += 1
                
                # 保存结果
                results.append({
                    'index': idx,
                    'audio': Path(audio_path).name,
                    'ground_truth': ground_truth,
                    'raw_text': raw_text,
                    'recognized': recognized_text,
                    'is_correct': is_correct,
                    'ground_truth_clean': ground_truth_clean,
                    'recognized_clean': recognized_clean
                })
                
                print(f"  处理样本 {idx}/{len(data)}: {'✓' if is_correct else '✗'} {Path(audio_path).name}")
            else:
                results.append({
                    'index': idx,
                    'audio': Path(audio_path).name,
                    'ground_truth': ground_truth,
                    'raw_text': '',
                    'recognized': '',
                    'is_correct': False,
                    'error': '模型未返回结果'
                })
                total_count += 1
                print(f"  处理样本 {idx}/{len(data)}: ✗ {Path(audio_path).name} (无结果)")
                
        except Exception as e:
            results.append({
                'index': idx,
                'audio': Path(audio_path).name,
                'ground_truth': ground_truth,
                'raw_text': '',
                'recognized': '',
                'is_correct': False,
                'error': str(e)
            })
            total_count += 1
            print(f"  处理样本 {idx}/{len(data)}: ✗ {Path(audio_path).name} (错误: {e})")
    
    # 统计信息
    stats = {
        'total': total_count,
        'correct': correct_count,
        'incorrect': total_count - correct_count,
        'accuracy': correct_count / total_count if total_count > 0 else 0
    }
    
    print(f"\n{model_name} 测试完成:")
    print(f"  总样本数: {stats['total']}")
    print(f"  正确数: {stats['correct']}")
    print(f"  错误数: {stats['incorrect']}")
    print(f"  准确率: {stats['accuracy']*100:.2f}%")
    
    return results, stats


def compare_results(onnx_results, quant_results):
    """
    比较两个模型的结果差异
    
    Args:
        onnx_results: ONNX 模型结果
        quant_results: 量化模型结果
    
    Returns:
        差异列表
    """
    differences = []
    
    for onnx_res, quant_res in zip(onnx_results, quant_results):
        if onnx_res['recognized_clean'] != quant_res['recognized_clean']:
            differences.append({
                'index': onnx_res['index'],
                'audio': onnx_res['audio'],
                'ground_truth': onnx_res['ground_truth'],
                'onnx_result': onnx_res['recognized'],
                'quant_result': quant_res['recognized'],
                'onnx_correct': onnx_res['is_correct'],
                'quant_correct': quant_res['is_correct'],
                'onnx_raw': onnx_res['raw_text'],
                'quant_raw': quant_res['raw_text']
            })
    
    return differences


def generate_markdown_report(onnx_results, onnx_stats, quant_results, quant_stats, differences, output_path):
    """
    生成 Markdown 比较报告
    
    Args:
        onnx_results: ONNX 模型结果
        onnx_stats: ONNX 模型统计
        quant_results: 量化模型结果
        quant_stats: 量化模型统计
        differences: 差异列表
        output_path: 输出文件路径
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        # 标题
        f.write("# ONNX 模型与量化模型推理对比报告\n\n")
        f.write(f"**生成时间**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}\n\n")
        
        # 概览
        f.write("## 📊 对比概览\n\n")
        f.write("| 模型类型 | 准确率 | 正确数 | 错误数 | 总样本数 |\n")
        f.write("|---------|--------|--------|--------|----------|\n")
        f.write(f"| ONNX 完整精度模型 | {onnx_stats['accuracy']*100:.2f}% | {onnx_stats['correct']} | {onnx_stats['incorrect']} | {onnx_stats['total']} |\n")
        f.write(f"| ONNX 量化模型 | {quant_stats['accuracy']*100:.2f}% | {quant_stats['correct']} | {quant_stats['incorrect']} | {quant_stats['total']} |\n\n")
        
        # 差异统计
        f.write("## 🔍 差异分析\n\n")
        f.write(f"**识别结果差异**: 共 {len(differences)} 个样本的识别结果不同\n\n")
        
        if len(differences) > 0:
            # 差异率
            diff_rate = len(differences) / len(onnx_results) * 100
            f.write(f"**差异率**: {diff_rate:.2f}% ({len(differences)}/{len(onnx_results)})\n\n")
            
            # 差异影响
            onnx_better = sum(1 for d in differences if d['onnx_correct'] and not d['quant_correct'])
            quant_better = sum(1 for d in differences if d['quant_correct'] and not d['onnx_correct'])
            both_wrong = sum(1 for d in differences if not d['onnx_correct'] and not d['quant_correct'])
            
            f.write("### 差异影响统计\n\n")
            f.write(f"- ONNX 模型更准确: {onnx_better} 个样本\n")
            f.write(f"- 量化模型更准确: {quant_better} 个样本\n")
            f.write(f"- 两者都错误但结果不同: {both_wrong} 个样本\n\n")
            
            # 详细差异列表
            f.write("### 差异详情\n\n")
            
            for diff in differences:
                f.write(f"#### 样本 {diff['index']}: {diff['audio']}\n\n")
                f.write(f"**标注文本**: {diff['ground_truth']}\n\n")
                
                f.write("| 模型 | 识别结果 | 是否正确 | 完整输出 |\n")
                f.write("|------|----------|----------|----------|\n")
                f.write(f"| ONNX 完整精度 | {diff['onnx_result']} | {'✓' if diff['onnx_correct'] else '✗'} | `{diff['onnx_raw']}` |\n")
                f.write(f"| ONNX 量化 | {diff['quant_result']} | {'✓' if diff['quant_correct'] else '✗'} | `{diff['quant_raw']}` |\n\n")
        else:
            f.write("**结论**: 两个模型在所有测试样本上的识别结果完全一致！\n\n")
        
        # ONNX 模型详细结果
        f.write("## 📋 ONNX 完整精度模型详细结果\n\n")
        f.write("| 序号 | 音频文件 | 标注文本 | 识别结果 | 状态 |\n")
        f.write("|------|----------|----------|----------|------|\n")
        
        for res in onnx_results:
            status = '✓ 正确' if res['is_correct'] else '✗ 错误'
            f.write(f"| {res['index']} | {res['audio']} | {res['ground_truth']} | {res['recognized']} | {status} |\n")
        
        f.write("\n")
        
        # 量化模型详细结果
        f.write("## 📋 ONNX 量化模型详细结果\n\n")
        f.write("| 序号 | 音频文件 | 标注文本 | 识别结果 | 状态 |\n")
        f.write("|------|----------|----------|----------|------|\n")
        
        for res in quant_results:
            status = '✓ 正确' if res['is_correct'] else '✗ 错误'
            f.write(f"| {res['index']} | {res['audio']} | {res['ground_truth']} | {res['recognized']} | {status} |\n")
        
        f.write("\n")
        
        # 总结
        f.write("## 📌 总结\n\n")
        
        # 准确率对比
        acc_diff = abs(onnx_stats['accuracy'] - quant_stats['accuracy']) * 100
        if acc_diff < 0.01:
            f.write(f"1. **准确率**: 两个模型的准确率几乎相同 (差异 {acc_diff:.4f}%)\n")
        else:
            better_model = "ONNX 完整精度模型" if onnx_stats['accuracy'] > quant_stats['accuracy'] else "ONNX 量化模型"
            f.write(f"1. **准确率**: {better_model} 略优 (差异 {acc_diff:.2f}%)\n")
        
        # 识别结果一致性
        consistency_rate = (len(onnx_results) - len(differences)) / len(onnx_results) * 100
        f.write(f"2. **识别一致性**: {consistency_rate:.2f}% 的样本识别结果一致\n")
        
        # 量化影响评估
        if len(differences) == 0:
            f.write("3. **量化影响**: 量化对模型识别结果无影响\n")
        elif len(differences) / len(onnx_results) < 0.05:
            f.write("3. **量化影响**: 量化对模型识别结果影响极小 (< 5%)\n")
        elif len(differences) / len(onnx_results) < 0.10:
            f.write("3. **量化影响**: 量化对模型识别结果影响较小 (< 10%)\n")
        else:
            f.write("3. **量化影响**: 量化对模型识别结果有明显影响 (≥ 10%)\n")
        
        # 推荐
        f.write("\n### 推荐使用\n\n")
        if quant_stats['accuracy'] >= onnx_stats['accuracy'] * 0.99:  # 量化模型准确率不低于完整模型的99%
            f.write("✅ **推荐使用量化模型 (`model_quant.onnx`)**\n\n")
            f.write("**理由**:\n")
            f.write("- 模型大小更小 (约 1/4)\n")
            f.write("- 推理速度更快\n")
            f.write(f"- 准确率损失极小 ({acc_diff:.2f}%)\n")
        else:
            f.write("⚠️ **建议根据具体场景选择**\n\n")
            f.write("- 如果追求最高准确率: 使用完整精度模型 (`model.onnx`)\n")
            f.write("- 如果追求速度和体积: 使用量化模型 (`model_quant.onnx`)\n")
    
    print(f"\n✓ 报告已生成: {output_path}")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='对比 ONNX 模型和量化模型的推理差异')
    parser.add_argument('--onnx_model_dir', type=str, default='../../exp_svs_onnx',
                        help='ONNX 模型目录')
    parser.add_argument('--val_data', type=str, default='../../data/list/val_from_excel.jsonl',
                        help='验证数据 JSONL 文件')
    parser.add_argument('--batch_size', type=int, default=10,
                        help='批处理大小')
    parser.add_argument('--output_dir', type=str, default='../..',
                        help='报告输出目录')
    
    args = parser.parse_args()
    
    # 生成报告文件名
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = Path(args.output_dir) / f"onnx_comparison_{timestamp}.md"
    
    # 加载验证数据
    print(f"\n加载验证数据: {args.val_data}")
    val_data = load_validation_data(args.val_data)
    print(f"✓ 加载了 {len(val_data)} 个验证样本")
    
    # 测试 ONNX 完整精度模型
    onnx_model_path = Path(args.onnx_model_dir)
    onnx_results, onnx_stats = test_model(
        str(onnx_model_path),
        val_data,
        "ONNX 完整精度模型",
        batch_size=args.batch_size,
        quantize=False
    )
    
    # 测试 ONNX 量化模型
    quant_results, quant_stats = test_model(
        str(onnx_model_path),
        val_data,
        "ONNX 量化模型",
        batch_size=args.batch_size,
        quantize=True
    )
    
    # 比较结果
    print(f"\n{'='*80}")
    print("对比两个模型的识别结果...")
    print(f"{'='*80}\n")
    
    differences = compare_results(onnx_results, quant_results)
    print(f"✓ 发现 {len(differences)} 个样本的识别结果不同")
    
    # 生成报告
    generate_markdown_report(
        onnx_results, onnx_stats,
        quant_results, quant_stats,
        differences,
        report_path
    )
    
    print(f"\n{'='*80}")
    print("对比测试完成!")
    print(f"{'='*80}\n")


if __name__ == '__main__':
    main()
