---
title: "Generative Modeling of Entangled Polymers with a Distance-Based Variational Autoencoder"
title_zh: "基于距离矩阵的变分自编码器生成缠结聚合物模型"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01953"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1bm3Sq14xo-2Fvlh6rSHjrxIsIgwiRHFl9MPm8xRvQaipYTqbt1cjPqH84BEG4H5j3jgJ-2FkdS6PP9nENqhMsWGsWvt6WG3B8-2BrTJH7K10S9X86bls-2B0h1BhTKUCVBKqUi8yUelf_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXdFSUWtQE-2B5skZiI4w23DsDjFiKRTafWDFW-2BURIWLK48hELMYZwg5TyKhaep3ZvIr-2Fg3rx5OSJWbtjGrYxOw2G5aOaAhjXWkCJvi-2FOLo13AY1nNSFyAn5dR8odSze1makfyUyc9lQ0Y7GgC4PUjJnNTWRtOnm5FDyFnu-2F-2BJKNz-2BHD-2BSjTvkWkyiMWUPzb-2FrDfg-3D"
pub_date: ""
tags: ["generative-models", "polymer-simulation", "variational-autoencoder", "deep-learning", "molecular-dynamics"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Generative Modeling of Entangled Polymers with a Distance-Based Variational Autoencoder

**基于距离矩阵的变分自编码器生成缠结聚合物模型**

## 精华总结
基于距离矩阵的变分自编码器框架可将分子动力学弛豫时间减少一个数量级，在采样不相关聚合物构型时具有显著的计算优势。

**关键词**: 变分自编码器、聚合物、分子动力学、生成模型、深度学习

## 摘要（英文）
We present a variational autoencoder framework for learning and generating configurations of structured polymer globules from distance matrices. We used coarse-grained molecular dynamics to sample polyethylene structures, which we used as the training set for our deep learning model. By combining convolution and attention layers, the model encodes the structural patterns of distance matrices into an organized and rototranslationally invariant latent space of lower dimensionality. The generative capability of the variational autoencoder, coupled with a postprocessing pipeline based on multidimensional scaling and short molecular dynamics, enables the recovery of physically meaningful configurations. The reconstructed and generated samples reproduce key observables, including energy, size, and entanglement, despite minor discrepancies in the raw decoder output. Interestingly, the length of the molecular dynamics relaxation required to generate canonical structures starting from the decoder outputs is 1 order of magnitude smaller than the corresponding relaxation time needed to sample structures using a pure MD approach, suggesting that our method can offer computational advantages in sampling uncorrelated structures.

## 摘要（中文）
本研究提出了一种变分自编码器框架，用于从距离矩阵学习和生成结构化聚合物球体的构型。采用粗粒化分子动力学采样聚乙烯结构作为训练集，通过结合卷积和注意力层，将距离矩阵的结构模式编码到低维的旋转平移不变隐空间。该生成模型结合多维缩放和短时分子动力学后处理管道，能够恢复物理上有意义的构型，重构和生成样本再现了能量、尺寸和缠结等关键观测量。分子动力学弛豫时间比纯MD方法小一个数量级，表明该方法在采样不相关结构时具有计算优势。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1bm3Sq14xo-2Fvlh6rSHjrxIsIgwiRHFl9MPm8xRvQaipYTqbt1cjPqH84BEG4H5j3jgJ-2FkdS6PP9nENqhMsWGsWvt6WG3B8-2BrTJH7K10S9X86bls-2B0h1BhTKUCVBKqUi8yUelf_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXdFSUWtQE-2B5skZiI4w23DsDjFiKRTafWDFW-2BURIWLK48hELMYZwg5TyKhaep3ZvIr-2Fg3rx5OSJWbtjGrYxOw2G5aOaAhjXWkCJvi-2FOLo13AY1nNSFyAn5dR8odSze1makfyUyc9lQ0Y7GgC4PUjJnNTWRtOnm5FDyFnu-2F-2BJKNz-2BHD-2BSjTvkWkyiMWUPzb-2FrDfg-3D)
