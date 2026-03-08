---
title: "UniDock-Pro: A Unified GPU-Accelerated Platform for High-Throughput Structure-Based, Ligand-Based, and Synergistic Hybrid Virtual Screening"
title_zh: "UniDock-Pro：用于高通量基于结构、基于配体和协同混合虚拟筛选的统一GPU加速平台"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02587"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPc7INhjcuOdtwI-2FKA8DOHqA-2BxaTN-2BU5eCj4wE8RC0TLTORQDdNkVLqtacGcg4AvzoMaJOcrRi2NkGyMotIBojnmjLq-2BdGnOE9dSB11-2BUPTVXk85oPmk0dWefSYflToeiP4TZd_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBApsTIGBJA501RAyftmBUg-2FoErvMG7pOWEiTlO47Ph6eJmZmdogLWoYqdQiutkD9mCnMgSp9NgYFnnE7X32SYHiDwn8z99Po0h5RPqAaXXfwOhpfsSE34cNqrnL3onPRMOVKI72Nxq-2FJtnco3ERK4mKo3Au-2BpyKzBTlK3P24WbcTDoyKVdo5rHGdVehbGIZ-2BY-3D"
pub_date: ""
tags: ["drug-discovery", "virtual-screening", "gpu-acceleration", "computational-chemistry", "deep-learning"]
ai_relevance: 4
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
UniDock-Pro是基于GPU加速Uni-Dock架构的统一平台，整合结构基虚拟筛选、配体基虚拟筛选和新颖的混合虚拟筛选模式，通过协同整合互补信息，大幅提升虚拟筛选效率和准确性。

**关键词**: 虚拟筛选、GPU加速、药物发现、结构基设计、配体基设计

## 摘要（英文）
The screening of ultralarge chemical libraries requires high-throughput computational tools that can efficiently exploit all available structural and chemical information. We present UniDock-Pro, a unified platform based on the GPU-accelerated Uni-Dock architecture that integrates structure-based virtual screening (SBVS), ligand-based virtual screening (LBVS), and a novel hybrid virtual screening mode. By capitalizing on inter-ligand (batch) parallelism, UniDock-Pro achieves substantial throughput gains, enabling the processing of millions of compounds per day on a single GPU. We significantly enhanced the LBVS methodology by implementing a smooth, Lennard-Jones-like potential optimized for gradient-based search, which replaces the rugged recursive model employed in our previous work. This optimization yields a substantial 2.42-fold improvement in early enrichment (EF1%) over the legacy AutoDock-SS on the DUDE-Z benchmark. The Hybrid mode combines complementary information by integrating receptor- and ligand-derived grid maps on-the-fly during the conformational search, delivering strong early enrichment on DUDE-Z and competitive performance on the more stringent VSDS-vd TrueDecoy benchmark. To understand the mechanisms underlying this synergy, we introduce Force Field Complementarity Analysis (FFCA), a method for quantifying the spatial alignment between receptor and ligand force fields. UniDock-Pro offers a robust, versatile, and highly efficient solution for accelerating drug discovery campaigns across the expansive modern chemical space.

## 摘要（中文）
UniDock-Pro是一个统一的虚拟筛选平台，基于GPU加速的Uni-Dock架构，集成了基于结构(SBVS)、基于配体(LBVS)和新颖的混合虚拟筛选模式。通过利用GPU的批并行计算能力，该平台每天可在单个GPU上处理数百万个化合物。改进的LBVS方法采用优化的Lennard-Jones势函数替代递归模型，在DUDE-Z基准上的早期富集度(EF1%)提高2.42倍。混合模式通过构象搜索期间动态整合受体和配体网格图，实现强大的虚拟筛选性能。引入力场互补性分析(FFCA)方法定量评估受体和配体力场的空间对齐，为药物发现提供高效解决方案。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPc7INhjcuOdtwI-2FKA8DOHqA-2BxaTN-2BU5eCj4wE8RC0TLTORQDdNkVLqtacGcg4AvzoMaJOcrRi2NkGyMotIBojnmjLq-2BdGnOE9dSB11-2BUPTVXk85oPmk0dWefSYflToeiP4TZd_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBApsTIGBJA501RAyftmBUg-2FoErvMG7pOWEiTlO47Ph6eJmZmdogLWoYqdQiutkD9mCnMgSp9NgYFnnE7X32SYHiDwn8z99Po0h5RPqAaXXfwOhpfsSE34cNqrnL3onPRMOVKI72Nxq-2FJtnco3ERK4mKo3Au-2BpyKzBTlK3P24WbcTDoyKVdo5rHGdVehbGIZ-2BY-3D)
