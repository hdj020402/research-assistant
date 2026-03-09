---
title: "Efficient Protein–Ligand Binding Free Energy Estimation with Coarse-Grained Funnel Metadynamics"
title_zh: "基于粗粒漏斗元动力学的高效蛋白质-配体结合自由能估算"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01785"
url: "https://app.acspubs.org/e/er?s=1913652004&lid=109584&pci=CACSR000013623915&elqTrackId=d72112e480044f848672b53c3c761796&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF56703BC36D04744F96E49B1BEFDB38CA2DF669D1886211F10624EBC003E655BFD"
pub_date: ""
tags: ["molecular-dynamics", "binding-free-energy", "coarse-graining", "enhanced-sampling", "computational-chemistry"]
ai_relevance: 2
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Efficient Protein–Ligand Binding Free Energy Estimation with Coarse-Grained Funnel Metadynamics

**基于粗粒漏斗元动力学的高效蛋白质-配体结合自由能估算**

## 精华总结
本研究提出粗粒化漏斗元动力学(CG-FMD)方法结合Martini 3力场，在保持物理意义的同时显著降低计算成本，实现了与全原子分子动力学相当的蛋白-配体结合自由能预测精度。通过超过7毫秒的采样验证了该方法的稳健性和准确性，为高通量药物发现提供了新的计算途径。

**关键词**: 蛋白-配体结合、自由能计算、粗粒化分子动力学、元动力学、高通量计算

## 摘要（英文）
Despite considerable advances in computational chemistry, bridging the gap between the accuracy of all-atom molecular dynamics (AA-MD) and the high-throughput capabilities of docking remains an unsolved problem in protein-ligand binding free energy predictions. In this work, we propose to address this challenge through coarse-grained funnel metadynamics (CG-FMD) with the Martini 3 force field. This approach combines the reduced computational cost of a CG representation with state-of-the-art enhanced sampling techniques and the interpretability of a physics-based force field. Specifically, the binding of colchicine to two different protein targets was modeled at both AA and CG resolutions, and the corresponding ΔGbind predictions were compared with experimental references. Additionally, the robustness of CG-FMD-based ΔGbind predictions was evaluated with respect to various aspects of the simulation setup by collecting more than 7 ms of CG-FMD simulations. The optimal simulation protocol has been further validated against a limited set of compounds chemically different from colchicine. The results demonstrate that CG-FMD yields ΔGbind estimates comparable to experimental values while requiring only a fraction of the computational cost of AA-MD simulations. Moreover, the extensive sampling achievable with CG-FMD reduces statistical uncertainty in the final predictions, effectively compensating for the simplified system representation. Future work should build upon these methodological insights to broaden the scope of ligands and targets explored.

## 摘要（中文）
尽管计算化学取得了长足的进步，但弥合全原子分子动力学 (aa-md) 的准确性与对接的高通量能力之间的差距仍然是蛋白质-配体结合自由能预测中尚未解决的问题。在这项工作中，我们建议通过粗粒漏斗元动力学 (cg-fmd) 与马提尼3力场来解决这一挑战。这种方法将CG表示的降低的计算成本与最先进的增强采样技术以及基于物理的力场的可解释性相结合。具体而言，在AA和CG分辨率下对秋水仙碱与两种不同蛋白质靶标的结合进行建模，并将相应的 Δ gbind预测与实验参考进行比较。此外，通过收集超过7毫秒的cg-fmd模拟，针对模拟设置的各个方面评估了基于cg-fmd的 Δ gbind预测的稳健性。最佳模拟方案已针对化学上不同于秋水仙碱的有限化合物进行了进一步验证。结果表明，cg-fmd产生的 Δ gbind估计值与实验值相当，而仅需要aa-md模拟的一小部分计算成本。此外，cg-fmd可实现的广泛采样减少了最终预测中的统计不确定性，从而有效地补偿了简化的系统表示。未来的工作应建立在这些方法论见解的基础上，以扩大所探索的配体和目标的范围。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](https://app.acspubs.org/e/er?s=1913652004&lid=109584&pci=CACSR000013623915&elqTrackId=d72112e480044f848672b53c3c761796&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF56703BC36D04744F96E49B1BEFDB38CA2DF669D1886211F10624EBC003E655BFD)
