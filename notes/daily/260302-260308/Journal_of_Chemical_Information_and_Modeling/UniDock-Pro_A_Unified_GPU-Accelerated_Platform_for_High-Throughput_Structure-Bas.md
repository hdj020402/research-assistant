---
title: "UniDock-Pro: A Unified GPU-Accelerated Platform for High-Throughput Structure-Based, Ligand-Based, and Synergistic Hybrid Virtual Screening"
title_zh: "UniDock-Pro：用于高通量基于结构、基于配体和协同混合虚拟筛选的统一GPU加速平台"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02587"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPc7INhjcuOdtwI-2FKA8DOHqA-2BxaTN-2BU5eCj4wE8RC0TLTORQDdNkVLqtacGcg4AvzoMaJOcrRi2NkGyMotIBojnmjLq-2BdGnOE9dSB11-2BUPTVXk85oPmk0dWefSYflToeiP4TZd_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBApsTIGBJA501RAyftmBUg-2FoErvMG7pOWEiTlO47Ph6eJmZmdogLWoYqdQiutkD9mCnMgSp9NgYFnnE7X32SYHiDwn8z99Po0h5RPqAaXXfwOhpfsSE34cNqrnL3onPRMOVKI72Nxq-2FJtnco3ERK4mKo3Au-2BpyKzBTlK3P24WbcTDoyKVdo5rHGdVehbGIZ-2BY-3D"
pub_date: ""
tags: ["virtual-screening", "drug-discovery", "gpu-acceleration", "molecular-docking", "high-throughput-computation"]
ai_relevance: 3
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# UniDock-Pro: A Unified GPU-Accelerated Platform for High-Throughput Structure-Based, Ligand-Based, and Synergistic Hybrid Virtual Screening

**UniDock-Pro：用于高通量基于结构、基于配体和协同混合虚拟筛选的统一GPU加速平台**

## 精华总结
UniDock-Pro是一个统一的GPU加速平台，整合了基于结构、基于配体和混合虚拟筛选模式，能够以显著提升的效率处理数百万个化合物的高通量筛选。该平台通过新型力场互补性分析方法揭示了协同筛选的机制，在多个基准上展现了优异的早期富集性能。

**关键词**: 虚拟筛选、GPU加速、药物发现、混合方法、力场分析

## 摘要（英文）
The screening of ultralarge chemical libraries requires high-throughput computational tools that can efficiently exploit all available structural and chemical information. We present UniDock-Pro, a unified platform based on the GPU-accelerated Uni-Dock architecture that integrates structure-based virtual screening (SBVS), ligand-based virtual screening (LBVS), and a novel hybrid virtual screening mode. By capitalizing on inter-ligand (batch) parallelism, UniDock-Pro achieves substantial throughput gains, enabling the processing of millions of compounds per day on a single GPU. We significantly enhanced the LBVS methodology by implementing a smooth, Lennard-Jones-like potential optimized for gradient-based search, which replaces the rugged recursive model employed in our previous work. This optimization yields a substantial 2.42-fold improvement in early enrichment (EF1%) over the legacy AutoDock-SS on the DUDE-Z benchmark. The Hybrid mode combines complementary information by integrating receptor- and ligand-derived grid maps on-the-fly during the conformational search, delivering strong early enrichment on DUDE-Z and competitive performance on the more stringent VSDS-vd TrueDecoy benchmark. To understand the mechanisms underlying this synergy, we introduce Force Field Complementarity Analysis (FFCA), a method for quantifying the spatial alignment between receptor and ligand force fields. UniDock-Pro offers a robust, versatile, and highly efficient solution for accelerating drug discovery campaigns across the expansive modern chemical space.

## 摘要（中文）
超大型化学库的筛选需要能够高效利用所有可用结构和化学信息的高通量计算工具。我们提出了UniDock-Pro，一个基于GPU加速Uni-Dock架构的统一平台，集成了基于结构的虚拟筛选（SBVS）、基于配体的虚拟筛选（LBVS）和一种新颖的混合虚拟筛选模式。通过利用配体间（批处理）并行性，UniDock-Pro实现了显著的通量提升，能够在单个GPU上每天处理数百万个化合物。我们通过实现平滑的Lennard-Jones型势能（针对基于梯度的搜索进行优化）显著增强了LBVS方法，这替代了我们之前工作中采用的复杂递归模型。该优化在DUDE-Z基准上相对于传统AutoDock-SS的早期富集（EF1%）产生了2.42倍的显著改进。混合模式通过在构象搜索过程中即时整合受体和配体衍生的网格图，结合了互补信息，在DUDE-Z上提供了强大的早期富集，在更严格的VSDS-vd TrueDecoy基准上实现了具竞争力的性能。为了理解这种协同作用的潜在机制，我们引入了力场互补性分析（FFCA），这是一种量化受体和配体力场之间空间对齐的方法。UniDock-Pro为加速跨越广阔的现代化学空间的药物发现活动提供了一个健壮、多功能且高效的解决方案。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPc7INhjcuOdtwI-2FKA8DOHqA-2BxaTN-2BU5eCj4wE8RC0TLTORQDdNkVLqtacGcg4AvzoMaJOcrRi2NkGyMotIBojnmjLq-2BdGnOE9dSB11-2BUPTVXk85oPmk0dWefSYflToeiP4TZd_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBApsTIGBJA501RAyftmBUg-2FoErvMG7pOWEiTlO47Ph6eJmZmdogLWoYqdQiutkD9mCnMgSp9NgYFnnE7X32SYHiDwn8z99Po0h5RPqAaXXfwOhpfsSE34cNqrnL3onPRMOVKI72Nxq-2FJtnco3ERK4mKo3Au-2BpyKzBTlK3P24WbcTDoyKVdo5rHGdVehbGIZ-2BY-3D)
