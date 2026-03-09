---
title: "Machine-Learning Interatomic Potentials Achieving CCSD(T) Accuracy for Systems with Extended Covalent Networks and van der Waals Interactions"
title_zh: "达到CCSD(T)精度的机器学习原子间势能模型，适用于具有扩展共价网络和范德华相互作用的体系"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c02045"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE14dTqmOR82krA9g9pC0I3UU0kReZ7w12g40vsY0KAJjTkqMNtZsdKGsbcLXTcmqydD4peqUDM3IX-2F4bqe3anaqd-2FxfSm5kPyR9Uze1sHbpBd9xiODLjOWE1M0037WZBP4SLQL_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjW7AaooT4Kl7cFUzD7LieLOKneDI-2B5uQ7uNzJXnkKHZ3EdpDWVtkW9VFJn1b9jGoOWwwUdC-2FbbhgomsyeFpdsTo5kpCv862OJIezMqV5wm-2FjCd1uexewptPuEMD3ldXgrXJEE85Qim9MHRxaC-2FWSbxkZLv9CMnOjxYWsLKG3K-2FcjLTvwHIzMZXzuqItXcJrnq6pm5pdQg7Q73y28r7vvfvg-2B4MAhwzWKSDaWVn7Wo6-2B8-3D"
pub_date: ""
tags: ["machine-learning", "interatomic-potentials", "coupled-cluster", "covalent-organic-frameworks", "van-der-waals"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Machine-Learning Interatomic Potentials Achieving CCSD(T) Accuracy for Systems with Extended Covalent Networks and van der Waals Interactions

**达到CCSD(T)精度的机器学习原子间势能模型，适用于具有扩展共价网络和范德华相互作用的体系**

## 精华总结
一种训练机器学习原子间势能函数（MLIPs）以实现CCSD(T)精度的方法被开发出来，该方法适用于具有扩展共价网络和范德华相互作用的系统，为这类系统的大规模原子论模拟提供了实用的路线。

**关键词**: 机器学习势能函数、CCSD(T)精度、共价有机框架、范德华相互作用、Δ-学习方法

## 摘要（英文）
Machine-learning interatomic potentials (MLIPs) enable large-scale atomistic simulations at moderate computational cost while retaining ab initio accuracy. In recent years, MLIPs trained on coupled-cluster data─particularly CCSD(T), which includes single, double, and perturbative triple excitations─have emerged as a promising route to achieve chemical accuracy (1 kcal/mol) beyond the limits of density functional theory (DFT) and to incorporate nonempirical van der Waals (vdW) interactions. Most existing approaches are, however, still not straightforwardly applicable for systems with extended covalent networks such as covalent organic frameworks (COFs) due to the limited availability of CCSD(T) under periodic boundary conditions. Here we present a methodology to train MLIPs with CCSD(T) accuracy for systems with extended covalent networks. The approach is based on the Δ-learning method with a dispersion-corrected tight-binding baseline and an MLIP trained on the differences of the target CCSD(T) energies from the baseline. This Δ-learning strategy enables training on compact molecular fragments while preserving transferability toward the periodic systems. Dispersion interactions are accounted for by including vdW-bound multimers in the training set, and the combination with a vdW-aware tight-binding baseline allows the formally local MLIP to attain CCSD(T)-level accuracy even for systems dominated by long-range vdW forces. The resulting potential yields root-mean-square energy errors below 0.4 meV/atom on both training and test sets and reproduces electronic total atomization energies, bond lengths, harmonic vibrational frequencies, and intermolecular interaction energies for benchmark molecular systems. We apply the method to a prototypical quasi-two-dimensional covalent organic framework (COF) composed of carbon and hydrogen. The COF structure, interlayer binding energies, and hydrogen absorption are analyzed at CCSD(T) accuracy. Overall, the developed methodology opens a practical route to large-scale atomistic simulations for systems with extended covalent networks and vdW interactions with chemical accuracy.

## 摘要（中文）
机器学习原子间势能函数（MLIPs）能够在保持从头算精度的同时，以适中的计算成本实现大规模原子尺度模拟。近年来，基于耦合簇理论数据（尤其是包含单激发、双激发和微扰三重激发的CCSD(T)）训练的机器学习势能面已成为一种很有前景的方法，它能够在超越密度泛函理论（DFT）极限的同时实现化学精度（1 kcal/mol），并纳入非经验性的范德华相互作用。然而，由于在周期性边界条件下CCSD(T)方法的可用性有限，大多数现有方法仍然无法直接应用于具有扩展共价网络的体系，例如共价有机框架（COFs）。在此，我们提出了一种方法，用于训练具有CCSD(T)精度的MLIP模型，以描述具有扩展共价网络的体系。该方法基于Δ-学习框架，以色散校正的紧束缚基线模型为基础，并采用机器学习势能面（MLIP）来拟合目标CCSD(T)能量与基线能量之间的差异。这种Δ-学习策略能够在紧凑的分子片段上进行训练，同时保持对周期性体系的可迁移性。通过在训练集中纳入范德华键合的多聚体来考虑色散相互作用；再结合一种具有范德华效应感知能力的紧束缚基线模型，即便对于以长程范德华力为主的体系，这种形式上局部的机器学习势也能达到CCSD(T)级别的精度。所得势函数在训练集和测试集上均能给出低于0.4 meV/原子的均方根能量误差，并能准确预测基准分子体系的电子总解离能、键长、简谐振动频率以及分子间相互作用能。我们将该方法应用于由碳和氢组成的典型准二维共价有机框架（COF）。在CCSD(T)精度下，对COF的结构、层间结合能以及氢气吸附性能进行了分析。总体而言，所发展的方法学为具有扩展共价网络和范德华相互作用的体系提供了实现化学精度的大规模原子级模拟的实用途径。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE14dTqmOR82krA9g9pC0I3UU0kReZ7w12g40vsY0KAJjTkqMNtZsdKGsbcLXTcmqydD4peqUDM3IX-2F4bqe3anaqd-2FxfSm5kPyR9Uze1sHbpBd9xiODLjOWE1M0037WZBP4SLQL_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjW7AaooT4Kl7cFUzD7LieLOKneDI-2B5uQ7uNzJXnkKHZ3EdpDWVtkW9VFJn1b9jGoOWwwUdC-2FbbhgomsyeFpdsTo5kpCv862OJIezMqV5wm-2FjCd1uexewptPuEMD3ldXgrXJEE85Qim9MHRxaC-2FWSbxkZLv9CMnOjxYWsLKG3K-2FcjLTvwHIzMZXzuqItXcJrnq6pm5pdQg7Q73y28r7vvfvg-2B4MAhwzWKSDaWVn7Wo6-2B8-3D)
