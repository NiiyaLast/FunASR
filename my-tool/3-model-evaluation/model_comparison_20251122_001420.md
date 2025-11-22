# SenseVoice 模型对比测试报告

**生成时间**: 2025-11-22 00:15:16

## 模型信息

- **原始模型**: 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)
- **微调模型**: 微调模型 (model.pt.ep32)
- **测试样本数**: 468

## 整体性能对比

| 模型 | 测试样本 | 正确识别 | 准确率 |
|------|---------|---------|--------|
| 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall) | 468 | 213 | 45.51% |
| 微调模型 (model.pt.ep32) | 468 | 309 | 66.03% |

**✓ 性能提升**: +20.51%

## 详细测试结果

### 样本 1: 2025_11_20_23_18_02.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 2: 2025_11_21_10_39_25.wav

**真实文本**: VRU Handling

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>where are you handling`
- **识别文本**: where are you handling
- **差异**: `whereareyouhandling` vs `VRUHandling`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>where are you handling`
- **识别文本**: where are you handling
- **差异**: `whereareyouhandling` vs `VRUHandling`

**结论**: 两个模型均识别错误 ❌

---

### 样本 3: 2025_11_20_23_12_25.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 4: 2025_11_21_21_57_06.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>张hnson street`
- **识别文本**: 张hnson street
- **差异**: `张hnsonstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juhnction street`
- **识别文本**: juhnction street
- **差异**: `juhnctionstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 5: 2025_11_17_14_03_59.wav

**真实文本**: 其他

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|BGM|><|woitn|>其他`
- **识别文本**: 其他

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他`
- **识别文本**: 其他

**结论**: 两个模型均识别正确 ✅

---

### 样本 6: 2025_11_21_14_00_06.wav

**真实文本**: 路口右转

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转`
- **识别文本**: 路口右转

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转`
- **识别文本**: 路口右转

**结论**: 两个模型均识别正确 ✅

---

### 样本 7: 2025_11_20_23_18_13.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 8: 2025_11_21_21_57_24.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>johnson street`
- **识别文本**: johnson street
- **差异**: `johnsonstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juhnson street`
- **识别文本**: juhnson street
- **差异**: `juhnsonstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 9: 2025_11_20_22_52_52.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 10: 2025_11_21_14_21_27.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 11: 2025_11_20_23_11_48.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>红灯跟出`
- **识别文本**: 红灯跟出
- **差异**: `红灯跟出` vs `红灯跟车`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 微调模型改进 ⬆️

---

### 样本 12: 2025_11_21_13_15_47.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 13: 2025_11_20_19_49_06.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 14: 2025_11_17_13_31_35.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 15: 2025_11_21_10_30_35.wav

**真实文本**: 路口直行 识别闪烁的黄灯顺利通过 效率性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>入口执行识别闪烁的黄灯顺利通过效率性五分`
- **识别文本**: 入口执行识别闪烁的黄灯顺利通过效率性五分
- **差异**: `入口执行识别闪烁的黄灯顺利通过效率性五分` vs `路口直行识别闪烁的黄灯顺利通过效率性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 识别闪烁的黄灯顺利通过 效率性5分`
- **识别文本**: 路口直行 识别闪烁的黄灯顺利通过 效率性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 16: 2025_11_17_13_52_55.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 17: 2025_11_20_23_00_48.wav

**真实文本**: 开始测试

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

**结论**: 两个模型均识别正确 ✅

---

### 样本 18: 2025_11_20_19_42_18.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 19: 2025_11_21_14_29_46.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 20: 2025_11_20_19_43_35.wav

**真实文本**: 障碍物绕行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行`
- **识别文本**: 障碍物绕行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行`
- **识别文本**: 障碍物绕行

**结论**: 两个模型均识别正确 ✅

---

### 样本 21: 2025_11_21_10_46_11.wav

**真实文本**: CL

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>se`
- **识别文本**: se
- **差异**: `se` vs `CL`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>se`
- **识别文本**: se
- **差异**: `se` vs `CL`

**结论**: 两个模型均识别错误 ❌

---

### 样本 22: 2025_11_21_14_08_36.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 23: 2025_11_21_15_28_39.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>导航便到`
- **识别文本**: 导航便到
- **差异**: `导航便到` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 24: 2025_11_20_20_49_17.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 25: 2025_11_21_10_38_51.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>juhnction street`
- **识别文本**: juhnction street
- **差异**: `juhnctionstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>junction street`
- **识别文本**: junction street
- **差异**: `junctionstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 26: 2025_11_20_20_34_37.wav

**真实文本**: 路口右转 在右转时直奔前面的车辆开去 压力性一分 舒适性四分 效率性四分 预测性一分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转在右转时直奔前面的车辆开去压力性一分舒适性四分效率性四分热性一分`
- **识别文本**: 路口右转在右转时直奔前面的车辆开去压力性一分舒适性四分效率性四分热性一分
- **差异**: `路口右转在右转时直奔前面的车辆开去压力性一分舒适性四分效率性四分热性一分` vs `路口右转在右转时直奔前面的车辆开去压力性一分舒适性四分效率性四分预测性一分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转 在右转时直奔前面的车辆开去 压力性1分 舒适性4分 效率性4分 预测性1分`
- **识别文本**: 路口右转 在右转时直奔前面的车辆开去 压力性1分 舒适性4分 效率性4分 预测性1分
- **差异**: `路口右转在右转时直奔前面的车辆开去压力性1分舒适性4分效率性4分预测性1分` vs `路口右转在右转时直奔前面的车辆开去压力性一分舒适性四分效率性四分预测性一分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 27: 2025_11_21_21_57_01.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>dunkson street`
- **识别文本**: dunkson street
- **差异**: `dunksonstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>dunkson street`
- **识别文本**: dunkson street
- **差异**: `dunksonstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 28: 2025_11_20_20_49_14.wav

**真实文本**: 红灯领航

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红浪两行`
- **识别文本**: 红浪两行
- **差异**: `红浪两行` vs `红灯领航`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红狼领航`
- **识别文本**: 红狼领航
- **差异**: `红狼领航` vs `红灯领航`

**结论**: 两个模型均识别错误 ❌

---

### 样本 29: 2025_11_21_14_00_27.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|SAD|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 30: 2025_11_20_20_30_16.wav

**真实文本**: 路口右转 离马路牙子太近

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转离马路牙子太近`
- **识别文本**: 路口右转离马路牙子太近

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转 离马路牙子太近`
- **识别文本**: 路口右转 离马路牙子太近

**结论**: 两个模型均识别正确 ✅

---

### 样本 31: 2025_11_21_15_37_01.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航便道`
- **识别文本**: 导航便道
- **差异**: `导航便道` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 32: 2025_11_21_21_56_02.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>zhangsheng street`
- **识别文本**: zhangsheng street
- **差异**: `zhangshengstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>zhangsheng street`
- **识别文本**: zhangsheng street
- **差异**: `zhangshengstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 33: 2025_11_21_13_25_18.wav

**真实文本**: 绕行障碍物

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绕行障碍物`
- **识别文本**: 绕行障碍物

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绕行障碍物`
- **识别文本**: 绕行障碍物

**结论**: 两个模型均识别正确 ✅

---

### 样本 34: 2025_11_20_23_15_29.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯风车`
- **识别文本**: 红灯风车
- **差异**: `红灯风车` vs `红灯跟车`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 微调模型改进 ⬆️

---

### 样本 35: 2025_11_21_10_18_41.wav

**真实文本**: 弱势群体 但是弱势群体距离本车较远 且没有 动作 本车降速过大 效率性2分 压力性2分 预测性2分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体但是弱势群体距离本车较远且没有动作本车降速过大效率性二分压力性二分预测型二分`
- **识别文本**: 弱势群体但是弱势群体距离本车较远且没有动作本车降速过大效率性二分压力性二分预测型二分
- **差异**: `弱势群体但是弱势群体距离本车较远且没有动作本车降速过大效率性二分压力性二分预测型二分` vs `弱势群体但是弱势群体距离本车较远且没有动作本车降速过大效率性2分压力性2分预测性2分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 但是弱势群体距离本车较远 且没有动作 本车降速过大 效率性2分 压力性2分 预测性2分`
- **识别文本**: 弱势群体 但是弱势群体距离本车较远 且没有动作 本车降速过大 效率性2分 压力性2分 预测性2分

**结论**: 微调模型改进 ⬆️

---

### 样本 36: 2025_11_20_23_18_24.wav

**真实文本**: 路口左转 左转到目标车道后 有减速 减速不是很舒适

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转左转到目标车道后有减速减速不是很舒适`
- **识别文本**: 路口左转左转到目标车道后有减速减速不是很舒适

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转 左转到目标车道后有减速 减速不是很舒适`
- **识别文本**: 路口左转 左转到目标车道后有减速 减速不是很舒适

**结论**: 两个模型均识别正确 ✅

---

### 样本 37: 2025_11_21_10_13_17.wav

**真实文本**: 超车变道 效率性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道效率型五分`
- **识别文本**: 超车变道效率型五分
- **差异**: `超车变道效率型五分` vs `超车变道效率性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道 效率性5分`
- **识别文本**: 超车变道 效率性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 38: 2025_11_21_10_45_55.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>zhangctioneng street`
- **识别文本**: zhangctioneng street
- **差异**: `zhangctionengstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juhangction street`
- **识别文本**: juhangction street
- **差异**: `juhangctionstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 39: 2025_11_21_14_04_34.wav

**真实文本**: 环岛 环岛能够听从驾驶员指令 不变道 效率性5分 压力性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环导环岛能够听从驾驶员指令不变道效率性五分压力性五分`
- **识别文本**: 环导环岛能够听从驾驶员指令不变道效率性五分压力性五分
- **差异**: `环导环岛能够听从驾驶员指令不变道效率性五分压力性五分` vs `环岛环岛能够听从驾驶员指令不变道效率性5分压力性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛 环岛能够听从驾驶员指令 不变道 效率性5分 压力性5分`
- **识别文本**: 环岛 环岛能够听从驾驶员指令 不变道 效率性5分 压力性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 40: 2025_11_20_19_58_29.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 41: 2025_11_20_23_16_16.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 42: 2025_11_21_21_58_44.wav

**真实文本**: Junction Turn

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>junction turn`
- **识别文本**: junction turn
- **差异**: `junctionturn` vs `JunctionTurn`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>junction turn`
- **识别文本**: junction turn
- **差异**: `junctionturn` vs `JunctionTurn`

**结论**: 两个模型均识别错误 ❌

---

### 样本 43: 2025_11_21_10_43_42.wav

**真实文本**: CL

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>c l`
- **识别文本**: c l
- **差异**: `cl` vs `CL`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>c l`
- **识别文本**: c l
- **差异**: `cl` vs `CL`

**结论**: 两个模型均识别错误 ❌

---

### 样本 44: 2025_11_21_10_25_31.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 45: 2025_11_20_20_56_51.wav

**真实文本**: 障碍物绕行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>债碍务绕行`
- **识别文本**: 债碍务绕行
- **差异**: `债碍务绕行` vs `障碍物绕行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行`
- **识别文本**: 障碍物绕行

**结论**: 微调模型改进 ⬆️

---

### 样本 46: 2025_11_17_13_47_13.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|EMO_UNKNOWN|><|Speech|><|woitn|>执行`
- **识别文本**: 执行
- **差异**: `执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>执行`
- **识别文本**: 执行
- **差异**: `执行` vs `路口直行`

**结论**: 两个模型均识别错误 ❌

---

### 样本 47: 2025_11_17_14_02_50.wav

**真实文本**: 路口左转 旁边车道有大车距离较近 接管压力性2分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转旁边车道有大车距离较近接管压力性二分`
- **识别文本**: 路口左转旁边车道有大车距离较近接管压力性二分
- **差异**: `路口左转旁边车道有大车距离较近接管压力性二分` vs `路口左转旁边车道有大车距离较近接管压力性2分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转 旁边车道有大车距离较近 接管压力性2分`
- **识别文本**: 路口左转 旁边车道有大车距离较近 接管压力性2分

**结论**: 微调模型改进 ⬆️

---

### 样本 48: 2025_11_21_14_49_37.wav

**真实文本**: 开始测试

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

**结论**: 两个模型均识别正确 ✅

---

### 样本 49: 2025_11_20_20_32_58.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航面道`
- **识别文本**: 导航面道
- **差异**: `导航面道` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 50: 2025_11_20_23_09_03.wav

**真实文本**: 环岛 这个环岛表现很差 在车道中间选择错误的车道 舒适性2分 预测性2分 剪辑

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛这个环岛表现很差在车道中间选择错误的车道舒适性两分越性两分剪辑`
- **识别文本**: 环岛这个环岛表现很差在车道中间选择错误的车道舒适性两分越性两分剪辑
- **差异**: `环岛这个环岛表现很差在车道中间选择错误的车道舒适性两分越性两分剪辑` vs `环岛这个环岛表现很差在车道中间选择错误的车道舒适性2分预测性2分剪辑`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛 这个环岛表现很差 在车道中间选择错误的车道 舒适性两分 预测性2分 剪辑`
- **识别文本**: 环岛 这个环岛表现很差 在车道中间选择错误的车道 舒适性两分 预测性2分 剪辑
- **差异**: `环岛这个环岛表现很差在车道中间选择错误的车道舒适性两分预测性2分剪辑` vs `环岛这个环岛表现很差在车道中间选择错误的车道舒适性2分预测性2分剪辑`

**结论**: 两个模型均识别错误 ❌

---

### 样本 51: 2025_11_21_21_54_25.wav

**真实文本**: VRU Handling

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>v r u handle`
- **识别文本**: v r u handle
- **差异**: `vruhandle` vs `VRUHandling`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>v r u handling`
- **识别文本**: v r u handling
- **差异**: `vruhandling` vs `VRUHandling`

**结论**: 两个模型均识别错误 ❌

---

### 样本 52: 2025_11_17_13_33_33.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 53: 2025_11_17_13_32_02.wav

**真实文本**: 避让变道 无障碍物 剪辑

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|BGM|><|woitn|>避让便道无障碍物剪辑`
- **识别文本**: 避让便道无障碍物剪辑
- **差异**: `避让便道无障碍物剪辑` vs `避让变道无障碍物剪辑`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>避让变道 无障碍物 剪辑`
- **识别文本**: 避让变道 无障碍物 剪辑

**结论**: 微调模型改进 ⬆️

---

### 样本 54: 2025_11_21_10_15_49.wav

**真实文本**: 前车切入 车辆有减速 舒适性5分 预测性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>前车前入车辆有减速舒适性五分预测性五分`
- **识别文本**: 前车前入车辆有减速舒适性五分预测性五分
- **差异**: `前车前入车辆有减速舒适性五分预测性五分` vs `前车切入车辆有减速舒适性5分预测性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>前车切入 车辆有减速 舒适性5分 预测性5分`
- **识别文本**: 前车切入 车辆有减速 舒适性5分 预测性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 55: 2025_11_21_21_59_04.wav

**真实文本**: Change Lane

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>chanch lion`
- **识别文本**: chanch lion
- **差异**: `chanchlion` vs `ChangeLane`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>change lion`
- **识别文本**: change lion
- **差异**: `changelion` vs `ChangeLane`

**结论**: 两个模型均识别错误 ❌

---

### 样本 56: 2025_11_20_23_16_24.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 57: 2025_11_20_20_33_37.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 58: 2025_11_20_19_42_21.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 59: 2025_11_21_15_28_56.wav

**真实文本**: 环岛 可以接受

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛可以接收`
- **识别文本**: 环岛可以接收
- **差异**: `环岛可以接收` vs `环岛可以接受`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛 可以接受`
- **识别文本**: 环岛 可以接受

**结论**: 微调模型改进 ⬆️

---

### 样本 60: 2025_11_20_20_57_03.wav

**真实文本**: 路口直行 在碰到路口处有对向左转车辆时 能够提前减速刹车避让 预测性6分 舒适性6分 压力性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行在碰到路口处有对向左转车辆时能够提前减速刹车避让预测性六分舒适性六分压力性五分`
- **识别文本**: 路口直行在碰到路口处有对向左转车辆时能够提前减速刹车避让预测性六分舒适性六分压力性五分
- **差异**: `路口直行在碰到路口处有对向左转车辆时能够提前减速刹车避让预测性六分舒适性六分压力性五分` vs `路口直行在碰到路口处有对向左转车辆时能够提前减速刹车避让预测性6分舒适性6分压力性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 在碰到路口处有对向左转车辆时 能够提前减速刹车避让 预测性6分 舒适性6分 压力性5分`
- **识别文本**: 路口直行 在碰到路口处有对向左转车辆时 能够提前减速刹车避让 预测性6分 舒适性6分 压力性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 61: 2025_11_20_22_57_21.wav

**真实文本**: 障碍物绕行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍勿绕行`
- **识别文本**: 障碍勿绕行
- **差异**: `障碍勿绕行` vs `障碍物绕行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行`
- **识别文本**: 障碍物绕行

**结论**: 微调模型改进 ⬆️

---

### 样本 62: 2025_11_21_15_17_08.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 63: 2025_11_20_22_53_20.wav

**真实文本**: 弱势群体 当右边出现送外卖小哥时 能够及时刹车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体当右边出现送外卖小哥时能够及时刹车`
- **识别文本**: 弱势群体当右边出现送外卖小哥时能够及时刹车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 当右边出现送外卖小哥时 能够及时刹车`
- **识别文本**: 弱势群体 当右边出现送外卖小哥时 能够及时刹车

**结论**: 两个模型均识别正确 ✅

---

### 样本 64: 2025_11_21_15_34_40.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 65: 2025_11_21_14_29_51.wav

**真实文本**: 路口直行在夜间没有红绿灯的路口通过不减速 压力性3分 效率性3分 预测性三分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行在夜间没有红绿灯的路口通过不减速压力性三分效率性三分预测性三分`
- **识别文本**: 路口直行在夜间没有红绿灯的路口通过不减速压力性三分效率性三分预测性三分
- **差异**: `路口直行在夜间没有红绿灯的路口通过不减速压力性三分效率性三分预测性三分` vs `路口直行在夜间没有红绿灯的路口通过不减速压力性3分效率性3分预测性三分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 在夜间没有红绿灯的路口 通过不减速 压力性3分 效率性3分 预测性3分`
- **识别文本**: 路口直行 在夜间没有红绿灯的路口 通过不减速 压力性3分 效率性3分 预测性3分
- **差异**: `路口直行在夜间没有红绿灯的路口通过不减速压力性3分效率性3分预测性3分` vs `路口直行在夜间没有红绿灯的路口通过不减速压力性3分效率性3分预测性三分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 66: 2025_11_17_13_56_10.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>执行`
- **识别文本**: 执行
- **差异**: `执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>直行`
- **识别文本**: 直行
- **差异**: `直行` vs `路口直行`

**结论**: 两个模型均识别错误 ❌

---

### 样本 67: 2025_11_20_21_01_46.wav

**真实文本**: 环岛 预测性3分 还是老问题

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛预测性三分还是老问题`
- **识别文本**: 环岛预测性三分还是老问题
- **差异**: `环岛预测性三分还是老问题` vs `环岛预测性3分还是老问题`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛 预测性3分 还是老问题`
- **识别文本**: 环岛 预测性3分 还是老问题

**结论**: 微调模型改进 ⬆️

---

### 样本 68: 2025_11_20_19_56_16.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>lo口执行`
- **识别文本**: lo口执行
- **差异**: `lo口执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 69: 2025_11_21_10_43_02.wav

**真实文本**: Junction straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>dunkson street`
- **识别文本**: dunkson street
- **差异**: `dunksonstreet` vs `Junctionstraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>dunkson street`
- **识别文本**: dunkson street
- **差异**: `dunksonstreet` vs `Junctionstraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 70: 2025_11_21_13_20_52.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 71: 2025_11_20_23_22_58.wav

**真实文本**: 测试结束

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>测试结束`
- **识别文本**: 测试结束

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>测试结束`
- **识别文本**: 测试结束

**结论**: 两个模型均识别正确 ✅

---

### 样本 72: 2025_11_21_14_21_31.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|SAD|><|Speech|><|woitn|>导航便道`
- **识别文本**: 导航便道
- **差异**: `导航便道` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 73: 2025_11_17_13_55_12.wav

**真实文本**: 其他 开启车道巡航 没有到位

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|BGM|><|woitn|>其他开启车道巡航没有到位`
- **识别文本**: 其他开启车道巡航没有到位

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他 开启车道巡航 没有到位`
- **识别文本**: 其他 开启车道巡航 没有到位

**结论**: 两个模型均识别正确 ✅

---

### 样本 74: 2025_11_20_20_04_29.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>党面闹`
- **识别文本**: 党面闹
- **差异**: `党面闹` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 75: 2025_11_20_22_51_08.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>落后执行`
- **识别文本**: 落后执行
- **差异**: `落后执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 76: 2025_11_20_19_39_19.wav

**真实文本**: 路口直行 在旁边车辆车辆切入的时候 不选择避让旁边车辆 有点抢路 压力性3分 舒适性3分 效率性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行在旁边车辆车辆切入的时候不选择避让旁边车辆有点抢路压力性三分舒适性三分效率性五分`
- **识别文本**: 路口直行在旁边车辆车辆切入的时候不选择避让旁边车辆有点抢路压力性三分舒适性三分效率性五分
- **差异**: `路口直行在旁边车辆车辆切入的时候不选择避让旁边车辆有点抢路压力性三分舒适性三分效率性五分` vs `路口直行在旁边车辆车辆切入的时候不选择避让旁边车辆有点抢路压力性3分舒适性3分效率性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 在旁边车辆车辆切入的时候 不选择避让旁边车辆有点抢入 压力性3分 舒适性3分 效率性5分`
- **识别文本**: 路口直行 在旁边车辆车辆切入的时候 不选择避让旁边车辆有点抢入 压力性3分 舒适性3分 效率性5分
- **差异**: `路口直行在旁边车辆车辆切入的时候不选择避让旁边车辆有点抢入压力性3分舒适性3分效率性5分` vs `路口直行在旁边车辆车辆切入的时候不选择避让旁边车辆有点抢路压力性3分舒适性3分效率性5分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 77: 2025_11_20_20_42_16.wav

**真实文本**: 跟车 KD 受到旁边车辆影响 误减速 NSS 舒适性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>跟车 k d 受到旁边车辆影响物减速 n s s 舒适性三分`
- **识别文本**: 跟车 k d 受到旁边车辆影响物减速 n s s 舒适性三分
- **差异**: `跟车kd受到旁边车辆影响物减速nss舒适性三分` vs `跟车KD受到旁边车辆影响误减速NSS舒适性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>跟车KD 受到旁边车辆影响 误减速 NSS 舒适性3分`
- **识别文本**: 跟车KD 受到旁边车辆影响 误减速 NSS 舒适性3分

**结论**: 微调模型改进 ⬆️

---

### 样本 78: 2025_11_20_23_19_37.wav

**真实文本**: 障碍物绕行 避让旁边公交车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行避让旁边公交车`
- **识别文本**: 障碍物绕行避让旁边公交车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行 避让旁边公交车`
- **识别文本**: 障碍物绕行 避让旁边公交车

**结论**: 两个模型均识别正确 ✅

---

### 样本 79: 2025_11_17_13_32_22.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|BGM|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 80: 2025_11_21_15_46_49.wav

**真实文本**: 车道保持 一直压黄色车道线 压力性三分 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保持一直压黄色车道线压力性三分预测性三分`
- **识别文本**: 车道保持一直压黄色车道线压力性三分预测性三分
- **差异**: `车道保持一直压黄色车道线压力性三分预测性三分` vs `车道保持一直压黄色车道线压力性三分预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保持 一直压黄色车道线 压力性3分 预测性3分`
- **识别文本**: 车道保持 一直压黄色车道线 压力性3分 预测性3分
- **差异**: `车道保持一直压黄色车道线压力性3分预测性3分` vs `车道保持一直压黄色车道线压力性三分预测性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 81: 2025_11_21_15_45_04.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 82: 2025_11_21_13_36_48.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 83: 2025_11_20_22_58_56.wav

**真实文本**: 汇出变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绘除变道`
- **识别文本**: 绘除变道
- **差异**: `绘除变道` vs `汇出变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>汇出变道`
- **识别文本**: 汇出变道

**结论**: 微调模型改进 ⬆️

---

### 样本 84: 2025_11_17_13_43_53.wav

**真实文本**: 测试结束

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>测试结束`
- **识别文本**: 测试结束

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>测试测束`
- **识别文本**: 测试测束
- **差异**: `测试测束` vs `测试结束`

**结论**: 微调模型退化 ⬇️

---

### 样本 85: 2025_11_20_20_39_40.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 86: 2025_11_20_20_12_09.wav

**真实文本**: 路口直行 直行过程中变了个道 没问题

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行直行过程中变了个道没问题`
- **识别文本**: 路口直行直行过程中变了个道没问题

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 直行过程中变了个道 没问题`
- **识别文本**: 路口直行 直行过程中变了个道 没问题

**结论**: 两个模型均识别正确 ✅

---

### 样本 87: 2025_11_20_20_32_13.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 88: 2025_11_21_10_42_20.wav

**真实文本**: Red Light Following

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|SAD|><|Speech|><|woitn|>rightd light following`
- **识别文本**: rightd light following
- **差异**: `rightdlightfollowing` vs `RedLightFollowing`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>red light following`
- **识别文本**: red light following
- **差异**: `redlightfollowing` vs `RedLightFollowing`

**结论**: 两个模型均识别错误 ❌

---

### 样本 89: 2025_11_17_13_33_06.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|BGM|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 90: 2025_11_17_13_57_50.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 91: 2025_11_21_14_03_08.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 92: 2025_11_20_23_15_22.wav

**真实文本**: 弱势群体 避让路中间站着的老人 预测性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体必让路中间站着的老人约得见五分`
- **识别文本**: 弱势群体必让路中间站着的老人约得见五分
- **差异**: `弱势群体必让路中间站着的老人约得见五分` vs `弱势群体避让路中间站着的老人预测性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 避让路中间站着的老人 预测性5分`
- **识别文本**: 弱势群体 避让路中间站着的老人 预测性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 93: 2025_11_20_23_18_52.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 94: 2025_11_17_13_42_00.wav

**真实文本**: 避让障碍物

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>避让障碍物`
- **识别文本**: 避让障碍物

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>避让障碍物`
- **识别文本**: 避让障碍物

**结论**: 两个模型均识别正确 ✅

---

### 样本 95: 2025_11_21_14_04_19.wav

**真实文本**: 开始测试

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

**结论**: 两个模型均识别正确 ✅

---

### 样本 96: 2025_11_20_20_35_50.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 97: 2025_11_21_13_37_52.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 98: 2025_11_21_13_16_38.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 99: 2025_11_21_15_41_38.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 100: 2025_11_20_23_21_05.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 101: 2025_11_20_23_15_41.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红了跟车`
- **识别文本**: 红了跟车
- **差异**: `红了跟车` vs `红灯跟车`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红了跟车`
- **识别文本**: 红了跟车
- **差异**: `红了跟车` vs `红灯跟车`

**结论**: 两个模型均识别错误 ❌

---

### 样本 102: 2025_11_17_13_44_30.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|BGM|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 103: 2025_11_17_13_32_55.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|BGM|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 104: 2025_11_21_15_45_55.wav

**真实文本**: 左前方车辆切入本车一直压左侧车道线行驶 且未减速 有碰撞风险 压力性2分 预测性2分 剪辑

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>左前方车辆切入本车一直压左侧车道线行驶且未减速有碰撞风险压力性二分预测性二分剪辑`
- **识别文本**: 左前方车辆切入本车一直压左侧车道线行驶且未减速有碰撞风险压力性二分预测性二分剪辑
- **差异**: `左前方车辆切入本车一直压左侧车道线行驶且未减速有碰撞风险压力性二分预测性二分剪辑` vs `左前方车辆切入本车一直压左侧车道线行驶且未减速有碰撞风险压力性2分预测性2分剪辑`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>左前方车辆切入 本车一直压左侧车道线行驶 且未减速 有碰撞风险 压力性2分 预测性2分 剪辑`
- **识别文本**: 左前方车辆切入 本车一直压左侧车道线行驶 且未减速 有碰撞风险 压力性2分 预测性2分 剪辑

**结论**: 微调模型改进 ⬆️

---

### 样本 105: 2025_11_21_10_18_17.wav

**真实文本**: 路口直行 过路口时受到对向向左转弯车影响 停在路口中间 效率性两分 压力性两分 预测性2分 剪辑

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行过路口时受到对向向左转弯车影响停在路口中间小路行两分压力性两分预测性二分剪急`
- **识别文本**: 路口直行过路口时受到对向向左转弯车影响停在路口中间小路行两分压力性两分预测性二分剪急
- **差异**: `路口直行过路口时受到对向向左转弯车影响停在路口中间小路行两分压力性两分预测性二分剪急` vs `路口直行过路口时受到对向向左转弯车影响停在路口中间效率性两分压力性两分预测性2分剪辑`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 过路口时受到对向向左转弯车影响 停在路口中间 效率性2分 压力性2分 预测性2分 剪辑`
- **识别文本**: 路口直行 过路口时受到对向向左转弯车影响 停在路口中间 效率性2分 压力性2分 预测性2分 剪辑
- **差异**: `路口直行过路口时受到对向向左转弯车影响停在路口中间效率性2分压力性2分预测性2分剪辑` vs `路口直行过路口时受到对向向左转弯车影响停在路口中间效率性两分压力性两分预测性2分剪辑`

**结论**: 两个模型均识别错误 ❌

---

### 样本 106: 2025_11_20_20_30_23.wav

**真实文本**: 路口右转 右转非常犹豫 且离右边很近 预测性2分 压力性2分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转右转非常犹豫且离右边很近预测性两分压力性两分`
- **识别文本**: 路口右转右转非常犹豫且离右边很近预测性两分压力性两分
- **差异**: `路口右转右转非常犹豫且离右边很近预测性两分压力性两分` vs `路口右转右转非常犹豫且离右边很近预测性2分压力性2分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转 右转非常犹豫 且离右边很近 预测性2分 压力性2分`
- **识别文本**: 路口右转 右转非常犹豫 且离右边很近 预测性2分 压力性2分

**结论**: 微调模型改进 ⬆️

---

### 样本 107: 2025_11_21_10_26_22.wav

**真实文本**: 弱势群体 在路口直行过程中 受弱势群体的不必要减速至停止 效率性二分 预测性2分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体在路口执行过程中受弱势群体的不必要减速至停止效率性二分预测性二分`
- **识别文本**: 弱势群体在路口执行过程中受弱势群体的不必要减速至停止效率性二分预测性二分
- **差异**: `弱势群体在路口执行过程中受弱势群体的不必要减速至停止效率性二分预测性二分` vs `弱势群体在路口直行过程中受弱势群体的不必要减速至停止效率性二分预测性2分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 在路口直行过程中 受弱势群体的不必要减速 致停止 效率性2分 预测性2分`
- **识别文本**: 弱势群体 在路口直行过程中 受弱势群体的不必要减速 致停止 效率性2分 预测性2分
- **差异**: `弱势群体在路口直行过程中受弱势群体的不必要减速致停止效率性2分预测性2分` vs `弱势群体在路口直行过程中受弱势群体的不必要减速至停止效率性二分预测性2分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 108: 2025_11_21_15_30_10.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口之星`
- **识别文本**: 路口之星
- **差异**: `路口之星` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 109: 2025_11_21_15_37_58.wav

**真实文本**: 路口左转

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转`
- **识别文本**: 路口左转

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转`
- **识别文本**: 路口左转

**结论**: 两个模型均识别正确 ✅

---

### 样本 110: 2025_11_20_20_54_40.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 111: 2025_11_21_10_11_11.wav

**真实文本**: 障碍物绕行 右方有这个电动车本车向左轻微绕行 舒适性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行右方有这个电动车本车向左轻微绕行舒适性五分`
- **识别文本**: 障碍物绕行右方有这个电动车本车向左轻微绕行舒适性五分
- **差异**: `障碍物绕行右方有这个电动车本车向左轻微绕行舒适性五分` vs `障碍物绕行右方有这个电动车本车向左轻微绕行舒适性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行 右方有这个电动车 本车向左轻微绕行 舒适性5分`
- **识别文本**: 障碍物绕行 右方有这个电动车 本车向左轻微绕行 舒适性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 112: 2025_11_17_13_54_13.wav

**真实文本**: 汇入

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>魏入`
- **识别文本**: 魏入
- **差异**: `魏入` vs `汇入`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>未入`
- **识别文本**: 未入
- **差异**: `未入` vs `汇入`

**结论**: 两个模型均识别错误 ❌

---

### 样本 113: 2025_11_21_10_15_34.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 114: 2025_11_21_21_56_41.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>junction street`
- **识别文本**: junction street
- **差异**: `junctionstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>junction street`
- **识别文本**: junction street
- **差异**: `junctionstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 115: 2025_11_21_15_38_00.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 116: 2025_11_17_13_53_45.wav

**真实文本**: 弱势群体

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>我是群体`
- **识别文本**: 我是群体
- **差异**: `我是群体` vs `弱势群体`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱是群体`
- **识别文本**: 弱是群体
- **差异**: `弱是群体` vs `弱势群体`

**结论**: 两个模型均识别错误 ❌

---

### 样本 117: 2025_11_21_10_44_23.wav

**真实文本**: Bypass Obstacle

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>bypas obstacle`
- **识别文本**: bypas obstacle
- **差异**: `bypasobstacle` vs `BypassObstacle`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>bypas obstacle`
- **识别文本**: bypas obstacle
- **差异**: `bypasobstacle` vs `BypassObstacle`

**结论**: 两个模型均识别错误 ❌

---

### 样本 118: 2025_11_21_15_40_29.wav

**真实文本**: 其他 在园区内可以开启智驾

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他在园区内可以开启支架`
- **识别文本**: 其他在园区内可以开启支架
- **差异**: `其他在园区内可以开启支架` vs `其他在园区内可以开启智驾`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他 在园区内可以开启自驾`
- **识别文本**: 其他 在园区内可以开启自驾
- **差异**: `其他在园区内可以开启自驾` vs `其他在园区内可以开启智驾`

**结论**: 两个模型均识别错误 ❌

---

### 样本 119: 2025_11_21_21_57_04.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juhnction street`
- **识别文本**: juhnction street
- **差异**: `juhnctionstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juhnction street`
- **识别文本**: juhnction street
- **差异**: `juhnctionstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 120: 2025_11_17_13_56_40.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯奔车`
- **识别文本**: 红灯奔车
- **差异**: `红灯奔车` vs `红灯跟车`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 微调模型改进 ⬆️

---

### 样本 121: 2025_11_21_13_21_25.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 122: 2025_11_17_13_49_11.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>重刚跟车`
- **识别文本**: 重刚跟车
- **差异**: `重刚跟车` vs `红灯跟车`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 微调模型改进 ⬆️

---

### 样本 123: 2025_11_21_10_43_15.wav

**真实文本**: Junction Turn

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>dction turn`
- **识别文本**: dction turn
- **差异**: `dctionturn` vs `JunctionTurn`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>dction turn`
- **识别文本**: dction turn
- **差异**: `dctionturn` vs `JunctionTurn`

**结论**: 两个模型均识别错误 ❌

---

### 样本 124: 2025_11_21_21_54_32.wav

**真实文本**: VRU Handling

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>v r u 憨豆岭`
- **识别文本**: v r u 憨豆岭
- **差异**: `vru憨豆岭` vs `VRUHandling`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>v areU handling`
- **识别文本**: v areU handling
- **差异**: `vareUhandling` vs `VRUHandling`

**结论**: 两个模型均识别错误 ❌

---

### 样本 125: 2025_11_20_23_22_20.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 126: 2025_11_20_23_18_04.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>绿豆`
- **识别文本**: 绿豆
- **差异**: `绿豆` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>绿道`
- **识别文本**: 绿道
- **差异**: `绿道` vs `绿灯`

**结论**: 两个模型均识别错误 ❌

---

### 样本 127: 2025_11_20_23_04_46.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 128: 2025_11_20_22_56_34.wav

**真实文本**: 弱势群体 躲避对向车道来的弱势群体 向右打了把方向

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体躲避对象车道来的弱势群体向又打了把方向`
- **识别文本**: 弱势群体躲避对象车道来的弱势群体向又打了把方向
- **差异**: `弱势群体躲避对象车道来的弱势群体向又打了把方向` vs `弱势群体躲避对向车道来的弱势群体向右打了把方向`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 躲避对象车道来的弱势群体 性又打了把方向`
- **识别文本**: 弱势群体 躲避对象车道来的弱势群体 性又打了把方向
- **差异**: `弱势群体躲避对象车道来的弱势群体性又打了把方向` vs `弱势群体躲避对向车道来的弱势群体向右打了把方向`

**结论**: 两个模型均识别错误 ❌

---

### 样本 129: 2025_11_21_15_29_30.wav

**真实文本**: 环岛结束后 走 两条路中间压虚线 然后再向左边动 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛结束后走两条路中间压虚线然后再向左变动预测性三分`
- **识别文本**: 环岛结束后走两条路中间压虚线然后再向左变动预测性三分
- **差异**: `环岛结束后走两条路中间压虚线然后再向左变动预测性三分` vs `环岛结束后走两条路中间压虚线然后再向左边动预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛结束后 走两条路中间压虚线 然后再向左变动 预测性3分`
- **识别文本**: 环岛结束后 走两条路中间压虚线 然后再向左变动 预测性3分
- **差异**: `环岛结束后走两条路中间压虚线然后再向左变动预测性3分` vs `环岛结束后走两条路中间压虚线然后再向左边动预测性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 130: 2025_11_20_20_17_26.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯儿`
- **识别文本**: 绿灯儿
- **差异**: `绿灯儿` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 微调模型改进 ⬆️

---

### 样本 131: 2025_11_21_15_28_25.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 132: 2025_11_21_21_54_15.wav

**真实文本**: VRU Handling

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>we are you handling`
- **识别文本**: we are you handling
- **差异**: `weareyouhandling` vs `VRUHandling`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>v are you handling`
- **识别文本**: v are you handling
- **差异**: `vareyouhandling` vs `VRUHandling`

**结论**: 两个模型均识别错误 ❌

---

### 样本 133: 2025_11_17_14_03_13.wav

**真实文本**: 道路切换

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>道路切换四八二八`
- **识别文本**: 道路切换四八二八
- **差异**: `道路切换四八二八` vs `道路切换`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>道路切换4八28`
- **识别文本**: 道路切换4八28
- **差异**: `道路切换4八28` vs `道路切换`

**结论**: 两个模型均识别错误 ❌

---

### 样本 134: 2025_11_20_20_46_32.wav

**真实文本**: 障碍物绕行 华为在停车场里表现总体来说不错 在窄路中绕行障碍物 预测性5分 压力性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行华为在停车场里表现总体来说不错在载录中绕行障碍物预测性五分压力线五分`
- **识别文本**: 障碍物绕行华为在停车场里表现总体来说不错在载录中绕行障碍物预测性五分压力线五分
- **差异**: `障碍物绕行华为在停车场里表现总体来说不错在载录中绕行障碍物预测性五分压力线五分` vs `障碍物绕行华为在停车场里表现总体来说不错在窄路中绕行障碍物预测性5分压力性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行 华为在停车场里表现总体来说不错 在窄路中绕行障碍物 预测性5分 压力性5分`
- **识别文本**: 障碍物绕行 华为在停车场里表现总体来说不错 在窄路中绕行障碍物 预测性5分 压力性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 135: 2025_11_20_19_53_19.wav

**真实文本**: 弱势群体避让 它选择去避让一个还有很久才能过来的自行车 效率性三分 压力性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体避让他选择去避让一个还有很久才能过来的自行车效率性三分压力性五分`
- **识别文本**: 弱势群体避让他选择去避让一个还有很久才能过来的自行车效率性三分压力性五分
- **差异**: `弱势群体避让他选择去避让一个还有很久才能过来的自行车效率性三分压力性五分` vs `弱势群体避让它选择去避让一个还有很久才能过来的自行车效率性三分压力性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体避让 他选择去避让一个还有很久才能过来的自行车 效率性3分 压力性5分`
- **识别文本**: 弱势群体避让 他选择去避让一个还有很久才能过来的自行车 效率性3分 压力性5分
- **差异**: `弱势群体避让他选择去避让一个还有很久才能过来的自行车效率性3分压力性5分` vs `弱势群体避让它选择去避让一个还有很久才能过来的自行车效率性三分压力性5分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 136: 2025_11_17_13_58_08.wav

**真实文本**: 开始测试

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

**结论**: 两个模型均识别正确 ✅

---

### 样本 137: 2025_11_21_10_12_05.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 138: 2025_11_21_15_47_05.wav

**真实文本**: 弱势群体 识别路边 临停停止的电动三轮车有绕行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体识别路边临停停止的电动三轮车有绕行`
- **识别文本**: 弱势群体识别路边临停停止的电动三轮车有绕行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 识别路边临停停止的电动三轮车有绕行`
- **识别文本**: 弱势群体 识别路边临停停止的电动三轮车有绕行

**结论**: 两个模型均识别正确 ✅

---

### 样本 139: 2025_11_20_20_34_01.wav

**真实文本**: 环岛 环岛后路线规划有点问题 预测性三分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环导环岛后路线规划有点问题预测性三分`
- **识别文本**: 环导环岛后路线规划有点问题预测性三分
- **差异**: `环导环岛后路线规划有点问题预测性三分` vs `环岛环岛后路线规划有点问题预测性三分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛 环岛后路线规划有点问题 预测性3分`
- **识别文本**: 环岛 环岛后路线规划有点问题 预测性3分
- **差异**: `环岛环岛后路线规划有点问题预测性3分` vs `环岛环岛后路线规划有点问题预测性三分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 140: 2025_11_21_13_37_43.wav

**真实文本**: 路口右转

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转`
- **识别文本**: 路口右转

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转`
- **识别文本**: 路口右转

**结论**: 两个模型均识别正确 ✅

---

### 样本 141: 2025_11_21_15_47_46.wav

**真实文本**: 障碍物绕行 识别旁边 停止的车辆有绕行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行识别旁边停止的车辆有绕行`
- **识别文本**: 障碍物绕行识别旁边停止的车辆有绕行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行 识别旁边停止的车辆 有绕行`
- **识别文本**: 障碍物绕行 识别旁边停止的车辆 有绕行

**结论**: 两个模型均识别正确 ✅

---

### 样本 142: 2025_11_20_22_50_03.wav

**真实文本**: 路口右转 受到左侧车辆影响 在出口有个减速 但是那辆车还很远 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转受到左左侧车辆影响在出口有个减速但是那辆车很还很远预测性三分`
- **识别文本**: 路口右转受到左左侧车辆影响在出口有个减速但是那辆车很还很远预测性三分
- **差异**: `路口右转受到左左侧车辆影响在出口有个减速但是那辆车很还很远预测性三分` vs `路口右转受到左侧车辆影响在出口有个减速但是那辆车还很远预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转 受到左左侧车辆影响 在出口有个减速 但是那辆车很还很远 预测性3分`
- **识别文本**: 路口右转 受到左左侧车辆影响 在出口有个减速 但是那辆车很还很远 预测性3分
- **差异**: `路口右转受到左左侧车辆影响在出口有个减速但是那辆车很还很远预测性3分` vs `路口右转受到左侧车辆影响在出口有个减速但是那辆车还很远预测性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 143: 2025_11_21_13_15_22.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 144: 2025_11_20_23_22_27.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 145: 2025_11_21_10_40_09.wav

**真实文本**: Others

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>other`
- **识别文本**: other
- **差异**: `other` vs `Others`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>other`
- **识别文本**: other
- **差异**: `other` vs `Others`

**结论**: 两个模型均识别错误 ❌

---

### 样本 146: 2025_11_21_10_45_14.wav

**真实文本**: Green Light

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>green light`
- **识别文本**: green light
- **差异**: `greenlight` vs `GreenLight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>green light`
- **识别文本**: green light
- **差异**: `greenlight` vs `GreenLight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 147: 2025_11_20_19_39_56.wav

**真实文本**: 路口直行 路口直行后选择变道 离旁边车辆太近了 预测性一分 压力性一分 舒适性 四分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行路口直行后选择变道离旁边车辆太近了预测性一分压力性一分舒适性四分`
- **识别文本**: 路口直行路口直行后选择变道离旁边车辆太近了预测性一分压力性一分舒适性四分

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 路口直行后选择变道 离旁边车辆太近了 预测性1分 压力性1分 舒适性4分`
- **识别文本**: 路口直行 路口直行后选择变道 离旁边车辆太近了 预测性1分 压力性1分 舒适性4分
- **差异**: `路口直行路口直行后选择变道离旁边车辆太近了预测性1分压力性1分舒适性4分` vs `路口直行路口直行后选择变道离旁边车辆太近了预测性一分压力性一分舒适性四分`

**结论**: 微调模型退化 ⬇️

---

### 样本 148: 2025_11_20_20_56_09.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿东`
- **识别文本**: 绿东
- **差异**: `绿东` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 微调模型改进 ⬆️

---

### 样本 149: 2025_11_21_15_36_59.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 150: 2025_11_20_20_48_09.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 151: 2025_11_21_15_34_25.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口执行`
- **识别文本**: 路口执行
- **差异**: `路口执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 152: 2025_11_20_20_14_14.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 153: 2025_11_21_15_25_37.wav

**真实文本**: 路口直行 当对象来车想要左转时 没有提前减速 停车 而是选择开到了离对象车很近的位置 跟他对上 预测性两分 压力性2分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行当对象来车想要左转时没有提前减速停车而是选择开到了离对象车很近的位置跟他对上预测性两分压力性两分`
- **识别文本**: 路口直行当对象来车想要左转时没有提前减速停车而是选择开到了离对象车很近的位置跟他对上预测性两分压力性两分
- **差异**: `路口直行当对象来车想要左转时没有提前减速停车而是选择开到了离对象车很近的位置跟他对上预测性两分压力性两分` vs `路口直行当对象来车想要左转时没有提前减速停车而是选择开到了离对象车很近的位置跟他对上预测性两分压力性2分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 当对向来车 想要左转时没有提前减速停车 而是选择开到了离对象车很近的位置 跟他对上 预测性2分 压力性2分`
- **识别文本**: 路口直行 当对向来车 想要左转时没有提前减速停车 而是选择开到了离对象车很近的位置 跟他对上 预测性2分 压力性2分
- **差异**: `路口直行当对向来车想要左转时没有提前减速停车而是选择开到了离对象车很近的位置跟他对上预测性2分压力性2分` vs `路口直行当对象来车想要左转时没有提前减速停车而是选择开到了离对象车很近的位置跟他对上预测性两分压力性2分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 154: 2025_11_21_14_02_37.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 155: 2025_11_21_14_29_12.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 156: 2025_11_21_15_42_55.wav

**真实文本**: 路口右转

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转`
- **识别文本**: 路口右转

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转`
- **识别文本**: 路口右转

**结论**: 两个模型均识别正确 ✅

---

### 样本 157: 2025_11_21_14_52_46.wav

**真实文本**: 车到保持 大堤路 向右转弯的时候压实线 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保持大堤路向右转弯时候压实线预测性三分`
- **识别文本**: 车道保持大堤路向右转弯时候压实线预测性三分
- **差异**: `车道保持大堤路向右转弯时候压实线预测性三分` vs `车到保持大堤路向右转弯的时候压实线预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保持 大堤路向右转弯时候 压实线 预测性3分`
- **识别文本**: 车道保持 大堤路向右转弯时候 压实线 预测性3分
- **差异**: `车道保持大堤路向右转弯时候压实线预测性3分` vs `车到保持大堤路向右转弯的时候压实线预测性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 158: 2025_11_20_23_14_20.wav

**真实文本**: 弱势群体 变道时躲避左侧电瓶车辆减速

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体变道时躲避左侧电瓶车辆减速`
- **识别文本**: 弱势群体变道时躲避左侧电瓶车辆减速

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 变道时 躲避左侧电瓶车辆减速`
- **识别文本**: 弱势群体 变道时 躲避左侧电瓶车辆减速

**结论**: 两个模型均识别正确 ✅

---

### 样本 159: 2025_11_20_23_03_42.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>倒霉到`
- **识别文本**: 倒霉到
- **差异**: `倒霉到` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>到没岛`
- **识别文本**: 到没岛
- **差异**: `到没岛` vs `导航变道`

**结论**: 两个模型均识别错误 ❌

---

### 样本 160: 2025_11_21_14_52_16.wav

**真实文本**: 车道保持 在大路上频繁的 压左边线 刚才还回去 在左边画龙 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保持在大路上频繁的压左边线刚才还回去在左边画龙预测性三分`
- **识别文本**: 车道保持在大路上频繁的压左边线刚才还回去在左边画龙预测性三分
- **差异**: `车道保持在大路上频繁的压左边线刚才还回去在左边画龙预测性三分` vs `车道保持在大路上频繁的压左边线刚才还回去在左边画龙预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保持 在大路上频繁的压左边线 刚才还回去 在左边画龙 预测性3分`
- **识别文本**: 车道保持 在大路上频繁的压左边线 刚才还回去 在左边画龙 预测性3分

**结论**: 微调模型改进 ⬆️

---

### 样本 161: 2025_11_20_23_22_41.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 162: 2025_11_21_15_24_07.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 163: 2025_11_21_15_45_40.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 164: 2025_11_20_20_53_09.wav

**真实文本**: 超车变道 无效变道 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超时变道无效变道预测性三分`
- **识别文本**: 超时变道无效变道预测性三分
- **差异**: `超时变道无效变道预测性三分` vs `超车变道无效变道预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道 无效变道 预测性3分`
- **识别文本**: 超车变道 无效变道 预测性3分

**结论**: 微调模型改进 ⬆️

---

### 样本 165: 2025_11_21_21_58_32.wav

**真实文本**: Junction Turn

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juhnction turn`
- **识别文本**: juhnction turn
- **差异**: `juhnctionturn` vs `JunctionTurn`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>junction turn`
- **识别文本**: junction turn
- **差异**: `junctionturn` vs `JunctionTurn`

**结论**: 两个模型均识别错误 ❌

---

### 样本 166: 2025_11_17_13_31_31.wav

**真实文本**: 红灯领航

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航`
- **识别文本**: 红灯领航

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航`
- **识别文本**: 红灯领航

**结论**: 两个模型均识别正确 ✅

---

### 样本 167: 2025_11_21_10_44_05.wav

**真实文本**: VRU Handling

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>where are you handling`
- **识别文本**: where are you handling
- **差异**: `whereareyouhandling` vs `VRUHandling`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>where are you handling`
- **识别文本**: where are you handling
- **差异**: `whereareyouhandling` vs `VRUHandling`

**结论**: 两个模型均识别错误 ❌

---

### 样本 168: 2025_11_20_20_55_00.wav

**真实文本**: 红灯领航

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红辣两行`
- **识别文本**: 红辣两行
- **差异**: `红辣两行` vs `红灯领航`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红蓝领航`
- **识别文本**: 红蓝领航
- **差异**: `红蓝领航` vs `红灯领航`

**结论**: 两个模型均识别错误 ❌

---

### 样本 169: 2025_11_21_10_15_36.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿的`
- **识别文本**: 绿的
- **差异**: `绿的` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 微调模型改进 ⬆️

---

### 样本 170: 2025_11_21_21_53_34.wav

**真实文本**: VRU Handling

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>where are you handling豆`
- **识别文本**: where are you handling豆
- **差异**: `whereareyouhandling豆` vs `VRUHandling`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>where are you handling`
- **识别文本**: where are you handling
- **差异**: `whereareyouhandling` vs `VRUHandling`

**结论**: 两个模型均识别错误 ❌

---

### 样本 171: 2025_11_21_15_48_15.wav

**真实文本**: 弱势群体 识别路旁边 蹲下洗车的人 并且有减速

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体识别路边蹲下洗车的人并且有减速`
- **识别文本**: 弱势群体识别路边蹲下洗车的人并且有减速
- **差异**: `弱势群体识别路边蹲下洗车的人并且有减速` vs `弱势群体识别路旁边蹲下洗车的人并且有减速`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 识别路边蹲下写车的人 并且有减速`
- **识别文本**: 弱势群体 识别路边蹲下写车的人 并且有减速
- **差异**: `弱势群体识别路边蹲下写车的人并且有减速` vs `弱势群体识别路旁边蹲下洗车的人并且有减速`

**结论**: 两个模型均识别错误 ❌

---

### 样本 172: 2025_11_21_15_41_41.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 173: 2025_11_20_23_22_18.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 174: 2025_11_17_13_38_46.wav

**真实文本**: 其他 退出智驾 剪辑

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他退出支架剪击`
- **识别文本**: 其他退出支架剪击
- **差异**: `其他退出支架剪击` vs `其他退出智驾剪辑`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他 退出支架 剪辑`
- **识别文本**: 其他 退出支架 剪辑
- **差异**: `其他退出支架剪辑` vs `其他退出智驾剪辑`

**结论**: 两个模型均识别错误 ❌

---

### 样本 175: 2025_11_20_20_14_27.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>如何执行`
- **识别文本**: 如何执行
- **差异**: `如何执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 176: 2025_11_21_21_59_18.wav

**真实文本**: Change Lane

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>change lane`
- **识别文本**: change lane
- **差异**: `changelane` vs `ChangeLane`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>change lane`
- **识别文本**: change lane
- **差异**: `changelane` vs `ChangeLane`

**结论**: 两个模型均识别错误 ❌

---

### 样本 177: 2025_11_17_13_41_09.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|BGM|><|woitn|>执行`
- **识别文本**: 执行
- **差异**: `执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>直行`
- **识别文本**: 直行
- **差异**: `直行` vs `路口直行`

**结论**: 两个模型均识别错误 ❌

---

### 样本 178: 2025_11_20_20_30_02.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变到`
- **识别文本**: 导航变到
- **差异**: `导航变到` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 179: 2025_11_20_23_15_37.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 180: 2025_11_21_10_21_51.wav

**真实文本**: 限速信息 前方限速60 识别为50 自车车速60

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>限速信息前方限速六十识别为五十支车车速六十`
- **识别文本**: 限速信息前方限速六十识别为五十支车车速六十
- **差异**: `限速信息前方限速六十识别为五十支车车速六十` vs `限速信息前方限速60识别为50自车车速60`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>限速信息 前方限速60 识别为50 自车测速60`
- **识别文本**: 限速信息 前方限速60 识别为50 自车测速60
- **差异**: `限速信息前方限速60识别为50自车测速60` vs `限速信息前方限速60识别为50自车车速60`

**结论**: 两个模型均识别错误 ❌

---

### 样本 181: 2025_11_20_23_03_36.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>大棉袄`
- **识别文本**: 大棉袄
- **差异**: `大棉袄` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>大棉袄`
- **识别文本**: 大棉袄
- **差异**: `大棉袄` vs `导航变道`

**结论**: 两个模型均识别错误 ❌

---

### 样本 182: 2025_11_21_10_39_55.wav

**真实文本**: Bypass Obstacle

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>bypass obstacle`
- **识别文本**: bypass obstacle
- **差异**: `bypassobstacle` vs `BypassObstacle`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>bypass obstacle`
- **识别文本**: bypass obstacle
- **差异**: `bypassobstacle` vs `BypassObstacle`

**结论**: 两个模型均识别错误 ❌

---

### 样本 183: 2025_11_21_15_36_35.wav

**真实文本**: 开始测试

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

**结论**: 两个模型均识别正确 ✅

---

### 样本 184: 2025_11_21_10_22_13.wav

**真实文本**: 车道保存 一直压左侧车道线 压力性三分 预测性三分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保存一直压左侧车道线压力型塞分 预测型`
- **识别文本**: 车道保存一直压左侧车道线压力型塞分 预测型
- **差异**: `车道保存一直压左侧车道线压力型塞分预测型` vs `车道保存一直压左侧车道线压力性三分预测性三分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保存 一直压左侧车道线 压力性3分 预测性3分`
- **识别文本**: 车道保存 一直压左侧车道线 压力性3分 预测性3分
- **差异**: `车道保存一直压左侧车道线压力性3分预测性3分` vs `车道保存一直压左侧车道线压力性三分预测性三分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 185: 2025_11_21_21_58_02.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>dnction street`
- **识别文本**: dnction street
- **差异**: `dnctionstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>dunkction street`
- **识别文本**: dunkction street
- **差异**: `dunkctionstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 186: 2025_11_20_22_52_22.wav

**真实文本**: 障碍物绕行 当有旁边车辆侵入我们车道时 能够绕过去 预测性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行当有旁边车辆侵入我们车道时能够绕过去预测线五分`
- **识别文本**: 障碍物绕行当有旁边车辆侵入我们车道时能够绕过去预测线五分
- **差异**: `障碍物绕行当有旁边车辆侵入我们车道时能够绕过去预测线五分` vs `障碍物绕行当有旁边车辆侵入我们车道时能够绕过去预测性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行 当有旁边车辆侵入我们车道时 能够绕过去 预测性5分`
- **识别文本**: 障碍物绕行 当有旁边车辆侵入我们车道时 能够绕过去 预测性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 187: 2025_11_21_14_50_13.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 188: 2025_11_20_19_58_38.wav

**真实文本**: 路口左转 左转过程中 打方向很快 速度也不慢 压力性2分 舒适性3分 且在变道完成时压左边 压左边虚线

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转左转过程中打方向很快速度也不慢压力性两分舒适性三分且在变道完成时压左边压左边的虚线`
- **识别文本**: 路口左转左转过程中打方向很快速度也不慢压力性两分舒适性三分且在变道完成时压左边压左边的虚线
- **差异**: `路口左转左转过程中打方向很快速度也不慢压力性两分舒适性三分且在变道完成时压左边压左边的虚线` vs `路口左转左转过程中打方向很快速度也不慢压力性2分舒适性3分且在变道完成时压左边压左边虚线`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转 左转过程中打方向很快 速度也不慢 压力性2分 舒适性3分 且在变道完成时压左边 压左边的虚线`
- **识别文本**: 路口左转 左转过程中打方向很快 速度也不慢 压力性2分 舒适性3分 且在变道完成时压左边 压左边的虚线
- **差异**: `路口左转左转过程中打方向很快速度也不慢压力性2分舒适性3分且在变道完成时压左边压左边的虚线` vs `路口左转左转过程中打方向很快速度也不慢压力性2分舒适性3分且在变道完成时压左边压左边虚线`

**结论**: 两个模型均识别错误 ❌

---

### 样本 189: 2025_11_20_23_16_22.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口执行`
- **识别文本**: 路口执行
- **差异**: `路口执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 190: 2025_11_21_10_22_34.wav

**真实文本**: 限速信息 识别到限速牌 限速50 自车识别 50 本车车速60

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>限速信息识别到限速牌限速五十自车识别五十本车车速六十`
- **识别文本**: 限速信息识别到限速牌限速五十自车识别五十本车车速六十
- **差异**: `限速信息识别到限速牌限速五十自车识别五十本车车速六十` vs `限速信息识别到限速牌限速50自车识别50本车车速60`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>限速信息 识别到限速盘 限速50 自车识别50 本车测速60`
- **识别文本**: 限速信息 识别到限速盘 限速50 自车识别50 本车测速60
- **差异**: `限速信息识别到限速盘限速50自车识别50本车测速60` vs `限速信息识别到限速牌限速50自车识别50本车车速60`

**结论**: 两个模型均识别错误 ❌

---

### 样本 191: 2025_11_21_14_01_46.wav

**真实文本**: 导航变道 但变道过程有犹豫嗯别到了左后方车辆压力性三分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道但变道过程有犹豫变道了左后方车辆压力性三分`
- **识别文本**: 导航变道但变道过程有犹豫变道了左后方车辆压力性三分
- **差异**: `导航变道但变道过程有犹豫变道了左后方车辆压力性三分` vs `导航变道但变道过程有犹豫嗯别到了左后方车辆压力性三分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道 但变道过程有犹豫 别到了左后方车辆 压力性3分`
- **识别文本**: 导航变道 但变道过程有犹豫 别到了左后方车辆 压力性3分
- **差异**: `导航变道但变道过程有犹豫别到了左后方车辆压力性3分` vs `导航变道但变道过程有犹豫嗯别到了左后方车辆压力性三分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 192: 2025_11_21_13_30_46.wav

**真实文本**: 前车切入 前方车辆切入本车适当减速

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>前车切入前方车辆切入本车适当减速`
- **识别文本**: 前车切入前方车辆切入本车适当减速

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>前车切入 前方车辆切入 本车适当减速`
- **识别文本**: 前车切入 前方车辆切入 本车适当减速

**结论**: 两个模型均识别正确 ✅

---

### 样本 193: 2025_11_21_13_29_32.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 194: 2025_11_21_10_24_53.wav

**真实文本**: 障碍物绕行 绕行停在路中的车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>债务绕行绕幸停在路中的车`
- **识别文本**: 债务绕行绕幸停在路中的车
- **差异**: `债务绕行绕幸停在路中的车` vs `障碍物绕行绕行停在路中的车`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行 绕行停在路中的车`
- **识别文本**: 障碍物绕行 绕行停在路中的车

**结论**: 微调模型改进 ⬆️

---

### 样本 195: 2025_11_20_22_58_23.wav

**真实文本**: 路口左转 转小弯儿 压双黄线 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转转小弯压双黄线预测性三十分`
- **识别文本**: 路口左转转小弯压双黄线预测性三十分
- **差异**: `路口左转转小弯压双黄线预测性三十分` vs `路口左转转小弯儿压双黄线预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转 转小弯 压双黄线 预测性3分`
- **识别文本**: 路口左转 转小弯 压双黄线 预测性3分
- **差异**: `路口左转转小弯压双黄线预测性3分` vs `路口左转转小弯儿压双黄线预测性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 196: 2025_11_20_23_16_28.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>绿动`
- **识别文本**: 绿动
- **差异**: `绿动` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>绿动`
- **识别文本**: 绿动
- **差异**: `绿动` vs `绿灯`

**结论**: 两个模型均识别错误 ❌

---

### 样本 197: 2025_11_20_20_32_47.wav

**真实文本**: 红灯领航

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红狼娘号`
- **识别文本**: 红狼娘号
- **差异**: `红狼娘号` vs `红灯领航`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红狼领航`
- **识别文本**: 红狼领航
- **差异**: `红狼领航` vs `红灯领航`

**结论**: 两个模型均识别错误 ❌

---

### 样本 198: 2025_11_17_14_02_45.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 199: 2025_11_21_10_27_56.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 200: 2025_11_20_22_56_47.wav

**真实文本**: 弱势群体 绕行弱势群体

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体绕行弱势群体`
- **识别文本**: 弱势群体绕行弱势群体

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 绕行弱势群体`
- **识别文本**: 弱势群体 绕行弱势群体

**结论**: 两个模型均识别正确 ✅

---

### 样本 201: 2025_11_20_20_53_34.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 202: 2025_11_20_22_59_54.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 203: 2025_11_20_21_00_50.wav

**真实文本**: 汇入

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>汇入`
- **识别文本**: 汇入

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>汇入`
- **识别文本**: 汇入

**结论**: 两个模型均识别正确 ✅

---

### 样本 204: 2025_11_21_15_22_40.wav

**真实文本**: 路口直行 能够避让公交车 预测性5分 压力性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行能够避让公交车预测性五分压力性五分`
- **识别文本**: 路口直行能够避让公交车预测性五分压力性五分
- **差异**: `路口直行能够避让公交车预测性五分压力性五分` vs `路口直行能够避让公交车预测性5分压力性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 能够避让公交车 预测性5分 压力性5分`
- **识别文本**: 路口直行 能够避让公交车 预测性5分 压力性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 205: 2025_11_20_20_41_47.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 206: 2025_11_21_14_10_30.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 207: 2025_11_21_13_12_50.wav

**真实文本**: 路口左转 左转待转区识别有问题 红灯时本车已超过 停止线进入待转区 效率性3分 压力性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转左转带转区识别有问题红灯时本车已超过停止线进入带转区效率性三分压力性三分`
- **识别文本**: 路口左转左转带转区识别有问题红灯时本车已超过停止线进入带转区效率性三分压力性三分
- **差异**: `路口左转左转带转区识别有问题红灯时本车已超过停止线进入带转区效率性三分压力性三分` vs `路口左转左转待转区识别有问题红灯时本车已超过停止线进入待转区效率性3分压力性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转 左转待转区识别有问题 红灯时本车已超过停止线进入待转区 效率性3分 压力性3分`
- **识别文本**: 路口左转 左转待转区识别有问题 红灯时本车已超过停止线进入待转区 效率性3分 压力性3分

**结论**: 微调模型改进 ⬆️

---

### 样本 208: 2025_11_17_13_56_00.wav

**真实文本**: 其他无故变道剪辑

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他无故变道剪辑`
- **识别文本**: 其他无故变道剪辑

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他无故变道 剪辑`
- **识别文本**: 其他无故变道 剪辑

**结论**: 两个模型均识别正确 ✅

---

### 样本 209: 2025_11_21_10_20_58.wav

**真实文本**: 复杂场景 宽度比较窄 是可以允许车辆宽度通行 本车速度降为0 不继续行驶 效率性1分 驾驶员接管 剪辑

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>复杂场景宽度比较窄是可以允许车辆宽度通行本车速度降为零不继续行驶效率性一分驾驶员接管见机`
- **识别文本**: 复杂场景宽度比较窄是可以允许车辆宽度通行本车速度降为零不继续行驶效率性一分驾驶员接管见机
- **差异**: `复杂场景宽度比较窄是可以允许车辆宽度通行本车速度降为零不继续行驶效率性一分驾驶员接管见机` vs `复杂场景宽度比较窄是可以允许车辆宽度通行本车速度降为0不继续行驶效率性1分驾驶员接管剪辑`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>复杂场景 宽度比较窄 是可以允许车辆宽度通行 本车速度将为0 不继续行驶 效率性1分 驾驶员接管剪辑`
- **识别文本**: 复杂场景 宽度比较窄 是可以允许车辆宽度通行 本车速度将为0 不继续行驶 效率性1分 驾驶员接管剪辑
- **差异**: `复杂场景宽度比较窄是可以允许车辆宽度通行本车速度将为0不继续行驶效率性1分驾驶员接管剪辑` vs `复杂场景宽度比较窄是可以允许车辆宽度通行本车速度降为0不继续行驶效率性1分驾驶员接管剪辑`

**结论**: 两个模型均识别错误 ❌

---

### 样本 210: 2025_11_17_13_45_42.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 211: 2025_11_21_21_57_22.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>johnson street`
- **识别文本**: johnson street
- **差异**: `johnsonstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>johnson street`
- **识别文本**: johnson street
- **差异**: `johnsonstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 212: 2025_11_20_20_32_02.wav

**真实文本**: 路口左转 速度非常奇怪 不舒服 很快 压力性3分 舒适性3分 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转速度非常奇怪不舒服很快压力性三分舒适性三分预测性三分`
- **识别文本**: 路口左转速度非常奇怪不舒服很快压力性三分舒适性三分预测性三分
- **差异**: `路口左转速度非常奇怪不舒服很快压力性三分舒适性三分预测性三分` vs `路口左转速度非常奇怪不舒服很快压力性3分舒适性3分预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转 速度非常奇怪 不舒服 很快 压力性3分 舒适性3分 预测性3分`
- **识别文本**: 路口左转 速度非常奇怪 不舒服 很快 压力性3分 舒适性3分 预测性3分

**结论**: 微调模型改进 ⬆️

---

### 样本 213: 2025_11_20_19_35_51.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 214: 2025_11_20_20_42_29.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口执行`
- **识别文本**: 路口执行
- **差异**: `路口执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 215: 2025_11_20_23_09_25.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>律动`
- **识别文本**: 律动
- **差异**: `律动` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>律动`
- **识别文本**: 律动
- **差异**: `律动` vs `绿灯`

**结论**: 两个模型均识别错误 ❌

---

### 样本 216: 2025_11_21_10_40_00.wav

**真实文本**: Bypass Obstacle

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>bypass obstacle`
- **识别文本**: bypass obstacle
- **差异**: `bypassobstacle` vs `BypassObstacle`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>bypass obstacle`
- **识别文本**: bypass obstacle
- **差异**: `bypassobstacle` vs `BypassObstacle`

**结论**: 两个模型均识别错误 ❌

---

### 样本 217: 2025_11_21_14_03_36.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 218: 2025_11_20_22_53_17.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 219: 2025_11_20_23_02_03.wav

**真实文本**: 红灯跟车 红灯跟车起步太慢 效率性三分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车红灯跟车起步太慢效率性三分`
- **识别文本**: 红灯跟车红灯跟车起步太慢效率性三分

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车 红灯跟车起步太慢 效率性3分`
- **识别文本**: 红灯跟车 红灯跟车起步太慢 效率性3分
- **差异**: `红灯跟车红灯跟车起步太慢效率性3分` vs `红灯跟车红灯跟车起步太慢效率性三分`

**结论**: 微调模型退化 ⬇️

---

### 样本 220: 2025_11_21_15_40_59.wav

**真实文本**: 车道保持 偏左行驶压左侧车道线 预测性三分 压力性三分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保持偏左行驶压左侧车道线预测性三分压力性三分`
- **识别文本**: 车道保持偏左行驶压左侧车道线预测性三分压力性三分

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保持 偏左行驶压左侧车道线 预测性3分 压力性3分`
- **识别文本**: 车道保持 偏左行驶压左侧车道线 预测性3分 压力性3分
- **差异**: `车道保持偏左行驶压左侧车道线预测性3分压力性3分` vs `车道保持偏左行驶压左侧车道线预测性三分压力性三分`

**结论**: 微调模型退化 ⬇️

---

### 样本 221: 2025_11_20_20_04_18.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 222: 2025_11_21_15_23_14.wav

**真实文本**: 路口直行 这个路口有点复杂 他能准确的绕过栅栏 且插到旁边车的前边 通过这个路口 且开的很合理 预测性6分 压力性6分 效率性5分 剪辑

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行这个路口有点复杂它能准确的绕过栅栏且插到旁边车的前边通过这个路口 <|zh|><|NEUTRAL|><|Speech|><|woitn|>且开的很合理预测性六分压力性六分效率性五分剪辑`
- **识别文本**: 路口直行这个路口有点复杂它能准确的绕过栅栏且插到旁边车的前边通过这个路口 且开的很合理预测性六分压力性六分效率性五分剪辑
- **差异**: `路口直行这个路口有点复杂它能准确的绕过栅栏且插到旁边车的前边通过这个路口且开的很合理预测性六分压力性六分效率性五分剪辑` vs `路口直行这个路口有点复杂他能准确的绕过栅栏且插到旁边车的前边通过这个路口且开的很合理预测性6分压力性6分效率性5分剪辑`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 这个路口有点复杂 它能准确的绕过栅栏 且插到旁边车的前边 通过这个路口 <|zh|><|NEUTRAL|><|Speech|><|woitn|>且开的很合理 预测性6分 压力性6分 效率性5分 剪辑`
- **识别文本**: 路口直行 这个路口有点复杂 它能准确的绕过栅栏 且插到旁边车的前边 通过这个路口 且开的很合理 预测性6分 压力性6分 效率性5分 剪辑
- **差异**: `路口直行这个路口有点复杂它能准确的绕过栅栏且插到旁边车的前边通过这个路口且开的很合理预测性6分压力性6分效率性5分剪辑` vs `路口直行这个路口有点复杂他能准确的绕过栅栏且插到旁边车的前边通过这个路口且开的很合理预测性6分压力性6分效率性5分剪辑`

**结论**: 两个模型均识别错误 ❌

---

### 样本 223: 2025_11_21_10_12_03.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 224: 2025_11_20_19_50_56.wav

**真实文本**: 路口掉头 路口掉头没有响应 预测性2分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口掉头路口掉头没有响应预测性两分`
- **识别文本**: 路口掉头路口掉头没有响应预测性两分
- **差异**: `路口掉头路口掉头没有响应预测性两分` vs `路口掉头路口掉头没有响应预测性2分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口掉头 路口掉头没有响应 预测性2分`
- **识别文本**: 路口掉头 路口掉头没有响应 预测性2分

**结论**: 微调模型改进 ⬆️

---

### 样本 225: 2025_11_20_19_59_31.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 226: 2025_11_20_22_51_06.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 227: 2025_11_20_23_03_17.wav

**真实文本**: 汇出

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>会出`
- **识别文本**: 会出
- **差异**: `会出` vs `汇出`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>汇出`
- **识别文本**: 汇出

**结论**: 微调模型改进 ⬆️

---

### 样本 228: 2025_11_20_19_54_49.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 229: 2025_11_17_13_35_06.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿东`
- **识别文本**: 绿东
- **差异**: `绿东` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 微调模型改进 ⬆️

---

### 样本 230: 2025_11_21_13_20_56.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 231: 2025_11_20_23_09_18.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 232: 2025_11_20_23_21_06.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航元老`
- **识别文本**: 导航元老
- **差异**: `导航元老` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变老`
- **识别文本**: 导航变老
- **差异**: `导航变老` vs `导航变道`

**结论**: 两个模型均识别错误 ❌

---

### 样本 233: 2025_11_21_15_37_17.wav

**真实文本**: 车道保持 路上右转压实线 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保石路上右转压实线预测性三分`
- **识别文本**: 车道保石路上右转压实线预测性三分
- **差异**: `车道保石路上右转压实线预测性三分` vs `车道保持路上右转压实线预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保持 路上右转压实性 预测性3分`
- **识别文本**: 车道保持 路上右转压实性 预测性3分
- **差异**: `车道保持路上右转压实性预测性3分` vs `车道保持路上右转压实线预测性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 234: 2025_11_20_20_02_50.wav

**真实文本**: 其他 刚出潮汐车道的范围内 华为ADS4 0自动激活

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他刚出潮汐车道的范围内而为 a d s 四点零自动激活`
- **识别文本**: 其他刚出潮汐车道的范围内而为 a d s 四点零自动激活
- **差异**: `其他刚出潮汐车道的范围内而为ads四点零自动激活` vs `其他刚出潮汐车道的范围内华为ADS40自动激活`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他 刚出潮汐车道的范围内 华为 ADDS40 自动激活`
- **识别文本**: 其他 刚出潮汐车道的范围内 华为 ADDS40 自动激活
- **差异**: `其他刚出潮汐车道的范围内华为ADDS40自动激活` vs `其他刚出潮汐车道的范围内华为ADS40自动激活`

**结论**: 两个模型均识别错误 ❌

---

### 样本 235: 2025_11_20_20_47_39.wav

**真实文本**: 前车切入 大挂车进入本车道 减速舒适 预测性5分 舒适性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>前车切入大挂车进入本车道减速舒适预测线五分舒适线五分`
- **识别文本**: 前车切入大挂车进入本车道减速舒适预测线五分舒适线五分
- **差异**: `前车切入大挂车进入本车道减速舒适预测线五分舒适线五分` vs `前车切入大挂车进入本车道减速舒适预测性5分舒适性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>前车切入 大挂车进入本车道 减速舒适 预测性5分 舒适性5分`
- **识别文本**: 前车切入 大挂车进入本车道 减速舒适 预测性5分 舒适性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 236: 2025_11_20_19_43_55.wav

**真实文本**: 障碍物绕行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行`
- **识别文本**: 障碍物绕行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行`
- **识别文本**: 障碍物绕行

**结论**: 两个模型均识别正确 ✅

---

### 样本 237: 2025_11_20_20_29_57.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航面道`
- **识别文本**: 导航面道
- **差异**: `导航面道` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 238: 2025_11_20_20_00_48.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口执行`
- **识别文本**: 路口执行
- **差异**: `路口执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 239: 2025_11_21_13_10_58.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 240: 2025_11_20_23_19_03.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 241: 2025_11_21_10_15_11.wav

**真实文本**: 汇入变道 汇入到辅路中行驶

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>会路变道贿路到辅路中行驶`
- **识别文本**: 会路变道贿路到辅路中行驶
- **差异**: `会路变道贿路到辅路中行驶` vs `汇入变道汇入到辅路中行驶`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>汇路变道 汇入到辅路中行驶`
- **识别文本**: 汇路变道 汇入到辅路中行驶
- **差异**: `汇路变道汇入到辅路中行驶` vs `汇入变道汇入到辅路中行驶`

**结论**: 两个模型均识别错误 ❌

---

### 样本 242: 2025_11_21_15_27_57.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 243: 2025_11_20_23_21_10.wav

**真实文本**: 导航变道 连续变换两条车道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道连续变换两条车道`
- **识别文本**: 导航变道连续变换两条车道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道 连续变换两条车道`
- **识别文本**: 导航变道 连续变换两条车道

**结论**: 两个模型均识别正确 ✅

---

### 样本 244: 2025_11_20_23_18_39.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>大棉袄`
- **识别文本**: 大棉袄
- **差异**: `大棉袄` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 245: 2025_11_21_10_30_41.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航密脑`
- **识别文本**: 导航密脑
- **差异**: `导航密脑` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 246: 2025_11_21_13_31_40.wav

**真实文本**: 障碍物绕行 前方有静止车辆本车也不会绕行效率性两分驾驶员接管

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行前方有静止车辆本车也不会绕行效率性两分驾驶员接管`
- **识别文本**: 障碍物绕行前方有静止车辆本车也不会绕行效率性两分驾驶员接管

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行 前方有静止车辆 本车也不会绕行 效率性2分 驾驶员接管`
- **识别文本**: 障碍物绕行 前方有静止车辆 本车也不会绕行 效率性2分 驾驶员接管
- **差异**: `障碍物绕行前方有静止车辆本车也不会绕行效率性2分驾驶员接管` vs `障碍物绕行前方有静止车辆本车也不会绕行效率性两分驾驶员接管`

**结论**: 微调模型退化 ⬇️

---

### 样本 247: 2025_11_21_10_43_21.wav

**真实文本**: Junction Turn

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>juction turn`
- **识别文本**: juction turn
- **差异**: `juctionturn` vs `JunctionTurn`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juction turn`
- **识别文本**: juction turn
- **差异**: `juctionturn` vs `JunctionTurn`

**结论**: 两个模型均识别错误 ❌

---

### 样本 248: 2025_11_21_15_22_05.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 249: 2025_11_21_15_19_41.wav

**真实文本**: 绿灯 在红灯还有几秒时选择减速 当绿灯亮起时在加速 没有上一条那么不舒服 但是也不太好

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯在红灯还有几秒时选择减速当绿灯亮起时在加速没有上一条那么不舒服但是也不太好`
- **识别文本**: 绿灯在红灯还有几秒时选择减速当绿灯亮起时在加速没有上一条那么不舒服但是也不太好

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯 在红灯还有几秒时选择减速 当绿灯亮起时在加速 没有上一条那么不舒服 但是也不太好`
- **识别文本**: 绿灯 在红灯还有几秒时选择减速 当绿灯亮起时在加速 没有上一条那么不舒服 但是也不太好

**结论**: 两个模型均识别正确 ✅

---

### 样本 250: 2025_11_21_21_57_43.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juangction street`
- **识别文本**: juangction street
- **差异**: `juangctionstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juangction street`
- **识别文本**: juangction street
- **差异**: `juangctionstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 251: 2025_11_20_23_06_27.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>渡可执行`
- **识别文本**: 渡可执行
- **差异**: `渡可执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 252: 2025_11_20_23_08_25.wav

**真实文本**: 红灯领航 在红灯前停下的时候 选择了右转道 别住了后边右转的车 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航在红灯前停下来的时候选择了右转道别住了后边右转的车热性三分`
- **识别文本**: 红灯领航在红灯前停下来的时候选择了右转道别住了后边右转的车热性三分
- **差异**: `红灯领航在红灯前停下来的时候选择了右转道别住了后边右转的车热性三分` vs `红灯领航在红灯前停下的时候选择了右转道别住了后边右转的车预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航 在红灯前停下来的时候 选择了右转道 别住了后边右转的车 预测性3分`
- **识别文本**: 红灯领航 在红灯前停下来的时候 选择了右转道 别住了后边右转的车 预测性3分
- **差异**: `红灯领航在红灯前停下来的时候选择了右转道别住了后边右转的车预测性3分` vs `红灯领航在红灯前停下的时候选择了右转道别住了后边右转的车预测性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 253: 2025_11_20_19_57_54.wav

**真实文本**: 路口直行 路口直行的过程中有一个向左的超车变道 预测性四分 效率性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口执行路口执行的过程中有一个向左的超时变道预测性四分效率性五分`
- **识别文本**: 路口执行路口执行的过程中有一个向左的超时变道预测性四分效率性五分
- **差异**: `路口执行路口执行的过程中有一个向左的超时变道预测性四分效率性五分` vs `路口直行路口直行的过程中有一个向左的超车变道预测性四分效率性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 路口直行的过程中有一个向左的超车变道 预测性4分 效率性5分`
- **识别文本**: 路口直行 路口直行的过程中有一个向左的超车变道 预测性4分 效率性5分
- **差异**: `路口直行路口直行的过程中有一个向左的超车变道预测性4分效率性5分` vs `路口直行路口直行的过程中有一个向左的超车变道预测性四分效率性5分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 254: 2025_11_20_23_05_14.wav

**真实文本**: 路口直行 直行受后方车辆影响晃了一下

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口执行执行后受后方车辆影响晃了一下`
- **识别文本**: 路口执行执行后受后方车辆影响晃了一下
- **差异**: `路口执行执行后受后方车辆影响晃了一下` vs `路口直行直行受后方车辆影响晃了一下`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 直行后 受后方车辆影响晃了一下`
- **识别文本**: 路口直行 直行后 受后方车辆影响晃了一下
- **差异**: `路口直行直行后受后方车辆影响晃了一下` vs `路口直行直行受后方车辆影响晃了一下`

**结论**: 两个模型均识别错误 ❌

---

### 样本 255: 2025_11_20_23_06_07.wav

**真实文本**: 车道保持 进环岛之前 车往右晃了一下 又回去了 应该是想要变道 但是发现变道又不合适 就取消了 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保持进环岛之前车网又晃了一下又回去了应该是想要变道但是发现变道又不合适就取消了预测性三分`
- **识别文本**: 车道保持进环岛之前车网又晃了一下又回去了应该是想要变道但是发现变道又不合适就取消了预测性三分
- **差异**: `车道保持进环岛之前车网又晃了一下又回去了应该是想要变道但是发现变道又不合适就取消了预测性三分` vs `车道保持进环岛之前车往右晃了一下又回去了应该是想要变道但是发现变道又不合适就取消了预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保持 进环岛之前 车往又晃了一下 又回去了 应该是想要变道 但是发现变道又不合适 就取消了 预测性3分`
- **识别文本**: 车道保持 进环岛之前 车往又晃了一下 又回去了 应该是想要变道 但是发现变道又不合适 就取消了 预测性3分
- **差异**: `车道保持进环岛之前车往又晃了一下又回去了应该是想要变道但是发现变道又不合适就取消了预测性3分` vs `车道保持进环岛之前车往右晃了一下又回去了应该是想要变道但是发现变道又不合适就取消了预测性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 256: 2025_11_20_23_05_48.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿豆`
- **识别文本**: 绿豆
- **差异**: `绿豆` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿到`
- **识别文本**: 绿到
- **差异**: `绿到` vs `绿灯`

**结论**: 两个模型均识别错误 ❌

---

### 样本 257: 2025_11_21_21_56_08.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>junction street`
- **识别文本**: junction street
- **差异**: `junctionstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>junction street`
- **识别文本**: junction street
- **差异**: `junctionstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 258: 2025_11_17_13_44_40.wav

**真实文本**: 路口右转 避让障碍物有问题 剪辑

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转避让障碍问有问题点急`
- **识别文本**: 路口右转避让障碍问有问题点急
- **差异**: `路口右转避让障碍问有问题点急` vs `路口右转避让障碍物有问题剪辑`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转 避让障碍物有问题 剪辑`
- **识别文本**: 路口右转 避让障碍物有问题 剪辑

**结论**: 微调模型改进 ⬆️

---

### 样本 259: 2025_11_21_10_46_42.wav

**真实文本**: VRU Handling

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>we are you handling`
- **识别文本**: we are you handling
- **差异**: `weareyouhandling` vs `VRUHandling`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>where are you handling`
- **识别文本**: where are you handling
- **差异**: `whereareyouhandling` vs `VRUHandling`

**结论**: 两个模型均识别错误 ❌

---

### 样本 260: 2025_11_21_14_05_08.wav

**真实文本**: 红灯领航 红绿灯识别失败 预测性一分 压力性一分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航红绿灯识别失败预测性一分压力性一分`
- **识别文本**: 红灯领航红绿灯识别失败预测性一分压力性一分

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航 红绿灯识别失败 预测性1分 压力性1分`
- **识别文本**: 红灯领航 红绿灯识别失败 预测性1分 压力性1分
- **差异**: `红灯领航红绿灯识别失败预测性1分压力性1分` vs `红灯领航红绿灯识别失败预测性一分压力性一分`

**结论**: 微调模型退化 ⬇️

---

### 样本 261: 2025_11_21_13_37_15.wav

**真实文本**: 汇入变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>汇入变道`
- **识别文本**: 汇入变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>汇入变道`
- **识别文本**: 汇入变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 262: 2025_11_21_21_54_22.wav

**真实文本**: VRU Handling

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>v r u 韩豆林`
- **识别文本**: v r u 韩豆林
- **差异**: `vru韩豆林` vs `VRUHandling`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>v rU 航道林`
- **识别文本**: v rU 航道林
- **差异**: `vrU航道林` vs `VRUHandling`

**结论**: 两个模型均识别错误 ❌

---

### 样本 263: 2025_11_20_20_09_45.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 264: 2025_11_21_10_09_24.wav

**真实文本**: 开始测试

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

**结论**: 两个模型均识别正确 ✅

---

### 样本 265: 2025_11_21_15_34_30.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口执行`
- **识别文本**: 路口执行
- **差异**: `路口执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 266: 2025_11_20_21_00_46.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿到`
- **识别文本**: 绿到
- **差异**: `绿到` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 微调模型改进 ⬆️

---

### 样本 267: 2025_11_17_13_52_18.wav

**真实文本**: 前车切入有巴士想切入本车道 没有让行 司机压力较大 压力性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|BGM|><|woitn|>前车切入有巴士想切入本车道没有让行司机压力较大压力性三分`
- **识别文本**: 前车切入有巴士想切入本车道没有让行司机压力较大压力性三分
- **差异**: `前车切入有巴士想切入本车道没有让行司机压力较大压力性三分` vs `前车切入有巴士想切入本车道没有让行司机压力较大压力性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>前车切入有巴士想切入本车道 没有让行 司机压力较大 压力性3分`
- **识别文本**: 前车切入有巴士想切入本车道 没有让行 司机压力较大 压力性3分

**结论**: 微调模型改进 ⬆️

---

### 样本 268: 2025_11_20_19_43_10.wav

**真实文本**: 路口直行 没有红绿灯的路口 减速有点早 并且有点急 呃 舒适性3分 压力性5分 预测性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行没有红绿灯的路口减速有点早并且有点急啊舒适性三分压力性五分预测性五分`
- **识别文本**: 路口直行没有红绿灯的路口减速有点早并且有点急啊舒适性三分压力性五分预测性五分
- **差异**: `路口直行没有红绿灯的路口减速有点早并且有点急啊舒适性三分压力性五分预测性五分` vs `路口直行没有红绿灯的路口减速有点早并且有点急呃舒适性3分压力性5分预测性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 没有红绿灯的路口 减速有点早 并且有点急 嗯 舒适性3分 压力性5分 预测性5分`
- **识别文本**: 路口直行 没有红绿灯的路口 减速有点早 并且有点急 嗯 舒适性3分 压力性5分 预测性5分
- **差异**: `路口直行没有红绿灯的路口减速有点早并且有点急嗯舒适性3分压力性5分预测性5分` vs `路口直行没有红绿灯的路口减速有点早并且有点急呃舒适性3分压力性5分预测性5分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 269: 2025_11_20_23_08_07.wav

**真实文本**: 路口右转 速度稍微有点快

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转速度稍微有点快`
- **识别文本**: 路口右转速度稍微有点快

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转 速度稍微有点快`
- **识别文本**: 路口右转 速度稍微有点快

**结论**: 两个模型均识别正确 ✅

---

### 样本 270: 2025_11_20_19_43_57.wav

**真实文本**: 障碍物绕行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>长安勿绕行`
- **识别文本**: 长安勿绕行
- **差异**: `长安勿绕行` vs `障碍物绕行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行`
- **识别文本**: 障碍物绕行

**结论**: 微调模型改进 ⬆️

---

### 样本 271: 2025_11_17_13_34_13.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|BGM|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 272: 2025_11_17_13_56_21.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 273: 2025_11_21_14_21_13.wav

**真实文本**: 红灯领航 闯红灯 在闯红灯时没有减速行为 效率性5分 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航闯红灯在闯红灯时没有减速行为效率性五分舒适性三分`
- **识别文本**: 红灯领航闯红灯在闯红灯时没有减速行为效率性五分舒适性三分
- **差异**: `红灯领航闯红灯在闯红灯时没有减速行为效率性五分舒适性三分` vs `红灯领航闯红灯在闯红灯时没有减速行为效率性5分预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航 闯红灯 在闯红灯时没有减速行为 效率性5分 舒适性3分`
- **识别文本**: 红灯领航 闯红灯 在闯红灯时没有减速行为 效率性5分 舒适性3分
- **差异**: `红灯领航闯红灯在闯红灯时没有减速行为效率性5分舒适性3分` vs `红灯领航闯红灯在闯红灯时没有减速行为效率性5分预测性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 274: 2025_11_17_13_47_01.wav

**真实文本**: 其他 可能要闯红灯 接管

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他可能要闯红灯接管`
- **识别文本**: 其他可能要闯红灯接管

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他可能要闯红灯接管`
- **识别文本**: 其他可能要闯红灯接管

**结论**: 两个模型均识别正确 ✅

---

### 样本 275: 2025_11_20_20_40_50.wav

**真实文本**: 路口右转 在环岛处路口右转 觉得还好

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转在环岛处路口右转觉得还好`
- **识别文本**: 路口右转在环岛处路口右转觉得还好

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转 在环岛处 路口右转 觉得还好`
- **识别文本**: 路口右转 在环岛处 路口右转 觉得还好

**结论**: 两个模型均识别正确 ✅

---

### 样本 276: 2025_11_21_15_36_37.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 277: 2025_11_20_23_15_33.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 278: 2025_11_21_15_33_03.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 279: 2025_11_20_23_01_23.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 280: 2025_11_21_21_54_01.wav

**真实文本**: VRU Handling

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>b r u handling`
- **识别文本**: b r u handling
- **差异**: `bruhandling` vs `VRUHandling`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>bRU handling`
- **识别文本**: bRU handling
- **差异**: `bRUhandling` vs `VRUHandling`

**结论**: 两个模型均识别错误 ❌

---

### 样本 281: 2025_11_20_23_15_46.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 282: 2025_11_20_20_16_01.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 283: 2025_11_20_23_02_44.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 284: 2025_11_20_19_42_43.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口执行`
- **识别文本**: 路口执行
- **差异**: `路口执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 285: 2025_11_21_13_16_52.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 286: 2025_11_17_13_52_58.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|BGM|><|woitn|>入口直行`
- **识别文本**: 入口直行
- **差异**: `入口直行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 287: 2025_11_20_19_42_22.wav

**真实文本**: 障碍物绕行 绕行大车 预测性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行绕行大车预测性五分`
- **识别文本**: 障碍物绕行绕行大车预测性五分
- **差异**: `障碍物绕行绕行大车预测性五分` vs `障碍物绕行绕行大车预测性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行 绕行大车 预测性5分`
- **识别文本**: 障碍物绕行 绕行大车 预测性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 288: 2025_11_17_13_47_10.wav

**真实文本**: 红灯领航

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: ``
- **识别文本**: 
- **差异**: `` vs `红灯领航`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: ``
- **识别文本**: 
- **差异**: `` vs `红灯领航`

**结论**: 两个模型均识别错误 ❌

---

### 样本 289: 2025_11_17_13_56_46.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 290: 2025_11_20_20_16_56.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿的`
- **识别文本**: 绿的
- **差异**: `绿的` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿的`
- **识别文本**: 绿的
- **差异**: `绿的` vs `绿灯`

**结论**: 两个模型均识别错误 ❌

---

### 样本 291: 2025_11_21_14_08_45.wav

**真实文本**: 环岛 进环岛前速度很快 减到30公里每小时 在环岛中尝试多次尝试变道 且方向盘有点左右乱晃 速度稍微有点快 出环岛时 方向盘也乱晃 预测性三分 压力性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|nospeech|><|EMO_UNKNOWN|><|Speech|><|woitn|>ok <|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛进环岛前速度很快减到三十公里每小时在环岛中尝试多次尝试变道且方向盘有点左右乱晃速度稍微有点快出环岛时 <|zh|><|NEUTRAL|><|Speech|><|woitn|>方向盘也乱晃预测性三分压力性三分`
- **识别文本**: ok 环岛进环岛前速度很快减到三十公里每小时在环岛中尝试多次尝试变道且方向盘有点左右乱晃速度稍微有点快出环岛时 方向盘也乱晃预测性三分压力性三分
- **差异**: `ok环岛进环岛前速度很快减到三十公里每小时在环岛中尝试多次尝试变道且方向盘有点左右乱晃速度稍微有点快出环岛时方向盘也乱晃预测性三分压力性三分` vs `环岛进环岛前速度很快减到30公里每小时在环岛中尝试多次尝试变道且方向盘有点左右乱晃速度稍微有点快出环岛时方向盘也乱晃预测性三分压力性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>ok <|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛 进环岛前速度很快 减到30公里每小时 在环岛中尝试多次尝试变道 且方向盘有点左右乱晃 速度稍微有点快 出环岛时 <|zh|><|NEUTRAL|><|Speech|><|woitn|>方向盘也乱晃 预测性3分 压力性3分`
- **识别文本**: ok 环岛 进环岛前速度很快 减到30公里每小时 在环岛中尝试多次尝试变道 且方向盘有点左右乱晃 速度稍微有点快 出环岛时 方向盘也乱晃 预测性3分 压力性3分
- **差异**: `ok环岛进环岛前速度很快减到30公里每小时在环岛中尝试多次尝试变道且方向盘有点左右乱晃速度稍微有点快出环岛时方向盘也乱晃预测性3分压力性3分` vs `环岛进环岛前速度很快减到30公里每小时在环岛中尝试多次尝试变道且方向盘有点左右乱晃速度稍微有点快出环岛时方向盘也乱晃预测性三分压力性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 292: 2025_11_21_13_12_03.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 293: 2025_11_21_10_20_34.wav

**真实文本**: 路口直行 过程中遇到旁边车辆切入情况 减速过多 加速过慢 效率性2分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行过程中遇到旁边车辆泄漏情况减触过多加速过慢效率性二分`
- **识别文本**: 路口直行过程中遇到旁边车辆泄漏情况减触过多加速过慢效率性二分
- **差异**: `路口直行过程中遇到旁边车辆泄漏情况减触过多加速过慢效率性二分` vs `路口直行过程中遇到旁边车辆切入情况减速过多加速过慢效率性2分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 过程中遇到旁边车辆切入情况 减速过多 加速过慢 效率性2分`
- **识别文本**: 路口直行 过程中遇到旁边车辆切入情况 减速过多 加速过慢 效率性2分

**结论**: 微调模型改进 ⬆️

---

### 样本 294: 2025_11_20_23_09_31.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>骆执行`
- **识别文本**: 骆执行
- **差异**: `骆执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路直行`
- **识别文本**: 路直行
- **差异**: `路直行` vs `路口直行`

**结论**: 两个模型均识别错误 ❌

---

### 样本 295: 2025_11_17_14_01_42.wav

**真实文本**: 导航变道预测性较晚 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航面到预测性较晚预测性三三`
- **识别文本**: 导航面到预测性较晚预测性三三
- **差异**: `导航面到预测性较晚预测性三三` vs `导航变道预测性较晚预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道 预测性较晚 预测性3分`
- **识别文本**: 导航变道 预测性较晚 预测性3分

**结论**: 微调模型改进 ⬆️

---

### 样本 296: 2025_11_21_21_54_43.wav

**真实文本**: VRU Handling

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>v are you handling`
- **识别文本**: v are you handling
- **差异**: `vareyouhandling` vs `VRUHandling`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>v are you handling`
- **识别文本**: v are you handling
- **差异**: `vareyouhandling` vs `VRUHandling`

**结论**: 两个模型均识别错误 ❌

---

### 样本 297: 2025_11_20_20_42_50.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 298: 2025_11_21_15_24_11.wav

**真实文本**: 车道保持 在接近路口时有一个很大的横摆 压力性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保持在接近路口时有一个很大的横板压力性三分`
- **识别文本**: 车道保持在接近路口时有一个很大的横板压力性三分
- **差异**: `车道保持在接近路口时有一个很大的横板压力性三分` vs `车道保持在接近路口时有一个很大的横摆压力性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>车道保持 在接近路口时有一个很大的横板 压力性3分`
- **识别文本**: 车道保持 在接近路口时有一个很大的横板 压力性3分
- **差异**: `车道保持在接近路口时有一个很大的横板压力性3分` vs `车道保持在接近路口时有一个很大的横摆压力性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 299: 2025_11_21_15_14_06.wav

**真实文本**: 环岛 这次还行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛这次还行`
- **识别文本**: 环岛这次还行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛 这次还行`
- **识别文本**: 环岛 这次还行

**结论**: 两个模型均识别正确 ✅

---

### 样本 300: 2025_11_20_19_52_04.wav

**真实文本**: 弱势群体

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体`
- **识别文本**: 弱势群体

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体`
- **识别文本**: 弱势群体

**结论**: 两个模型均识别正确 ✅

---

### 样本 301: 2025_11_17_13_55_22.wav

**真实文本**: 其他 开启智驾

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他开启支架`
- **识别文本**: 其他开启支架
- **差异**: `其他开启支架` vs `其他开启智驾`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他 开启支驾`
- **识别文本**: 其他 开启支驾
- **差异**: `其他开启支驾` vs `其他开启智驾`

**结论**: 两个模型均识别错误 ❌

---

### 样本 302: 2025_11_21_15_42_41.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 303: 2025_11_21_14_02_45.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 304: 2025_11_21_13_10_06.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 305: 2025_11_20_20_16_45.wav

**真实文本**: 跟车 莫名其妙减速 NSS 预测性三分 舒适性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>跟车莫名其妙减速 n s s 预测性三分数适性三分`
- **识别文本**: 跟车莫名其妙减速 n s s 预测性三分数适性三分
- **差异**: `跟车莫名其妙减速nss预测性三分数适性三分` vs `跟车莫名其妙减速NSS预测性三分舒适性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>跟车 莫名其妙减速 NSS预测性3分 舒适性3分`
- **识别文本**: 跟车 莫名其妙减速 NSS预测性3分 舒适性3分
- **差异**: `跟车莫名其妙减速NSS预测性3分舒适性3分` vs `跟车莫名其妙减速NSS预测性三分舒适性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 306: 2025_11_21_21_56_46.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>junction street`
- **识别文本**: junction street
- **差异**: `junctionstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juction street`
- **识别文本**: juction street
- **差异**: `juctionstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 307: 2025_11_17_13_53_06.wav

**真实文本**: 路口执行 过入口时有无意义的换道压力性三分 舒适性三分剪辑

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行过路口时有不明意的管道压力性三分舒适性三分紧急`
- **识别文本**: 路口直行过路口时有不明意的管道压力性三分舒适性三分紧急
- **差异**: `路口直行过路口时有不明意的管道压力性三分舒适性三分紧急` vs `路口执行过入口时有无意义的换道压力性三分舒适性三分剪辑`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 过路口时有不明义的换道 压力性3分 舒适性3分 剪辑`
- **识别文本**: 路口直行 过路口时有不明义的换道 压力性3分 舒适性3分 剪辑
- **差异**: `路口直行过路口时有不明义的换道压力性3分舒适性3分剪辑` vs `路口执行过入口时有无意义的换道压力性三分舒适性三分剪辑`

**结论**: 两个模型均识别错误 ❌

---

### 样本 308: 2025_11_21_15_15_33.wav

**真实文本**: 红灯领航

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航`
- **识别文本**: 红灯领航

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航`
- **识别文本**: 红灯领航

**结论**: 两个模型均识别正确 ✅

---

### 样本 309: 2025_11_21_13_36_27.wav

**真实文本**: 跟车车辆突然异常减速预测性两分 压力性两分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>跟车车辆突然异常减速预测性两分压力性两分`
- **识别文本**: 跟车车辆突然异常减速预测性两分压力性两分

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>跟车 车辆突然异常减速 预测性2分 压力性2分`
- **识别文本**: 跟车 车辆突然异常减速 预测性2分 压力性2分
- **差异**: `跟车车辆突然异常减速预测性2分压力性2分` vs `跟车车辆突然异常减速预测性两分压力性两分`

**结论**: 微调模型退化 ⬇️

---

### 样本 310: 2025_11_20_23_08_11.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 311: 2025_11_20_22_51_12.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>落后执行`
- **识别文本**: 落后执行
- **差异**: `落后执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 312: 2025_11_21_15_33_28.wav

**真实文本**: 路口直行 通过路口后压左线 预测性三分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行通过路口后压左线预测性三分`
- **识别文本**: 路口直行通过路口后压左线预测性三分

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 通过路口后压左线 预测性3分`
- **识别文本**: 路口直行 通过路口后压左线 预测性3分
- **差异**: `路口直行通过路口后压左线预测性3分` vs `路口直行通过路口后压左线预测性三分`

**结论**: 微调模型退化 ⬇️

---

### 样本 313: 2025_11_20_23_06_04.wav

**真实文本**: 环岛

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>混脑`
- **识别文本**: 混脑
- **差异**: `混脑` vs `环岛`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛`
- **识别文本**: 环岛

**结论**: 微调模型改进 ⬆️

---

### 样本 314: 2025_11_20_22_51_38.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>大后面脑`
- **识别文本**: 大后面脑
- **差异**: `大后面脑` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 315: 2025_11_20_20_57_51.wav

**真实文本**: 路口右转

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转`
- **识别文本**: 路口右转

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转`
- **识别文本**: 路口右转

**结论**: 两个模型均识别正确 ✅

---

### 样本 316: 2025_11_21_10_23_53.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航面的`
- **识别文本**: 导航面的
- **差异**: `导航面的` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 317: 2025_11_17_14_04_06.wav

**真实文本**: 超车变道 咱们先用超车变道后又取消总分3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道咱们先用超车便道后又取消总分三分`
- **识别文本**: 超车变道咱们先用超车便道后又取消总分三分
- **差异**: `超车变道咱们先用超车便道后又取消总分三分` vs `超车变道咱们先用超车变道后又取消总分3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道 咱们先用超车变道后又取消总分3分`
- **识别文本**: 超车变道 咱们先用超车变道后又取消总分3分

**结论**: 微调模型改进 ⬆️

---

### 样本 318: 2025_11_20_22_51_10.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 319: 2025_11_20_19_43_38.wav

**真实文本**: 障碍物绕行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍勿绕行`
- **识别文本**: 障碍勿绕行
- **差异**: `障碍勿绕行` vs `障碍物绕行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行`
- **识别文本**: 障碍物绕行

**结论**: 微调模型改进 ⬆️

---

### 样本 320: 2025_11_20_19_51_50.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 321: 2025_11_21_10_24_14.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航边度`
- **识别文本**: 导航边度
- **差异**: `导航边度` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航边度`
- **识别文本**: 导航边度
- **差异**: `导航边度` vs `导航变道`

**结论**: 两个模型均识别错误 ❌

---

### 样本 322: 2025_11_20_20_17_38.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>我了跟臭`
- **识别文本**: 我了跟臭
- **差异**: `我了跟臭` vs `红灯跟车`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红了跟错`
- **识别文本**: 红了跟错
- **差异**: `红了跟错` vs `红灯跟车`

**结论**: 两个模型均识别错误 ❌

---

### 样本 323: 2025_11_21_10_38_58.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>jungcent`
- **识别文本**: jungcent
- **差异**: `jungcent` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>jungcent`
- **识别文本**: jungcent
- **差异**: `jungcent` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 324: 2025_11_21_13_30_52.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>luong`
- **识别文本**: luong
- **差异**: `luong` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>luong`
- **识别文本**: luong
- **差异**: `luong` vs `绿灯`

**结论**: 两个模型均识别错误 ❌

---

### 样本 325: 2025_11_21_14_30_02.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 326: 2025_11_21_22_00_04.wav

**真实文本**: Change Lane

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>穿起来`
- **识别文本**: 穿起来
- **差异**: `穿起来` vs `ChangeLane`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>ch去lan`
- **识别文本**: ch去lan
- **差异**: `ch去lan` vs `ChangeLane`

**结论**: 两个模型均识别错误 ❌

---

### 样本 327: 2025_11_20_19_41_47.wav

**真实文本**: VRU Handling VRU侵入我们的 driving tube 时 刹车不够及时 有碰撞风险 预测性一分 压力性一分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>v r u handling v r u 侵入到我们的 driving兵 tube 时刹车不够及时有碰撞风险预测性一分压力性一分`
- **识别文本**: v r u handling v r u 侵入到我们的 driving兵 tube 时刹车不够及时有碰撞风险预测性一分压力性一分
- **差异**: `vruhandlingvru侵入到我们的driving兵tube时刹车不够及时有碰撞风险预测性一分压力性一分` vs `VRUHandlingVRU侵入我们的drivingtube时刹车不够及时有碰撞风险预测性一分压力性一分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>vRU handling VRU侵入到我们的 driving兵 tube 时 刹车不够及时 有碰撞风险 预测性1分 压力性1分`
- **识别文本**: vRU handling VRU侵入到我们的 driving兵 tube 时 刹车不够及时 有碰撞风险 预测性1分 压力性1分
- **差异**: `vRUhandlingVRU侵入到我们的driving兵tube时刹车不够及时有碰撞风险预测性1分压力性1分` vs `VRUHandlingVRU侵入我们的drivingtube时刹车不够及时有碰撞风险预测性一分压力性一分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 328: 2025_11_21_15_17_14.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 329: 2025_11_21_21_59_39.wav

**真实文本**: Change Lane

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>change lane`
- **识别文本**: change lane
- **差异**: `changelane` vs `ChangeLane`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>change lane`
- **识别文本**: change lane
- **差异**: `changelane` vs `ChangeLane`

**结论**: 两个模型均识别错误 ❌

---

### 样本 330: 2025_11_21_15_29_13.wav

**真实文本**: 环岛 出环岛后 又找左侧左侧第二条车道 道路开的绝对不合理呀 预测性2分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|SAD|><|Speech|><|woitn|>环岛出环岛后右找左侧左侧第二条车道道路开的绝对不合理呀 <|zh|><|NEUTRAL|><|Speech|><|woitn|>预测性两分`
- **识别文本**: 环岛出环岛后右找左侧左侧第二条车道道路开的绝对不合理呀 预测性两分
- **差异**: `环岛出环岛后右找左侧左侧第二条车道道路开的绝对不合理呀预测性两分` vs `环岛出环岛后又找左侧左侧第二条车道道路开的绝对不合理呀预测性2分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛 出环岛后 右找左侧左侧第二条车道 道路开的绝对不合理呀 <|zh|><|NEUTRAL|><|Speech|><|woitn|>预测性两分`
- **识别文本**: 环岛 出环岛后 右找左侧左侧第二条车道 道路开的绝对不合理呀 预测性两分
- **差异**: `环岛出环岛后右找左侧左侧第二条车道道路开的绝对不合理呀预测性两分` vs `环岛出环岛后又找左侧左侧第二条车道道路开的绝对不合理呀预测性2分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 331: 2025_11_20_22_52_06.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>朝这边闹`
- **识别文本**: 朝这边闹
- **差异**: `朝这边闹` vs `超车变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 微调模型改进 ⬆️

---

### 样本 332: 2025_11_20_23_08_13.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 333: 2025_11_20_23_02_22.wav

**真实文本**: 弱势群体 能够避让送外卖小哥

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体能够避让送外卖小哥`
- **识别文本**: 弱势群体能够避让送外卖小哥

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 能够避让送外卖小哥`
- **识别文本**: 弱势群体 能够避让送外卖小哥

**结论**: 两个模型均识别正确 ✅

---

### 样本 334: 2025_11_20_20_54_35.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿的`
- **识别文本**: 绿的
- **差异**: `绿的` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 微调模型改进 ⬆️

---

### 样本 335: 2025_11_21_21_55_14.wav

**真实文本**: VRU Handling

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>v r u handling`
- **识别文本**: v r u handling
- **差异**: `vruhandling` vs `VRUHandling`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>v are u handling`
- **识别文本**: v are u handling
- **差异**: `vareuhandling` vs `VRUHandling`

**结论**: 两个模型均识别错误 ❌

---

### 样本 336: 2025_11_21_21_59_28.wav

**真实文本**: Change Lane

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>change lane`
- **识别文本**: change lane
- **差异**: `changelane` vs `ChangeLane`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>change lane`
- **识别文本**: change lane
- **差异**: `changelane` vs `ChangeLane`

**结论**: 两个模型均识别错误 ❌

---

### 样本 337: 2025_11_20_23_15_59.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>不可执行`
- **识别文本**: 不可执行
- **差异**: `不可执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 338: 2025_11_20_20_39_59.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口执行`
- **识别文本**: 路口执行
- **差异**: `路口执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 339: 2025_11_21_10_39_42.wav

**真实文本**: Bypass Obstacle

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>bypa of circle`
- **识别文本**: bypa of circle
- **差异**: `bypaofcircle` vs `BypassObstacle`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>bypa obstacle circle`
- **识别文本**: bypa obstacle circle
- **差异**: `bypaobstaclecircle` vs `BypassObstacle`

**结论**: 两个模型均识别错误 ❌

---

### 样本 340: 2025_11_21_15_15_52.wav

**真实文本**: 跟车 受旁边车辆影响 突然急刹车 NSS 预测性2分 压力性1分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>跟车受旁边车辆影响突然急刹车 n s s 预测性二分压力性一分`
- **识别文本**: 跟车受旁边车辆影响突然急刹车 n s s 预测性二分压力性一分
- **差异**: `跟车受旁边车辆影响突然急刹车nss预测性二分压力性一分` vs `跟车受旁边车辆影响突然急刹车NSS预测性2分压力性1分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>跟车 受旁边车辆影响 突然急刹车 NSS 预测性2分 压力性1分`
- **识别文本**: 跟车 受旁边车辆影响 突然急刹车 NSS 预测性2分 压力性1分

**结论**: 微调模型改进 ⬆️

---

### 样本 341: 2025_11_21_13_23_34.wav

**真实文本**: 开始测试

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

**结论**: 两个模型均识别正确 ✅

---

### 样本 342: 2025_11_20_23_22_31.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>大元老`
- **识别文本**: 大元老
- **差异**: `大元老` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>大元老`
- **识别文本**: 大元老
- **差异**: `大元老` vs `导航变道`

**结论**: 两个模型均识别错误 ❌

---

### 样本 343: 2025_11_21_10_27_59.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航频道`
- **识别文本**: 导航频道
- **差异**: `导航频道` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 344: 2025_11_20_23_17_59.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口执行`
- **识别文本**: 路口执行
- **差异**: `路口执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 345: 2025_11_20_20_00_35.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 346: 2025_11_21_14_21_05.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 347: 2025_11_20_20_14_24.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口执行`
- **识别文本**: 路口执行
- **差异**: `路口执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 348: 2025_11_17_14_01_29.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 349: 2025_11_17_13_44_46.wav

**真实文本**: 避让障碍物上压力大 预测差

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>避让障碍物上压力大预测差`
- **识别文本**: 避让障碍物上压力大预测差

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>避让障碍物 障压力大 预测差`
- **识别文本**: 避让障碍物 障压力大 预测差
- **差异**: `避让障碍物障压力大预测差` vs `避让障碍物上压力大预测差`

**结论**: 微调模型退化 ⬇️

---

### 样本 350: 2025_11_20_23_03_47.wav

**真实文本**: 弱势群体 弱势群体并没有下斑马线 可是车辆还是误刹车两次 舒适性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体弱势群体并没有下斑马线可是车辆还是误刹车两次直性三分`
- **识别文本**: 弱势群体弱势群体并没有下斑马线可是车辆还是误刹车两次直性三分
- **差异**: `弱势群体弱势群体并没有下斑马线可是车辆还是误刹车两次直性三分` vs `弱势群体弱势群体并没有下斑马线可是车辆还是误刹车两次舒适性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 弱势群体并没有下斑马线 可是车辆还是误刹车两次 舒适性3分`
- **识别文本**: 弱势群体 弱势群体并没有下斑马线 可是车辆还是误刹车两次 舒适性3分

**结论**: 微调模型改进 ⬆️

---

### 样本 351: 2025_11_20_20_00_37.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>readder`
- **识别文本**: readder
- **差异**: `readder` vs `绿灯`

**结论**: 微调模型退化 ⬇️

---

### 样本 352: 2025_11_21_15_20_21.wav

**真实文本**: 导航变道 变道后压实线就往回甩 拐大了 也变道特别 特别 让人感到突然 舒适性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道变道后压实线就往回甩呃拐大了也变道特别特别让人感到 <|zh|><|NEUTRAL|><|Speech|><|woitn|>突然舒适性三分`
- **识别文本**: 导航变道变道后压实线就往回甩呃拐大了也变道特别特别让人感到 突然舒适性三分
- **差异**: `导航变道变道后压实线就往回甩呃拐大了也变道特别特别让人感到突然舒适性三分` vs `导航变道变道后压实线就往回甩拐大了也变道特别特别让人感到突然舒适性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道 变道后 压实线就往回甩 呃 拐大了 也变道特别特别让人感到 <|zh|><|NEUTRAL|><|Speech|><|woitn|>突然 舒适性3分`
- **识别文本**: 导航变道 变道后 压实线就往回甩 呃 拐大了 也变道特别特别让人感到 突然 舒适性3分
- **差异**: `导航变道变道后压实线就往回甩呃拐大了也变道特别特别让人感到突然舒适性3分` vs `导航变道变道后压实线就往回甩拐大了也变道特别特别让人感到突然舒适性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 353: 2025_11_21_10_20_42.wav

**真实文本**: 弱势群体

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体`
- **识别文本**: 弱势群体

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体`
- **识别文本**: 弱势群体

**结论**: 两个模型均识别正确 ✅

---

### 样本 354: 2025_11_21_14_15_12.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>导航便道`
- **识别文本**: 导航便道
- **差异**: `导航便道` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 355: 2025_11_20_22_57_27.wav

**真实文本**: 弱势群体 够绕行弱势群体

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体能够绕行弱势群体`
- **识别文本**: 弱势群体能够绕行弱势群体
- **差异**: `弱势群体能够绕行弱势群体` vs `弱势群体够绕行弱势群体`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 能够绕行弱势群体`
- **识别文本**: 弱势群体 能够绕行弱势群体
- **差异**: `弱势群体能够绕行弱势群体` vs `弱势群体够绕行弱势群体`

**结论**: 两个模型均识别错误 ❌

---

### 样本 356: 2025_11_20_23_16_26.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口执行`
- **识别文本**: 路口执行
- **差异**: `路口执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 357: 2025_11_20_19_50_54.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 358: 2025_11_21_14_28_19.wav

**真实文本**: 红灯领航 在黄灯马上要变成红灯的时候 还在 还没有减速 然后当意识到马上要过不去 变成红灯的时候 急速刹停并且智驾退出 预测性一分 压力性一分 舒适性一般 效率性1分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航在黄灯马上要变成红灯的时候还在还没有减速然后当意识到了马上要过不去 <|zh|><|NEUTRAL|><|Speech|><|woitn|>变成红灯的时候急速杀停并且支驾退出预测性一分压力性一分舒适性一分效率性一分`
- **识别文本**: 红灯领航在黄灯马上要变成红灯的时候还在还没有减速然后当意识到了马上要过不去 变成红灯的时候急速杀停并且支驾退出预测性一分压力性一分舒适性一分效率性一分
- **差异**: `红灯领航在黄灯马上要变成红灯的时候还在还没有减速然后当意识到了马上要过不去变成红灯的时候急速杀停并且支驾退出预测性一分压力性一分舒适性一分效率性一分` vs `红灯领航在黄灯马上要变成红灯的时候还在还没有减速然后当意识到马上要过不去变成红灯的时候急速刹停并且智驾退出预测性一分压力性一分舒适性一般效率性1分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航 在黄灯马上要变成红灯的时候 还在 还没有减速 然后当意识到了 马上要过不去 <|zh|><|NEUTRAL|><|Speech|><|woitn|>变成红灯的时候 急速刹停并且自驾退出 预测性1分 压力性1分 舒适性1分 效率性1分`
- **识别文本**: 红灯领航 在黄灯马上要变成红灯的时候 还在 还没有减速 然后当意识到了 马上要过不去 变成红灯的时候 急速刹停并且自驾退出 预测性1分 压力性1分 舒适性1分 效率性1分
- **差异**: `红灯领航在黄灯马上要变成红灯的时候还在还没有减速然后当意识到了马上要过不去变成红灯的时候急速刹停并且自驾退出预测性1分压力性1分舒适性1分效率性1分` vs `红灯领航在黄灯马上要变成红灯的时候还在还没有减速然后当意识到马上要过不去变成红灯的时候急速刹停并且智驾退出预测性一分压力性一分舒适性一般效率性1分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 359: 2025_11_20_20_14_22.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 360: 2025_11_20_19_56_01.wav

**真实文本**: 测试结束

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>测试结束`
- **识别文本**: 测试结束

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>测试结束`
- **识别文本**: 测试结束

**结论**: 两个模型均识别正确 ✅

---

### 样本 361: 2025_11_20_23_02_27.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 362: 2025_11_21_10_26_56.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 363: 2025_11_20_19_54_23.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 364: 2025_11_20_22_52_41.wav

**真实文本**: 障碍物绕行 能够尝试绕过骑线开的慢行车辆 预测性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物造型能够尝试绕过祁线开的慢行车车辆预测性五分`
- **识别文本**: 障碍物造型能够尝试绕过祁线开的慢行车车辆预测性五分
- **差异**: `障碍物造型能够尝试绕过祁线开的慢行车车辆预测性五分` vs `障碍物绕行能够尝试绕过骑线开的慢行车辆预测性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行 能够尝试绕过骑线开的慢行车辆 预测性5分`
- **识别文本**: 障碍物绕行 能够尝试绕过骑线开的慢行车辆 预测性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 365: 2025_11_21_14_12_04.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 366: 2025_11_21_13_29_47.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 367: 2025_11_20_20_58_48.wav

**真实文本**: 弱势群体避让 知道避让不抢路 预测性5分 压力性6分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体避让知道避让不抢路预测性五分压力性六分`
- **识别文本**: 弱势群体避让知道避让不抢路预测性五分压力性六分
- **差异**: `弱势群体避让知道避让不抢路预测性五分压力性六分` vs `弱势群体避让知道避让不抢路预测性5分压力性6分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体避让 知道避让不抢路 预测性5分 压力性6分`
- **识别文本**: 弱势群体避让 知道避让不抢路 预测性5分 压力性6分

**结论**: 微调模型改进 ⬆️

---

### 样本 368: 2025_11_21_14_05_48.wav

**真实文本**: 弱势群体 在路口右转时 可以避让弱势群体 速度较慢 得提前减速 舒适性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体在路口右转时可以避让弱势群体速度较慢得提前减速舒适性五分`
- **识别文本**: 弱势群体在路口右转时可以避让弱势群体速度较慢得提前减速舒适性五分
- **差异**: `弱势群体在路口右转时可以避让弱势群体速度较慢得提前减速舒适性五分` vs `弱势群体在路口右转时可以避让弱势群体速度较慢得提前减速舒适性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 在路口右转时 可以避让弱势群体 速度较慢 得提前减速 舒适性5分`
- **识别文本**: 弱势群体 在路口右转时 可以避让弱势群体 速度较慢 得提前减速 舒适性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 369: 2025_11_21_15_18_43.wav

**真实文本**: 环岛 在环岛里的路线总是 导致了压力有点大 压力性三分 预测性三分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛在环岛里的路线总是导致的压力有点大压力性三分预测性三分`
- **识别文本**: 环岛在环岛里的路线总是导致的压力有点大压力性三分预测性三分
- **差异**: `环岛在环岛里的路线总是导致的压力有点大压力性三分预测性三分` vs `环岛在环岛里的路线总是导致了压力有点大压力性三分预测性三分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛 在环岛里的路线总是导致的压力有点大 压力性3分 预测性3分`
- **识别文本**: 环岛 在环岛里的路线总是导致的压力有点大 压力性3分 预测性3分
- **差异**: `环岛在环岛里的路线总是导致的压力有点大压力性3分预测性3分` vs `环岛在环岛里的路线总是导致了压力有点大压力性三分预测性三分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 370: 2025_11_21_13_26_15.wav

**真实文本**: 前车切入 右侧有车辆切入本车速度过慢效率性三分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>前车切入右侧有车辆接入本车速度过慢效率响三分`
- **识别文本**: 前车切入右侧有车辆接入本车速度过慢效率响三分
- **差异**: `前车切入右侧有车辆接入本车速度过慢效率响三分` vs `前车切入右侧有车辆切入本车速度过慢效率性三分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>前车切入 右侧有车辆切入 本车速度过慢 效率性3分`
- **识别文本**: 前车切入 右侧有车辆切入 本车速度过慢 效率性3分
- **差异**: `前车切入右侧有车辆切入本车速度过慢效率性3分` vs `前车切入右侧有车辆切入本车速度过慢效率性三分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 371: 2025_11_21_14_02_23.wav

**真实文本**: 红灯领航

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航`
- **识别文本**: 红灯领航

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航`
- **识别文本**: 红灯领航

**结论**: 两个模型均识别正确 ✅

---

### 样本 372: 2025_11_21_15_47_01.wav

**真实文本**: 路口左转

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转`
- **识别文本**: 路口左转

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转`
- **识别文本**: 路口左转

**结论**: 两个模型均识别正确 ✅

---

### 样本 373: 2025_11_17_13_50_32.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 374: 2025_11_20_23_16_32.wav

**真实文本**: 红灯领航

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>红灯领行`
- **识别文本**: 红灯领行
- **差异**: `红灯领行` vs `红灯领航`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航`
- **识别文本**: 红灯领航

**结论**: 微调模型改进 ⬆️

---

### 样本 375: 2025_11_17_13_36_57.wav

**真实文本**: 弱势群体 不舒适 舒适性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体不舒适舒适性三分`
- **识别文本**: 弱势群体不舒适舒适性三分
- **差异**: `弱势群体不舒适舒适性三分` vs `弱势群体不舒适舒适性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 不舒适 舒适性3分`
- **识别文本**: 弱势群体 不舒适 舒适性3分

**结论**: 微调模型改进 ⬆️

---

### 样本 376: 2025_11_20_23_00_36.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 377: 2025_11_21_10_47_03.wav

**真实文本**: Others

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>others`
- **识别文本**: others
- **差异**: `others` vs `Others`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>others`
- **识别文本**: others
- **差异**: `others` vs `Others`

**结论**: 两个模型均识别错误 ❌

---

### 样本 378: 2025_11_21_15_30_12.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 379: 2025_11_20_23_04_34.wav

**真实文本**: 汇出

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>会出`
- **识别文本**: 会出
- **差异**: `会出` vs `汇出`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>汇出`
- **识别文本**: 汇出

**结论**: 微调模型改进 ⬆️

---

### 样本 380: 2025_11_20_23_18_50.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 381: 2025_11_21_21_53_31.wav

**真实文本**: VRU Handling

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>v r u handling`
- **识别文本**: v r u handling
- **差异**: `vruhandling` vs `VRUHandling`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>vRU handling`
- **识别文本**: vRU handling
- **差异**: `vRUhandling` vs `VRUHandling`

**结论**: 两个模型均识别错误 ❌

---

### 样本 382: 2025_11_20_23_18_11.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 383: 2025_11_21_10_11_33.wav

**真实文本**: 其他 在环岛绕行过程中 突然打左转向灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他在环岛绕行过程中突然打左转行灯`
- **识别文本**: 其他在环岛绕行过程中突然打左转行灯
- **差异**: `其他在环岛绕行过程中突然打左转行灯` vs `其他在环岛绕行过程中突然打左转向灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>其他 在环岛绕行过程中 突然打左转向灯`
- **识别文本**: 其他 在环岛绕行过程中 突然打左转向灯

**结论**: 微调模型改进 ⬆️

---

### 样本 384: 2025_11_21_10_46_18.wav

**真实文本**: CL

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>xiao`
- **识别文本**: xiao
- **差异**: `xiao` vs `CL`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>seiao`
- **识别文本**: seiao
- **差异**: `seiao` vs `CL`

**结论**: 两个模型均识别错误 ❌

---

### 样本 385: 2025_11_21_10_44_41.wav

**真实文本**: Others

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>others`
- **识别文本**: others
- **差异**: `others` vs `Others`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>others`
- **识别文本**: others
- **差异**: `others` vs `Others`

**结论**: 两个模型均识别错误 ❌

---

### 样本 386: 2025_11_21_14_03_17.wav

**真实文本**: 路口直 行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 387: 2025_11_20_23_04_48.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>落可执行`
- **识别文本**: 落可执行
- **差异**: `落可执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 388: 2025_11_20_19_57_22.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿豆`
- **识别文本**: 绿豆
- **差异**: `绿豆` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿岛`
- **识别文本**: 绿岛
- **差异**: `绿岛` vs `绿灯`

**结论**: 两个模型均识别错误 ❌

---

### 样本 389: 2025_11_21_13_36_43.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 390: 2025_11_21_15_32_03.wav

**真实文本**: 提示尾门空间不足

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>提示尾门空间不足`
- **识别文本**: 提示尾门空间不足

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>提示尾门空间不足`
- **识别文本**: 提示尾门空间不足

**结论**: 两个模型均识别正确 ✅

---

### 样本 391: 2025_11_21_10_37_45.wav

**真实文本**: Green Light

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>green light`
- **识别文本**: green light
- **差异**: `greenlight` vs `GreenLight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>green light`
- **识别文本**: green light
- **差异**: `greenlight` vs `GreenLight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 392: 2025_11_20_23_18_30.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>大面倒`
- **识别文本**: 大面倒
- **差异**: `大面倒` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 393: 2025_11_17_13_37_17.wav

**真实文本**: 路口左转 速度较慢 路口较窄 有对向有车效率性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转速度较慢路口较窄对向有车效率性三分`
- **识别文本**: 路口左转速度较慢路口较窄对向有车效率性三分
- **差异**: `路口左转速度较慢路口较窄对向有车效率性三分` vs `路口左转速度较慢路口较窄有对向有车效率性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转 速度较慢 路口较窄 对向有车 效率性3分`
- **识别文本**: 路口左转 速度较慢 路口较窄 对向有车 效率性3分
- **差异**: `路口左转速度较慢路口较窄对向有车效率性3分` vs `路口左转速度较慢路口较窄有对向有车效率性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 394: 2025_11_17_14_00_25.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 395: 2025_11_20_23_08_18.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 396: 2025_11_20_20_11_43.wav

**真实文本**: 跟车 在避让弱势群体后 经过那个路口之后 有一个减速 不是很舒服 预测性3分 舒适性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>跟车在避让弱势群体后经过那个路口之后有一个减速不是很舒服预见性三分舒适性三分`
- **识别文本**: 跟车在避让弱势群体后经过那个路口之后有一个减速不是很舒服预见性三分舒适性三分
- **差异**: `跟车在避让弱势群体后经过那个路口之后有一个减速不是很舒服预见性三分舒适性三分` vs `跟车在避让弱势群体后经过那个路口之后有一个减速不是很舒服预测性3分舒适性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>跟车 在避让弱势群体后 经过那个路口之后 有一个减速 不是很舒服 预测性3分 舒适性3分`
- **识别文本**: 跟车 在避让弱势群体后 经过那个路口之后 有一个减速 不是很舒服 预测性3分 舒适性3分

**结论**: 微调模型改进 ⬆️

---

### 样本 397: 2025_11_21_15_29_06.wav

**真实文本**: 路口直行 结束后压左边线

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行结束后压左边线`
- **识别文本**: 路口直行结束后压左边线

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 结束后压左边线`
- **识别文本**: 路口直行 结束后压左边线

**结论**: 两个模型均识别正确 ✅

---

### 样本 398: 2025_11_20_19_42_01.wav

**真实文本**: 弱势群体避让 弱势群体侵入我们车道后 刹车不够及时 有碰撞风险 预测性一分 压力性一分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体避让弱势群体侵入到我们车道后刹车不够及时有碰撞风险预测性一分压力性一分`
- **识别文本**: 弱势群体避让弱势群体侵入到我们车道后刹车不够及时有碰撞风险预测性一分压力性一分
- **差异**: `弱势群体避让弱势群体侵入到我们车道后刹车不够及时有碰撞风险预测性一分压力性一分` vs `弱势群体避让弱势群体侵入我们车道后刹车不够及时有碰撞风险预测性一分压力性一分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体避让 弱势群体侵入到我们车道后 刹车不够及时 有碰撞风险 预测性1分 压力性1分`
- **识别文本**: 弱势群体避让 弱势群体侵入到我们车道后 刹车不够及时 有碰撞风险 预测性1分 压力性1分
- **差异**: `弱势群体避让弱势群体侵入到我们车道后刹车不够及时有碰撞风险预测性1分压力性1分` vs `弱势群体避让弱势群体侵入我们车道后刹车不够及时有碰撞风险预测性一分压力性一分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 399: 2025_11_21_15_41_14.wav

**真实文本**: 环岛 进环岛时打转向灯 在环岛内行驶压线行驶 变道时不打转向灯 在变道快要结束时打转向灯 预测性3分压力性3分 剪辑

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛 <|zh|><|NEUTRAL|><|Speech|><|woitn|>进环岛时打转向灯在环岛内行驶压线行驶变道时不打转向灯在变道快要结束时打转向灯预测性三份压力性三份剪辑`
- **识别文本**: 环岛 进环岛时打转向灯在环岛内行驶压线行驶变道时不打转向灯在变道快要结束时打转向灯预测性三份压力性三份剪辑
- **差异**: `环岛进环岛时打转向灯在环岛内行驶压线行驶变道时不打转向灯在变道快要结束时打转向灯预测性三份压力性三份剪辑` vs `环岛进环岛时打转向灯在环岛内行驶压线行驶变道时不打转向灯在变道快要结束时打转向灯预测性3分压力性3分剪辑`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛 <|zh|><|NEUTRAL|><|Speech|><|woitn|>进环岛时 打转向灯 在环岛内行驶压线行驶 变道时不打转向灯 在变道快要结束时 打转向灯 预测性3分 压力性3分 剪辑`
- **识别文本**: 环岛 进环岛时 打转向灯 在环岛内行驶压线行驶 变道时不打转向灯 在变道快要结束时 打转向灯 预测性3分 压力性3分 剪辑

**结论**: 微调模型改进 ⬆️

---

### 样本 400: 2025_11_21_14_29_27.wav

**真实文本**: 路口左转

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转`
- **识别文本**: 路口左转

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转`
- **识别文本**: 路口左转

**结论**: 两个模型均识别正确 ✅

---

### 样本 401: 2025_11_20_20_40_43.wav

**真实文本**: 红灯领航

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红狼领行`
- **识别文本**: 红狼领行
- **差异**: `红狼领行` vs `红灯领航`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航`
- **识别文本**: 红灯领航

**结论**: 微调模型改进 ⬆️

---

### 样本 402: 2025_11_20_22_52_20.wav

**真实文本**: 障碍物绕行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行`
- **识别文本**: 障碍物绕行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>障碍物绕行`
- **识别文本**: 障碍物绕行

**结论**: 两个模型均识别正确 ✅

---

### 样本 403: 2025_11_21_10_39_13.wav

**真实文本**: CL

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>是呀`
- **识别文本**: 是呀
- **差异**: `是呀` vs `CL`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>sah`
- **识别文本**: sah
- **差异**: `sah` vs `CL`

**结论**: 两个模型均识别错误 ❌

---

### 样本 404: 2025_11_20_23_08_20.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>对的`
- **识别文本**: 对的
- **差异**: `对的` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 微调模型改进 ⬆️

---

### 样本 405: 2025_11_20_20_04_27.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>当面闹`
- **识别文本**: 当面闹
- **差异**: `当面闹` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 微调模型改进 ⬆️

---

### 样本 406: 2025_11_20_23_13_29.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 407: 2025_11_21_15_41_44.wav

**真实文本**: 环岛

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛`
- **识别文本**: 环岛

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>环岛`
- **识别文本**: 环岛

**结论**: 两个模型均识别正确 ✅

---

### 样本 408: 2025_11_17_13_57_35.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|BGM|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 409: 2025_11_21_15_25_55.wav

**真实文本**: 路口直行 在过路口时 后侧有车已经贴近 并排行走行走时 本车往左侧车身上贴 预测性一分 压力性一分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行在过路口时后侧有车已经贴近并排行走行走时本车往左侧车身上贴预测性一分压力性一分`
- **识别文本**: 路口直行在过路口时后侧有车已经贴近并排行走行走时本车往左侧车身上贴预测性一分压力性一分

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 在过路口时 后侧有车已经贴近 并排行走 行走时本车往左侧车身上贴 预测性1分 压力性1分`
- **识别文本**: 路口直行 在过路口时 后侧有车已经贴近 并排行走 行走时本车往左侧车身上贴 预测性1分 压力性1分
- **差异**: `路口直行在过路口时后侧有车已经贴近并排行走行走时本车往左侧车身上贴预测性1分压力性1分` vs `路口直行在过路口时后侧有车已经贴近并排行走行走时本车往左侧车身上贴预测性一分压力性一分`

**结论**: 微调模型退化 ⬇️

---

### 样本 410: 2025_11_21_15_16_45.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 411: 2025_11_20_19_49_36.wav

**真实文本**: 导航变道 变道太晚了 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道变道太晚了预测性三分`
- **识别文本**: 导航变道变道太晚了预测性三分
- **差异**: `导航变道变道太晚了预测性三分` vs `导航变道变道太晚了预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道 变道太晚了 预测性3分`
- **识别文本**: 导航变道 变道太晚了 预测性3分

**结论**: 微调模型改进 ⬆️

---

### 样本 412: 2025_11_20_19_40_13.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超帅别闹`
- **识别文本**: 超帅别闹
- **差异**: `超帅别闹` vs `超车变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 微调模型改进 ⬆️

---

### 样本 413: 2025_11_20_23_00_19.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 414: 2025_11_20_19_36_56.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 415: 2025_11_21_15_40_56.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 416: 2025_11_21_15_41_32.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 417: 2025_11_20_20_32_35.wav

**真实文本**: 绿灯 绿灯变黄灯时 闯黄灯 效率性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯绿灯变黄灯时闯黄灯效率性五分`
- **识别文本**: 绿灯绿灯变黄灯时闯黄灯效率性五分
- **差异**: `绿灯绿灯变黄灯时闯黄灯效率性五分` vs `绿灯绿灯变黄灯时闯黄灯效率性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯 绿灯变黄灯时闯黄灯 效率性5分`
- **识别文本**: 绿灯 绿灯变黄灯时闯黄灯 效率性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 418: 2025_11_20_21_00_22.wav

**真实文本**: 跟车 KD 在一个乱七八糟的路口 还有施工区域的围挡的时候 速度的过快 压力性3分 预测性4分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>跟车 k d 在一个乱七八糟的路口还有施工区域围挡的时候速度过快压力性三分预测性四分`
- **识别文本**: 跟车 k d 在一个乱七八糟的路口还有施工区域围挡的时候速度过快压力性三分预测性四分
- **差异**: `跟车kd在一个乱七八糟的路口还有施工区域围挡的时候速度过快压力性三分预测性四分` vs `跟车KD在一个乱七八糟的路口还有施工区域的围挡的时候速度的过快压力性3分预测性4分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>跟车 KD 在一个乱七八糟的路口 还有施工区域围挡的时候 速度过快 压力性3分 预测性4分`
- **识别文本**: 跟车 KD 在一个乱七八糟的路口 还有施工区域围挡的时候 速度过快 压力性3分 预测性4分
- **差异**: `跟车KD在一个乱七八糟的路口还有施工区域围挡的时候速度过快压力性3分预测性4分` vs `跟车KD在一个乱七八糟的路口还有施工区域的围挡的时候速度的过快压力性3分预测性4分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 419: 2025_11_21_15_42_30.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 420: 2025_11_17_13_40_29.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 421: 2025_11_21_15_40_53.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 422: 2025_11_21_22_00_02.wav

**真实文本**: Change Lane

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>change lane`
- **识别文本**: change lane
- **差异**: `changelane` vs `ChangeLane`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>change lane`
- **识别文本**: change lane
- **差异**: `changelane` vs `ChangeLane`

**结论**: 两个模型均识别错误 ❌

---

### 样本 423: 2025_11_20_20_58_13.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>绿道`
- **识别文本**: 绿道
- **差异**: `绿道` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>绿道`
- **识别文本**: 绿道
- **差异**: `绿道` vs `绿灯`

**结论**: 两个模型均识别错误 ❌

---

### 样本 424: 2025_11_21_21_56_54.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>johnson street`
- **识别文本**: johnson street
- **差异**: `johnsonstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>johnson street`
- **识别文本**: johnson street
- **差异**: `johnsonstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 425: 2025_11_21_10_27_07.wav

**真实文本**: 红灯跟车

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯跟车`
- **识别文本**: 红灯跟车

**结论**: 两个模型均识别正确 ✅

---

### 样本 426: 2025_11_20_19_53_11.wav

**真实文本**: 汇出

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>会出`
- **识别文本**: 会出
- **差异**: `会出` vs `汇出`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>汇出`
- **识别文本**: 汇出

**结论**: 微调模型改进 ⬆️

---

### 样本 427: 2025_11_21_10_26_05.wav

**真实文本**: 路线规划 没有按正确的车道线行驶 没有提前变到右侧右转专用道 剪辑

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路线规划没有按正确的车道线行驶没有提前变道右侧右转专用道剪辑`
- **识别文本**: 路线规划没有按正确的车道线行驶没有提前变道右侧右转专用道剪辑
- **差异**: `路线规划没有按正确的车道线行驶没有提前变道右侧右转专用道剪辑` vs `路线规划没有按正确的车道线行驶没有提前变到右侧右转专用道剪辑`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路线规划 没有按正确的车道线行驶 没有提前变道右侧右转专用道剪辑`
- **识别文本**: 路线规划 没有按正确的车道线行驶 没有提前变道右侧右转专用道剪辑
- **差异**: `路线规划没有按正确的车道线行驶没有提前变道右侧右转专用道剪辑` vs `路线规划没有按正确的车道线行驶没有提前变到右侧右转专用道剪辑`

**结论**: 两个模型均识别错误 ❌

---

### 样本 428: 2025_11_20_20_59_56.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 429: 2025_11_20_20_11_59.wav

**真实文本**: 红灯领航

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红南领航`
- **识别文本**: 红南领航
- **差异**: `红南领航` vs `红灯领航`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红挡领航`
- **识别文本**: 红挡领航
- **差异**: `红挡领航` vs `红灯领航`

**结论**: 两个模型均识别错误 ❌

---

### 样本 430: 2025_11_21_15_20_08.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>reader`
- **识别文本**: reader
- **差异**: `reader` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>read灯`
- **识别文本**: read灯
- **差异**: `read灯` vs `绿灯`

**结论**: 两个模型均识别错误 ❌

---

### 样本 431: 2025_11_21_14_14_47.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 432: 2025_11_21_15_15_43.wav

**真实文本**: 施工路段 被锥桶挡住 完全动不了 效率性2分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>施工路段被追同挡住完全动不了了效率性二分`
- **识别文本**: 施工路段被追同挡住完全动不了了效率性二分
- **差异**: `施工路段被追同挡住完全动不了了效率性二分` vs `施工路段被锥桶挡住完全动不了效率性2分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>施工路段 被锥桶挡住 完全动不了了 效率性2分`
- **识别文本**: 施工路段 被锥桶挡住 完全动不了了 效率性2分
- **差异**: `施工路段被锥桶挡住完全动不了了效率性2分` vs `施工路段被锥桶挡住完全动不了效率性2分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 433: 2025_11_21_15_27_45.wav

**真实文本**: 红灯领航 红灯响应慢 预测性3分 效率性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航红灯响要慢预测性三分效率性三分`
- **识别文本**: 红灯领航红灯响要慢预测性三分效率性三分
- **差异**: `红灯领航红灯响要慢预测性三分效率性三分` vs `红灯领航红灯响应慢预测性3分效率性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯领航 红灯响要慢 预测性3分 效率性3分`
- **识别文本**: 红灯领航 红灯响要慢 预测性3分 效率性3分
- **差异**: `红灯领航红灯响要慢预测性3分效率性3分` vs `红灯领航红灯响应慢预测性3分效率性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 434: 2025_11_21_13_37_29.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 435: 2025_11_20_20_53_18.wav

**真实文本**: 路口右转 在右转时骑上了马路牙子 预测性2分 压力性两分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转在右转时骑上了马路牙子预测性两分压力性两分`
- **识别文本**: 路口右转在右转时骑上了马路牙子预测性两分压力性两分
- **差异**: `路口右转在右转时骑上了马路牙子预测性两分压力性两分` vs `路口右转在右转时骑上了马路牙子预测性2分压力性两分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口右转 在右转时骑上了马路牙子 预测性2分 压力性2分`
- **识别文本**: 路口右转 在右转时骑上了马路牙子 预测性2分 压力性2分
- **差异**: `路口右转在右转时骑上了马路牙子预测性2分压力性2分` vs `路口右转在右转时骑上了马路牙子预测性2分压力性两分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 436: 2025_11_20_23_22_22.wav

**真实文本**: 红灯领航

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯两行`
- **识别文本**: 红灯两行
- **差异**: `红灯两行` vs `红灯领航`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>红灯两航`
- **识别文本**: 红灯两航
- **差异**: `红灯两航` vs `红灯领航`

**结论**: 两个模型均识别错误 ❌

---

### 样本 437: 2025_11_21_21_56_31.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juhnson street`
- **识别文本**: juhnson street
- **差异**: `juhnsonstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juson street`
- **识别文本**: juson street
- **差异**: `jusonstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 438: 2025_11_20_23_08_56.wav

**真实文本**: 弱势群体 在环岛中避让弱势群体

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体在环岛中别让弱势群体`
- **识别文本**: 弱势群体在环岛中别让弱势群体
- **差异**: `弱势群体在环岛中别让弱势群体` vs `弱势群体在环岛中避让弱势群体`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 在环岛中避让弱势群体`
- **识别文本**: 弱势群体 在环岛中避让弱势群体

**结论**: 微调模型改进 ⬆️

---

### 样本 439: 2025_11_21_21_59_46.wav

**真实文本**: Change Lane

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>changelan`
- **识别文本**: changelan
- **差异**: `changelan` vs `ChangeLane`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>trengelan`
- **识别文本**: trengelan
- **差异**: `trengelan` vs `ChangeLane`

**结论**: 两个模型均识别错误 ❌

---

### 样本 440: 2025_11_20_23_01_46.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>绿到`
- **识别文本**: 绿到
- **差异**: `绿到` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>绿道`
- **识别文本**: 绿道
- **差异**: `绿道` vs `绿灯`

**结论**: 两个模型均识别错误 ❌

---

### 样本 441: 2025_11_21_10_23_51.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超寿频的`
- **识别文本**: 超寿频的
- **差异**: `超寿频的` vs `超车变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变`
- **识别文本**: 超车变
- **差异**: `超车变` vs `超车变道`

**结论**: 两个模型均识别错误 ❌

---

### 样本 442: 2025_11_21_15_20_10.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口执行`
- **识别文本**: 路口执行
- **差异**: `路口执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 443: 2025_11_20_23_17_03.wav

**真实文本**: 导航变道 导航变道略微有一些晚 但在前方插入后面行驶较慢的大车 效率性3份 预测性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道导航变道略微有一些晚但在前方插入后面行驶较慢的大车效率性三分预算性三分`
- **识别文本**: 导航变道导航变道略微有一些晚但在前方插入后面行驶较慢的大车效率性三分预算性三分
- **差异**: `导航变道导航变道略微有一些晚但在前方插入后面行驶较慢的大车效率性三分预算性三分` vs `导航变道导航变道略微有一些晚但在前方插入后面行驶较慢的大车效率性3份预测性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道 导航变道略微有一些晚 但在前方插入后面行驶较慢的大车 效率性3分 预测性3分`
- **识别文本**: 导航变道 导航变道略微有一些晚 但在前方插入后面行驶较慢的大车 效率性3分 预测性3分
- **差异**: `导航变道导航变道略微有一些晚但在前方插入后面行驶较慢的大车效率性3分预测性3分` vs `导航变道导航变道略微有一些晚但在前方插入后面行驶较慢的大车效率性3份预测性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 444: 2025_11_21_15_30_25.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|SAD|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 445: 2025_11_21_10_21_15.wav

**真实文本**: 路口左转 在左转过程中加速

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转在左转过程中加速`
- **识别文本**: 路口左转在左转过程中加速

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口左转 在左转过程中加速`
- **识别文本**: 路口左转 在左转过程中加速

**结论**: 两个模型均识别正确 ✅

---

### 样本 446: 2025_11_21_21_56_29.wav

**真实文本**: Junction Straight

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juhnson street`
- **识别文本**: juhnson street
- **差异**: `juhnsonstreet` vs `JunctionStraight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juhnction street`
- **识别文本**: juhnction street
- **差异**: `juhnctionstreet` vs `JunctionStraight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 447: 2025_11_21_13_15_37.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 448: 2025_11_20_19_34_18.wav

**真实文本**: 开始测试

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>开始测试`
- **识别文本**: 开始测试

**结论**: 两个模型均识别正确 ✅

---

### 样本 449: 2025_11_17_13_30_13.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>浴灯`
- **识别文本**: 浴灯
- **差异**: `浴灯` vs `绿灯`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 微调模型改进 ⬆️

---

### 样本 450: 2025_11_21_14_12_08.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|SAD|><|Speech|><|woitn|>路口执行`
- **识别文本**: 路口执行
- **差异**: `路口执行` vs `路口直行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 微调模型改进 ⬆️

---

### 样本 451: 2025_11_21_15_36_46.wav

**真实文本**: 弱势群体 能够避让骑自行车的老头儿 预测性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体能够避让骑自行车的老头预测性五分`
- **识别文本**: 弱势群体能够避让骑自行车的老头预测性五分
- **差异**: `弱势群体能够避让骑自行车的老头预测性五分` vs `弱势群体能够避让骑自行车的老头儿预测性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 能够避让骑自行车的老头 预测性5分`
- **识别文本**: 弱势群体 能够避让骑自行车的老头 预测性5分
- **差异**: `弱势群体能够避让骑自行车的老头预测性5分` vs `弱势群体能够避让骑自行车的老头儿预测性5分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 452: 2025_11_20_20_56_35.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航面罩`
- **识别文本**: 导航面罩
- **差异**: `导航面罩` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>导航面道`
- **识别文本**: 导航面道
- **差异**: `导航面道` vs `导航变道`

**结论**: 两个模型均识别错误 ❌

---

### 样本 453: 2025_11_21_21_58_22.wav

**真实文本**: Junction Turn

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>junction turn`
- **识别文本**: junction turn
- **差异**: `junctionturn` vs `JunctionTurn`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>juangction turn`
- **识别文本**: juangction turn
- **差异**: `juangctionturn` vs `JunctionTurn`

**结论**: 两个模型均识别错误 ❌

---

### 样本 454: 2025_11_21_10_37_43.wav

**真实文本**: Green Light

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>green light`
- **识别文本**: green light
- **差异**: `greenlight` vs `GreenLight`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>green light`
- **识别文本**: green light
- **差异**: `greenlight` vs `GreenLight`

**结论**: 两个模型均识别错误 ❌

---

### 样本 455: 2025_11_20_20_56_00.wav

**真实文本**: 超车变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超帅变道`
- **识别文本**: 超帅变道
- **差异**: `超帅变道` vs `超车变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>超车变道`
- **识别文本**: 超车变道

**结论**: 微调模型改进 ⬆️

---

### 样本 456: 2025_11_20_22_52_15.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 457: 2025_11_21_15_42_57.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 458: 2025_11_21_15_34_27.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 459: 2025_11_21_15_12_40.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航变道`
- **识别文本**: 导航变道

**结论**: 两个模型均识别正确 ✅

---

### 样本 460: 2025_11_20_23_05_52.wav

**真实文本**: 弱势群体 弱势群体绕行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱弱群体弱群体绕形`
- **识别文本**: 弱弱群体弱群体绕形
- **差异**: `弱弱群体弱群体绕形` vs `弱势群体弱势群体绕行`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>弱势群体 弱势群体绕行`
- **识别文本**: 弱势群体 弱势群体绕行

**结论**: 微调模型改进 ⬆️

---

### 样本 461: 2025_11_20_20_53_24.wav

**真实文本**: 路口直行 直行过程中没有灯 且路有点黑 有减速 压力性5分 预测性5分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行执行过程中没有灯且路有点黑有减速压力线五分预测线五分`
- **识别文本**: 路口直行执行过程中没有灯且路有点黑有减速压力线五分预测线五分
- **差异**: `路口直行执行过程中没有灯且路有点黑有减速压力线五分预测线五分` vs `路口直行直行过程中没有灯且路有点黑有减速压力性5分预测性5分`

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行 直行过程中没有灯 且路有点黑 有减速 压力性5分 预测性5分`
- **识别文本**: 路口直行 直行过程中没有灯 且路有点黑 有减速 压力性5分 预测性5分

**结论**: 微调模型改进 ⬆️

---

### 样本 462: 2025_11_20_20_29_59.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 463: 2025_11_20_20_17_28.wav

**真实文本**: 路口直行

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>路口直行`
- **识别文本**: 路口直行

**结论**: 两个模型均识别正确 ✅

---

### 样本 464: 2025_11_17_13_56_30.wav

**真实文本**: 前车切入 刹车不舒适 压力3分 舒适性3分

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>前车切入他刹车不舒适压力三分舒适性三分`
- **识别文本**: 前车切入他刹车不舒适压力三分舒适性三分
- **差异**: `前车切入他刹车不舒适压力三分舒适性三分` vs `前车切入刹车不舒适压力3分舒适性3分`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>前车切入 他刹车不舒适 压力3分 舒适性3分`
- **识别文本**: 前车切入 他刹车不舒适 压力3分 舒适性3分
- **差异**: `前车切入他刹车不舒适压力3分舒适性3分` vs `前车切入刹车不舒适压力3分舒适性3分`

**结论**: 两个模型均识别错误 ❌

---

### 样本 465: 2025_11_20_23_22_03.wav

**真实文本**: 导航变道

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航别闹`
- **识别文本**: 导航别闹
- **差异**: `导航别闹` vs `导航变道`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>导航别道`
- **识别文本**: 导航别道
- **差异**: `导航别道` vs `导航变道`

**结论**: 两个模型均识别错误 ❌

---

### 样本 466: 2025_11_21_15_22_33.wav

**真实文本**: 绿灯

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

#### 微调模型 (model.pt.ep32)

- **状态**: ✅ 正确
- **原始输出**: `<|zh|><|NEUTRAL|><|Speech|><|woitn|>绿灯`
- **识别文本**: 绿灯

**结论**: 两个模型均识别正确 ✅

---

### 样本 467: 2025_11_21_10_46_14.wav

**真实文本**: CL

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|yue|><|NEUTRAL|><|Speech|><|woitn|>笑`
- **识别文本**: 笑
- **差异**: `笑` vs `CL`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>笑`
- **识别文本**: 笑
- **差异**: `笑` vs `CL`

**结论**: 两个模型均识别错误 ❌

---

### 样本 468: 2025_11_21_10_38_27.wav

**真实文本**: Red Light Leading

#### 原始模型 (C:\niiya\tools\AI\FunASR\models\SenseVoiceSmall)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|EMO_UNKNOWN|><|Speech|><|woitn|>right the light leading`
- **识别文本**: right the light leading
- **差异**: `rightthelightleading` vs `RedLightLeading`

#### 微调模型 (model.pt.ep32)

- **状态**: ❌ 错误
- **原始输出**: `<|en|><|NEUTRAL|><|Speech|><|woitn|>right light leading`
- **识别文本**: right light leading
- **差异**: `rightlightleading` vs `RedLightLeading`

**结论**: 两个模型均识别错误 ❌

---

## 总结

本次测试共评估 468 个音频样本:

- **原始模型准确率**: 45.51%
- **微调模型准确率**: 66.03%
- **准确率变化**: +20.51%

✅ **微调成功**: 模型性能提升了 20.51%
