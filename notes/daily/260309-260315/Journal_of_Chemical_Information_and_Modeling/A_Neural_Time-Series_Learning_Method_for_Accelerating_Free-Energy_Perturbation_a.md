---
title: "A Neural Time-Series Learning Method for Accelerating Free-Energy Perturbation and Rare-Event Molecular Dynamics Simulations"
title_zh: "用于加速自由能微扰和罕见事件分子动力学模拟的神经时间序列学习方法"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c03127"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPCRlWUSwQ0a8eQqEWu-2BeSh0MqAAclE-2Bhw9a-2FcBmJ5aiB9s6QetTa7WalDOqKKv9flugxWck9OSmsqgIY903h7kcCiR0V7fPVsKFBypkfLPrx2-2B6HYPsNg3F4RhjtUutARxxsn_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBDsnXsjSZT2MEt8ZzbaUJSVAm-2BXE1p3p5WcDXukU0LxltAecEC110NcDPE4KDONm8s-2Bl5l62g7-2FbKpwoqtnVoJkmEPM6ApiTa51qdz5-2BglRPdAZCoj5XbD5WMf78TaWM5Bk-2FVRk-2F0BHrSBzo5cWj6DIkuOaCzpJqSNrCCkDURS9ZjxUITDy5SOc-2BewtQIG9RI-3D"
pub_date: ""
tags: ["deep-learning", "molecular-dynamics", "free-energy-calculation", "surrogate-models", "rare-event-sampling"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# A Neural Time-Series Learning Method for Accelerating Free-Energy Perturbation and Rare-Event Molecular Dynamics Simulations

**用于加速自由能微扰和罕见事件分子动力学模拟的神经时间序列学习方法**

## 精华总结
BiLSTMK-MD是一种神经时间序列学习方法，通过构建保因果性的分子动力学轨迹替代模型，显著降低自由能估计和罕见事件表征的采样需求，实现高达700倍的计算加速。

**关键词**: 分子动力学、自由能微扰、神经网络、时间序列学习、稀有事件采样

## 摘要（英文）
Molecular dynamics (MD) simulations are central to materials and drug discovery yet remain computationally demanding, particularly for free-energy perturbation (FEP) protocols and rare-event sampling. Existing sequence-based accelerators, especially Long Short-Term Memory (LSTM) models, often fail to capture long-range temporal structure and provide sufficient expressive capacity in noisy trajectories. Here, we introduce BiLSTMK-MD, a neural time-series learning method that constructs a causality-preserving surrogate for MD and FEP trajectories to reduce sampling requirements. The approach couples a sliding-window bidirectional LSTM encoder, which preserves long-range correlations, with an attention mechanism to enhance temporally informative frames, while a Kolmogorov-Arnold network output layer applies expressive nonlinear readout to decode the attention-refined representation into the final output. A two-stage, fANOVA-guided Bayesian optimization process searches for the optimal hyperparameter configuration for each system. Across four data sets, BiLSTMK-MD achieves mean absolute errors below 1.5 kcal mol-1 for window-resolved free-energy increments, reconstructs dihedral free-energy basins from 1-10% of trajectories, and maintains performance across systems. In long-trajectory regimes, it affords up to 400-fold acceleration for FEP and >700-fold speedup for rare-conformation sampling over conventional MD/FEP simulation. This neural time-series surrogate therefore provides a route to reducing sampling demands for free-energy estimation and rare-event characterization.

## 摘要（中文）
分子动力学模拟在材料和药物发现中至关重要但计算量大。本文提出BiLSTMK-MD方法，结合双向LSTM编码器、注意力机制和Kolmogorov-Arnold网络，构建保因果性的MD和FEP轨迹替代模型。该方法通过两阶段贝叶斯优化搜索最优超参数，在四个数据集上实现相对自由能增量的平均绝对误差<1.5 kcal/mol，可从1-10%的轨迹重构二面体自由能盆地，为自由能估计和罕见事件采样提供400-700倍加速。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPCRlWUSwQ0a8eQqEWu-2BeSh0MqAAclE-2Bhw9a-2FcBmJ5aiB9s6QetTa7WalDOqKKv9flugxWck9OSmsqgIY903h7kcCiR0V7fPVsKFBypkfLPrx2-2B6HYPsNg3F4RhjtUutARxxsn_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBDsnXsjSZT2MEt8ZzbaUJSVAm-2BXE1p3p5WcDXukU0LxltAecEC110NcDPE4KDONm8s-2Bl5l62g7-2FbKpwoqtnVoJkmEPM6ApiTa51qdz5-2BglRPdAZCoj5XbD5WMf78TaWM5Bk-2FVRk-2F0BHrSBzo5cWj6DIkuOaCzpJqSNrCCkDURS9ZjxUITDy5SOc-2BewtQIG9RI-3D)
