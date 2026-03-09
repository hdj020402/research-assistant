---
title: "UniDock-Pro: A Unified GPU-Accelerated Platform for High-Throughput Structure-Based, Ligand-Based, and Synergistic Hybrid Virtual Screening"
title_zh: "Unidock-pro: 一个统一的GPU加速平台，用于基于结构、基于配体和协同的混合虚拟筛选"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02587"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPc7INhjcuOdtwI-2FKA8DOHqA-2BxaTN-2BU5eCj4wE8RC0TLTORQDdNkVLqtacGcg4AvzoMaJOcrRi2NkGyMotIBojnmjLq-2BdGnOE9dSB11-2BUPTVXk85oPmk0dWefSYflToeiP4TZd_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBApsTIGBJA501RAyftmBUg-2FoErvMG7pOWEiTlO47Ph6eJmZmdogLWoYqdQiutkD9mCnMgSp9NgYFnnE7X32SYHiDwn8z99Po0h5RPqAaXXfwOhpfsSE34cNqrnL3onPRMOVKI72Nxq-2FJtnco3ERK4mKo3Au-2BpyKzBTlK3P24WbcTDoyKVdo5rHGdVehbGIZ-2BY-3D"
pub_date: ""
tags: ["virtual-screening", "gpu-acceleration", "drug-discovery", "structure-based-docking", "hybrid-methods"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# UniDock-Pro: A Unified GPU-Accelerated Platform for High-Throughput Structure-Based, Ligand-Based, and Synergistic Hybrid Virtual Screening

**Unidock-pro: 一个统一的GPU加速平台，用于基于结构、基于配体和协同的混合虚拟筛选**

## 精华总结
UniDock-Pro是一个基于GPU加速Uni-Dock架构的统一平台，整合了基于结构的虚拟筛选(SBVS)、基于配体的虚拟筛选(LBVS)和新颖的混合虚拟筛选模式，通过在构象搜索中结合互补信息，能够在单个GPU上每天处理数百万个化合物。

**关键词**: 虚拟筛选、GPU加速、药物发现、混合方法、力场分析

## 摘要（英文）
The screening of ultralarge chemical libraries requires high-throughput computational tools that can efficiently exploit all available structural and chemical information. We present UniDock-Pro, a unified platform based on the GPU-accelerated Uni-Dock architecture that integrates structure-based virtual screening (SBVS), ligand-based virtual screening (LBVS), and a novel hybrid virtual screening mode. By capitalizing on inter-ligand (batch) parallelism, UniDock-Pro achieves substantial throughput gains, enabling the processing of millions of compounds per day on a single GPU. We significantly enhanced the LBVS methodology by implementing a smooth, Lennard-Jones-like potential optimized for gradient-based search, which replaces the rugged recursive model employed in our previous work. This optimization yields a substantial 2.42-fold improvement in early enrichment (EF1%) over the legacy AutoDock-SS on the DUDE-Z benchmark. The Hybrid mode combines complementary information by integrating receptor- and ligand-derived grid maps on-the-fly during the conformational search, delivering strong early enrichment on DUDE-Z and competitive performance on the more stringent VSDS-vd TrueDecoy benchmark. To understand the mechanisms underlying this synergy, we introduce Force Field Complementarity Analysis (FFCA), a method for quantifying the spatial alignment between receptor and ligand force fields. UniDock-Pro offers a robust, versatile, and highly efficient solution for accelerating drug discovery campaigns across the expansive modern chemical space.

## 摘要（中文）
超大规模化学库的筛选需要高通量计算工具，能够高效地利用所有可用的结构和化学信息。我们提出了UniDock-Pro，这是一个基于GPU加速的Uni-Dock架构的统一平台，集成了基于结构的虚拟筛选（SBVS）、基于配体的虚拟筛选（LBVS）以及一种新颖的混合型虚拟筛选模式。通过充分利用配体间（批次）并行性，UniDock-Pro实现了显著的吞吐量提升，能够在单张GPU上每天处理数百万个化合物。我们通过引入一种平滑的、类Lennard-Jones势能函数，并针对基于梯度的搜索进行优化，显著提升了LBVS方法学。该势能函数取代了我们先前工作中所采用的崎岖递归模型。在DUDE-Z基准测试上，该优化方法相比传统AutoDock-SS，早期富集度（EF1%）提升了高达2.42倍。混合模式在构象搜索过程中实时整合受体和配体衍生的网格图，从而融合互补信息，在DUDE-Z数据集上实现了优异的早期富集效果，并在更为严格的VSDS-vd TrueDecoy基准测试中表现出具有竞争力的性能。为揭示这一协同效应的分子机制，我们提出了力场互补性分析（FFCA），这是一种用于量化受体与配体力场空间匹配程度的方法。UniDock-Pro提供了一套强大、versatile且高效的解决方案，可加速覆盖广阔现代化学空间的药物发现项目。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPc7INhjcuOdtwI-2FKA8DOHqA-2BxaTN-2BU5eCj4wE8RC0TLTORQDdNkVLqtacGcg4AvzoMaJOcrRi2NkGyMotIBojnmjLq-2BdGnOE9dSB11-2BUPTVXk85oPmk0dWefSYflToeiP4TZd_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBApsTIGBJA501RAyftmBUg-2FoErvMG7pOWEiTlO47Ph6eJmZmdogLWoYqdQiutkD9mCnMgSp9NgYFnnE7X32SYHiDwn8z99Po0h5RPqAaXXfwOhpfsSE34cNqrnL3onPRMOVKI72Nxq-2FJtnco3ERK4mKo3Au-2BpyKzBTlK3P24WbcTDoyKVdo5rHGdVehbGIZ-2BY-3D)
