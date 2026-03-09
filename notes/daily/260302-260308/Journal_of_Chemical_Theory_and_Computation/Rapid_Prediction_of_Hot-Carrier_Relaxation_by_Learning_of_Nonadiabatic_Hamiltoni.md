---
title: "Rapid Prediction of Hot-Carrier Relaxation by Learning of Nonadiabatic Hamiltonians with Graph Neural Networks"
title_zh: "通过使用图神经网络学习非绝热哈密顿量来快速预测热载流子弛豫"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c02178"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1o3ajbKkLGHaZrFbhBmd5L-2BI-2BKOBpjAnkFsANn5zBnYn8GM0RXz5p9uWSIyX6xvj2V4wYu-2FFUfxzi2ZznPgE6LY6ZoNuP9cvcCrEdQwbnFVLcP-2B8y6vR2TlUyEBZhD8ozmXXl_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXe13lHC8CJK3Ctsw-2F3uHnu5bxlLCh0Ps6vitUeIdt6pDvY-2FMXarEfh0aUI4RDHejYQgZREVHQPBWP8Z7SFnMKgFfuybAYd-2BAeNrvll6URNdL9g06cZHVjdZy7fUbk6TfU4-2FHsX1odh1TRwkaQEdjuGhs5FRqgxjkVk7ENiHys4zXB8xO9mFPsqWsp7HFNdWues-3D"
pub_date: ""
tags: ["graph-neural-networks", "hot-carrier-dynamics", "nonadiabatic-dynamics", "machine-learning-acceleration", "computational-chemistry"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Rapid Prediction of Hot-Carrier Relaxation by Learning of Nonadiabatic Hamiltonians with Graph Neural Networks

**通过使用图神经网络学习非绝热哈密顿量来快速预测热载流子弛豫**

## 精华总结
开发了一种通用图神经网络AI2NAMD，能够直接从哈密顿量映射到热载流子弛豫动力学，相比标准NAMD模拟加速超过6个数量级。该方法为使用机器学习加速非绝热分子动力学模拟提供了新的计算方法论和概念框架。

**关键词**: 图神经网络、热载流子弛豫、非绝热分子动力学、哈密顿量、机器学习加速

## 摘要（英文）
An electron-vibrational Hamiltonian fully encodes corresponding quantum dynamics; however, extracting the dynamics still relies on time and memory-consuming trajectory-based nonadiabatic molecular dynamics (NAMD) simulations, typically stochastic surface hopping. Here, we develop a general graph neural network, artificial intelligence ab initio NAMD (AI2NAMD) that establishes an end-to-end mapping from Hamiltonian to hot carrier relaxation dynamics. We validated the generality of AI2NAMD across multiple materials, including a zero-dimensional Si quantum dot (QD), a one-dimensional carbon nanotube (CNT), a two-dimensional twisted MoS2/WS2 bilayer, and a three-dimensional soft-lattice MAPbI3 perovskite. With only 10% training data, AI2NAMD can rapidly and accurately generate picosecond energy decay curves for hot electron and hot hole relaxation for the remaining 90% Hamiltonians, while delivering a computational speed-up of more than 6 orders of magnitude compared to standard CPU-based NAMD simulations. Moreover, AI2NAMD can also map directly the Hamiltonian to the carrier relaxation time, bypassing generation of the energy decay curves and demonstrating the ability to handle complex NAMD tasks. Further, by projecting high-dimensional Hamiltonian encoding features into a two-dimensional space with unsupervised learning, we demonstrate that AI2NAMD can effectively distinguish Hamiltonian types, verifying its ability to identify a particular system (QD, CNT, MoS2/WS2 and MAPbI3) and a charge carrier (electron or hole). Overall, the developed AI2NAMD approach provides a novel computational methodology and a conceptual framework for accelerating NAMD simulations with machine learning by many orders of magnitude.

## 摘要（中文）
电子振动哈密顿量完全编码了相应的量子动力学; 但是，提取动力学仍然依赖于基于时间和内存的基于轨迹的非绝热分子动力学 (NAMD) 模拟，通常是随机表面跳跃。在这里，我们开发了一个通用的图形神经网络，人工智能从头算NAMD (AI2NAMD)，它建立了从哈密顿量到热载流子弛豫动力学的端到端映射。我们验证了al2namd在多种材料中的通用性，包括零维Si量子点 (QD)，一维碳纳米管 (CNT)，二维扭曲的MoS2/WS2双层和三维软晶格MAPbI3钙钛矿。仅使用10% 训练数据，AI2NAMD可以快速准确地为剩余的90% 个哈密顿量生成热电子和热空穴弛豫的皮秒能量衰减曲线，同时与标准的基于CPU的NAMD模拟相比，计算速度提高了6个数量级以上。此外，AI2NAMD还可以将哈密顿量直接映射到载流子弛豫时间，从而绕过能量衰减曲线的产生，并展示了处理复杂NAMD任务的能力。此外，通过将高维哈密顿量编码特征投影到具有无监督学习的二维空间中，我们证明了AI2NAMD可以有效地区分哈密顿量类型，验证了其识别特定系统 (QD，CNT，MoS2/WS2和MAPbI3) 和电荷载体 (电子或空穴) 的能力。总的来说，开发的AI2NAMD方法提供了一种新颖的计算方法和概念框架，用于通过机器学习加速NAMD模拟许多数量级。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1o3ajbKkLGHaZrFbhBmd5L-2BI-2BKOBpjAnkFsANn5zBnYn8GM0RXz5p9uWSIyX6xvj2V4wYu-2FFUfxzi2ZznPgE6LY6ZoNuP9cvcCrEdQwbnFVLcP-2B8y6vR2TlUyEBZhD8ozmXXl_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXe13lHC8CJK3Ctsw-2F3uHnu5bxlLCh0Ps6vitUeIdt6pDvY-2FMXarEfh0aUI4RDHejYQgZREVHQPBWP8Z7SFnMKgFfuybAYd-2BAeNrvll6URNdL9g06cZHVjdZy7fUbk6TfU4-2FHsX1odh1TRwkaQEdjuGhs5FRqgxjkVk7ENiHys4zXB8xO9mFPsqWsp7HFNdWues-3D)
