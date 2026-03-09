---
title: "CO2Capture from Flue Gas: A High-Fidelity Force Field and Machine Learning Framework for Adsorbent Discovery"
title_zh: "烟道气中二氧化碳捕集：用于吸附剂发现的高精度力场与机器学习框架"
journal: "Journal of Chemical Theory and Computation"
doi: "10.1021/acs.jctc.5c02156"
url: "http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE13pmqQWZjrtpapPNhewa-2Bya4Kwweygq-2B3nj-2BQtrpFZj5shrdK1fu-2Be1Bx-2BqblFkVxuMkexrXfxRDsE0sXFRKgmwuJrHls46i-2F-2BYYy0H9CvOpHRfN5SQN9vBmkHkmewLaYXqlD_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjW7AaooT4Kl7cFUzD7LieLOKneDI-2B5uQ7uNzJXnkKHZ3fQsd0CtEBeXqCqXr5z14dJhbGEIDIKQj5OI1NxamBrLKsUkmlkvzwBwIRU-2BexcTijXAZzq2KLG118-2FIkqKVccE6knjlcZUox-2FHb9nAPUkHV1ghAIYh0wHX4uMMMEqg0oIrOvrZW1JIYK7WrV1JhJMqs5lp8MdfdwUs9qWH7B4fxWFFLfiWPYeJRiKGmuH31g-3D"
pub_date: ""
tags: ["machine-learning", "force-field", "co2-capture", "adsorbent-discovery", "materials-design"]
ai_relevance: 4
relevance: null
innovation: null
methods: null
read_status: "unread"
type: paper-note
date_added: "2026-03-09"
---

# CO2Capture from Flue Gas: A High-Fidelity Force Field and Machine Learning Framework for Adsorbent Discovery

**烟道气中二氧化碳捕集：用于吸附剂发现的高精度力场与机器学习框架**

## 精华总结
本研究开发了基于Exp-PE势的高保真范德华力场和CO2吸附数据库,通过引入四极矩响应描述符改进机器学习模型的预测精度,解决了传统Lennard-Jones力场在CO2吸附数据中的系统偏差问题,成功发现了性能优异的COF/MOF吸附剂。

**关键词**: CO2捕获、力场、机器学习、吸附剂发现、孔隙材料

## 摘要（英文）
CO2 from flue gas is central to mitigating fossil-fuel-derived emissions, where adsorbent performance directly dictates process energy efficiency and process cost. Although machine learning (ML) has emerged as a powerful tool for accelerating adsorbent discovery, its predictive accuracy is fundamentally limited by the physical reliability of the underlying training data, a manifestation of the "garbage in, garbage out" (GIGO) problem. Most existing CO2 adsorption databases rely on Lennard-Jones (LJ) force fields, whose deficiencies in describing CO2-CO2 and CO2-framework interactions, particularly at high pressures, introduce systematic bias into the ML models. To address this, we developed a physically accurate van der Waals force field based on an Exp-PE potential and constructed a high-fidelity CO2 adsorption database. Building on this data set, we introduce quadrupole-responsive descriptors that explicitly capture the anisotropic electrostatics of CO2, leading to improved ML predictive accuracy. This framework identifies high-performing COF/MOF adsorbents, including COF-50 (ΔNCO2 = 13.58 mol/kg) and COF-364 (ΔNCO2 = 12.43 mol/kg), whose working capacities exceed those of current reported porous materials.

## 摘要（中文）
烟道气中的二氧化碳是减缓化石燃料排放的关键，吸附剂的性能直接决定工艺的能源效率和成本。尽管机器学习（ML）已成为加速吸附剂发现的强大工具，但其预测精度从根本上受限于底层训练数据的物理可靠性，这正是“垃圾进、垃圾出”（GIGO）问题的体现。现有的大多数CO2吸附数据库均依赖于Lennard-Jones（LJ）力场，而该力场在描述CO2-CO2以及CO2-框架相互作用方面存在不足，尤其是在高压条件下，这会给机器学习模型带来系统性偏差。为此，我们基于Exp-PE势能函数开发了一个物理上精确的范德华力场，并构建了一个高保真度的二氧化碳吸附数据库。基于该数据集，我们引入了四极矩响应描述符，这些描述符能够显式地刻画CO2的各向异性静电特性，从而显著提升机器学习模型的预测精度。该框架识别出若干高性能的COF/MOF吸附剂，其中包括COF-50（ΔNCO2 = 13.58 mol/kg）和COF-364（ΔNCO2 = 12.43 mol/kg），其工作容量均高于目前已报道的多孔材料。

## 笔记
<!-- 在此处添加阅读笔记 -->

## Links
- [Full Article](http://url5675.acs.org/ls/click?upn=u001.GXhmshJPA1t8vlxMR-2FToII2roP7p3-2BAW2NtcJEvBqZ6xT1Jb4aEyuRmDh55EbZE13pmqQWZjrtpapPNhewa-2Bya4Kwweygq-2B3nj-2BQtrpFZj5shrdK1fu-2Be1Bx-2BqblFkVxuMkexrXfxRDsE0sXFRKgmwuJrHls46i-2F-2BYYy0H9CvOpHRfN5SQN9vBmkHkmewLaYXqlD_lCfgyiCVNF2aFl1C5Hre7Otyl3MOx4XtLxhxzfQ-2BJEA4TixnLSSnHKtti6TVNqJjW7AaooT4Kl7cFUzD7LieLOKneDI-2B5uQ7uNzJXnkKHZ3fQsd0CtEBeXqCqXr5z14dJhbGEIDIKQj5OI1NxamBrLKsUkmlkvzwBwIRU-2BexcTijXAZzq2KLG118-2FIkqKVccE6knjlcZUox-2FHb9nAPUkHV1ghAIYh0wHX4uMMMEqg0oIrOvrZW1JIYK7WrV1JhJMqs5lp8MdfdwUs9qWH7B4fxWFFLfiWPYeJRiKGmuH31g-3D)
