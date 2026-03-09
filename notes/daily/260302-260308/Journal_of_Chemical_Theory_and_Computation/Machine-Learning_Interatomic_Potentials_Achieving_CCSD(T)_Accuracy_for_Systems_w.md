---
title: "Machine-Learning Interatomic Potentials Achieving CCSD(T) Accuracy for Systems with Extended Covalent Networks and van der Waals Interactions"
title_zh: "具有扩展共价网络和范德华相互作用的系统的机器学习原子间势实现CCSD(T) 精度"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c02045"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE14dTqmOR82krA9g9pC0I3UU0kReZ7w12g40vsY0KAJjTkqMNtZsdKGsbcLXTcmqydD4peqUDM3IX-2F4bqe3anaqd-2FxfSm5kPyR9Uze1sHbpBd9xiODLjOWE1M0037WZBP4SLQL_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjW7AaooT4Kl7cFUzD7LieLOKneDI-2B5uQ7uNzJXnkKHZ3EdpDWVtkW9VFJn1b9jGoOWwwUdC-2FbbhgomsyeFpdsTo5kpCv862OJIezMqV5wm-2FjCd1uexewptPuEMD3ldXgrXJEE85Qim9MHRxaC-2FWSbxkZLv9CMnOjxYWsLKG3K-2FcjLTvwHIzMZXzuqItXcJrnq6pm5pdQg7Q73y28r7vvfvg-2B4MAhwzWKSDaWVn7Wo6-2B8-3D"
pub_date: ""
tags: ["machine-learning-potentials", "coupled-cluster-theory", "covalent-organic-frameworks", "interatomic-forces", "atomistic-simulations"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Machine-Learning Interatomic Potentials Achieving CCSD(T) Accuracy for Systems with Extended Covalent Networks and van der Waals Interactions

**具有扩展共价网络和范德华相互作用的系统的机器学习原子间势实现CCSD(T) 精度**

## 精华总结
开发了一种基于Δ-学习方法的机器学习势能训练策略,可以为具有扩展共价网络和范德华相互作用的系统实现CCSD(T)精度,为大规模原子模拟提供了实用的新途径。

**关键词**: 机器学习势能、CCSD(T)精度、共价有机框架、范德华相互作用、Δ-学习

## 摘要（英文）
Machine-learning interatomic potentials (MLIPs) enable large-scale atomistic simulations at moderate computational cost while retaining ab initio accuracy. In recent years, MLIPs trained on coupled-cluster data─particularly CCSD(T), which includes single, double, and perturbative triple excitations─have emerged as a promising route to achieve chemical accuracy (1 kcal/mol) beyond the limits of density functional theory (DFT) and to incorporate nonempirical van der Waals (vdW) interactions. Most existing approaches are, however, still not straightforwardly applicable for systems with extended covalent networks such as covalent organic frameworks (COFs) due to the limited availability of CCSD(T) under periodic boundary conditions. Here we present a methodology to train MLIPs with CCSD(T) accuracy for systems with extended covalent networks. The approach is based on the Δ-learning method with a dispersion-corrected tight-binding baseline and an MLIP trained on the differences of the target CCSD(T) energies from the baseline. This Δ-learning strategy enables training on compact molecular fragments while preserving transferability toward the periodic systems. Dispersion interactions are accounted for by including vdW-bound multimers in the training set, and the combination with a vdW-aware tight-binding baseline allows the formally local MLIP to attain CCSD(T)-level accuracy even for systems dominated by long-range vdW forces. The resulting potential yields root-mean-square energy errors below 0.4 meV/atom on both training and test sets and reproduces electronic total atomization energies, bond lengths, harmonic vibrational frequencies, and intermolecular interaction energies for benchmark molecular systems. We apply the method to a prototypical quasi-two-dimensional covalent organic framework (COF) composed of carbon and hydrogen. The COF structure, interlayer binding energies, and hydrogen absorption are analyzed at CCSD(T) accuracy. Overall, the developed methodology opens a practical route to large-scale atomistic simulations for systems with extended covalent networks and vdW interactions with chemical accuracy.

## 摘要（中文）
机器学习原子间势 (mlps) 能够以适中的计算成本进行大规模原子模拟，同时保持从头算精度。近年来，MLIPs在耦合聚类数据上训练，特别是CCSD(T)，包括单，双，微扰三重激发已成为实现化学精度 (1 °kcal/mol) 的有希望的途径，超出了密度泛函理论 (DFT) 的限制，并结合了非经验范德华 (vdW) 相互作用。然而，由于在周期性边界条件下CCSD(T) 的有限可用性，大多数现有方法仍然不能直接适用于具有扩展共价网络的系统，例如共价有机框架 (cof)。在这里，我们提出了一种方法来训练具有CCSD(T) 精度的mlps，用于具有扩展共价网络的系统。该方法基于 Δ 学习方法，该方法具有色散校正的紧密结合基线和根据目标CCSD(T) 能量与基线的差异训练的mlp。这种 Δ 学习策略可以在紧凑的分子片段上进行训练，同时保留向周期系统的可转移性。通过在训练集中包含vdW绑定的多聚体来考虑分散相互作用，并且与vdW感知的紧密结合基线的组合允许正式本地MLIP达到CCSD(T) 级精度，即使对于由远程控制的系统vdW部队。由此产生的电势在训练集和测试一下集上均产生低于0.4 °mev/原子的均方根能量误差，并再现基准分子系统的电子总雾化能，键长，谐波振动频率和分子间相互作用能。我们将该方法应用于由碳和氢组成的原型准二维共价有机框架 (COF)。以CCSD(T) 精度分析COF结构，层间结合能和氢吸收。总的来说，所开发的方法为具有扩展的共价网络和具有化学准确性的vdW相互作用的系统的大规模原子模拟开辟了一条实用的途径。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE14dTqmOR82krA9g9pC0I3UU0kReZ7w12g40vsY0KAJjTkqMNtZsdKGsbcLXTcmqydD4peqUDM3IX-2F4bqe3anaqd-2FxfSm5kPyR9Uze1sHbpBd9xiODLjOWE1M0037WZBP4SLQL_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjW7AaooT4Kl7cFUzD7LieLOKneDI-2B5uQ7uNzJXnkKHZ3EdpDWVtkW9VFJn1b9jGoOWwwUdC-2FbbhgomsyeFpdsTo5kpCv862OJIezMqV5wm-2FjCd1uexewptPuEMD3ldXgrXJEE85Qim9MHRxaC-2FWSbxkZLv9CMnOjxYWsLKG3K-2FcjLTvwHIzMZXzuqItXcJrnq6pm5pdQg7Q73y28r7vvfvg-2B4MAhwzWKSDaWVn7Wo6-2B8-3D)
