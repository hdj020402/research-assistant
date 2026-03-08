---
title: "Using Density-Corrected DFT to Understand Density-Driven and Functional-Dependent Errors in Ab Initio Simulations of the Hydrated Electron"
title_zh: "使用密度校正DFT理解水合电子原位模拟中的密度驱动和泛函依赖误差"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01944"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1pICPQZRLAPrJHdL6Wjy9q-2BdcxjI976msKNnN9YGbN8Vo58RP0rD59whqRuHqCBSMj3ESygp4YbHpqggWv0nMOhFp0tczQ-2Ff5izioQP3-2BHUDcNCuWL9QgOeJdO-2BpxexVE0MFJ_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXftCnjkXfe-2F1TMU23p7HBBjCG6VtXxnRXPjQTbeY0th2HJ9g2Mca2DNJbc-2FMRHGDgxqWgKI5-2FRdxoPobtrgJ0ILfppFEsrregWN-2FpEoXpCs2qv2SK-2BeDHnFF-2Bt5LrVDVM4woRhbbY-2BhkYz1wRe0aEmMVaupNxbFNQK8HYIbdMfXx9U5d6wp6LTEj66sW7Ndbbs-3D"
pub_date: ""
tags: ["density-functional-theory", "computational-chemistry", "hydrated-electron", "charge-delocalization", "molecular-dynamics"]
ai_relevance: 2
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Using Density-Corrected DFT to Understand Density-Driven and Functional-Dependent Errors in Ab Initio Simulations of the Hydrated Electron

**使用密度校正DFT理解水合电子原位模拟中的密度驱动和泛函依赖误差**

## 精华总结
通过密度校正DFT方法研究水合电子的密度驱动误差，发现密度校正虽能减少离域化但导致与实验结果偏离更大，表明DFT模拟水合电子的困难主要源于泛函本身的近似而非密度驱动误差。

**关键词**: 密度泛函理论、水合电子、密度驱动误差、密度校正、分子动力学模拟

## 摘要（英文）
The hydrated electron, an excess electron in liquid water, plays a crucial role in a plethora of chemical processes, motivating extensive research efforts to characterize its structure, dynamics, and reactivity in solution. Recent theoretical approaches to understanding this intriguing object have involved ab initio simulations based on density functional theory (DFT). Although DFT allows for the study of hydrated electron reactivity and quantum mechanical behavior, it is well-known that anionic systems can suffer from significant density-driven errors (DDEs). Density-corrected DFT (DC-DFT) provides a framework to mitigate such errors; the method reduces DDEs by replacing the self-consistent (SC) density associated with a given density functional with the Hartree-Fock (HF) density. Since HF densities tend to be more localized than DFT SC densities, the DC-DFT scheme significantly improves errors in calculations where the SC density is spuriously delocalized. Here, we investigate how the use of density correction affects the calculated properties of the DFT-simulated (PBEh) hydrated electron, a particularly challenging diffuse anionic system to simulate. First, we analyze charge delocalization in a system consisting of a model octahedral hydrated electron water cluster (the so-called Kevan structure) along with a spatially separated sulfur atom. We show that the use of density correction indeed reduces DDEs in comparison to a standard DFT global hybrid functional. We then propagate molecular dynamics trajectories of the hydrated electron using DC-DFT, where we find that DC further localizes electron density in the cavity region, a signature of reduced charge delocalization. Unfortunately, the decreased radius of gyration of the spin density and corresponding tightening of the local solvation structure from density correction causes predicted observables to deviate further from experimental measurements than when density correction is not employed. We argue that DC's worse agreement with experiment results from the removal of a fortuitous cancellation of errors that is intrinsic to the PBEh functional. This indicates that the difficulties with DFT to simulate hydrated electrons are primarily due to the inherent approximations in DFT rather than to density-driven errors.

## 摘要（中文）
水合电子（液态水中的过量电子）在众多化学过程中起着至关重要的作用，促使大量研究工作致力于表征其在溶液中的结构、动力学和反应性。最近理解这一有趣对象的理论方法涉及基于密度泛函理论（DFT）的原位模拟。尽管DFT允许研究水合电子的反应性和量子力学行为，但众所周知，阴离子体系可能受到显著的密度驱动误差（DDEs）的影响。密度校正DFT（DC-DFT）提供了一种框架来减轻这些误差；该方法通过用Hartree-Fock（HF）密度替换与给定密度泛函相关的自洽（SC）密度来减少DDEs。由于HF密度往往比DFT SC密度更加局域化，DC-DFT方案显著改进了SC密度虚假离域化的计算中的误差。在这里，我们研究了密度校正的使用如何影响DFT模拟（PBEh）水合电子的计算性质，这是一个特别难以模拟的扩散阴离子体系。首先，我们分析了由模型八面体水合电子水簇（所谓的Kevan结构）加上空间分离的硫原子组成的体系中的电荷离域化。我们证明使用密度校正确实与标准DFT全局混合泛函相比减少了DDEs。然后，我们使用DC-DFT传播水合电子的分子动力学轨迹，其中我们发现DC进一步将电子密度局域化在空腔区域中，这是电荷离域化减少的信号。不幸的是，密度校正导致的自旋密度回旋半径减少和相应的局部溶剂化结构紧密，使预测的可观测量偏离实验测量值的程度比不采用密度校正时更远。我们论证DC与实验的更差协议是由于去除了内在于PBEh泛函的误差补偿的巧合抵消所致。这表明DFT模拟水合电子的困难主要源于DFT中的固有近似而不是密度驱动的误差。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1pICPQZRLAPrJHdL6Wjy9q-2BdcxjI976msKNnN9YGbN8Vo58RP0rD59whqRuHqCBSMj3ESygp4YbHpqggWv0nMOhFp0tczQ-2Ff5izioQP3-2BHUDcNCuWL9QgOeJdO-2BpxexVE0MFJ_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXftCnjkXfe-2F1TMU23p7HBBjCG6VtXxnRXPjQTbeY0th2HJ9g2Mca2DNJbc-2FMRHGDgxqWgKI5-2FRdxoPobtrgJ0ILfppFEsrregWN-2FpEoXpCs2qv2SK-2BeDHnFF-2Bt5LrVDVM4woRhbbY-2BhkYz1wRe0aEmMVaupNxbFNQK8HYIbdMfXx9U5d6wp6LTEj66sW7Ndbbs-3D)
