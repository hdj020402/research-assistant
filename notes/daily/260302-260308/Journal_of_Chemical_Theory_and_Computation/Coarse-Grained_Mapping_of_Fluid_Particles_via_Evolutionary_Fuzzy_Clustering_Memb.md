---
title: "Coarse-Grained Mapping of Fluid Particles via Evolutionary Fuzzy Clustering: Membership-Evolution Term as a Pressure Correction Mechanism"
title_zh: "通过进化模糊聚类对流体颗粒进行粗粒度映射: 隶属进化项作为压力校正机制"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01867"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1US8EKTjTxS2OmW4-2B0mjRUPqGGQS4yxDw1yTZZuM2GpRoGGxPIriYdNQ9eYXef9zjTCW389G7b9f3SY72tEt4hHMf3t4SmRRoXv46erLP4-2B1nY41iFExQkGYoefXrQ59rUZDI_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXc2RYNe3UlLS9pq-2BEMdtMXEs8oRUs7Pon-2B4zQV6XjgAKbCQnIIBQGtKdNzKY6cmS-2ByXXEJXkbQjUc4mk20adAPQp10uYTWoNl0WXsM1JbZyT0EUjKFBxAuvilOuFjtpRYqSN3ZbA57sw8EI42QvcaiIhVknC0qbYhcZkamYgi21cj6RuuGjLEcH8-2Bjz2BdaC8Q-3D"
pub_date: ""
tags: ["coarse-graining", "fuzzy-clustering", "molecular-dynamics", "force-matching"]
ai_relevance: 3
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Coarse-Grained Mapping of Fluid Particles via Evolutionary Fuzzy Clustering: Membership-Evolution Term as a Pressure Correction Mechanism

**通过进化模糊聚类对流体颗粒进行粗粒度映射: 隶属进化项作为压力校正机制**

## 精华总结
提出了一种熵正则化模糊聚类方法用于流体粒子的粗粒化映射，通过时间平滑约束控制成员度演化；发现成员度演化项在力匹配框架中提供斥力贡献，可有效修正粗粒化动力学模拟中的系统压力。

**关键词**: 粗粒化、模糊聚类、熵正则化、压力修正、分子动力学

## 摘要（英文）
Coarse-graining is an effective approach for bridging atomistic and mesoscopic descriptions of fluid particle systems. However, fixed coarse-grained (CG) mappings do not account for the unbundled nature of fluid particles. We propose an entropy-regularized fuzzy clustering method with temporal smoothness constraints, examining in detail the role of the evolution of fuzzy particle-cluster membership degrees throughout the coarse-graining process. Entropy regularization controls the level of spatial fuzziness, while the temporal smoothness constraints enhance the continuity of cluster position evolution. Within a bottom-up force-matching framework, the interactions between clusters are decomposed into two contributions: a particle-interaction term, which is the weighted sum of interactions between particles, and a membership-evolution term, which originates from the temporal variation of membership degrees. Analyses based on the Lennard-Jones (L-J) fluid particle system and the water molecule system show that an intermediate level of fuzziness yields the most pronounced structural features in the radial distribution functions. The particle-interaction term exhibits system-dependent characteristics, whereas the membership-evolution term consistently provides a repulsive contribution across different systems. Moreover, CG dynamics simulations of the L-J fluid demonstrate that including the membership-evolution term effectively restores the system pressure, which could be interpreted as a pressure correction scheme. This finding provides a physical perspective on the transition from microscopic particle interactions to macroscopic fluid pressure constraints and reveals a bottom-up origin for incorporating additional pressure corrections into fluid CG dynamics, which could be beneficial for the future design of coarse-graining strategies.

## 摘要（中文）
粗粒度是桥接流体粒子系统的原子和介观描述的有效方法。然而，固定的粗粒度 (CG) 映射不考虑流体颗粒的未捆绑性质。我们提出了一种具有时间平滑度约束的熵正则化模糊聚类方法，详细研究了模糊粒子聚类隶属度在整个粗粒化过程中的作用。熵正则化控制了空间模糊性的水平，而时间平滑性约束增强了簇位置演化的连续性。在自下而上的力匹配框架内，簇之间的相互作用被分解为两个贡献: 粒子相互作用项，它是粒子之间相互作用的加权和，以及成员演化项，它源于时间变化。隶属度。基于lennard-jones (l-j) 流体粒子系统和水分子系统的分析表明，中等水平的模糊性在径向分布函数中产生最明显的结构特征。粒子相互作用项表现出与系统相关的特征，而成员演化项在不同系统中始终提供排斥作用。此外，l-j流体的CG动力学模拟表明，包括成员演化项有效地恢复了系统压力，这可以解释为压力校正方案。这一发现为从微观粒子相互作用到宏观流体压力约束的转变提供了物理视角，并揭示了将额外的压力校正纳入流体CG动力学的自下而上的起源，这可能有利于粗粒度策略的未来设计。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1US8EKTjTxS2OmW4-2B0mjRUPqGGQS4yxDw1yTZZuM2GpRoGGxPIriYdNQ9eYXef9zjTCW389G7b9f3SY72tEt4hHMf3t4SmRRoXv46erLP4-2B1nY41iFExQkGYoefXrQ59rUZDI_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXc2RYNe3UlLS9pq-2BEMdtMXEs8oRUs7Pon-2B4zQV6XjgAKbCQnIIBQGtKdNzKY6cmS-2ByXXEJXkbQjUc4mk20adAPQp10uYTWoNl0WXsM1JbZyT0EUjKFBxAuvilOuFjtpRYqSN3ZbA57sw8EI42QvcaiIhVknC0qbYhcZkamYgi21cj6RuuGjLEcH8-2Bjz2BdaC8Q-3D)
