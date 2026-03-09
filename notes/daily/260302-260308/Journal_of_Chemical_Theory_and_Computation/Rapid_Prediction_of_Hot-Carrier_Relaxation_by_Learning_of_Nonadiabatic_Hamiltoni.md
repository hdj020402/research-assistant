---
title: "Rapid Prediction of Hot-Carrier Relaxation by Learning of Nonadiabatic Hamiltonians with Graph Neural Networks"
title_zh: "基于图神经网络学习非绝热哈密顿量的热载流子弛豫快速预测"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c02178"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1o3ajbKkLGHaZrFbhBmd5L-2BI-2BKOBpjAnkFsANn5zBnYn8GM0RXz5p9uWSIyX6xvj2V4wYu-2FFUfxzi2ZznPgE6LY6ZoNuP9cvcCrEdQwbnFVLcP-2B8y6vR2TlUyEBZhD8ozmXXl_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXe13lHC8CJK3Ctsw-2F3uHnu5bxlLCh0Ps6vitUeIdt6pDvY-2FMXarEfh0aUI4RDHejYQgZREVHQPBWP8Z7SFnMKgFfuybAYd-2BAeNrvll6URNdL9g06cZHVjdZy7fUbk6TfU4-2FHsX1odh1TRwkaQEdjuGhs5FRqgxjkVk7ENiHys4zXB8xO9mFPsqWsp7HFNdWues-3D"
pub_date: ""
tags: ["graph-neural-networks", "nonadiabatic-dynamics", "machine-learning", "quantum-dynamics", "hot-carrier-relaxation"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Rapid Prediction of Hot-Carrier Relaxation by Learning of Nonadiabatic Hamiltonians with Graph Neural Networks

**基于图神经网络学习非绝热哈密顿量的热载流子弛豫快速预测**

## 精华总结
开发了一种通用的图神经网络AI2NAMD，建立了从哈密顿量到热载流子弛豫动力学的端到端映射，将非绝热分子动力学模拟的计算速度提高了6个数量级以上。

**关键词**: 图神经网络、非绝热分子动力学、热载流子弛豫、哈密顿量、机器学习加速

## 摘要（英文）
An electron-vibrational Hamiltonian fully encodes corresponding quantum dynamics; however, extracting the dynamics still relies on time and memory-consuming trajectory-based nonadiabatic molecular dynamics (NAMD) simulations, typically stochastic surface hopping. Here, we develop a general graph neural network, artificial intelligence ab initio NAMD (AI2NAMD) that establishes an end-to-end mapping from Hamiltonian to hot carrier relaxation dynamics. We validated the generality of AI2NAMD across multiple materials, including a zero-dimensional Si quantum dot (QD), a one-dimensional carbon nanotube (CNT), a two-dimensional twisted MoS2/WS2 bilayer, and a three-dimensional soft-lattice MAPbI3 perovskite. With only 10% training data, AI2NAMD can rapidly and accurately generate picosecond energy decay curves for hot electron and hot hole relaxation for the remaining 90% Hamiltonians, while delivering a computational speed-up of more than 6 orders of magnitude compared to standard CPU-based NAMD simulations. Moreover, AI2NAMD can also map directly the Hamiltonian to the carrier relaxation time, bypassing generation of the energy decay curves and demonstrating the ability to handle complex NAMD tasks. Further, by projecting high-dimensional Hamiltonian encoding features into a two-dimensional space with unsupervised learning, we demonstrate that AI2NAMD can effectively distinguish Hamiltonian types, verifying its ability to identify a particular system (QD, CNT, MoS2/WS2 and MAPbI3) and a charge carrier (electron or hole). Overall, the developed AI2NAMD approach provides a novel computational methodology and a conceptual framework for accelerating NAMD simulations with machine learning by many orders of magnitude.

## 摘要（中文）
电子-振动哈密顿量完整地刻画了相应的量子动力学；然而，要从中提取动力学信息，仍需依赖耗时且占用大量内存的基于轨迹的非绝热分子动力学（NAMD）模拟，通常采用随机表面跳跃算法。在此，我们开发了一种通用的图神经网络——从头计算人工智能非绝热分子动力学（AI2NAMD），该模型建立了从哈密顿量到热载流子弛豫动力学的端到端映射。我们验证了AI2NAMD在多种材料中的通用性，包括零维硅量子点（QD）、一维碳纳米管（CNT）、二维扭转双层MoS2/WS2以及三维软晶格MAPbI3钙钛矿。仅使用10%的训练数据，AI2NAMD便能快速且准确地为剩余90%的哈密顿量生成热电子和热空穴弛豫的皮秒级能量衰减曲线，同时相比基于CPU的标准NAMD模拟，计算速度提升了超过六个数量级。此外，AI2NAMD还能够直接将哈密顿量映射到载流子弛豫时间，无需生成能量衰减曲线，从而展现出处理复杂非绝热分子动力学任务的能力。此外，通过无监督学习将高维哈密顿量编码特征投影到二维空间，我们证明了AI2NAMD能够有效区分不同类型的哈密顿量，从而验证了其识别特定体系（量子点、碳纳米管、MoS2/WS2及MAPbI3）和载流子类型（电子或空穴）的能力。总体而言，所提出的AI2NAMD方法提供了一种新颖的计算方法学和概念框架，能够借助机器学习将NAMD模拟的速度提升多个数量级。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1o3ajbKkLGHaZrFbhBmd5L-2BI-2BKOBpjAnkFsANn5zBnYn8GM0RXz5p9uWSIyX6xvj2V4wYu-2FFUfxzi2ZznPgE6LY6ZoNuP9cvcCrEdQwbnFVLcP-2B8y6vR2TlUyEBZhD8ozmXXl_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXe13lHC8CJK3Ctsw-2F3uHnu5bxlLCh0Ps6vitUeIdt6pDvY-2FMXarEfh0aUI4RDHejYQgZREVHQPBWP8Z7SFnMKgFfuybAYd-2BAeNrvll6URNdL9g06cZHVjdZy7fUbk6TfU4-2FHsX1odh1TRwkaQEdjuGhs5FRqgxjkVk7ENiHys4zXB8xO9mFPsqWsp7HFNdWues-3D)
