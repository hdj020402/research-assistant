---
title: "YOLO-PeakDetect: A Convolutional Neural Network for Automatic Analysis of Irregular Bands in Gel Electrophoresis"
title_zh: "YOLO-PeakDetect：用于凝胶电泳中不规则条带自动分析的卷积神经网络"
journal: "Analytical Chemistry"
doi: "10.1021/acs.analchem.5c07582"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6m9dwOKKpz9-2BWBhH0scpkFDBkm7wt3-2Fa75mkgkhpVZ57diHUZR0VrOWkI2Roc-2FsYRaNnQ2AjCtZZuh9Czqy6qVa3944EfXwH-2FJe55nA19OyfijzCDH-2BBXRKx2PQG1Z8RYF-2BigFpPQS8vs1-2B5T6UxMvZ6-Z_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjGwpEj2H7owzqYEdyo186pK6iN5aTK8WBkO-2Ff68T8E22z9STS-2Fx4ywuM0zf8a5pgvf-2BrLWcw8z0b1lwFB4isABDWaw-2BVB4Y7oRGRzC-2BjQXS3PgLygwiFusBpOUBUsy9YFCbob21IeP-2BSXDFQ-2F7Jr9LSjRvHhWJzUTGFuchtg6x3xRM-2BWAMMkkDwF-2BKvaNZWPc0N4PliHj7iyAPr-2BxdPxi1aH2CmwV9vV3MHHuBoIWo7c-3D"
pub_date: ""
tags: ["deep-learning", "object-detection", "analytical-chemistry", "image-analysis", "biopharmaceuticals"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# YOLO-PeakDetect: A Convolutional Neural Network for Automatic Analysis of Irregular Bands in Gel Electrophoresis

**YOLO-PeakDetect：用于凝胶电泳中不规则条带自动分析的卷积神经网络**

## 精华总结
开发了基于YOLO架构的卷积神经网络YOLO-PeakDetect，用于凝胶电泳中不规则条带的自动检测，对病毒载体聚集体、单克隆抗体沉淀和蛋白质条带的检测精度显著提高。

**关键词**: 凝胶电泳、卷积神经网络、YOLO架构、峰值检测、生物制药分析

## 摘要（英文）
Gel electrophoresis (GE) is a critical tool in the fields of molecular biology and biopharmaceuticals. However, the current analysis software requires extensive manual adjustments and cannot accurately determinate particle-like bands of virus vector aggregates and monoclonal antibody (mAb) or protein precipitates in GE. Herein, we developed a convolutional neural network of YOLO-PeakDetect based on the You-only look-once (YOLO) network architecture. Comparative results demonstrate that on the simulated data set, the YOLO-PeakDetect network attains the average precision 50-95 (AP50_95) of 0.9717, which is remarkably superior to those obtained by the traditional algorithm and the existing CNN-based peak detection model. In the experimental data set evaluated against manually precisely annotated GE peak profiles, YOLO-PeakDetect outperforms the traditional algorithm for both single peaks and overlapping peaks. Meanwhile, in GE experiments employing three standard proteins, the proposed network elevates the average linear correlation coefficient from 0.9883 (achieved by ImageJ) to 0.9952. Particularly, the network could detect the aggregate ratio of particle-like adeno-associated virus (AAV) band in the sample well, full and empty AAV capsid from the crescent-like vector bands, and the precipitate ratio of particle-like bands of instable mAb accumulation. All the data showcased that the network model achieves significant improvements in the accuracy, noise resistance, and automation level of irregular band detection, providing a reliable and intelligent solution for particle-like bands of virus vector aggregates and instable mAb precipitates as well as regular bands of proteins in GE.

## 摘要（中文）
凝胶电泳 (GE) 是分子生物学和生物制药领域的重要工具。然而，目前的分析软件需要大量的手动调整，并且不能准确地确定病毒载体聚集体和单克隆抗体 (mAb) 或GE中的蛋白质沉淀物的颗粒样条带。在此，我们基于YOLO网络架构开发了yolo-peakdetect的卷积神经网络。比较结果表明，在模拟数据集上，yolo-peakdetect网络达到0.9717的平均精度50-95 (AP50_95)，明显优于传统算法和现有的基于CNN的峰值检测模型。在针对手动精确注释的GE峰轮廓评估的实验数据集中，yolo-peakdetect在单峰和重叠峰方面均优于传统算法。同时，在使用三种标准蛋白质的GE实验中，所提出的网络将平均线性相关系数从0.9883 (通过ImageJ实现) 提高到0.9952。特别是，该网络可以检测样品孔中颗粒样腺相关病毒 (AAV) 带的聚集率，新月状载体带的完整和空AAV衣壳，以及不稳定mAb积累的颗粒样带的沉淀率。所有数据表明，网络模型在不规则条带检测的准确性，抗噪性和自动化水平方面取得了显着改善，为病毒载体聚集体和不稳定的mAb沉淀物的颗粒样条带以及GE中蛋白质的规则条带提供了可靠且智能的解决方案。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6m9dwOKKpz9-2BWBhH0scpkFDBkm7wt3-2Fa75mkgkhpVZ57diHUZR0VrOWkI2Roc-2FsYRaNnQ2AjCtZZuh9Czqy6qVa3944EfXwH-2FJe55nA19OyfijzCDH-2BBXRKx2PQG1Z8RYF-2BigFpPQS8vs1-2B5T6UxMvZ6-Z_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjGwpEj2H7owzqYEdyo186pK6iN5aTK8WBkO-2Ff68T8E22z9STS-2Fx4ywuM0zf8a5pgvf-2BrLWcw8z0b1lwFB4isABDWaw-2BVB4Y7oRGRzC-2BjQXS3PgLygwiFusBpOUBUsy9YFCbob21IeP-2BSXDFQ-2F7Jr9LSjRvHhWJzUTGFuchtg6x3xRM-2BWAMMkkDwF-2BKvaNZWPc0N4PliHj7iyAPr-2BxdPxi1aH2CmwV9vV3MHHuBoIWo7c-3D)
