---
title: "VFMol: A Discrete Flow Matching Variational Autoencoder for Molecular Graph Generation"
title_zh: "VFMol: 用于分子图生成的离散流匹配变分自动编码器"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c03005"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPw1cSAUW80S4U4hZAL2i-2FBmZiaP5bfa46Vdwhnh955b7NkG1hRFG8ByHx1Y839YbYzpEbiP6OuhgmfvCHFXZZBuQCb6v9-2BaZqbZfGX1Y2e6kg3CbzLx1RGBIzxcdhLmZCNgsy_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBpU59g7iZbF5MtF7FsdepEh-2FaM9I01XVcw4Q8J30NAHRcbjyy1cLD4Cnb-2BjAE7KQOCQIZ6rmT0iPze5Dz1Tt19TBXPeI7yyxMqaCbobZvtrDjXw8PcHGzjze7N0AoieoM9GIPfL1f2qWNtUCyljb6aHDNSUObT5qIX-2BMDeOClBqGLA2m0LPFt6YpNJgEeI0uc-3D"
pub_date: ""
tags: ["molecular-generation", "variational-autoencoder", "flow-matching", "deep-learning", "drug-discovery"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# VFMol: A Discrete Flow Matching Variational Autoencoder for Molecular Graph Generation

**VFMol: 用于分子图生成的离散流匹配变分自动编码器**

## 精华总结
本工作提出VFMol框架，创新性地结合了个性化VAE隐空间建模与离散流匹配的高效采样机制，引入基于KAN和无分类器引导的轻量级性质引导框架，实现了无需辅助性质预测器的条件生成。

**关键词**: 分子图生成、变分自编码器、离散流匹配、药物发现、条件生成

## 摘要（英文）
Molecular graph generation is a key task in drug discovery, aiming to efficiently identify novel compounds with desired properties. While variational autoencoders (VAEs) excel at latent space modeling and discrete flow matching (DFM) enables efficient continuous-time sampling, existing approaches still face critical limitations. VAE decoders struggle with permutation invariance and suffer from one-shot generation bottlenecks, whereas DFM models often rely on a fixed prior initialization that lacks adaptability to specific molecular structures. To address these issues, we propose VFMol, a novel framework that synergistically integrates personalized VAE latent space modeling with the efficient stepwise sampling mechanism of DFM in the discrete space. Specifically, the encoder learns a posterior distribution tailored to each input graph as the generation starting point, thereby enhancing both structural fidelity and diversity. Moreover, we introduce a lightweight property-guided framework based on KAN and classifier-free guidance, enabling conditional generation without auxiliary property predictors. Experiments on two widely used molecular data sets demonstrate that VFMol achieves state-of-the-art performance in terms of molecular structural quality and property controllability, verifying its generality and effectiveness.

## 摘要（中文）
分子图生成是药物发现中的一项关键任务，旨在有效地识别具有所需特性的新型化合物。虽然变分自编码器 (vae) 在潜在空间建模和离散流匹配 (DFM) 方面表现出色，但可以实现高效的连续时间采样，但现有方法仍然面临严重的局限性。VAE解码器在置换不变性方面苦苦挣扎，并遭受一次性生成瓶颈的困扰，而DFM模型通常依赖于固定的先验初始化，该初始化缺乏对特定分子结构的适应性。为了解决这些问题，我们提出了VFMol，这是一种新颖的框架，可将个性化的VAE潜在空间建模与离散空间中DFM的高效逐步采样机制协同集成。具体地，编码器学习针对每个输入图定制的后验分布作为生成起点，从而增强结构保真度和多样性。此外，我们引入了一个基于KAN和无分类器指导的轻量级属性指导框架，从而可以在没有辅助属性预测器的情况下进行条件生成。在两个广泛使用的分子数据集上的实验表明，VFMol在分子结构质量和性质可控性方面达到了最先进的性能，验证了其通用性和有效性。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPw1cSAUW80S4U4hZAL2i-2FBmZiaP5bfa46Vdwhnh955b7NkG1hRFG8ByHx1Y839YbYzpEbiP6OuhgmfvCHFXZZBuQCb6v9-2BaZqbZfGX1Y2e6kg3CbzLx1RGBIzxcdhLmZCNgsy_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBpU59g7iZbF5MtF7FsdepEh-2FaM9I01XVcw4Q8J30NAHRcbjyy1cLD4Cnb-2BjAE7KQOCQIZ6rmT0iPze5Dz1Tt19TBXPeI7yyxMqaCbobZvtrDjXw8PcHGzjze7N0AoieoM9GIPfL1f2qWNtUCyljb6aHDNSUObT5qIX-2BMDeOClBqGLA2m0LPFt6YpNJgEeI0uc-3D)
