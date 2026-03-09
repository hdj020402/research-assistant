---
title: "A Neural Time-Series Learning Method for Accelerating Free-Energy Perturbation and Rare-Event Molecular Dynamics Simulations"
title_zh: "用于加速自由能扰动和稀有事件分子动力学模拟的神经时间序列学习方法"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c03127"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPCRlWUSwQ0a8eQqEWu-2BeSh0MqAAclE-2Bhw9a-2FcBmJ5aiB9s6QetTa7WalDOqKKv9flugxWck9OSmsqgIY903h7kcCiR0V7fPVsKFBypkfLPrx2-2B6HYPsNg3F4RhjtUutARxxsn_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBDsnXsjSZT2MEt8ZzbaUJSVAm-2BXE1p3p5WcDXukU0LxltAecEC110NcDPE4KDONm8s-2Bl5l62g7-2FbKpwoqtnVoJkmEPM6ApiTa51qdz5-2BglRPdAZCoj5XbD5WMf78TaWM5Bk-2FVRk-2F0BHrSBzo5cWj6DIkuOaCzpJqSNrCCkDURS9ZjxUITDy5SOc-2BewtQIG9RI-3D"
pub_date: ""
tags: ["neural-networks", "molecular-dynamics", "free-energy-calculations", "deep-learning", "surrogate-modeling"]
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
本研究介绍了BiLSTMK-MD，一种神经时间序列学习方法，为分子动力学和自由能微扰轨迹构建因果保持代理模型，大幅减少采样需求，为自由能估计和稀有事件表征提供了新途径。

**关键词**: 神经网络、分子动力学、自由能微扰、时间序列学习、LSTM、稀有事件采样

## 摘要（英文）
Molecular dynamics (MD) simulations are central to materials and drug discovery yet remain computationally demanding, particularly for free-energy perturbation (FEP) protocols and rare-event sampling. Existing sequence-based accelerators, especially Long Short-Term Memory (LSTM) models, often fail to capture long-range temporal structure and provide sufficient expressive capacity in noisy trajectories. Here, we introduce BiLSTMK-MD, a neural time-series learning method that constructs a causality-preserving surrogate for MD and FEP trajectories to reduce sampling requirements. The approach couples a sliding-window bidirectional LSTM encoder, which preserves long-range correlations, with an attention mechanism to enhance temporally informative frames, while a Kolmogorov-Arnold network output layer applies expressive nonlinear readout to decode the attention-refined representation into the final output. A two-stage, fANOVA-guided Bayesian optimization process searches for the optimal hyperparameter configuration for each system. Across four data sets, BiLSTMK-MD achieves mean absolute errors below 1.5 kcal mol-1 for window-resolved free-energy increments, reconstructs dihedral free-energy basins from 1-10% of trajectories, and maintains performance across systems. In long-trajectory regimes, it affords up to 400-fold acceleration for FEP and >700-fold speedup for rare-conformation sampling over conventional MD/FEP simulation. This neural time-series surrogate therefore provides a route to reducing sampling demands for free-energy estimation and rare-event characterization.

## 摘要（中文）
分子动力学（MD）模拟在材料和药物发现中占据核心地位，但其计算成本仍然很高，尤其是在自由能微扰（FEP）方法和稀有事件采样方面。现有的基于序列的加速器，尤其是长短期记忆（LSTM）模型，往往难以捕捉长时间尺度的时序结构，并且在噪声较大的轨迹中缺乏足够的表达能力。在此，我们提出BiLSTMK-MD——一种基于神经网络的时间序列学习方法，该方法为分子动力学和自由能计算轨迹构建保持因果关系的替代数据，以降低采样需求。该方法将滑动窗口双向LSTM编码器（能够保留长距离相关性）与注意力机制相结合，以增强具有时间信息的帧；同时，采用科尔莫戈洛夫–阿诺德网络输出层进行富有表现力的非线性读出，将经过注意力机制精炼的表示解码为最终输出。一个由fANOVA指导的两阶段贝叶斯优化过程，用于为每个系统搜索最优的超参数配置。在四个数据集上，BiLSTMK-MD对窗口分辨的自由能增量实现了低于1.5 kcal mol⁻¹ 的平均绝对误差，仅需1% 至10% 的轨迹即可重建二面角自由能势阱，并且在不同体系间保持稳定的性能。在长轨迹模拟中，相较于传统的分子动力学/自由能微扰模拟，该方法可将FEP计算加速多达400倍，并将稀有构象采样速度提升700倍以上。因此，这种神经时间序列替代模型为降低自由能估计和稀有事件表征所需的采样量提供了一条途径。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPCRlWUSwQ0a8eQqEWu-2BeSh0MqAAclE-2Bhw9a-2FcBmJ5aiB9s6QetTa7WalDOqKKv9flugxWck9OSmsqgIY903h7kcCiR0V7fPVsKFBypkfLPrx2-2B6HYPsNg3F4RhjtUutARxxsn_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBDsnXsjSZT2MEt8ZzbaUJSVAm-2BXE1p3p5WcDXukU0LxltAecEC110NcDPE4KDONm8s-2Bl5l62g7-2FbKpwoqtnVoJkmEPM6ApiTa51qdz5-2BglRPdAZCoj5XbD5WMf78TaWM5Bk-2FVRk-2F0BHrSBzo5cWj6DIkuOaCzpJqSNrCCkDURS9ZjxUITDy5SOc-2BewtQIG9RI-3D)
