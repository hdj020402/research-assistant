---
title: "Coarse-Grained Mapping of Fluid Particles via Evolutionary Fuzzy Clustering: Membership-Evolution Term as a Pressure Correction Mechanism"
title_zh: "通过演化模糊聚类的流体粒子粗粒化映射：膜元演化项作为压力修正机制"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c01867"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1US8EKTjTxS2OmW4-2B0mjRUPqGGQS4yxDw1yTZZuM2GpRoGGxPIriYdNQ9eYXef9zjTCW389G7b9f3SY72tEt4hHMf3t4SmRRoXv46erLP4-2B1nY41iFExQkGYoefXrQ59rUZDI_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXc2RYNe3UlLS9pq-2BEMdtMXEs8oRUs7Pon-2B4zQV6XjgAKbCQnIIBQGtKdNzKY6cmS-2ByXXEJXkbQjUc4mk20adAPQp10uYTWoNl0WXsM1JbZyT0EUjKFBxAuvilOuFjtpRYqSN3ZbA57sw8EI42QvcaiIhVknC0qbYhcZkamYgi21cj6RuuGjLEcH8-2Bjz2BdaC8Q-3D"
pub_date: ""
tags: ["coarse-graining", "fuzzy-clustering", "molecular-dynamics", "force-matching", "pressure-correction"]
ai_relevance: 3
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# Coarse-Grained Mapping of Fluid Particles via Evolutionary Fuzzy Clustering: Membership-Evolution Term as a Pressure Correction Mechanism

**通过演化模糊聚类的流体粒子粗粒化映射：膜元演化项作为压力修正机制**

## 精华总结
提出了考虑粒子动态聚类特性的粗粒化方法，通过隶属度演化项实现压力自动修正，为流体粗粒化动力学的设计提供了物理视角。

**关键词**: 粗粒化、模糊聚类、分子动力学、压力修正、多尺度模拟

## 摘要（英文）
Coarse-graining is an effective approach for bridging atomistic and mesoscopic descriptions of fluid particle systems. However, fixed coarse-grained (CG) mappings do not account for the unbundled nature of fluid particles. We propose an entropy-regularized fuzzy clustering method with temporal smoothness constraints, examining in detail the role of the evolution of fuzzy particle-cluster membership degrees throughout the coarse-graining process. Entropy regularization controls the level of spatial fuzziness, while the temporal smoothness constraints enhance the continuity of cluster position evolution. Within a bottom-up force-matching framework, the interactions between clusters are decomposed into two contributions: a particle-interaction term, which is the weighted sum of interactions between particles, and a membership-evolution term, which originates from the temporal variation of membership degrees. Analyses based on the Lennard-Jones (L-J) fluid particle system and the water molecule system show that an intermediate level of fuzziness yields the most pronounced structural features in the radial distribution functions. The particle-interaction term exhibits system-dependent characteristics, whereas the membership-evolution term consistently provides a repulsive contribution across different systems. Moreover, CG dynamics simulations of the L-J fluid demonstrate that including the membership-evolution term effectively restores the system pressure, which could be interpreted as a pressure correction scheme. This finding provides a physical perspective on the transition from microscopic particle interactions to macroscopic fluid pressure constraints and reveals a bottom-up origin for incorporating additional pressure corrections into fluid CG dynamics, which could be beneficial for the future design of coarse-graining strategies.

## 摘要（中文）
粗粒化是连接原子和介观流体粒子体系描述的有效方法。本研究提出了具有时间平滑约束的熵正则化模糊聚类方法，详细研究了粗粒化过程中模糊粒子-簇隶属度演化的作用。在自下而上的力匹配框架中，簇间相互作用分解为粒子相互作用项和隶属度演化项。通过Lennard-Jones流体和水分子体系的分析表明，中等模糊度水平产生最显著的结构特征，而隶属度演化项可有效修正系统压力。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE1US8EKTjTxS2OmW4-2B0mjRUPqGGQS4yxDw1yTZZuM2GpRoGGxPIriYdNQ9eYXef9zjTCW389G7b9f3SY72tEt4hHMf3t4SmRRoXv46erLP4-2B1nY41iFExQkGYoefXrQ59rUZDI_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjRUiIjfFOgquT67-2Bwuql2fc-2FgVxAFC1RWERMKinc1JXc2RYNe3UlLS9pq-2BEMdtMXEs8oRUs7Pon-2B4zQV6XjgAKbCQnIIBQGtKdNzKY6cmS-2ByXXEJXkbQjUc4mk20adAPQp10uYTWoNl0WXsM1JbZyT0EUjKFBxAuvilOuFjtpRYqSN3ZbA57sw8EI42QvcaiIhVknC0qbYhcZkamYgi21cj6RuuGjLEcH8-2Bjz2BdaC8Q-3D)
