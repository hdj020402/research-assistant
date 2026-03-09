---
title: "Following the Committor Flow: A Data-Driven Discovery of Transition Pathways"
title_zh: "沿着传递子流：基于数据的过渡路径发现"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.6c00007"
url: "https://app.acspubs.org/e/er?s=1913652004&lid=109587&pci=CACSR000013623915&elqTrackId=61dd119f148f43eb8d86f8310108bd01&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF5B87095763DF70F3ADD6AB06A791F2283DF669D1886211F10624EBC003E655BFD"
pub_date: ""
tags: ["rare-event-sampling", "machine-learning", "reaction-pathways", "neural-networks", "molecular-dynamics"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Following the Committor Flow: A Data-Driven Discovery of Transition Pathways

**沿着传递子流：基于数据的过渡路径发现**

## 精华总结
本工作提出了一个迭代框架来推断committor函数，进而识别最相关的过渡路径，并在二维势能模型、肽构象转变、Diels-Alder反应和Trp-cage可逆折叠等基准系统上验证了该方法的有效性。

**关键词**: committor概率、过渡路径、神经网络、反应机制、罕见事件采样

## 摘要（英文）
The discovery of transition pathways to unravel distinct reaction mechanisms and, in general, rare events that occur in molecular systems is still a challenge. Recent advances have focused on analyzing the transition-path ensemble using the committor probability, widely regarded as the most informative one-dimensional reaction coordinate. Consistency between transition pathways and the committor function is essential for accurate mechanistic insight. In this work, we propose an iterative framework to infer the committor and, subsequently, to identify the most relevant transition pathways. Starting from an initial guess for the transition path, we generate biased sampling, from which we train a neural network to approximate the committor probability. From this learned committor, we extract dominant transition channels as discretized strings lying on isocommittor surfaces. These pathways are then used to enhance sampling and iteratively refine both the committor and transition paths until convergence. The resulting committor enables accurate estimation of the reaction rate constant. We demonstrate the effectiveness of our approach on benchmark systems, including a two-dimensional model potential, peptide conformational transitions, a Diels-Alder reaction, and the reversible folding of the Trp-cage.

## 摘要（中文）
发现过渡途径以解开不同的反应机制，以及通常在分子系统中发生的罕见事件仍然是一个挑战。最近的进展集中在使用提交人概率分析过渡路径集合，该概率被广泛认为是信息量最大的一维反应坐标。过渡路径和提交者功能之间的一致性对于准确的机械洞察力至关重要。在这项工作中，我们提出了一个迭代框架来推断提交者，并随后确定最相关的过渡路径。从过渡路径的初始猜测开始，我们生成有偏采样，从中我们训练神经网络以近似提交者概率。从这个学习的提交者中，我们将主要过渡通道提取为位于等提交者表面上的离散字符串。然后，这些路径用于增强采样，并迭代地细化提交者和过渡路径，直到收敛。生成的提交者可以准确估计反应速率常数。我们证明了我们的方法在基准系统上的有效性，包括二维模型电势，肽构象转变，diels-alder反应以及Trp笼的可逆折叠。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](https://app.acspubs.org/e/er?s=1913652004&lid=109587&pci=CACSR000013623915&elqTrackId=61dd119f148f43eb8d86f8310108bd01&elq=51f4713da496490ea94be1416e307abc&elqaid=32172&elqat=1&elqak=8AF5B87095763DF70F3ADD6AB06A791F2283DF669D1886211F10624EBC003E655BFD)
