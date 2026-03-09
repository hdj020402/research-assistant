---
title: "Revealing the Atomistic Mechanism of Rare Events in Molecular Dynamics"
title_zh: "揭示分子动力学中罕见事件的原子机制"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01906"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1ukjiDPcq1QYLB-2Fr4fk58sfh-2BF7PilAJaAQFW5Z-2FBycNhmj56l305gTdgVeTL4CsF6U-2Bftxv0SjMsqnAxZOz-2Fk4yE9WlGYWOuJO5r3eh2ygEuPJr-2FIq0q-2FotyXNiBFijIfqm2_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXdoApGTUY5Z3Y7f4nMUM-2FACQFvbZDK-2BXlQk70-2B9-2F3odnMGp7fOA1dB-2BzZF-2FSiCxECzzi6q1gdakDAqdoFu03KefD-2BIr4b9CRZnFHURZvti5Ndjl31a3RsMya-2Bzr-2B-2FRqPjWahI2Ofax0lpUtokOOma6LNiApcd3CekMcV-2F9B7yzYANZhq4xB-2BziAtWW2e78LSF8-3D"
pub_date: ""
tags: ["molecular-dynamics", "deep-learning", "rare-events", "interpretability", "enhanced-sampling"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Revealing the Atomistic Mechanism of Rare Events in Molecular Dynamics

**揭示分子动力学中罕见事件的原子机制**

## 精华总结
AMORE-MD框架利用ISOKANN算法学习神经成员函数χ来表示主导缓慢过程，通过梯度对齐重建转移路径，并通过基于梯度的灵敏度分析量化原子贡献，实现对分子动力学中罕见事件的可解释性研究。

**关键词**: 分子动力学、罕见事件、深度学习、反应坐标、神经网络、原子机制

## 摘要（英文）
Interpretable reaction coordinates are essential for understanding rare conformational transitions in molecular dynamics. The Atomistic Mechanism of Rare Events in Molecular Dynamics (AMORE-MD) framework enhances the interpretability of deep-learned reaction coordinates by connecting them to atomistic mechanisms, without requiring any a priori knowledge of collective variables, pathways, or end points. Here, AMORE-MD employs the ISOKANN algorithm to learn a neural membership function χ representing the dominant slow process, from which transition pathways are reconstructed as minimum-energy paths aligned with the gradient of χ, and atomic contributions are quantified through gradient-based sensitivity analysis. Iterative enhanced sampling further enriches transition regions and improves coverage of rare events, enabling recovery of known mechanisms and chemically interpretable structural rearrangements at atomic resolution for the Müller-Brown potential, alanine dipeptide, and the elastin-derived hexapeptide VGVAPG.

## 摘要（中文）
可解释的反应坐标对于理解分子动力学中的稀有构象转变至关重要。分子动力学中的稀有事件原子机制框架（AMORE-MD）通过将深度学习提取的反应坐标与原子级机制相联系，提升了其可解释性，且无需预先了解集体变量、反应路径或终态。在此，AMORE-MD采用ISOKANN算法学习一个神经网络隶属函数 χ，用于表征主导的慢动力学过程；由此，可沿 χ 的梯度方向重构出最小能量路径作为反应通道，并通过基于梯度的灵敏度分析量化各原子的贡献。迭代式增强采样进一步富集过渡态区域、提升稀有事件的采样覆盖率，从而在原子分辨率下恢复已知的作用机制，并获得具有化学可解释性的结构重排，这些结果分别适用于Müller-Brown势能面、丙氨酸二肽以及弹性蛋白来源的六肽VGVAPG。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1ukjiDPcq1QYLB-2Fr4fk58sfh-2BF7PilAJaAQFW5Z-2FBycNhmj56l305gTdgVeTL4CsF6U-2Bftxv0SjMsqnAxZOz-2Fk4yE9WlGYWOuJO5r3eh2ygEuPJr-2FIq0q-2FotyXNiBFijIfqm2_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXdoApGTUY5Z3Y7f4nMUM-2FACQFvbZDK-2BXlQk70-2B9-2F3odnMGp7fOA1dB-2BzZF-2FSiCxECzzi6q1gdakDAqdoFu03KefD-2BIr4b9CRZnFHURZvti5Ndjl31a3RsMya-2Bzr-2B-2FRqPjWahI2Ofax0lpUtokOOma6LNiApcd3CekMcV-2F9B7yzYANZhq4xB-2BziAtWW2e78LSF8-3D)
