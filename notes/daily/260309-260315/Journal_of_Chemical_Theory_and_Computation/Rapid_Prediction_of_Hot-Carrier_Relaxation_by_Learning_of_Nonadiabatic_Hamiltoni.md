---
title: "Rapid Prediction of Hot-Carrier Relaxation by Learning of Nonadiabatic Hamiltonians with Graph Neural Networks"
title_zh: "利用图神经网络学习非绝热哈密顿量进行热载流子弛豫的快速预测"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c02178"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1o3ajbKkLGHaZrFbhBmd5L-2BI-2BKOBpjAnkFsANn5zBnYn8GM0RXz5p9uWSIyX6xvj2V4wYu-2FFUfxzi2ZznPgE6LY6ZoNuP9cvcCrEdQwbnFVLcP-2B8y6vR2TlUyEBZhD8ozmXXl_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXe13lHC8CJK3Ctsw-2F3uHnu5bxlLCh0Ps6vitUeIdt6pDvY-2FMXarEfh0aUI4RDHejYQgZREVHQPBWP8Z7SFnMKgFfuybAYd-2BAeNrvll6URNdL9g06cZHVjdZy7fUbk6TfU4-2FHsX1odh1TRwkaQEdjuGhs5FRqgxjkVk7ENiHys4zXB8xO9mFPsqWsp7HFNdWues-3D"
pub_date: ""
tags: ["graph-neural-networks", "nonadiabatic-dynamics", "hot-carrier-relaxation", "machine-learning", "materials-science"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Rapid Prediction of Hot-Carrier Relaxation by Learning of Nonadiabatic Hamiltonians with Graph Neural Networks

**利用图神经网络学习非绝热哈密顿量进行热载流子弛豫的快速预测**

## 精华总结
开发图神经网络AI2NAMD方法,建立哈密顿量到热载流子弛豫动力学的映射,将非绝热分子动力学模拟加速6个数量级以上。

**关键词**: 图神经网络、热载流子弛豫、非绝热动力学、机器学习、计算加速

## 摘要（英文）
An electron-vibrational Hamiltonian fully encodes corresponding quantum dynamics; however, extracting the dynamics still relies on time and memory-consuming trajectory-based nonadiabatic molecular dynamics (NAMD) simulations, typically stochastic surface hopping. Here, we develop a general graph neural network, artificial intelligence ab initio NAMD (AI2NAMD) that establishes an end-to-end mapping from Hamiltonian to hot carrier relaxation dynamics. We validated the generality of AI2NAMD across multiple materials, including a zero-dimensional Si quantum dot (QD), a one-dimensional carbon nanotube (CNT), a two-dimensional twisted MoS2/WS2 bilayer, and a three-dimensional soft-lattice MAPbI3 perovskite. With only 10% training data, AI2NAMD can rapidly and accurately generate picosecond energy decay curves for hot electron and hot hole relaxation for the remaining 90% Hamiltonians, while delivering a computational speed-up of more than 6 orders of magnitude compared to standard CPU-based NAMD simulations. Moreover, AI2NAMD can also map directly the Hamiltonian to the carrier relaxation time, bypassing generation of the energy decay curves and demonstrating the ability to handle complex NAMD tasks. Further, by projecting high-dimensional Hamiltonian encoding features into a two-dimensional space with unsupervised learning, we demonstrate that AI2NAMD can effectively distinguish Hamiltonian types, verifying its ability to identify a particular system (QD, CNT, MoS2/WS2 and MAPbI3) and a charge carrier (electron or hole). Overall, the developed AI2NAMD approach provides a novel computational methodology and a conceptual framework for accelerating NAMD simulations with machine learning by many orders of magnitude.

## 摘要（中文）
开发了一种图神经网络方法AI2NAMD,可以建立从哈密顿量到热载流子弛豫动力学的端到端映射。该方法在零维硅量子点、一维碳纳米管、二维扭转MoS2/WS2双层和三维钙钛矿等多种材料上验证了通用性。仅用10%的训练数据,AI2NAMD就能快速准确地生成皮秒级能量衰减曲线,计算速度比标准CPU非绝热分子动力学模拟快6个数量级以上,为加速非绝热分子动力学模拟提供了新的方法和概念框架。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1o3ajbKkLGHaZrFbhBmd5L-2BI-2BKOBpjAnkFsANn5zBnYn8GM0RXz5p9uWSIyX6xvj2V4wYu-2FFUfxzi2ZznPgE6LY6ZoNuP9cvcCrEdQwbnFVLcP-2B8y6vR2TlUyEBZhD8ozmXXl_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXe13lHC8CJK3Ctsw-2F3uHnu5bxlLCh0Ps6vitUeIdt6pDvY-2FMXarEfh0aUI4RDHejYQgZREVHQPBWP8Z7SFnMKgFfuybAYd-2BAeNrvll6URNdL9g06cZHVjdZy7fUbk6TfU4-2FHsX1odh1TRwkaQEdjuGhs5FRqgxjkVk7ENiHys4zXB8xO9mFPsqWsp7HFNdWues-3D)
