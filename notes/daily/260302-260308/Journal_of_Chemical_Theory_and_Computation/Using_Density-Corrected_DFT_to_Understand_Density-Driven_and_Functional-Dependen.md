---
title: "Using Density-Corrected DFT to Understand Density-Driven and Functional-Dependent Errors in Ab Initio Simulations of the Hydrated Electron"
title_zh: "使用密度校正的DFT来理解水合电子的从头算模拟中的密度驱动和功能相关误差"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01944"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1pICPQZRLAPrJHdL6Wjy9q-2BdcxjI976msKNnN9YGbN8Vo58RP0rD59whqRuHqCBSMj3ESygp4YbHpqggWv0nMOhFp0tczQ-2Ff5izioQP3-2BHUDcNCuWL9QgOeJdO-2BpxexVE0MFJ_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXftCnjkXfe-2F1TMU23p7HBBjCG6VtXxnRXPjQTbeY0th2HJ9g2Mca2DNJbc-2FMRHGDgxqWgKI5-2FRdxoPobtrgJ0ILfppFEsrregWN-2FpEoXpCs2qv2SK-2BeDHnFF-2Bt5LrVDVM4woRhbbY-2BhkYz1wRe0aEmMVaupNxbFNQK8HYIbdMfXx9U5d6wp6LTEj66sW7Ndbbs-3D"
pub_date: ""
tags: ["density-functional-theory", "hydrated-electron", "computational-chemistry", "error-correction", "molecular-dynamics"]
ai_relevance: 2
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Using Density-Corrected DFT to Understand Density-Driven and Functional-Dependent Errors in Ab Initio Simulations of the Hydrated Electron

**使用密度校正的DFT来理解水合电子的从头算模拟中的密度驱动和功能相关误差**

## 精华总结
本研究采用密度校正DFT (DC-DFT) 方法系统研究了溶水电子体系中的密度驱动误差和泛函依赖错误，通过分子动力学模拟揭示了电荷离域化的改善与实验可观测量偏差之间的矛盾现象，提出DFT模拟溶水电子的困难主要源于DFT本身的近似而非密度驱动误差。

**关键词**: 密度泛函理论、溶水电子、密度校正、误差分析、分子动力学模拟

## 摘要（英文）
The hydrated electron, an excess electron in liquid water, plays a crucial role in a plethora of chemical processes, motivating extensive research efforts to characterize its structure, dynamics, and reactivity in solution. Recent theoretical approaches to understanding this intriguing object have involved ab initio simulations based on density functional theory (DFT). Although DFT allows for the study of hydrated electron reactivity and quantum mechanical behavior, it is well-known that anionic systems can suffer from significant density-driven errors (DDEs). Density-corrected DFT (DC-DFT) provides a framework to mitigate such errors; the method reduces DDEs by replacing the self-consistent (SC) density associated with a given density functional with the Hartree-Fock (HF) density. Since HF densities tend to be more localized than DFT SC densities, the DC-DFT scheme significantly improves errors in calculations where the SC density is spuriously delocalized. Here, we investigate how the use of density correction affects the calculated properties of the DFT-simulated (PBEh) hydrated electron, a particularly challenging diffuse anionic system to simulate. First, we analyze charge delocalization in a system consisting of a model octahedral hydrated electron water cluster (the so-called Kevan structure) along with a spatially separated sulfur atom. We show that the use of density correction indeed reduces DDEs in comparison to a standard DFT global hybrid functional. We then propagate molecular dynamics trajectories of the hydrated electron using DC-DFT, where we find that DC further localizes electron density in the cavity region, a signature of reduced charge delocalization. Unfortunately, the decreased radius of gyration of the spin density and corresponding tightening of the local solvation structure from density correction causes predicted observables to deviate further from experimental measurements than when density correction is not employed. We argue that DC's worse agreement with experiment results from the removal of a fortuitous cancellation of errors that is intrinsic to the PBEh functional. This indicates that the difficulties with DFT to simulate hydrated electrons are primarily due to the inherent approximations in DFT rather than to density-driven errors.

## 摘要（中文）
水合电子，即存在于液态水中的一颗过量电子，在众多化学过程中发挥着至关重要的作用，因而激发了大量研究工作，旨在表征其在溶液中的结构、动力学行为及反应活性。近年来，用于理解这一引人入胜的体系的理论方法包括基于密度泛函理论（DFT）的从头算模拟。尽管密度泛函理论能够用于研究水合电子的反应性和量子力学行为，但众所周知，阴离子体系容易受到显著的密度驱动误差（DDE）的影响。密度校正密度泛函理论（DC-DFT）提供了一种缓解此类误差的框架；该方法通过用哈特里–福克（HF）密度替代与特定密度泛函相关的自洽（SC）密度，从而减小密度泛函误差。由于HF波函数的电子密度通常比DFT自洽场波函数的电子密度更具局域性，DC-DFT方法能够显著改善在自洽场波函数出现虚假离域化时计算中存在的误差。在此，我们研究密度校正方法的引入对基于DFT（PBEh泛函）模拟的水合电子计算性质的影响，该体系作为一种具有高度弥散性的阴离子系统，其模拟极具挑战性。首先，我们分析了一个由模型八面体水合电子水簇（即所谓的Kevan结构）与空间上分离的硫原子组成的体系中的电荷离域现象。我们表明，与标准的DFT全局杂化泛函相比，采用密度校正确实能够降低差分密度误差。随后，我们利用直流密度泛函理论模拟了水合电子的分子动力学轨迹，结果发现直流效应进一步将电子密度局域化于空穴区域，这是电荷离域程度降低的特征。不幸的是，密度校正导致自旋密度的回转半径减小以及局部溶剂化结构更加紧密，从而使理论预测的观测量相比未进行密度校正时与实验值的偏差更大。我们认为，DC方法与实验结果的偏差更大，是因为它消除了PBEh泛函固有的、偶然发生的误差抵消效应。这表明，DFT在模拟水合电子时遇到的困难主要源于DFT本身的固有近似，而非由密度驱动的误差所致。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1pICPQZRLAPrJHdL6Wjy9q-2BdcxjI976msKNnN9YGbN8Vo58RP0rD59whqRuHqCBSMj3ESygp4YbHpqggWv0nMOhFp0tczQ-2Ff5izioQP3-2BHUDcNCuWL9QgOeJdO-2BpxexVE0MFJ_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXftCnjkXfe-2F1TMU23p7HBBjCG6VtXxnRXPjQTbeY0th2HJ9g2Mca2DNJbc-2FMRHGDgxqWgKI5-2FRdxoPobtrgJ0ILfppFEsrregWN-2FpEoXpCs2qv2SK-2BeDHnFF-2Bt5LrVDVM4woRhbbY-2BhkYz1wRe0aEmMVaupNxbFNQK8HYIbdMfXx9U5d6wp6LTEj66sW7Ndbbs-3D)
