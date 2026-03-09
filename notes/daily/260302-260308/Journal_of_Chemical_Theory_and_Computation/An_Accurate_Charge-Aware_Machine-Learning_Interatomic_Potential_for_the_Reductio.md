---
title: "An Accurate Charge-Aware Machine-Learning Interatomic Potential for the Reduction of Li-Ion Battery Electrolytes in Solution"
title_zh: "精确的电荷感知机器学习原子间电势，用于还原溶液中的锂离子电池电解质"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01735"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1kzQwJAG9ZSUfVAvvgjR9xRaoLMzMxX-2BilXdGkr9z-2BnHgkpeAwfdNGOLxeQ7N1DI7muxn4-2FDWbxx9yfhoMRAgVJ6fGl6ZQ-2FXp4PcYL60Wz-2FTdWOZmj006k9UX9fGSIZcnHtYM_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXfgAZ18HLNRpmcYTLlxYjqR4zHgSxlvVQykLdEd6XEAhqs6QRrt9SyM-2BV0ql6KkCLm4GEaDXp9tSdZhuiJToKTtSzHsGfUU4RooJgqCyOl2QjMjqYp0Sb44xej4sJc4colaNxTQpe8GRN-2F7kUwkuGTqopgIXtabbgGJoQ-2B8ZtDEFBZdoEPKxdisyUC-2ByjTOSJg-3D"
pub_date: ""
tags: ["machine-learning-potentials", "li-ion-battery", "molecular-dynamics", "charge-equilibration", "electrochemistry"]
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
本研究开发了一种电荷感知的机器学习原子间势(MLIP)模型MPNICE,能够以从头算精度(1 kcal/mol)准确模拟锂离子电池电解质的还原过程和SEI膜形成机制,特别是对离心自由基(OCR)的采样和训练策略进行了创新,为电化学中的电子转移过程模拟提供了新见解。

**关键词**: 机器学习势函数、锂离子电池、固体电解质界面、电荷平衡、分子动力学模拟

## 摘要（英文）
Machine learning interatomic potentials (MLIPs), also known as machine learning force fields (MLFFs), offer scalable means of simulating complex systems and processes at ab initio level accuracy. One such process is the critical yet still poorly understood formation of the solid electrolyte interphase (SEI) at the anode of a Li-ion battery (LIB) during the first charge cycle, where electrochemical reduction of the electrolyte leads to the generation of decomposition products. MLIPs are uniquely poised to atomistically describe these electrochemical processes, as they are not as affected by the same limitations in bonding and electron transfer as classical force fields. Nonetheless, training MLIPs to run accurate dynamics of a condensed phase with two different oxidation states, such as in electrochemistry, is challenging for many architectures. In this work, we show that by using MPNICE, a message passing MLIP architecture with iterative charge equilibration, we are able to accurately (within 1 kcal/mol) train models along two potential energy surfaces (reduced and unreduced) for LIB-relevant electrolyte systems. Importantly, we demonstrate strategies for sampling and training to examples of anion radicals of these species, which often are not centered on any atom (off-center radicals, or OCRs). We additionally discuss well-known limitations of global charge equilibration (Qeq) algorithms in erroneously delocalizing charge, and test methods to alleviate the impact on resulting dynamics. Simulations using these models reveal new insights into electrolyte reduction and considerations for the realistic simulation of electron transfer processes in the condensed phase.

## 摘要（中文）
机器学习原子间势 (mlps)，也称为机器学习力场 (mlff)，提供了从头计算精度模拟复杂系统和过程的可扩展方法。一种这样的过程是在第一次充电循环期间在锂离子电池 (LIB) 的阳极处形成固体电解质界面 (SEI) 的关键但仍知之甚少，其中电解质的电化学还原导致分解产物的产生。Mlps独特地准备以原子方式描述这些电化学过程，因为它们不受与经典力场相同的键合和电子转移限制的影响。尽管如此，训练mlps以运行具有两种不同氧化态的凝聚相的精确动力学，例如在电化学中，对于许多架构而言是具有挑战性的。在这项工作中，我们表明，通过使用MPNICE，一种具有迭代电荷平衡的消息传递MLIP架构，我们能够准确地 (在1 kcal/mol内) 沿着LIB相关电解质系统的两个势能表面 (减少和未减少) 训练模型。重要的是，我们演示了对这些物种的阴离子自由基的示例进行采样和训练的策略，这些阴离子自由基通常不以任何原子为中心 (偏心自由基或ocr)。我们还讨论了全局电荷平衡 (Qeq) 算法在错误地使电荷离域方面的众所周知的局限性，并测试一下了减轻对所得动力学影响的方法。使用这些模型进行的模拟揭示了对电解质还原的新见解，以及对冷凝相中电子转移过程的实际模拟的考虑。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1kzQwJAG9ZSUfVAvvgjR9xRaoLMzMxX-2BilXdGkr9z-2BnHgkpeAwfdNGOLxeQ7N1DI7muxn4-2FDWbxx9yfhoMRAgVJ6fGl6ZQ-2FXp4PcYL60Wz-2FTdWOZmj006k9UX9fGSIZcnHtYM_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXfgAZ18HLNRpmcYTLlxYjqR4zHgSxlvVQykLdEd6XEAhqs6QRrt9SyM-2BV0ql6KkCLm4GEaDXp9tSdZhuiJToKTtSzHsGfUU4RooJgqCyOl2QjMjqYp0Sb44xej4sJc4colaNxTQpe8GRN-2F7kUwkuGTqopgIXtabbgGJoQ-2B8ZtDEFBZdoEPKxdisyUC-2ByjTOSJg-3D)
