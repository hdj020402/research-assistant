---
title: "A Neural Time-Series Learning Method for Accelerating Free-Energy Perturbation and Rare-Event Molecular Dynamics Simulations"
title_zh: "用于加速自由能微扰和稀有事件分子动力学模拟的神经时间序列学习方法"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c03127"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPCRlWUSwQ0a8eQqEWu-2BeSh0MqAAclE-2Bhw9a-2FcBmJ5aiB9s6QetTa7WalDOqKKv9flugxWck9OSmsqgIY903h7kcCiR0V7fPVsKFBypkfLPrx2-2B6HYPsNg3F4RhjtUutARxxsn_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBDsnXsjSZT2MEt8ZzbaUJSVAm-2BXE1p3p5WcDXukU0LxltAecEC110NcDPE4KDONm8s-2Bl5l62g7-2FbKpwoqtnVoJkmEPM6ApiTa51qdz5-2BglRPdAZCoj5XbD5WMf78TaWM5Bk-2FVRk-2F0BHrSBzo5cWj6DIkuOaCzpJqSNrCCkDURS9ZjxUITDy5SOc-2BewtQIG9RI-3D"
pub_date: ""
tags: ["deep-learning", "molecular-dynamics", "free-energy-calculation", "neural-surrogate", "rare-event-sampling"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# A Neural Time-Series Learning Method for Accelerating Free-Energy Perturbation and Rare-Event Molecular Dynamics Simulations

**用于加速自由能微扰和稀有事件分子动力学模拟的神经时间序列学习方法**

## 精华总结
BiLSTMK-MD是一种神经时间序列学习方法,通过为MD和FEP轨迹构建因果性保留的代理模型来减少采样需求,为自由能估计和稀有事件表征提供了新途径,相比传统模拟方法实现了数百倍的加速。

**关键词**: 神经网络、分子动力学、自由能微扰、时间序列学习、稀有事件采样

## 摘要（英文）
Molecular dynamics (MD) simulations are central to materials and drug discovery yet remain computationally demanding, particularly for free-energy perturbation (FEP) protocols and rare-event sampling. Existing sequence-based accelerators, especially Long Short-Term Memory (LSTM) models, often fail to capture long-range temporal structure and provide sufficient expressive capacity in noisy trajectories. Here, we introduce BiLSTMK-MD, a neural time-series learning method that constructs a causality-preserving surrogate for MD and FEP trajectories to reduce sampling requirements. The approach couples a sliding-window bidirectional LSTM encoder, which preserves long-range correlations, with an attention mechanism to enhance temporally informative frames, while a Kolmogorov-Arnold network output layer applies expressive nonlinear readout to decode the attention-refined representation into the final output. A two-stage, fANOVA-guided Bayesian optimization process searches for the optimal hyperparameter configuration for each system. Across four data sets, BiLSTMK-MD achieves mean absolute errors below 1.5 kcal mol-1 for window-resolved free-energy increments, reconstructs dihedral free-energy basins from 1-10% of trajectories, and maintains performance across systems. In long-trajectory regimes, it affords up to 400-fold acceleration for FEP and >700-fold speedup for rare-conformation sampling over conventional MD/FEP simulation. This neural time-series surrogate therefore provides a route to reducing sampling demands for free-energy estimation and rare-event characterization.

## 摘要（中文）
分子动力学(MD)模拟是材料和药物发现的核心方法,但计算成本仍然很高,特别是在自由能微扰(FEP)协议和稀有事件采样中。现有的基于序列的加速器,尤其是长短期记忆(LSTM)模型,往往难以捕捉长距离时间结构,在嘈杂的轨迹中缺乏足够的表达能力。本文介绍了BiLSTMK-MD,一种神经时间序列学习方法,为MD和FEP轨迹构建因果性保留的代理模型,以减少采样需求。该方法将滑动窗口双向LSTM编码器(保留长距离相关性)与注意力机制相耦合,以增强时间信息丰富的帧,同时Kolmogorov-Arnold网络输出层应用表达力强的非线性读出,将注意力优化的表示解码为最终输出。两阶段、fANOVA引导的贝叶斯优化过程为每个系统搜索最优超参数配置。在四个数据集上,BiLSTMK-MD在窗口分辨自由能增量上实现了低于1.5 kcal mol⁻¹的平均绝对误差,能从10%的轨迹重建二面角自由能盆地,并在不同系统间保持性能。在长轨迹情况下,相比传统MD/FEP模拟,它为FEP提供高达400倍的加速,为稀有构象采样提供超过700倍的加速。因此,这一神经时间序列代理模型为减少自由能估计和稀有事件表征的采样需求提供了新途径。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPCRlWUSwQ0a8eQqEWu-2BeSh0MqAAclE-2Bhw9a-2FcBmJ5aiB9s6QetTa7WalDOqKKv9flugxWck9OSmsqgIY903h7kcCiR0V7fPVsKFBypkfLPrx2-2B6HYPsNg3F4RhjtUutARxxsn_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBDsnXsjSZT2MEt8ZzbaUJSVAm-2BXE1p3p5WcDXukU0LxltAecEC110NcDPE4KDONm8s-2Bl5l62g7-2FbKpwoqtnVoJkmEPM6ApiTa51qdz5-2BglRPdAZCoj5XbD5WMf78TaWM5Bk-2FVRk-2F0BHrSBzo5cWj6DIkuOaCzpJqSNrCCkDURS9ZjxUITDy5SOc-2BewtQIG9RI-3D)
