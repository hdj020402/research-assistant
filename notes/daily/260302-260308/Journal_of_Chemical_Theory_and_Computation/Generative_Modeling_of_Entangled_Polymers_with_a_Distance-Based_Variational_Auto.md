---
title: "Generative Modeling of Entangled Polymers with a Distance-Based Variational Autoencoder"
title_zh: "使用基于距离的变分自动编码器对纠缠聚合物进行生成建模"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01953"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1bm3Sq14xo-2Fvlh6rSHjrxIsIgwiRHFl9MPm8xRvQaipYTqbt1cjPqH84BEG4H5j3jgJ-2FkdS6PP9nENqhMsWGsWvt6WG3B8-2BrTJH7K10S9X86bls-2B0h1BhTKUCVBKqUi8yUelf_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXdFSUWtQE-2B5skZiI4w23DsDjFiKRTafWDFW-2BURIWLK48hELMYZwg5TyKhaep3ZvIr-2Fg3rx5OSJWbtjGrYxOw2G5aOaAhjXWkCJvi-2FOLo13AY1nNSFyAn5dR8odSze1makfyUyc9lQ0Y7GgC4PUjJnNTWRtOnm5FDyFnu-2F-2BJKNz-2BHD-2BSjTvkWkyiMWUPzb-2FrDfg-3D"
pub_date: ""
tags: ["generative-models", "variational-autoencoder", "polymer-simulation", "molecular-dynamics", "deep-learning"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Generative Modeling of Entangled Polymers with a Distance-Based Variational Autoencoder

**使用基于距离的变分自动编码器对纠缠聚合物进行生成建模**

## 精华总结
本研究开发了一个变分自编码器框架，用于从距离矩阵学习和生成缠绕聚合物的构型，通过结合卷积和注意力层实现结构模式编码。相比纯分子动力学方法，该方法所需的弛豫时间减少了一个数量级，在采样不相关结构时具有计算优势。

**关键词**: 变分自编码器、聚合物、生成模型、分子动力学、深度学习

## 摘要（英文）
We present a variational autoencoder framework for learning and generating configurations of structured polymer globules from distance matrices. We used coarse-grained molecular dynamics to sample polyethylene structures, which we used as the training set for our deep learning model. By combining convolution and attention layers, the model encodes the structural patterns of distance matrices into an organized and rototranslationally invariant latent space of lower dimensionality. The generative capability of the variational autoencoder, coupled with a postprocessing pipeline based on multidimensional scaling and short molecular dynamics, enables the recovery of physically meaningful configurations. The reconstructed and generated samples reproduce key observables, including energy, size, and entanglement, despite minor discrepancies in the raw decoder output. Interestingly, the length of the molecular dynamics relaxation required to generate canonical structures starting from the decoder outputs is 1 order of magnitude smaller than the corresponding relaxation time needed to sample structures using a pure MD approach, suggesting that our method can offer computational advantages in sampling uncorrelated structures.

## 摘要（中文）
我们提出了一种变分自动编码器框架，用于从距离矩阵学习和生成结构化聚合物小球的配置。我们使用粗粒度分子动力学对聚乙烯结构进行采样，并将其用作深度学习模型的训练集。通过结合卷积层和注意层，该模型将距离矩阵的结构模式编码为较低维度的有组织且旋转翻译不变的潜在空间。变分自动编码器的生成能力，再加上基于多维缩放和短分子动力学的后处理管道，可以恢复物理上有意义的配置。重建和生成的样本再现了关键的可观察量，包括能量、大小和纠缠，尽管原始解码器输出中有微小的差异。有趣的是，从解码器输出开始生成规范结构所需的分子动力学弛豫的长度比使用纯MD方法对结构进行采样所需的相应弛豫时间小1个数量级，这表明我们的方法可以在对不相关结构进行采样方面提供计算优势。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1bm3Sq14xo-2Fvlh6rSHjrxIsIgwiRHFl9MPm8xRvQaipYTqbt1cjPqH84BEG4H5j3jgJ-2FkdS6PP9nENqhMsWGsWvt6WG3B8-2BrTJH7K10S9X86bls-2B0h1BhTKUCVBKqUi8yUelf_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXdFSUWtQE-2B5skZiI4w23DsDjFiKRTafWDFW-2BURIWLK48hELMYZwg5TyKhaep3ZvIr-2Fg3rx5OSJWbtjGrYxOw2G5aOaAhjXWkCJvi-2FOLo13AY1nNSFyAn5dR8odSze1makfyUyc9lQ0Y7GgC4PUjJnNTWRtOnm5FDyFnu-2F-2BJKNz-2BHD-2BSjTvkWkyiMWUPzb-2FrDfg-3D)
