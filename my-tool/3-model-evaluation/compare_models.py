#!/usr/bin/env python3
"""
对比原始 SenseVoice 模型和微调后模型的 ASR 效果
"""

import json
from pathlib import Path
from datetime import datetime
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess


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


def test_model(model, data, model_name):
    """
    测试模型并返回详细结果
    
    Args:
        model: 模型实例
        data: 验证数据列表
        model_name: 模型名称
    
    Returns:
        测试结果字典列表和统计信息
    """
    print(f"\n{'='*80}")
    print(f"{model_name} - ASR 测试中...")
    print(f"{'='*80}\n")
    
    results = []
    correct_count = 0
    total_count = 0
    
    for idx, item in enumerate(data, 1):
        audio_path = item['source']
        ground_truth = item['target']
        
        # 执行识别
        try:
            result = model.generate(
                input=audio_path,
                cache={},
                language="auto",
                use_itn=False,
                batch_size_s=60,
                merge_vad=True,
                merge_length_s=15,
            )
            
            # 提取识别文本
            if result and len(result) > 0:
                raw_text = result[0]["text"]
                
                # 去除标签前缀 (如 <|zh|><|NEUTRAL|><|Speech|><|woitn|>)
                import re
                recognized_text = re.sub(r'<\|[^|]+\|>', '', raw_text).strip()
                
                # 去除空格并转换为小写进行比对(忽略大小写)
                recognized_clean = recognized_text.replace(" ", "").lower()
                ground_truth_clean = ground_truth.replace(" ", "").lower()
                
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
                    'error': '识别失败'
                })
                print(f"  处理样本 {idx}/{len(data)}: ✗ {Path(audio_path).name} (识别失败)")
                
        except Exception as e:
            results.append({
                'index': idx,
                'audio': Path(audio_path).name,
                'ground_truth': ground_truth,
                'error': str(e)
            })
            print(f"  处理样本 {idx}/{len(data)}: ✗ {Path(audio_path).name} (错误: {e})")
    
    # 统计信息
    accuracy = (correct_count / total_count * 100) if total_count > 0 else 0
    
    stats = {
        'total': len(data),
        'processed': total_count,
        'correct': correct_count,
        'accuracy': accuracy
    }
    
    print(f"\n✓ {model_name} 测试完成")
    print(f"  准确率: {accuracy:.2f}% ({correct_count}/{total_count})\n")
    
    return results, stats


def write_markdown_report(original_results, original_stats, finetuned_results, finetuned_stats, 
                          original_name, finetuned_name, output_path):
    """
    生成Markdown格式的对比报告
    
    Args:
        original_results: 原始模型测试结果
        original_stats: 原始模型统计信息
        finetuned_results: 微调模型测试结果
        finetuned_stats: 微调模型统计信息
        original_name: 原始模型名称
        finetuned_name: 微调模型名称
        output_path: 输出文件路径
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        # 标题和概览
        f.write("# SenseVoice 模型对比测试报告\n\n")
        f.write(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # 模型信息
        f.write("## 模型信息\n\n")
        f.write(f"- **原始模型**: {original_name}\n")
        f.write(f"- **微调模型**: {finetuned_name}\n")
        f.write(f"- **测试样本数**: {original_stats['total']}\n\n")
        
        # 整体对比
        f.write("## 整体性能对比\n\n")
        f.write("| 模型 | 测试样本 | 正确识别 | 准确率 |\n")
        f.write("|------|---------|---------|--------|\n")
        f.write(f"| {original_name} | {original_stats['processed']} | {original_stats['correct']} | {original_stats['accuracy']:.2f}% |\n")
        f.write(f"| {finetuned_name} | {finetuned_stats['processed']} | {finetuned_stats['correct']} | {finetuned_stats['accuracy']:.2f}% |\n\n")
        
        improvement = finetuned_stats['accuracy'] - original_stats['accuracy']
        if improvement > 0:
            f.write(f"**✓ 性能提升**: +{improvement:.2f}%\n\n")
        elif improvement < 0:
            f.write(f"**⚠️ 性能下降**: {improvement:.2f}%\n\n")
        else:
            f.write(f"**- 性能相同**: 0.00%\n\n")
        
        # 详细测试结果
        f.write("## 详细测试结果\n\n")
        
        for idx in range(len(original_results)):
            orig = original_results[idx]
            fine = finetuned_results[idx]
            
            f.write(f"### 样本 {orig['index']}: {orig['audio']}\n\n")
            
            # 真实文本
            f.write(f"**真实文本**: {orig['ground_truth']}\n\n")
            
            # 原始模型结果
            f.write(f"#### {original_name}\n\n")
            if 'error' in orig:
                f.write(f"- ❌ **错误**: {orig['error']}\n\n")
            else:
                status = "✅ 正确" if orig['is_correct'] else "❌ 错误"
                f.write(f"- **状态**: {status}\n")
                f.write(f"- **原始输出**: `{orig['raw_text']}`\n")
                f.write(f"- **识别文本**: {orig['recognized']}\n")
                if not orig['is_correct']:
                    f.write(f"- **差异**: `{orig['recognized_clean']}` vs `{orig['ground_truth_clean']}`\n")
                f.write("\n")
            
            # 微调模型结果
            f.write(f"#### {finetuned_name}\n\n")
            if 'error' in fine:
                f.write(f"- ❌ **错误**: {fine['error']}\n\n")
            else:
                status = "✅ 正确" if fine['is_correct'] else "❌ 错误"
                f.write(f"- **状态**: {status}\n")
                f.write(f"- **原始输出**: `{fine['raw_text']}`\n")
                f.write(f"- **识别文本**: {fine['recognized']}\n")
                if not fine['is_correct']:
                    f.write(f"- **差异**: `{fine['recognized_clean']}` vs `{fine['ground_truth_clean']}`\n")
                f.write("\n")
            
            # 对比结论
            if 'error' not in orig and 'error' not in fine:
                if orig['is_correct'] and fine['is_correct']:
                    f.write("**结论**: 两个模型均识别正确 ✅\n\n")
                elif not orig['is_correct'] and fine['is_correct']:
                    f.write("**结论**: 微调模型改进 ⬆️\n\n")
                elif orig['is_correct'] and not fine['is_correct']:
                    f.write("**结论**: 微调模型退化 ⬇️\n\n")
                else:
                    f.write("**结论**: 两个模型均识别错误 ❌\n\n")
            
            f.write("---\n\n")
        
        # 总结
        f.write("## 总结\n\n")
        f.write(f"本次测试共评估 {original_stats['total']} 个音频样本:\n\n")
        f.write(f"- **原始模型准确率**: {original_stats['accuracy']:.2f}%\n")
        f.write(f"- **微调模型准确率**: {finetuned_stats['accuracy']:.2f}%\n")
        f.write(f"- **准确率变化**: {improvement:+.2f}%\n\n")
        
        if improvement > 0:
            f.write(f"✅ **微调成功**: 模型性能提升了 {improvement:.2f}%\n")
        elif improvement < 0:
            f.write(f"⚠️ **需要优化**: 模型性能下降了 {abs(improvement):.2f}%，建议检查训练配置\n")
        else:
            f.write(f"➖ **性能持平**: 模型性能未发生变化\n")


def main():
    """主函数"""
    # 获取项目根目录（脚本在 my-tool/3-model-evaluation/ 下，向上两级）
    from pathlib import Path
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    
    # 配置（使用项目根目录拼接）
    val_jsonl_path = project_root / "data/list/val_from_excel.jsonl"
    original_model_dir = project_root / "models/SenseVoiceSmall"  # 原始模型(本地缓存)
    finetuned_model_dir = project_root / "exp_svs"  # 微调后的模型
    output_md = project_root / f"my-tool/3-model-evaluation/model_comparison_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    
    print(f"\n{'='*80}")
    print(f"SenseVoice 模型对比测试")
    print(f"{'='*80}")
    print(f"项目根目录: {project_root}")
    print(f"验证数据: {val_jsonl_path}")
    print(f"测试样本数: 全部")
    print(f"输出报告: {output_md}")
    print(f"{'='*80}\n")
    
    # 加载验证数据
    print("加载验证数据...")
    val_data = load_validation_data(str(val_jsonl_path))
    print(f"✓ 加载完成,共 {len(val_data)} 条数据\n")
    
    # 测试原始模型
    print("="*80)
    print("1. 加载原始 SenseVoice 模型...")
    print("="*80)
    original_model = AutoModel(
        model=str(original_model_dir),
        vad_model="fsmn-vad",
        vad_kwargs={"max_single_segment_time": 30000},
        device="cuda:0",
    )
    print("✓ 原始模型加载完成\n")
    
    original_results, original_stats = test_model(
        original_model, 
        val_data, 
        "原始模型"
    )
    
    # 检查微调模型是否存在
    finetuned_checkpoint = Path(finetuned_model_dir) / "model.pt.ep73"
    if not finetuned_checkpoint.exists():
        # 尝试查找最新的 epoch checkpoint
        import glob
        checkpoints = sorted(glob.glob(str(Path(finetuned_model_dir) / "model.pt.ep*")))
        if checkpoints:
            finetuned_checkpoint = Path(checkpoints[-1])
            print(f"\n✓ 找到微调模型: {finetuned_checkpoint.name}\n")
        else:
            print("\n⚠️  警告: 微调模型不存在!")
            print(f"   期望路径: {finetuned_model_dir}/model.pt.ep73")
            print(f"   或: {finetuned_model_dir}/model.pt.ep*")
            print(f"   请先完成模型训练\n")
            return
    
    # 测试微调后模型
    print("="*80)
    print("2. 加载微调后的 SenseVoice 模型...")
    print("="*80)
    finetuned_model = AutoModel(
        model=str(finetuned_model_dir),
        vad_model="fsmn-vad",
        vad_kwargs={"max_single_segment_time": 30000},
        device="cuda:0",
    )
    print("✓ 微调模型加载完成\n")
    
    finetuned_results, finetuned_stats = test_model(
        finetuned_model,
        val_data,
        "微调模型"
    )
    
    # 生成Markdown报告
    print("="*80)
    print("生成对比报告...")
    print("="*80)
    
    write_markdown_report(
        original_results, original_stats,
        finetuned_results, finetuned_stats,
        f"原始模型 ({original_model_dir})",
        f"微调模型 ({finetuned_checkpoint.name})",
        str(output_md)
    )
    
    print(f"\n✓ 报告已生成: {output_md}\n")
    
    # 控制台输出摘要
    print("\n" + "="*80)
    print("测试摘要")
    print("="*80)
    print(f"原始模型准确率: {original_stats['accuracy']:.2f}%")
    print(f"微调模型准确率: {finetuned_stats['accuracy']:.2f}%")
    improvement = finetuned_stats['accuracy'] - original_stats['accuracy']
    print(f"准确率提升: {improvement:+.2f}%")
    
    if improvement > 0:
        print(f"\n✓ 微调后模型性能提升了 {improvement:.2f}%!")
    elif improvement < 0:
        print(f"\n⚠️  微调后模型性能下降了 {abs(improvement):.2f}%")
    else:
        print(f"\n- 两个模型性能相同")
    
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
