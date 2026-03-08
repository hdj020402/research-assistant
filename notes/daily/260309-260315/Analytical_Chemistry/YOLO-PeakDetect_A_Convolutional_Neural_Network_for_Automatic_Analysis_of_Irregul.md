---
title: "YOLO-PeakDetect: A Convolutional Neural Network for Automatic Analysis of Irregular Bands in Gel Electrophoresis"
title_zh: "YOLO-PeakDetect：用于凝胶电泳不规则条纹自动分析的卷积神经网络"
journal: "Analytical Chemistry"
doi: "10.1021/acs.analchem.5c07582"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6m9dwOKKpz9-2BWBhH0scpkFDBkm7wt3-2Fa75mkgkhpVZ57diHUZR0VrOWkI2Roc-2FsYRaNnQ2AjCtZZuh9Czqy6qVa3944EfXwH-2FJe55nA19OyfijzCDH-2BBXRKx2PQG1Z8RYF-2BigFpPQS8vs1-2B5T6UxMvZ6-Z_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjGwpEj2H7owzqYEdyo186pK6iN5aTK8WBkO-2Ff68T8E22z9STS-2Fx4ywuM0zf8a5pgvf-2BrLWcw8z0b1lwFB4isABDWaw-2BVB4Y7oRGRzC-2BjQXS3PgLygwiFusBpOUBUsy9YFCbob21IeP-2BSXDFQ-2F7Jr9LSjRvHhWJzUTGFuchtg6x3xRM-2BWAMMkkDwF-2BKvaNZWPc0N4PliHj7iyAPr-2BxdPxi1aH2CmwV9vV3MHHuBoIWo7c-3D"
pub_date: ""
tags: ["deep-learning", "image-recognition", "gel-electrophoresis", "biopharmaceutical-analysis", "automated-detection"]
ai_relevance: 5
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# YOLO-PeakDetect: A Convolutional Neural Network for Automatic Analysis of Irregular Bands in Gel Electrophoresis

**YOLO-PeakDetect：用于凝胶电泳不规则条纹自动分析的卷积神经网络**

## 精华总结
基于YOLO网络架构开发YOLO-PeakDetect卷积神经网络，为凝胶电泳中病毒载体聚集体、单克隆抗体沉淀和蛋白质条纹提供可靠智能的检测方案。

**关键词**: 卷积神经网络、凝胶电泳、YOLO、生物制药、自动检测

## 摘要（英文）
Gel electrophoresis (GE) is a critical tool in the fields of molecular biology and biopharmaceuticals. However, the current analysis software requires extensive manual adjustments and cannot accurately determinate particle-like bands of virus vector aggregates and monoclonal antibody (mAb) or protein precipitates in GE. Herein, we developed a convolutional neural network of YOLO-PeakDetect based on the You-only look-once (YOLO) network architecture. Comparative results demonstrate that on the simulated data set, the YOLO-PeakDetect network attains the average precision 50-95 (AP50_95) of 0.9717, which is remarkably superior to those obtained by the traditional algorithm and the existing CNN-based peak detection model. In the experimental data set evaluated against manually precisely annotated GE peak profiles, YOLO-PeakDetect outperforms the traditional algorithm for both single peaks and overlapping peaks. Meanwhile, in GE experiments employing three standard proteins, the proposed network elevates the average linear correlation coefficient from 0.9883 (achieved by ImageJ) to 0.9952. Particularly, the network could detect the aggregate ratio of particle-like adeno-associated virus (AAV) band in the sample well, full and empty AAV capsid from the crescent-like vector bands, and the precipitate ratio of particle-like bands of instable mAb accumulation. All the data showcased that the network model achieves significant improvements in the accuracy, noise resistance, and automation level of irregular band detection, providing a reliable and intelligent solution for particle-like bands of virus vector aggregates and instable mAb precipitates as well as regular bands of proteins in GE.

## 摘要（中文）
凝胶电泳是分子生物学和生物制药领域的关键工具。本研究基于You-Only-Look-Once (YOLO)网络架构开发了YOLO-PeakDetect卷积神经网络，用于自动检测病毒载体聚集体、单克隆抗体或蛋白质沉淀产生的不规则条纹。在模拟数据集上，该网络平均精度达0.9717，远优于传统算法和现有CNN方法。在实验数据集上，YOLO-PeakDetect在单个和重叠峰值检测中均优于ImageJ，将线性相关系数从0.9883提升至0.9952。该网络可准确检测AAV聚集体比率、完全和空心AAV囊壳以及不稳定mAb沉淀比率。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6m9dwOKKpz9-2BWBhH0scpkFDBkm7wt3-2Fa75mkgkhpVZ57diHUZR0VrOWkI2Roc-2FsYRaNnQ2AjCtZZuh9Czqy6qVa3944EfXwH-2FJe55nA19OyfijzCDH-2BBXRKx2PQG1Z8RYF-2BigFpPQS8vs1-2B5T6UxMvZ6-Z_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjGwpEj2H7owzqYEdyo186pK6iN5aTK8WBkO-2Ff68T8E22z9STS-2Fx4ywuM0zf8a5pgvf-2BrLWcw8z0b1lwFB4isABDWaw-2BVB4Y7oRGRzC-2BjQXS3PgLygwiFusBpOUBUsy9YFCbob21IeP-2BSXDFQ-2F7Jr9LSjRvHhWJzUTGFuchtg6x3xRM-2BWAMMkkDwF-2BKvaNZWPc0N4PliHj7iyAPr-2BxdPxi1aH2CmwV9vV3MHHuBoIWo7c-3D)
