---
title: "Efficient Protein–Ligand Binding Free Energy Estimation with Coarse-Grained Funnel Metadynamics"
title_zh: "利用粗粒度漏斗元动力学进行高效的蛋白质-配体结合自由能估算"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01785"
url: "https://app.acspubs.org/e/er?s=1913652004&lid=109584&pci=CACSR000013623915&elqTrackId=d72112e480044f848672b53c3c761796&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF56703BC36D04744F96E49B1BEFDB38CA2DF669D1886211F10624EBC003E655BFD"
pub_date: ""
tags: ["molecular-dynamics", "free-energy-calculations", "protein-ligand-binding", "enhanced-sampling", "computational-chemistry"]
ai_relevance: 2
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Efficient Protein–Ligand Binding Free Energy Estimation with Coarse-Grained Funnel Metadynamics

**利用粗粒度漏斗元动力学进行高效的蛋白质-配体结合自由能估算**

## 精华总结
提出了结合粗粒度表示和增强采样技术的粗粒度漏斗元动力学方法，在保持预测精确性的同时显著降低计算成本；通过超过7毫秒的广泛采样验证了该方法的稳健性和可靠性，为蛋白质-配体结合自由能的高效预测提供了新的解决方案。

**关键词**: 蛋白质-配体结合、自由能计算、粗粒度分子动力学、增强采样、分子模拟

## 摘要（英文）
Despite considerable advances in computational chemistry, bridging the gap between the accuracy of all-atom molecular dynamics (AA-MD) and the high-throughput capabilities of docking remains an unsolved problem in protein-ligand binding free energy predictions. In this work, we propose to address this challenge through coarse-grained funnel metadynamics (CG-FMD) with the Martini 3 force field. This approach combines the reduced computational cost of a CG representation with state-of-the-art enhanced sampling techniques and the interpretability of a physics-based force field. Specifically, the binding of colchicine to two different protein targets was modeled at both AA and CG resolutions, and the corresponding ΔGbind predictions were compared with experimental references. Additionally, the robustness of CG-FMD-based ΔGbind predictions was evaluated with respect to various aspects of the simulation setup by collecting more than 7 ms of CG-FMD simulations. The optimal simulation protocol has been further validated against a limited set of compounds chemically different from colchicine. The results demonstrate that CG-FMD yields ΔGbind estimates comparable to experimental values while requiring only a fraction of the computational cost of AA-MD simulations. Moreover, the extensive sampling achievable with CG-FMD reduces statistical uncertainty in the final predictions, effectively compensating for the simplified system representation. Future work should build upon these methodological insights to broaden the scope of ligands and targets explored.

## 摘要（中文）
尽管计算化学取得了显著进展，但在蛋白质-配体结合自由能预测中，弥合全原子分子动力学(AA-MD)的精确性与分子对接的高通量能力之间的差距仍是一个未解决的问题。在这项工作中，我们提出通过采用Martini 3力场的粗粒度漏斗元动力学(CG-FMD)来应对这一挑战。该方法结合了粗粒度表示的低计算成本、最先进的增强采样技术以及基于物理力场的可解释性。具体地，我们在全原子和粗粒度分辨率下分别模拟了秋水仙素与两个不同蛋白质靶点的结合，并将相应的ΔGbind预测与实验参考值进行了比较。此外，我们通过收集超过7毫秒的CG-FMD模拟数据，评估了基于CG-FMD的ΔGbind预测相对于模拟设置各个方面的稳健性。最优模拟方案已进一步针对与秋水仙素在化学上不同的有限组合物进行了验证。结果表明，CG-FMD产生的ΔGbind估计值与实验值相当，同时仅需全原子分子动力学模拟计算成本的一小部分。此外，通过CG-FMD实现的广泛采样减少了最终预测中的统计不确定性，有效补偿了简化系统表示的不足。未来工作应基于这些方法学见解，扩展所探索的配体和靶点的范围。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](https://app.acspubs.org/e/er?s=1913652004&lid=109584&pci=CACSR000013623915&elqTrackId=d72112e480044f848672b53c3c761796&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF56703BC36D04744F96E49B1BEFDB38CA2DF669D1886211F10624EBC003E655BFD)
