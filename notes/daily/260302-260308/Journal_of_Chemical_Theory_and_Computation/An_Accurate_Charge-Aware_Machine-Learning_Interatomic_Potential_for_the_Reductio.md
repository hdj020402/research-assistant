---
title: "An Accurate Charge-Aware Machine-Learning Interatomic Potential for the Reduction of Li-Ion Battery Electrolytes in Solution"
title_zh: "锂离子电池电解质溶液还原反应的准确电荷感知机器学习原子间势"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01735"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1kzQwJAG9ZSUfVAvvgjR9xRaoLMzMxX-2BilXdGkr9z-2BnHgkpeAwfdNGOLxeQ7N1DI7muxn4-2FDWbxx9yfhoMRAgVJ6fGl6ZQ-2FXp4PcYL60Wz-2FTdWOZmj006k9UX9fGSIZcnHtYM_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXfgAZ18HLNRpmcYTLlxYjqR4zHgSxlvVQykLdEd6XEAhqs6QRrt9SyM-2BV0ql6KkCLm4GEaDXp9tSdZhuiJToKTtSzHsGfUU4RooJgqCyOl2QjMjqYp0Sb44xej4sJc4colaNxTQpe8GRN-2F7kUwkuGTqopgIXtabbgGJoQ-2B8ZtDEFBZdoEPKxdisyUC-2ByjTOSJg-3D"
pub_date: ""
tags: ["machine-learning", "interatomic-potentials", "battery-chemistry", "electrochemistry", "computational-chemistry"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# An Accurate Charge-Aware Machine-Learning Interatomic Potential for the Reduction of Li-Ion Battery Electrolytes in Solution

**锂离子电池电解质溶液还原反应的准确电荷感知机器学习原子间势**

## 精华总结
开发了具有迭代电荷平衡的消息传递机器学习原子间势(MPNICE),能够准确描述锂离子电池电解质的电化学还原过程,实现了第一性原理精度的凝聚相电子转移过程模拟。该工作提出了针对离心自由基的取样策略,并解决了全局电荷平衡算法的固有局限性,为电池SEI形成机制研究提供了新的原子尺度认识。

**关键词**: 机器学习力场、锂离子电池、固体电解质界面、电化学还原、电荷平衡、分子动力学

## 摘要（英文）
Machine learning interatomic potentials (MLIPs), also known as machine learning force fields (MLFFs), offer scalable means of simulating complex systems and processes at ab initio level accuracy. One such process is the critical yet still poorly understood formation of the solid electrolyte interphase (SEI) at the anode of a Li-ion battery (LIB) during the first charge cycle, where electrochemical reduction of the electrolyte leads to the generation of decomposition products. MLIPs are uniquely poised to atomistically describe these electrochemical processes, as they are not as affected by the same limitations in bonding and electron transfer as classical force fields. Nonetheless, training MLIPs to run accurate dynamics of a condensed phase with two different oxidation states, such as in electrochemistry, is challenging for many architectures. In this work, we show that by using MPNICE, a message passing MLIP architecture with iterative charge equilibration, we are able to accurately (within 1 kcal/mol) train models along two potential energy surfaces (reduced and unreduced) for LIB-relevant electrolyte systems. Importantly, we demonstrate strategies for sampling and training to examples of anion radicals of these species, which often are not centered on any atom (off-center radicals, or OCRs). We additionally discuss well-known limitations of global charge equilibration (Qeq) algorithms in erroneously delocalizing charge, and test methods to alleviate the impact on resulting dynamics. Simulations using these models reveal new insights into electrolyte reduction and considerations for the realistic simulation of electron transfer processes in the condensed phase.

## 摘要（中文）
机器学习原子间势(MLIPs),也称为机器学习力场(MLFFs),提供了以第一性原理精度模拟复杂系统和过程的可扩展手段。其中一个过程是在锂离子电池(LIB)放电循环中阳极处固体电解质界面(SEI)的形成,这是一个关键但仍未充分理解的过程,其中电解质的电化学还原导致分解产物的生成。MLIPs独特地能够原子尺度描述这些电化学过程,因为它们不受经典力场在成键和电子转移中相同局限的影响。尽管如此,训练MLIPs以运行具有两种不同氧化态的凝聚相(如电化学中的情况)的准确动力学对许多架构来说是具有挑战性的。在这项工作中,我们展示通过使用MPNICE(具有迭代电荷平衡的消息传递MLIP架构),我们能够准确地(在1 kcal/mol范围内)沿两个势能面(还原和未还原)对LIB相关电解质系统进行模型训练。重要的是,我们展示了对这些物质的阴离子自由基的取样和训练策略,这些往往不以任何原子为中心(离心自由基或OCRs)。我们另外讨论了全局电荷平衡(Qeq)算法的众所周知的局限性,即错误地离域化电荷,并测试了缓解所产生动力学影响的方法。使用这些模型的模拟揭示了电解质还原的新见解以及凝聚相中电子转移过程现实模拟的考虑因素。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1kzQwJAG9ZSUfVAvvgjR9xRaoLMzMxX-2BilXdGkr9z-2BnHgkpeAwfdNGOLxeQ7N1DI7muxn4-2FDWbxx9yfhoMRAgVJ6fGl6ZQ-2FXp4PcYL60Wz-2FTdWOZmj006k9UX9fGSIZcnHtYM_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXfgAZ18HLNRpmcYTLlxYjqR4zHgSxlvVQykLdEd6XEAhqs6QRrt9SyM-2BV0ql6KkCLm4GEaDXp9tSdZhuiJToKTtSzHsGfUU4RooJgqCyOl2QjMjqYp0Sb44xej4sJc4colaNxTQpe8GRN-2F7kUwkuGTqopgIXtabbgGJoQ-2B8ZtDEFBZdoEPKxdisyUC-2ByjTOSJg-3D)
