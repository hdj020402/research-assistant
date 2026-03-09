---
title: "A Neural Time-Series Learning Method for Accelerating Free-Energy Perturbation and Rare-Event Molecular Dynamics Simulations"
title_zh: "用于加速自由能扰动和稀有事件分子动力学模拟的神经时间序列学习方法"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c03127"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPCRlWUSwQ0a8eQqEWu-2BeSh0MqAAclE-2Bhw9a-2FcBmJ5aiB9s6QetTa7WalDOqKKv9flugxWck9OSmsqgIY903h7kcCiR0V7fPVsKFBypkfLPrx2-2B6HYPsNg3F4RhjtUutARxxsn_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBDsnXsjSZT2MEt8ZzbaUJSVAm-2BXE1p3p5WcDXukU0LxltAecEC110NcDPE4KDONm8s-2Bl5l62g7-2FbKpwoqtnVoJkmEPM6ApiTa51qdz5-2BglRPdAZCoj5XbD5WMf78TaWM5Bk-2FVRk-2F0BHrSBzo5cWj6DIkuOaCzpJqSNrCCkDURS9ZjxUITDy5SOc-2BewtQIG9RI-3D"
pub_date: ""
tags: ["neural-networks", "molecular-dynamics", "free-energy-calculation", "deep-learning", "rare-event-sampling"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# A Neural Time-Series Learning Method for Accelerating Free-Energy Perturbation and Rare-Event Molecular Dynamics Simulations

**用于加速自由能扰动和稀有事件分子动力学模拟的神经时间序列学习方法**

## 精华总结
介绍了BiLSTMK-MD，一种神经时间序列学习方法，为分子动力学和自由能微扰轨迹构建因果关系保留的代理模型，以减少采样需求，为自由能估计和稀有事件表征提供了降低采样需求的途径。

**关键词**: 神经网络、分子动力学模拟、自由能微扰、时间序列学习、LSTM

## 摘要（英文）
Molecular dynamics (MD) simulations are central to materials and drug discovery yet remain computationally demanding, particularly for free-energy perturbation (FEP) protocols and rare-event sampling. Existing sequence-based accelerators, especially Long Short-Term Memory (LSTM) models, often fail to capture long-range temporal structure and provide sufficient expressive capacity in noisy trajectories. Here, we introduce BiLSTMK-MD, a neural time-series learning method that constructs a causality-preserving surrogate for MD and FEP trajectories to reduce sampling requirements. The approach couples a sliding-window bidirectional LSTM encoder, which preserves long-range correlations, with an attention mechanism to enhance temporally informative frames, while a Kolmogorov-Arnold network output layer applies expressive nonlinear readout to decode the attention-refined representation into the final output. A two-stage, fANOVA-guided Bayesian optimization process searches for the optimal hyperparameter configuration for each system. Across four data sets, BiLSTMK-MD achieves mean absolute errors below 1.5 kcal mol-1 for window-resolved free-energy increments, reconstructs dihedral free-energy basins from 1-10% of trajectories, and maintains performance across systems. In long-trajectory regimes, it affords up to 400-fold acceleration for FEP and >700-fold speedup for rare-conformation sampling over conventional MD/FEP simulation. This neural time-series surrogate therefore provides a route to reducing sampling demands for free-energy estimation and rare-event characterization.

## 摘要（中文）
分子动力学 (MD) 模拟是材料和药物发现的核心，但仍然需要计算，特别是对于自由能扰动 (FEP) 协议和罕见事件采样。现有的基于序列的加速器，尤其是长短期记忆 (LSTM) 模型，通常无法捕获长程时间结构并在嘈杂的轨迹中提供足够的表达能力。在这里，我们介绍bilstmk-md，这是一种神经时间序列学习方法，该方法为MD和FEP轨迹构造了因果关系保留代理，以减少采样要求。该方法将保留长距离相关性的滑动窗口双向LSTM编码器与注意力机制耦合在一起，以增强时间信息帧，而kolmogorov-arnold网络输出层则应用表达性非线性读出将注意力细化的表示解码为最终输出。两阶段，fANOVA指导的贝叶斯优化过程为每个系统搜索最佳的超参数配置。在四个数据集上，bilstmk-md对于窗口分辨的自由能增量实现了低于1.5 kcal mol-1的平均绝对误差，从1-10% 个轨迹重建了二面角自由能盆地，并保持了整个系统的性能。在长轨迹方案中，与常规MD/FEP模拟相比，它为FEP提供了高达400倍的加速度，并且为稀有构象采样提供了&gt; 700倍的加速。因此，这种神经时间序列替代提供了减少自由能估计和罕见事件表征的采样需求的途径。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPCRlWUSwQ0a8eQqEWu-2BeSh0MqAAclE-2Bhw9a-2FcBmJ5aiB9s6QetTa7WalDOqKKv9flugxWck9OSmsqgIY903h7kcCiR0V7fPVsKFBypkfLPrx2-2B6HYPsNg3F4RhjtUutARxxsn_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBDsnXsjSZT2MEt8ZzbaUJSVAm-2BXE1p3p5WcDXukU0LxltAecEC110NcDPE4KDONm8s-2Bl5l62g7-2FbKpwoqtnVoJkmEPM6ApiTa51qdz5-2BglRPdAZCoj5XbD5WMf78TaWM5Bk-2FVRk-2F0BHrSBzo5cWj6DIkuOaCzpJqSNrCCkDURS9ZjxUITDy5SOc-2BewtQIG9RI-3D)
