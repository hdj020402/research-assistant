---
title: "VFMol: A Discrete Flow Matching Variational Autoencoder for Molecular Graph Generation"
title_zh: "VFMol: 用于分子图生成的离散流匹配变分自动编码器"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c03005"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPw1cSAUW80S4U4hZAL2i-2FBmZiaP5bfa46Vdwhnh955b7NkG1hRFG8ByHx1Y839YbYzpEbiP6OuhgmfvCHFXZZBuQCb6v9-2BaZqbZfGX1Y2e6kg3CbzLx1RGBIzxcdhLmZCNgsy_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBpU59g7iZbF5MtF7FsdepEh-2FaM9I01XVcw4Q8J30NAHRcbjyy1cLD4Cnb-2BjAE7KQOCQIZ6rmT0iPze5Dz1Tt19TBXPeI7yyxMqaCbobZvtrDjXw8PcHGzjze7N0AoieoM9GIPfL1f2qWNtUCyljb6aHDNSUObT5qIX-2BMDeOClBqGLA2m0LPFt6YpNJgEeI0uc-3D"
pub_date: ""
tags: ["molecular-generation", "generative-models", "drug-discovery", "deep-learning", "graph-neural-networks"]
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
本工作提出VFMol框架，将个性化VAE潜在空间建模与离散流匹配的高效逐步采样机制相结合，并引入基于KAN和无分类器引导的轻量级属性引导框架，实现无需辅助属性预测器的条件生成。

**关键词**: 分子图生成、变分自编码器、流匹配、药物发现、条件生成

## 摘要（英文）
Molecular graph generation is a key task in drug discovery, aiming to efficiently identify novel compounds with desired properties. While variational autoencoders (VAEs) excel at latent space modeling and discrete flow matching (DFM) enables efficient continuous-time sampling, existing approaches still face critical limitations. VAE decoders struggle with permutation invariance and suffer from one-shot generation bottlenecks, whereas DFM models often rely on a fixed prior initialization that lacks adaptability to specific molecular structures. To address these issues, we propose VFMol, a novel framework that synergistically integrates personalized VAE latent space modeling with the efficient stepwise sampling mechanism of DFM in the discrete space. Specifically, the encoder learns a posterior distribution tailored to each input graph as the generation starting point, thereby enhancing both structural fidelity and diversity. Moreover, we introduce a lightweight property-guided framework based on KAN and classifier-free guidance, enabling conditional generation without auxiliary property predictors. Experiments on two widely used molecular data sets demonstrate that VFMol achieves state-of-the-art performance in terms of molecular structural quality and property controllability, verifying its generality and effectiveness.

## 摘要（中文）
分子图生成是药物发现中的关键任务，旨在高效地筛选出具有预期性质的新型化合物。尽管变分自编码器（VAEs）在潜在空间建模方面表现出色，而离散流匹配（DFM）则实现了高效的连续时间采样，但现有方法仍面临关键性局限。VAE解码器在排列不变性方面存在困难，并且受限于单次生成的瓶颈；而DFM模型通常依赖于固定的先验初始化，难以适应特定的分子结构。为解决这些问题，我们提出VFMol——一个创新框架，它协同整合了个性化VAE隐空间建模与DFM在离散空间中的高效分步采样机制。具体而言，编码器为每个输入图学习一个定制的后验分布作为生成的起始点，从而同时提升生成结构的保真度和多样性。此外，我们提出了一种基于KAN和无分类器指导的轻量级属性引导框架，能够在无需辅助属性预测器的情况下实现条件生成。在两个广泛使用的分子数据集上的实验表明，VFMol在分子结构质量和性质可控性方面均达到了当前最先进的水平，验证了其通用性和有效性。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPw1cSAUW80S4U4hZAL2i-2FBmZiaP5bfa46Vdwhnh955b7NkG1hRFG8ByHx1Y839YbYzpEbiP6OuhgmfvCHFXZZBuQCb6v9-2BaZqbZfGX1Y2e6kg3CbzLx1RGBIzxcdhLmZCNgsy_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FBpU59g7iZbF5MtF7FsdepEh-2FaM9I01XVcw4Q8J30NAHRcbjyy1cLD4Cnb-2BjAE7KQOCQIZ6rmT0iPze5Dz1Tt19TBXPeI7yyxMqaCbobZvtrDjXw8PcHGzjze7N0AoieoM9GIPfL1f2qWNtUCyljb6aHDNSUObT5qIX-2BMDeOClBqGLA2m0LPFt6YpNJgEeI0uc-3D)
