---
title: "ChemTorch: A Deep Learning Framework for Benchmarking and Developing Chemical Reaction Property Prediction Models"
title_zh: "ChemTorch: 用于基准测试和开发化学反应性质预测模型的深度学习框架"
journal: "Journal of Chemical Information and Modeling"
doi: "10.1021/acs.jcim.5c02645"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPsMN1Rr-2FUsi7yOgdki9aZdcIj-2BaOVuqZyDIADiRFPYzUzZxtfwEyNSs4bFMQTWi3XZQjjNRPvAAw9yLZmp6t-2B-2Ff-2B0s2U3ftsofyffVQaG774l7rzf-2BGWrObDQzcggoFmj9DUU_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FA0zTu5T6MYzl65JxGVTTnSjaKCR0XDZTUfEOQSqWy8Ie8pAsH-2FXOeh40QA-2BaY7x7lfOK869DNeByxdGXlMCmU1BFL-2FIlLRWLeIwqt3AOTQdlnTe21B1DPQ-2B4aQMn6OdpBoZzKR8IOnUibVSNWygw0xZO6K97b-2BLLOWruCj4O9ghULTWx6VliMQD0qJspjR1R8-3D"
pub_date: ""
tags: ["deep-learning", "chemical-reactions", "benchmark-framework", "molecular-modeling", "computational-chemistry"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# ChemTorch: A Deep Learning Framework for Benchmarking and Developing Chemical Reaction Property Prediction Models

**ChemTorch: 用于基准测试和开发化学反应性质预测模型的深度学习框架**

## 精华总结
本工作介绍了ChemTorch，一个开源框架，通过模块化管道、标准化配置和内置数据分割器来简化模型开发、实验、超参数调整和基准测试，用于化学反应建模的分布内和分布外评估。

**关键词**: 深度学习、化学反应预测、基准测试框架、机器学习模型、分子表示

## 摘要（英文）
Modeling of chemical reactions is essential for understanding kinetic mechanisms and predicting possible outcomes of reacting systems. Quantum mechanical calculations are accurate but often prohibitively expensive. Deep learning has emerged as a faster alternative, but progress is slowed by a fragmented software ecosystem that hinders reuse, fair comparison, and reproducibility. We present ChemTorch, an open-source framework that streamlines model development, experimentation, hyperparameter tuning, and benchmarking through modular pipelines, standardized configuration, and built-in data splitters for in- and out-of-distribution evaluation. We envision ChemTorch as a foundation for community-driven method development and reproducible benchmarking in chemical reaction modeling. As a first step toward unified benchmarks, we compare four representative modalities for barrier-height prediction on the RDB7 data set, including fingerprint-, sequence-, graph-, and 3D-based approaches. Our results highlight clear advantages of structurally informed models and sharp performance drops under out-of-distribution conditions, highlighting the importance of rigorous benchmarking.

## 摘要（中文）
化学反应的建模对于理解反应动力学机制和预测反应体系的可能结果至关重要。量子力学计算虽然精确，但往往成本高昂，难以承受。深度学习已成为一种更快的替代方案，但其进展却因软件生态系统的碎片化而受阻，这不利于代码重用、公平对比和结果可复现性。我们提出了ChemTorch，这是一个开源框架，通过模块化流水线、标准化配置以及内置的训练集/测试集划分工具，简化了模型开发、实验、超参数调优和基准测试流程，支持分布内和分布外评估。我们设想ChemTorch将成为一个以社区驱动的方法开发和化学反应建模中可复现基准测试为基础的平台。作为迈向统一基准的第一步，我们在RDB7数据集上比较了四种具有代表性的能垒预测模态，包括基于指纹、序列、图和三维结构的方法。我们的研究结果凸显了基于结构信息的模型的显著优势，以及在分布外场景下性能的急剧下降，这进一步表明了严格基准测试的重要性。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6qwd-2BbfgJamG4wIcrwJFnPsMN1Rr-2FUsi7yOgdki9aZdcIj-2BaOVuqZyDIADiRFPYzUzZxtfwEyNSs4bFMQTWi3XZQjjNRPvAAw9yLZmp6t-2B-2Ff-2B0s2U3ftsofyffVQaG774l7rzf-2BGWrObDQzcggoFmj9DUU_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjhXgm129QW7OjPkMVv5vigIMEuG-2FfF497eI2FviJGe-2FA0zTu5T6MYzl65JxGVTTnSjaKCR0XDZTUfEOQSqWy8Ie8pAsH-2FXOeh40QA-2BaY7x7lfOK869DNeByxdGXlMCmU1BFL-2FIlLRWLeIwqt3AOTQdlnTe21B1DPQ-2B4aQMn6OdpBoZzKR8IOnUibVSNWygw0xZO6K97b-2BLLOWruCj4O9ghULTWx6VliMQD0qJspjR1R8-3D)
