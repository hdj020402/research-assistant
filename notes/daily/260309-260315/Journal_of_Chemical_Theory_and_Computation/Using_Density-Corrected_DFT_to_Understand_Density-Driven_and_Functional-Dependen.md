---
title: "Using Density-Corrected DFT to Understand Density-Driven and Functional-Dependent Errors in Ab Initio Simulations of the Hydrated Electron"
title_zh: "利用密度修正DFT理解水合电子从头计算模拟中的密度驱动和泛函依赖误差"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01944"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1pICPQZRLAPrJHdL6Wjy9q-2BdcxjI976msKNnN9YGbN8Vo58RP0rD59whqRuHqCBSMj3ESygp4YbHpqggWv0nMOhFp0tczQ-2Ff5izioQP3-2BHUDcNCuWL9QgOeJdO-2BpxexVE0MFJ_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXftCnjkXfe-2F1TMU23p7HBBjCG6VtXxnRXPjQTbeY0th2HJ9g2Mca2DNJbc-2FMRHGDgxqWgKI5-2FRdxoPobtrgJ0ILfppFEsrregWN-2FpEoXpCs2qv2SK-2BeDHnFF-2Bt5LrVDVM4woRhbbY-2BhkYz1wRe0aEmMVaupNxbFNQK8HYIbdMfXx9U5d6wp6LTEj66sW7Ndbbs-3D"
pub_date: ""
tags: ["density-functional-theory", "hydrated-electron", "computational-chemistry", "error-correction", "molecular-simulation"]
ai_relevance: 2
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Using Density-Corrected DFT to Understand Density-Driven and Functional-Dependent Errors in Ab Initio Simulations of the Hydrated Electron

**利用密度修正DFT理解水合电子从头计算模拟中的密度驱动和泛函依赖误差**

## 精华总结
研究表明密度修正DFT能有效减少水合电子模拟中的电荷离域问题,但这种改进反而导致预测结果与实验偏离更远,揭示了DFT方法的固有局限性。

**关键词**: 水合电子、密度泛函理论、密度驱动误差、分子动力学模拟、电荷离域

## 摘要（英文）
The hydrated electron, an excess electron in liquid water, plays a crucial role in a plethora of chemical processes, motivating extensive research efforts to characterize its structure, dynamics, and reactivity in solution. Recent theoretical approaches to understanding this intriguing object have involved ab initio simulations based on density functional theory (DFT). Although DFT allows for the study of hydrated electron reactivity and quantum mechanical behavior, it is well-known that anionic systems can suffer from significant density-driven errors (DDEs). Density-corrected DFT (DC-DFT) provides a framework to mitigate such errors; the method reduces DDEs by replacing the self-consistent (SC) density associated with a given density functional with the Hartree-Fock (HF) density. Since HF densities tend to be more localized than DFT SC densities, the DC-DFT scheme significantly improves errors in calculations where the SC density is spuriously delocalized. Here, we investigate how the use of density correction affects the calculated properties of the DFT-simulated (PBEh) hydrated electron, a particularly challenging diffuse anionic system to simulate. First, we analyze charge delocalization in a system consisting of a model octahedral hydrated electron water cluster (the so-called Kevan structure) along with a spatially separated sulfur atom. We show that the use of density correction indeed reduces DDEs in comparison to a standard DFT global hybrid functional. We then propagate molecular dynamics trajectories of the hydrated electron using DC-DFT, where we find that DC further localizes electron density in the cavity region, a signature of reduced charge delocalization. Unfortunately, the decreased radius of gyration of the spin density and corresponding tightening of the local solvation structure from density correction causes predicted observables to deviate further from experimental measurements than when density correction is not employed. We argue that DC's worse agreement with experiment results from the removal of a fortuitous cancellation of errors that is intrinsic to the PBEh functional. This indicates that the difficulties with DFT to simulate hydrated electrons are primarily due to the inherent approximations in DFT rather than to density-driven errors.

## 摘要（中文）
水合电子作为液态水中的过量电子,在众多化学过程中起关键作用。虽然基于密度泛函理论(DFT)的从头计算模拟可以研究水合电子的反应性和量子力学行为,但阴离子系统容易产生显著的密度驱动误差(DDE)。本研究采用密度修正DFT(DC-DFT)方法通过用Hartree-Fock密度替换自洽DFT密度来减少这些误差。研究发现,虽然密度修正确实减少了电荷离域现象,但预测的物理量与实验值的偏差反而更大,表明DFT模拟水合电子的困难主要源于DFT内在近似而非密度驱动误差。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1pICPQZRLAPrJHdL6Wjy9q-2BdcxjI976msKNnN9YGbN8Vo58RP0rD59whqRuHqCBSMj3ESygp4YbHpqggWv0nMOhFp0tczQ-2Ff5izioQP3-2BHUDcNCuWL9QgOeJdO-2BpxexVE0MFJ_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXftCnjkXfe-2F1TMU23p7HBBjCG6VtXxnRXPjQTbeY0th2HJ9g2Mca2DNJbc-2FMRHGDgxqWgKI5-2FRdxoPobtrgJ0ILfppFEsrregWN-2FpEoXpCs2qv2SK-2BeDHnFF-2Bt5LrVDVM4woRhbbY-2BhkYz1wRe0aEmMVaupNxbFNQK8HYIbdMfXx9U5d6wp6LTEj66sW7Ndbbs-3D)
