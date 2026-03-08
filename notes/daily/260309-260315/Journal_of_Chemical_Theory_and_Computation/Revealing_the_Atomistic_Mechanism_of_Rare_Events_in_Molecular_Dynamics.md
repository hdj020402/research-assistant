---
title: "Revealing the Atomistic Mechanism of Rare Events in Molecular Dynamics"
title_zh: "揭示分子动力学中稀有事件的原子论机制"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01906"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1ukjiDPcq1QYLB-2Fr4fk58sfh-2BF7PilAJaAQFW5Z-2FBycNhmj56l305gTdgVeTL4CsF6U-2Bftxv0SjMsqnAxZOz-2Fk4yE9WlGYWOuJO5r3eh2ygEuPJr-2FIq0q-2FotyXNiBFijIfqm2_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXdoApGTUY5Z3Y7f4nMUM-2FACQFvbZDK-2BXlQk70-2B9-2F3odnMGp7fOA1dB-2BzZF-2FSiCxECzzi6q1gdakDAqdoFu03KefD-2BIr4b9CRZnFHURZvti5Ndjl31a3RsMya-2Bzr-2B-2FRqPjWahI2Ofax0lpUtokOOma6LNiApcd3CekMcV-2F9B7yzYANZhq4xB-2BziAtWW2e78LSF8-3D"
pub_date: ""
tags: ["molecular-dynamics", "rare-events", "deep-learning", "reaction-coordinates", "neural-networks"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Revealing the Atomistic Mechanism of Rare Events in Molecular Dynamics

**揭示分子动力学中稀有事件的原子论机制**

## 精华总结
AMORE-MD通过ISOKANN算法学习神经隶属函数来表示主导慢过程,通过梯度对齐重建转移路径并通过敏感性分析量化原子贡献。

**关键词**: 分子动力学、稀有事件、深度学习、反应坐标、增强采样

## 摘要（英文）
Interpretable reaction coordinates are essential for understanding rare conformational transitions in molecular dynamics. The Atomistic Mechanism of Rare Events in Molecular Dynamics (AMORE-MD) framework enhances the interpretability of deep-learned reaction coordinates by connecting them to atomistic mechanisms, without requiring any a priori knowledge of collective variables, pathways, or end points. Here, AMORE-MD employs the ISOKANN algorithm to learn a neural membership function χ representing the dominant slow process, from which transition pathways are reconstructed as minimum-energy paths aligned with the gradient of χ, and atomic contributions are quantified through gradient-based sensitivity analysis. Iterative enhanced sampling further enriches transition regions and improves coverage of rare events, enabling recovery of known mechanisms and chemically interpretable structural rearrangements at atomic resolution for the Müller-Brown potential, alanine dipeptide, and the elastin-derived hexapeptide VGVAPG.

## 摘要（中文）
AMORE-MD框架通过ISOKANN算法学习神经隶属函数来表示主导慢过程,无需先验知识即可重建转移路径并量化原子贡献。该方法通过梯度敏感性分析实现对过渡区域的迭代增强采样,在Müller-Brown势、丙氨酸二肽和弹性蛋白衍生六肽等体系中成功恢复已知机制,在原子分辨率下获得化学可解释的结构重排。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1ukjiDPcq1QYLB-2Fr4fk58sfh-2BF7PilAJaAQFW5Z-2FBycNhmj56l305gTdgVeTL4CsF6U-2Bftxv0SjMsqnAxZOz-2Fk4yE9WlGYWOuJO5r3eh2ygEuPJr-2FIq0q-2FotyXNiBFijIfqm2_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXdoApGTUY5Z3Y7f4nMUM-2FACQFvbZDK-2BXlQk70-2B9-2F3odnMGp7fOA1dB-2BzZF-2FSiCxECzzi6q1gdakDAqdoFu03KefD-2BIr4b9CRZnFHURZvti5Ndjl31a3RsMya-2Bzr-2B-2FRqPjWahI2Ofax0lpUtokOOma6LNiApcd3CekMcV-2F9B7yzYANZhq4xB-2BziAtWW2e78LSF8-3D)
