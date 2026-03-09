---
title: "UniDock-Pro: A Unified GPU-Accelerated Platform for High-Throughput Structure-Based, Ligand-Based, and Synergistic Hybrid Virtual Screening"
title_zh: "Unidock-pro: 一个统一的GPU加速平台，用于基于结构、基于配体和协同的混合虚拟筛选"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02587"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPc7INhjcuOdtwI-2FKA8DOHqA-2BxaTN-2BU5eCj4wE8RC0TLTORQDdNkVLqtacGcg4AvzoMaJOcrRi2NkGyMotIBojnmjLq-2BdGnOE9dSB11-2BUPTVXk85oPmk0dWefSYflToeiP4TZd_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBApsTIGBJA501RAyftmBUg-2FoErvMG7pOWEiTlO47Ph6eJmZmdogLWoYqdQiutkD9mCnMgSp9NgYFnnE7X32SYHiDwn8z99Po0h5RPqAaXXfwOhpfsSE34cNqrnL3onPRMOVKI72Nxq-2FJtnco3ERK4mKo3Au-2BpyKzBTlK3P24WbcTDoyKVdo5rHGdVehbGIZ-2BY-3D"
pub_date: ""
tags: ["virtual-screening", "gpu-acceleration", "drug-discovery", "molecular-docking", "high-throughput-screening"]
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
UniDock-Pro是一个基于GPU加速的统一平台，整合了基于结构的虚拟筛选、基于配体的虚拟筛选和新颖的混合虚拟筛选模式，能够在单个GPU上每天处理数百万个化合物，在DUDE-Z基准上实现了2.42倍的早期富集改进。

**关键词**: 虚拟筛选、GPU加速、配体对接、药物发现、混合筛选模式

## 摘要（英文）
The screening of ultralarge chemical libraries requires high-throughput computational tools that can efficiently exploit all available structural and chemical information. We present UniDock-Pro, a unified platform based on the GPU-accelerated Uni-Dock architecture that integrates structure-based virtual screening (SBVS), ligand-based virtual screening (LBVS), and a novel hybrid virtual screening mode. By capitalizing on inter-ligand (batch) parallelism, UniDock-Pro achieves substantial throughput gains, enabling the processing of millions of compounds per day on a single GPU. We significantly enhanced the LBVS methodology by implementing a smooth, Lennard-Jones-like potential optimized for gradient-based search, which replaces the rugged recursive model employed in our previous work. This optimization yields a substantial 2.42-fold improvement in early enrichment (EF1%) over the legacy AutoDock-SS on the DUDE-Z benchmark. The Hybrid mode combines complementary information by integrating receptor- and ligand-derived grid maps on-the-fly during the conformational search, delivering strong early enrichment on DUDE-Z and competitive performance on the more stringent VSDS-vd TrueDecoy benchmark. To understand the mechanisms underlying this synergy, we introduce Force Field Complementarity Analysis (FFCA), a method for quantifying the spatial alignment between receptor and ligand force fields. UniDock-Pro offers a robust, versatile, and highly efficient solution for accelerating drug discovery campaigns across the expansive modern chemical space.

## 摘要（中文）
筛选超大型化学文库需要高通量计算工具，这些工具可以有效地利用所有可用的结构和化学信息。我们介绍了unidock-pro，这是一个基于GPU加速的uni-dock体系结构的统一平台，该平台集成了基于结构的虚拟筛选 (SBVS)，基于配体的虚拟筛选 (LBVS) 和新颖的混合虚拟筛选模式。通过利用配体间 (批处理) 并行性，unidock-pro实现了可观的吞吐量提升，使每天能够在单个GPU上处理数百万种化合物。我们通过实施针对基于梯度的搜索进行优化的平滑，类似lennard-jones的电势来显着增强LBVS方法，该电势取代了我们先前工作中采用的坚固递归模型。与dude-z基准上的传统autodock-ss相比，这种优化在早期富集 (EF1 %) 方面产生了2.42倍的实质性改进。混合模式通过在构象搜索期间即时整合受体和配体衍生的网格图来结合互补信息，在dude-z上提供强大的早期富集，并在更严格的vsds-vd TrueDecoy基准上提供竞争性能。为了理解这种协同作用的机制，我们引入力场互补分析 (FFCA)，一种用于量化受体和配体力场之间的空间对齐的方法。Unidock-pro提供了一个强大的，多功能的，高效的解决方案，加速药物发现活动在广阔的现代化学空间。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPc7INhjcuOdtwI-2FKA8DOHqA-2BxaTN-2BU5eCj4wE8RC0TLTORQDdNkVLqtacGcg4AvzoMaJOcrRi2NkGyMotIBojnmjLq-2BdGnOE9dSB11-2BUPTVXk85oPmk0dWefSYflToeiP4TZd_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBApsTIGBJA501RAyftmBUg-2FoErvMG7pOWEiTlO47Ph6eJmZmdogLWoYqdQiutkD9mCnMgSp9NgYFnnE7X32SYHiDwn8z99Po0h5RPqAaXXfwOhpfsSE34cNqrnL3onPRMOVKI72Nxq-2FJtnco3ERK4mKo3Au-2BpyKzBTlK3P24WbcTDoyKVdo5rHGdVehbGIZ-2BY-3D)
