---
title: "Rapid Prediction of Hot-Carrier Relaxation by Learning of Nonadiabatic Hamiltonians with Graph Neural Networks"
title_zh: "利用图神经网络学习非绝热哈密顿量快速预测热载流子弛豫"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c02178"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1o3ajbKkLGHaZrFbhBmd5L-2BI-2BKOBpjAnkFsANn5zBnYn8GM0RXz5p9uWSIyX6xvj2V4wYu-2FFUfxzi2ZznPgE6LY6ZoNuP9cvcCrEdQwbnFVLcP-2B8y6vR2TlUyEBZhD8ozmXXl_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXe13lHC8CJK3Ctsw-2F3uHnu5bxlLCh0Ps6vitUeIdt6pDvY-2FMXarEfh0aUI4RDHejYQgZREVHQPBWP8Z7SFnMKgFfuybAYd-2BAeNrvll6URNdL9g06cZHVjdZy7fUbk6TfU4-2FHsX1odh1TRwkaQEdjuGhs5FRqgxjkVk7ENiHys4zXB8xO9mFPsqWsp7HFNdWues-3D"
pub_date: ""
tags: ["graph-neural-networks", "machine-learning", "nonadiabatic-dynamics", "carrier-relaxation", "computational-chemistry"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Rapid Prediction of Hot-Carrier Relaxation by Learning of Nonadiabatic Hamiltonians with Graph Neural Networks

**利用图神经网络学习非绝热哈密顿量快速预测热载流子弛豫**

## 精华总结
开发了图神经网络方法AI2NAMD，建立从哈密顿量到热载流子弛豫动力学的映射，将非绝热分子动力学模拟计算速度提升6个数量级以上。

**关键词**: 图神经网络、热载流子弛豫、非绝热动力学、机器学习、哈密顿量

## 摘要（英文）
An electron-vibrational Hamiltonian fully encodes corresponding quantum dynamics; however, extracting the dynamics still relies on time and memory-consuming trajectory-based nonadiabatic molecular dynamics (NAMD) simulations, typically stochastic surface hopping. Here, we develop a general graph neural network, artificial intelligence ab initio NAMD (AI2NAMD) that establishes an end-to-end mapping from Hamiltonian to hot carrier relaxation dynamics. We validated the generality of AI2NAMD across multiple materials, including a zero-dimensional Si quantum dot (QD), a one-dimensional carbon nanotube (CNT), a two-dimensional twisted MoS2/WS2 bilayer, and a three-dimensional soft-lattice MAPbI3 perovskite. With only 10% training data, AI2NAMD can rapidly and accurately generate picosecond energy decay curves for hot electron and hot hole relaxation for the remaining 90% Hamiltonians, while delivering a computational speed-up of more than 6 orders of magnitude compared to standard CPU-based NAMD simulations. Moreover, AI2NAMD can also map directly the Hamiltonian to the carrier relaxation time, bypassing generation of the energy decay curves and demonstrating the ability to handle complex NAMD tasks. Further, by projecting high-dimensional Hamiltonian encoding features into a two-dimensional space with unsupervised learning, we demonstrate that AI2NAMD can effectively distinguish Hamiltonian types, verifying its ability to identify a particular system (QD, CNT, MoS2/WS2 and MAPbI3) and a charge carrier (electron or hole). Overall, the developed AI2NAMD approach provides a novel computational methodology and a conceptual framework for accelerating NAMD simulations with machine learning by many orders of magnitude.

## 摘要（中文）
开发了一种图神经网络方法AI2NAMD，建立了从哈密顿量到热载流子弛豫动力学的端到端映射。该方法在多种材料（硅量子点、碳纳米管、MoS₂/WS₂双层和钙钛矿）上验证了通用性，仅用10%的训练数据就能准确预测热电子和热空穴弛豫曲线，计算速度提升超过6个数量级，相比传统分子动力学模拟具有显著优势。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1o3ajbKkLGHaZrFbhBmd5L-2BI-2BKOBpjAnkFsANn5zBnYn8GM0RXz5p9uWSIyX6xvj2V4wYu-2FFUfxzi2ZznPgE6LY6ZoNuP9cvcCrEdQwbnFVLcP-2B8y6vR2TlUyEBZhD8ozmXXl_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXe13lHC8CJK3Ctsw-2F3uHnu5bxlLCh0Ps6vitUeIdt6pDvY-2FMXarEfh0aUI4RDHejYQgZREVHQPBWP8Z7SFnMKgFfuybAYd-2BAeNrvll6URNdL9g06cZHVjdZy7fUbk6TfU4-2FHsX1odh1TRwkaQEdjuGhs5FRqgxjkVk7ENiHys4zXB8xO9mFPsqWsp7HFNdWues-3D)
