---
title: "UniDock-Pro: A Unified GPU-Accelerated Platform for High-Throughput Structure-Based, Ligand-Based, and Synergistic Hybrid Virtual Screening"
title_zh: "UniDock-Pro：统一的GPU加速高通量基于结构、基于配体和混合虚拟筛选平台"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02587"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPc7INhjcuOdtwI-2FKA8DOHqA-2BxaTN-2BU5eCj4wE8RC0TLTORQDdNkVLqtacGcg4AvzoMaJOcrRi2NkGyMotIBojnmjLq-2BdGnOE9dSB11-2BUPTVXk85oPmk0dWefSYflToeiP4TZd_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBApsTIGBJA501RAyftmBUg-2FoErvMG7pOWEiTlO47Ph6eJmZmdogLWoYqdQiutkD9mCnMgSp9NgYFnnE7X32SYHiDwn8z99Po0h5RPqAaXXfwOhpfsSE34cNqrnL3onPRMOVKI72Nxq-2FJtnco3ERK4mKo3Au-2BpyKzBTlK3P24WbcTDoyKVdo5rHGdVehbGIZ-2BY-3D"
pub_date: ""
tags: ["virtual-screening", "gpu-acceleration", "drug-discovery", "ligand-docking", "high-throughput-screening"]
ai_relevance: 3
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# UniDock-Pro: A Unified GPU-Accelerated Platform for High-Throughput Structure-Based, Ligand-Based, and Synergistic Hybrid Virtual Screening

**UniDock-Pro：统一的GPU加速高通量基于结构、基于配体和混合虚拟筛选平台**

## 精华总结
UniDock-Pro是一个统一的GPU加速虚拟筛选平台，集成了基于结构、基于配体和混合虚拟筛选模式，通过新颖的混合方法和优化的算法在药物发现中实现了显著的高通量和准确性提升。

**关键词**: 虚拟筛选、GPU加速、混合方法、药物发现、高通量筛选

## 摘要（英文）
The screening of ultralarge chemical libraries requires high-throughput computational tools that can efficiently exploit all available structural and chemical information. We present UniDock-Pro, a unified platform based on the GPU-accelerated Uni-Dock architecture that integrates structure-based virtual screening (SBVS), ligand-based virtual screening (LBVS), and a novel hybrid virtual screening mode. By capitalizing on inter-ligand (batch) parallelism, UniDock-Pro achieves substantial throughput gains, enabling the processing of millions of compounds per day on a single GPU. We significantly enhanced the LBVS methodology by implementing a smooth, Lennard-Jones-like potential optimized for gradient-based search, which replaces the rugged recursive model employed in our previous work. This optimization yields a substantial 2.42-fold improvement in early enrichment (EF1%) over the legacy AutoDock-SS on the DUDE-Z benchmark. The Hybrid mode combines complementary information by integrating receptor- and ligand-derived grid maps on-the-fly during the conformational search, delivering strong early enrichment on DUDE-Z and competitive performance on the more stringent VSDS-vd TrueDecoy benchmark. To understand the mechanisms underlying this synergy, we introduce Force Field Complementarity Analysis (FFCA), a method for quantifying the spatial alignment between receptor and ligand force fields. UniDock-Pro offers a robust, versatile, and highly efficient solution for accelerating drug discovery campaigns across the expansive modern chemical space.

## 摘要（中文）
UniDock-Pro是一个基于GPU加速Uni-Dock架构的统一平台，集成了基于结构的虚拟筛选、基于配体的虚拟筛选和新型混合虚拟筛选模式。通过利用批间并行性，该平台在单个GPU上可日处理数百万化合物。改进的LBVS方法采用优化的Lennard-Jones势函数替代递归模型，在DUDE-Z基准上的早期富集提升了2.42倍。混合模式在构象搜索中结合受体和配体衍生的网格信息，提供强大的筛选性能。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPc7INhjcuOdtwI-2FKA8DOHqA-2BxaTN-2BU5eCj4wE8RC0TLTORQDdNkVLqtacGcg4AvzoMaJOcrRi2NkGyMotIBojnmjLq-2BdGnOE9dSB11-2BUPTVXk85oPmk0dWefSYflToeiP4TZd_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBApsTIGBJA501RAyftmBUg-2FoErvMG7pOWEiTlO47Ph6eJmZmdogLWoYqdQiutkD9mCnMgSp9NgYFnnE7X32SYHiDwn8z99Po0h5RPqAaXXfwOhpfsSE34cNqrnL3onPRMOVKI72Nxq-2FJtnco3ERK4mKo3Au-2BpyKzBTlK3P24WbcTDoyKVdo5rHGdVehbGIZ-2BY-3D)
