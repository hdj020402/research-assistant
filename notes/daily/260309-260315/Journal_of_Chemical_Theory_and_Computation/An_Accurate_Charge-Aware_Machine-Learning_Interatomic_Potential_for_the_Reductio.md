---
title: "An Accurate Charge-Aware Machine-Learning Interatomic Potential for the Reduction of Li-Ion Battery Electrolytes in Solution"
title_zh: "锂离子电池电解质溶液还原过程的精确电荷感知机器学习原子间势"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01735"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1kzQwJAG9ZSUfVAvvgjR9xRaoLMzMxX-2BilXdGkr9z-2BnHgkpeAwfdNGOLxeQ7N1DI7muxn4-2FDWbxx9yfhoMRAgVJ6fGl6ZQ-2FXp4PcYL60Wz-2FTdWOZmj006k9UX9fGSIZcnHtYM_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXfgAZ18HLNRpmcYTLlxYjqR4zHgSxlvVQykLdEd6XEAhqs6QRrt9SyM-2BV0ql6KkCLm4GEaDXp9tSdZhuiJToKTtSzHsGfUU4RooJgqCyOl2QjMjqYp0Sb44xej4sJc4colaNxTQpe8GRN-2F7kUwkuGTqopgIXtabbgGJoQ-2B8ZtDEFBZdoEPKxdisyUC-2ByjTOSJg-3D"
pub_date: ""
tags: ["machine-learning-potentials", "li-ion-batteries", "sei-formation", "charge-equilibration", "electrochemistry"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# An Accurate Charge-Aware Machine-Learning Interatomic Potential for the Reduction of Li-Ion Battery Electrolytes in Solution

**锂离子电池电解质溶液还原过程的精确电荷感知机器学习原子间势**

## 精华总结
开发了具有电荷感知能力的机器学习力场,可准确描述锂离子电池电解质的电化学还原过程,为固体电解质界面形成机制的原子层次理解奠定基础。

**关键词**: 机器学习力场、锂离子电池、固体电解质界面、电荷平衡、电化学还原

## 摘要（英文）
Machine learning interatomic potentials (MLIPs), also known as machine learning force fields (MLFFs), offer scalable means of simulating complex systems and processes at ab initio level accuracy. One such process is the critical yet still poorly understood formation of the solid electrolyte interphase (SEI) at the anode of a Li-ion battery (LIB) during the first charge cycle, where electrochemical reduction of the electrolyte leads to the generation of decomposition products. MLIPs are uniquely poised to atomistically describe these electrochemical processes, as they are not as affected by the same limitations in bonding and electron transfer as classical force fields. Nonetheless, training MLIPs to run accurate dynamics of a condensed phase with two different oxidation states, such as in electrochemistry, is challenging for many architectures. In this work, we show that by using MPNICE, a message passing MLIP architecture with iterative charge equilibration, we are able to accurately (within 1 kcal/mol) train models along two potential energy surfaces (reduced and unreduced) for LIB-relevant electrolyte systems. Importantly, we demonstrate strategies for sampling and training to examples of anion radicals of these species, which often are not centered on any atom (off-center radicals, or OCRs). We additionally discuss well-known limitations of global charge equilibration (Qeq) algorithms in erroneously delocalizing charge, and test methods to alleviate the impact on resulting dynamics. Simulations using these models reveal new insights into electrolyte reduction and considerations for the realistic simulation of electron transfer processes in the condensed phase.

## 摘要（中文）
机器学习原子间势(MLIPs)提供了以从头计算精度模拟复杂系统的可扩展方法。本工作针对锂离子电池充电循环中固体电解质界面(SEI)形成过程中的电解质电化学还原,采用具有迭代电荷平衡的MPNICE消息传递架构,成功训练了在还原和未还原两个势能面上精度达1 kcal/mol的机器学习力场模型。特别地,本工作发展了对阴离子自由基(包括非中心位置自由基)的采样和训练策略,讨论了全局电荷平衡算法的局限性,并测试了缓解其对动力学影响的方法。模拟结果揭示了电解质还原的新见解。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1kzQwJAG9ZSUfVAvvgjR9xRaoLMzMxX-2BilXdGkr9z-2BnHgkpeAwfdNGOLxeQ7N1DI7muxn4-2FDWbxx9yfhoMRAgVJ6fGl6ZQ-2FXp4PcYL60Wz-2FTdWOZmj006k9UX9fGSIZcnHtYM_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXfgAZ18HLNRpmcYTLlxYjqR4zHgSxlvVQykLdEd6XEAhqs6QRrt9SyM-2BV0ql6KkCLm4GEaDXp9tSdZhuiJToKTtSzHsGfUU4RooJgqCyOl2QjMjqYp0Sb44xej4sJc4colaNxTQpe8GRN-2F7kUwkuGTqopgIXtabbgGJoQ-2B8ZtDEFBZdoEPKxdisyUC-2ByjTOSJg-3D)
