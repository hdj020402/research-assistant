---
title: "Following the Committor Flow: A Data-Driven Discovery of Transition Pathways"
title_zh: "跟随承诺函数流：转移路径的数据驱动发现"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.6c00007"
url: "https://app.acspubs.org/e/er?s=1913652004&lid=109587&pci=CACSR000013623915&elqTrackId=61dd119f148f43eb8d86f8310108bd01&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF5B87095763DF70F3ADD6AB06A791F2283DF669D1886211F10624EBC003E655BFD"
pub_date: ""
tags: ["rare-event-sampling", "neural-networks", "molecular-dynamics", "reaction-pathways", "committor"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Following the Committor Flow: A Data-Driven Discovery of Transition Pathways

**跟随承诺函数流：转移路径的数据驱动发现**

## 精华总结
该工作提出了一个迭代框架来推断承诺函数并识别最相关的转移路径，并在多个基准系统上演示了该方法的有效性。

**关键词**: 承诺函数、转移路径、神经网络、分子模拟、罕见事件采样

## 摘要（英文）
The discovery of transition pathways to unravel distinct reaction mechanisms and, in general, rare events that occur in molecular systems is still a challenge. Recent advances have focused on analyzing the transition-path ensemble using the committor probability, widely regarded as the most informative one-dimensional reaction coordinate. Consistency between transition pathways and the committor function is essential for accurate mechanistic insight. In this work, we propose an iterative framework to infer the committor and, subsequently, to identify the most relevant transition pathways. Starting from an initial guess for the transition path, we generate biased sampling, from which we train a neural network to approximate the committor probability. From this learned committor, we extract dominant transition channels as discretized strings lying on isocommittor surfaces. These pathways are then used to enhance sampling and iteratively refine both the committor and transition paths until convergence. The resulting committor enables accurate estimation of the reaction rate constant. We demonstrate the effectiveness of our approach on benchmark systems, including a two-dimensional model potential, peptide conformational transitions, a Diels-Alder reaction, and the reversible folding of the Trp-cage.

## 摘要（中文）
发现转移路径以揭示不同的反应机制，以及分子系统中发生的罕见事件仍然是一个挑战。最近的研究进展集中在使用承诺概率分析转移路径集合，承诺概率被广泛认为是最具信息量的一维反应坐标。转移路径与承诺函数之间的一致性对于准确的机制理解至关重要。在这项工作中，我们提出了一个迭代框架来推断承诺函数，随后识别最相关的转移路径。从初始的转移路径猜测开始，我们生成偏置采样，从中训练神经网络来近似承诺概率。从学到的承诺函数，我们提取位于等承诺表面上的离散化字符串形式的主导转移通道。然后使用这些路径增强采样，并迭代精化承诺函数和转移路径直到收敛。所得的承诺函数能够准确估计反应速率常数。我们在基准系统上演示了我们方法的有效性，包括二维模型势、肽链构象转移、Diels-Alder反应和Trp-cage的可逆折叠。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](https://app.acspubs.org/e/er?s=1913652004&lid=109587&pci=CACSR000013623915&elqTrackId=61dd119f148f43eb8d86f8310108bd01&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF5B87095763DF70F3ADD6AB06A791F2283DF669D1886211F10624EBC003E655BFD)
