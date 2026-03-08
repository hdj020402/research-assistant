---
title: "Generative Modeling of Entangled Polymers with a Distance-Based Variational Autoencoder"
title_zh: "基于距离的变分自编码器生成纠缠聚合物结构"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01953"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1bm3Sq14xo-2Fvlh6rSHjrxIsIgwiRHFl9MPm8xRvQaipYTqbt1cjPqH84BEG4H5j3jgJ-2FkdS6PP9nENqhMsWGsWvt6WG3B8-2BrTJH7K10S9X86bls-2B0h1BhTKUCVBKqUi8yUelf_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXdFSUWtQE-2B5skZiI4w23DsDjFiKRTafWDFW-2BURIWLK48hELMYZwg5TyKhaep3ZvIr-2Fg3rx5OSJWbtjGrYxOw2G5aOaAhjXWkCJvi-2FOLo13AY1nNSFyAn5dR8odSze1makfyUyc9lQ0Y7GgC4PUjJnNTWRtOnm5FDyFnu-2F-2BJKNz-2BHD-2BSjTvkWkyiMWUPzb-2FrDfg-3D"
pub_date: ""
tags: ["generative-models", "polymer-simulation", "deep-learning", "molecular-dynamics", "structure-generation"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Generative Modeling of Entangled Polymers with a Distance-Based Variational Autoencoder

**基于距离的变分自编码器生成纠缠聚合物结构**

## 精华总结
将变分自编码器与分子动力学结合，从距离矩阵生成纠缠聚合物配置，使分子动力学弛豫时间缩短一个数量级，显著提高结构采样效率。

**关键词**: 变分自编码器、聚合物结构、分子动力学、深度学习、生成模型

## 摘要（英文）
We present a variational autoencoder framework for learning and generating configurations of structured polymer globules from distance matrices. We used coarse-grained molecular dynamics to sample polyethylene structures, which we used as the training set for our deep learning model. By combining convolution and attention layers, the model encodes the structural patterns of distance matrices into an organized and rototranslationally invariant latent space of lower dimensionality. The generative capability of the variational autoencoder, coupled with a postprocessing pipeline based on multidimensional scaling and short molecular dynamics, enables the recovery of physically meaningful configurations. The reconstructed and generated samples reproduce key observables, including energy, size, and entanglement, despite minor discrepancies in the raw decoder output. Interestingly, the length of the molecular dynamics relaxation required to generate canonical structures starting from the decoder outputs is 1 order of magnitude smaller than the corresponding relaxation time needed to sample structures using a pure MD approach, suggesting that our method can offer computational advantages in sampling uncorrelated structures.

## 摘要（中文）
本研究提出了一个变分自编码器框架，用于从距离矩阵学习和生成结构化聚合物球体配置。利用粗粒化分子动力学采样聚乙烯结构作为训练集，结合卷积和注意力层的深度学习模型将距离矩阵的结构特征编码到低维、旋转平移不变的隐空间。生成模型结合多维缩放和短分子动力学后处理，能重现物理意义的配置。重构和生成样本再现了能量、尺寸和纠缠等关键可观测量。解码器输出的分子动力学弛豫时间比纯MD采样方法短一个数量级，说明该方法在非相关结构采样中具有计算优势。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1bm3Sq14xo-2Fvlh6rSHjrxIsIgwiRHFl9MPm8xRvQaipYTqbt1cjPqH84BEG4H5j3jgJ-2FkdS6PP9nENqhMsWGsWvt6WG3B8-2BrTJH7K10S9X86bls-2B0h1BhTKUCVBKqUi8yUelf_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXdFSUWtQE-2B5skZiI4w23DsDjFiKRTafWDFW-2BURIWLK48hELMYZwg5TyKhaep3ZvIr-2Fg3rx5OSJWbtjGrYxOw2G5aOaAhjXWkCJvi-2FOLo13AY1nNSFyAn5dR8odSze1makfyUyc9lQ0Y7GgC4PUjJnNTWRtOnm5FDyFnu-2F-2BJKNz-2BHD-2BSjTvkWkyiMWUPzb-2FrDfg-3D)
