---
title: "An Accurate Charge-Aware Machine-Learning Interatomic Potential for the Reduction of Li-Ion Battery Electrolytes in Solution"
title_zh: "精确的电荷感知机器学习原子间电势，用于还原溶液中的锂离子电池电解质"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01735"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1kzQwJAG9ZSUfVAvvgjR9xRaoLMzMxX-2BilXdGkr9z-2BnHgkpeAwfdNGOLxeQ7N1DI7muxn4-2FDWbxx9yfhoMRAgVJ6fGl6ZQ-2FXp4PcYL60Wz-2FTdWOZmj006k9UX9fGSIZcnHtYM_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXfgAZ18HLNRpmcYTLlxYjqR4zHgSxlvVQykLdEd6XEAhqs6QRrt9SyM-2BV0ql6KkCLm4GEaDXp9tSdZhuiJToKTtSzHsGfUU4RooJgqCyOl2QjMjqYp0Sb44xej4sJc4colaNxTQpe8GRN-2F7kUwkuGTqopgIXtabbgGJoQ-2B8ZtDEFBZdoEPKxdisyUC-2ByjTOSJg-3D"
pub_date: ""
tags: ["machine-learning-potentials", "li-ion-battery", "electrochemistry", "molecular-dynamics", "neural-networks"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# An Accurate Charge-Aware Machine-Learning Interatomic Potential for the Reduction of Li-Ion Battery Electrolytes in Solution

**精确的电荷感知机器学习原子间电势，用于还原溶液中的锂离子电池电解质**

## 精华总结
本研究开发了一个电荷感知的机器学习势能模型(MPNICE),能够准确描述锂离子电池电解质在溶液中的电化学还原过程,特别是固体电解质界面(SEI)的形成机制。通过迭代电荷平衡策略和离中心自由基采样方法,该模型在两个势能面上实现了高精度动力学模拟,为电子转移过程的真实模拟提供了新的见解。

**关键词**: 机器学习势能、电化学还原、锂离子电池、电荷平衡、固体电解质界面

## 摘要（英文）
Machine learning interatomic potentials (MLIPs), also known as machine learning force fields (MLFFs), offer scalable means of simulating complex systems and processes at ab initio level accuracy. One such process is the critical yet still poorly understood formation of the solid electrolyte interphase (SEI) at the anode of a Li-ion battery (LIB) during the first charge cycle, where electrochemical reduction of the electrolyte leads to the generation of decomposition products. MLIPs are uniquely poised to atomistically describe these electrochemical processes, as they are not as affected by the same limitations in bonding and electron transfer as classical force fields. Nonetheless, training MLIPs to run accurate dynamics of a condensed phase with two different oxidation states, such as in electrochemistry, is challenging for many architectures. In this work, we show that by using MPNICE, a message passing MLIP architecture with iterative charge equilibration, we are able to accurately (within 1 kcal/mol) train models along two potential energy surfaces (reduced and unreduced) for LIB-relevant electrolyte systems. Importantly, we demonstrate strategies for sampling and training to examples of anion radicals of these species, which often are not centered on any atom (off-center radicals, or OCRs). We additionally discuss well-known limitations of global charge equilibration (Qeq) algorithms in erroneously delocalizing charge, and test methods to alleviate the impact on resulting dynamics. Simulations using these models reveal new insights into electrolyte reduction and considerations for the realistic simulation of electron transfer processes in the condensed phase.

## 摘要（中文）
机器学习原子间势能函数（MLIPs），又称机器学习力场（MLFFs），提供了一种可扩展的方法，能够在从头算精度下模拟复杂体系和过程。其中一个过程就是在锂离子电池负极上，于首次充电循环中形成至关重要的、但至今仍理解甚少的固体电解质界面膜（SEI）；该过程中，电解液发生电化学还原，进而产生分解产物。MLIPs具备从原子尺度精确描述这些电化学过程的独特优势，因为它们不受经典力场在键合和电子转移方面相同限制的影响。然而，对于许多模型架构而言，训练MLIPs以精确模拟凝聚相中存在两种不同氧化态的动力学行为——例如在电化学领域——仍是一项挑战。在本工作中，我们表明，通过使用MPNICE——一种具有迭代电荷平衡机制的消息传递机器学习力场架构——我们能够以高精度（误差within 1 kcal/mol）在锂离子电池相关电解液体系的两条势能曲面上（还原态和非还原态）训练模型。重要的是，我们展示了针对这类物种的阴离子自由基样本采集与训练策略，这些阴离子自由基往往不以任何特定原子为中心（即非中心自由基，OCR）。我们还讨论了全局电荷平衡（Qeq）算法在错误地扩展电荷分布方面的已知局限性，并测试了减轻其对最终动力学影响的方法。利用这些模型进行的模拟揭示了关于电解质还原的新见解，并为在凝聚相中真实地模拟电子转移过程提供了重要考量。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1kzQwJAG9ZSUfVAvvgjR9xRaoLMzMxX-2BilXdGkr9z-2BnHgkpeAwfdNGOLxeQ7N1DI7muxn4-2FDWbxx9yfhoMRAgVJ6fGl6ZQ-2FXp4PcYL60Wz-2FTdWOZmj006k9UX9fGSIZcnHtYM_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXfgAZ18HLNRpmcYTLlxYjqR4zHgSxlvVQykLdEd6XEAhqs6QRrt9SyM-2BV0ql6KkCLm4GEaDXp9tSdZhuiJToKTtSzHsGfUU4RooJgqCyOl2QjMjqYp0Sb44xej4sJc4colaNxTQpe8GRN-2F7kUwkuGTqopgIXtabbgGJoQ-2B8ZtDEFBZdoEPKxdisyUC-2ByjTOSJg-3D)
