---
title: "Efficient Protein–Ligand Binding Free Energy Estimation with Coarse-Grained Funnel Metadynamics"
title_zh: "基于粗粒化漏斗元动力学的高效蛋白质-配体结合自由能估算"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01785"
url: "https://app.acspubs.org/e/er?s=1913652004&lid=109584&pci=CACSR000013623915&elqTrackId=d72112e480044f848672b53c3c761796&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF56703BC36D04744F96E49B1BEFDB38CA2DF669D1886211F10624EBC003E655BFD"
pub_date: ""
tags: ["molecular-dynamics", "binding-free-energy", "enhanced-sampling", "coarse-grained-modeling", "computational-chemistry"]
ai_relevance: 2
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Efficient Protein–Ligand Binding Free Energy Estimation with Coarse-Grained Funnel Metadynamics

**基于粗粒化漏斗元动力学的高效蛋白质-配体结合自由能估算**

## 精华总结
本研究提出粗粒度漏斗式元动力学(CG-FMD)方法,结合Martini 3力场实现高效的蛋白-配体结合自由能预测,在保持计算效率的同时达到与全原子分子动力学相当的精度。基于7ms以上的CG-FMD模拟数据,该方法相比AA-MD大幅降低计算成本,同时通过广泛采样有效降低统计不确定性。

**关键词**: 蛋白-配体结合、自由能计算、粗粒度分子动力学、增强采样、元动力学

## 摘要（英文）
Despite considerable advances in computational chemistry, bridging the gap between the accuracy of all-atom molecular dynamics (AA-MD) and the high-throughput capabilities of docking remains an unsolved problem in protein-ligand binding free energy predictions. In this work, we propose to address this challenge through coarse-grained funnel metadynamics (CG-FMD) with the Martini 3 force field. This approach combines the reduced computational cost of a CG representation with state-of-the-art enhanced sampling techniques and the interpretability of a physics-based force field. Specifically, the binding of colchicine to two different protein targets was modeled at both AA and CG resolutions, and the corresponding ΔGbind predictions were compared with experimental references. Additionally, the robustness of CG-FMD-based ΔGbind predictions was evaluated with respect to various aspects of the simulation setup by collecting more than 7 ms of CG-FMD simulations. The optimal simulation protocol has been further validated against a limited set of compounds chemically different from colchicine. The results demonstrate that CG-FMD yields ΔGbind estimates comparable to experimental values while requiring only a fraction of the computational cost of AA-MD simulations. Moreover, the extensive sampling achievable with CG-FMD reduces statistical uncertainty in the final predictions, effectively compensating for the simplified system representation. Future work should build upon these methodological insights to broaden the scope of ligands and targets explored.

## 摘要（中文）
尽管计算化学取得了显著进展，但在蛋白质-配体结合自由能预测中，如何弥合全原子分子动力学（AA-MD）的精度与对接方法高通量能力之间的差距，仍然是一个尚未解决的问题。在本工作中，我们提出利用基于Martini 3力场的粗粒化漏斗元动力学（CG-FMD）来应对这一挑战。该方法将CG表示的低计算成本、最先进的增强采样技术以及基于物理的力场的可解释性相结合。具体而言，采用原子分辨率和粗粒化分辨率两种模拟方案，分别对秋水仙碱与两个不同蛋白质靶标的结合进行了建模，并将所得的结合自由能变化ΔGbind预测值与实验参考值进行了对比。此外，通过收集超过7毫秒的粗粒化分子动力学模拟数据，从模拟设置的多个方面评估了基于CG-FMD的ΔGbind预测的稳健性。最优模拟方案已针对一组化学结构与秋水仙碱迥异的有限化合物进一步验证。结果表明，CG-FMD能够得到与实验值相当的 ΔGbind估计值，同时所需的计算成本仅为AA-MD模拟的一小部分。此外，基于CG-FMD所能实现的广泛采样降低了最终预测中的统计不确定性，从而有效弥补了简化系统表征带来的不足。未来的工作应以这些方法学洞见为基础，进一步拓展所研究的配体和靶标的范围。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](https://app.acspubs.org/e/er?s=1913652004&lid=109584&pci=CACSR000013623915&elqTrackId=d72112e480044f848672b53c3c761796&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF56703BC36D04744F96E49B1BEFDB38CA2DF669D1886211F10624EBC003E655BFD)
