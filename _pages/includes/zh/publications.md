<span class='anchor' id='publications'></span>

# 📝 论文发表

> 更多文章请参见我的 [Google Scholar 主页](https://scholar.google.com/citations?user=VA9mUOsAAAAJ)。注：\* 表示共同一作；\† 表示通讯作者。

<!-- Uncode_acl -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026</div><img src='images/paper/uncode_acl26.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

# Empirical Analysis of Decoding Biases in Masked Diffusion Models

`Pengcheng Huang`, Tianming Liu, Zhenghao Liu†, Yukun Yan, Shuo Wang, Tong Xiao, Zulong Chen, Maosong Sun

[![arXiv](https://img.shields.io/badge/arXiv-2508.13021-b31b1b.svg)](https://arxiv.org/abs/2508.13021) [![GitHub Stars](https://img.shields.io/github/stars/NEUIR/Uncode)](https://github.com/NEUIR/Uncode)

- 本文揭示了掩码扩散模型中基于不确定性解码的两个系统性偏差——刚性边界偏差和无意义词偏差，并提出 Uncode，一个通过位置轨迹先验和语义信息先验重塑解码优先级的轻量级校准框架，平均性能提升超过 7%，达到与同规模自回归模型可比的效果。

</div>
</div>

<!-- longmab_acl26 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026</div><img src='images/paper/acl26_longmab.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

# Chunks as Arms: Multi-Armed Bandit-Guided Sampling for Long-Context LLM Preference Optimization

Shaohua Duan\*, `Pengcheng Huang*`, Xinze Li\*, Zhenghao Liu†, Xiaoyuan Yi, Yukun Yan, Shuo Wang, Yu Gu, Ge Yu, Maosong Sun

[![arXiv](https://img.shields.io/badge/arXiv-2508.13993-b31b1b.svg)](https://arxiv.org/abs/2508.13993) [![GitHub Stars](https://img.shields.io/github/stars/NEUIR/LongMab-PO)](https://github.com/NEUIR/LongMab-PO)

- 本文提出 LongMab，将长上下文分块视为多臂老虎机的臂，通过 UCB 引导的采样策略渐进识别最具信息量的分块组合，生成高质量多样化响应并构建偏好对用于 DPO 训练，在 Llama 和 Qwen 上平均提升超 4%。
</div>
</div>

<!-- attn floating mdm -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026</div><img src='images/paper/attn_floating_acl26.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
# Revealing the Attention Floating Mechanism in Masked Diffusion Models

Xin Dai, `Pengcheng Huang`, Zhenghao Liu†, Shuo Wang, Yukun Yan, Chaojun Xiao, Yu Gu, Ge Yu, Maosong Sun

[![arXiv](https://img.shields.io/badge/arXiv-2601.07894-b31b1b.svg)](https://arxiv.org/abs/2601.07894) [![GitHub Stars](https://img.shields.io/github/stars/NEUIR/Attention-Floating)](https://github.com/NEUIR/Attention-Floating)

- 本文研究了掩码扩散模型的内部注意力行为，发现了独特的"注意力漂浮"机制——注意力锚点在层和去噪步之间动态漂移，为其优于自回归模型的上下文学习能力提供了机理层面的解释。
</div>
</div>

<!-- CARD -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ArXiv</div><img src='images/paper/card_icml26.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
# Causal Autoregressive Diffusion Language Model

Junhao Ruan, Bei Li, Yongjing Yin, `Pengcheng Huang`, Xin Chen, Jingang Wang, Xunliang Cai, Tong Xiao†, JingBo Zhu

[![arXiv](https://img.shields.io/badge/arXiv-2601.22031-b31b1b.svg)](https://arxiv.org/abs/2601.22031)

- 本文提出因果自回归扩散模型（CARD），通过严格的因果注意力掩码和动态解码机制，将自回归模型的训练效率与扩散模型的高吞吐并行推理统一在一个框架中。
</div>
</div>


<!-- Tool master -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ArXiv</div><img src='images/paper/toolmaster_acl26.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
# Teaching LLMs to Learn Tool Trialing and Execution through Environment Interaction

Xingjie Gao*, `Pengcheng Huang*`, Zhenghao Liu†, Yukun Yan, Shuo Wang, Zulong Chen, Chen Qian, Ge Yu, Yu Gu

[![arXiv](https://img.shields.io/badge/arXiv-2601.12762-b31b1b.svg)](https://arxiv.org/abs/2601.12762) [![GitHub Stars](https://img.shields.io/github/stars/NEUIR/ToolMaster)](https://github.com/NEUIR/ToolMaster)

- 本文提出 ToolMaster，通过将被动模仿专家轨迹转变为主动试错执行的范式，使大语言模型在与环境的直接交互中学习探索和自我纠正，从而掌握复杂工具使用。
</div>
</div>



<!-- sac iclr -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/paper/sac_iclr26.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
# Autoencoding-free context compression for llms via contextual semantic anchors

Xin Liu*, Runsong Zhao*, `Pengcheng Huang`, Xinyu Liu, Junyi Xiao, Chunyang Xiao, Tong Xiao†, Shengxiang Gao, Zhengtao Yu, Jingbo Zhu

[![arXiv](https://img.shields.io/badge/arXiv-2510.08907-b31b1b.svg)](https://arxiv.org/abs/2510.08907)

- 本文提出语义锚点压缩（SAC），一种无需自编码训练的上下文压缩方法，通过直接选择并聚合信息到上下文"锚点词"中，实现高效的大语言模型上下文压缩。
</div>
</div>


<!-- speech grpo -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJCNN 2026</div><img src='images/paper/speech_grpo.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
# RLAIF-SPA: Optimizing LLM-based Emotional Speech Synthesis via RLAIF

Qing Yang, Zhenghao Liu†, Junxin Wang, Yangfan Du, `Pengcheng Huang`, Tong Xiao

[![arXiv](https://img.shields.io/badge/arXiv-2510.14628-b31b1b.svg)](https://arxiv.org/abs/2510.14628)

- 本文提出 RLAIF-SPA，通过基于 AI 反馈的强化学习优化语义准确性和细粒度韵律对齐，提升大语言模型语音合成的情感表现力和韵律自然度。

</div>
</div>


<!-- PamramMute_nips -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/paper/parammute_nips25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

# ParamMute: Suppressing Knowledge-Critical FFNs for Faithful Retrieval-Augmented Generation

`Pengcheng Huang`, Zhenghao Liu†, Yukun Yan, Xiaoyuan Yi, Hao Chen, Zhiyuan Liu, Maosong Sun, Tong Xiao, Ge Yu, Chenyan Xiong

[![arXiv](https://img.shields.io/badge/arXiv-2502.15543-b31b1b.svg)](https://arxiv.org/abs/2502.15543)

- 本文提出 ParamMute，通过识别并抑制与不忠实生成相关的前馈网络（FFN），并引入知识偏好适配模块，有效引导语言模型更好地利用检索到的证据，提升检索增强生成的忠实性。
</div>
</div>

<!-- rag_survey -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AI Open 2025</div><img src='images/paper/survey.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

# Knowledge Intensive Agents

Zhenghao Liu†, `Pengcheng Huang`, Zhipeng Xu, Xinze Li, Shuliang Liu, Chunyi Peng, Haidong Xin, Yukun Yan, Shuo Wang, Xu Han, Zhiyuan Liu, Maosong Sun, Yu Gu, Ge Yu

[**📄PDF**](https://papers.ssrn.com/sol3/Delivery.cfm/81afde5f-fbd1-4635-b582-7ac104b3322a-MECA.pdf?abstractid=5459034&mirid=1)

- 本文从智能体视角对检索增强生成进行了全面综述，将知识密集型智能体分为知识获取和知识利用两类角色，并指出多智能体 RAG 系统联合优化的未来方向。
</div>
</div>




<!-- Expandr_EMNLP_oral -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025 Oral</div><img src='images/paper/expandr_emnlp25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

# ExpandR: Teaching Dense Retrievers Beyond Queries with LLM Guidance

Sijia Yao*, `Pengcheng Huang*`, Zhenghao Liu†, Yu Gu, Yukun Yan, Shi Yu, Ge Yu


[![arXiv](https://img.shields.io/badge/arXiv-2502.17057-b31b1b.svg)](https://arxiv.org/abs/2502.17057) [![GitHub Stars](https://img.shields.io/github/stars/NEUIR/ExpandR)](https://github.com/NEUIR/ExpandR)

- 本文提出 ExpandR，一个联合训练大语言模型和稠密检索器的统一框架，通过让 LLM 生成丰富的查询扩展，并同时优化扩展生成和检索排序性能，在检索基准上比强基线提升超 5%。
</div>
</div>


<!-- ClueAnchor_EMNLP -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025</div><img src='images/paper/clueanchor_emnlp25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

# ClueAnchor: Clue-Anchored Knowledge Reasoning Exploration and Optimization for Retrieval-Augmented Generation

Hao Chen, Yukun Yan, Sen Mei, Wanxiang Che, Zhenghao Liu, Qi Shi, Xinze Li, Yuchun Fan, `Pengcheng Huang`, Qiushi Xiong, Zhiyuan Liu, Maosong Sun

[![arXiv](https://img.shields.io/badge/arXiv-2505.24388-b31b1b.svg)](https://arxiv.org/abs/2505.24388)

- 本文发现 RAG 系统常因关键证据隐含、分散或被噪声掩盖而未能充分利用检索文档，ClueAnchor 通过提取关键线索、在不同知识配置下生成多条推理路径，再通过基于奖励的偏好优化选择最优路径，显著提升推理完整性和鲁棒性。
</div>
</div>


<!-- positionid_EMNLP -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025</div><img src='images/paper/position_id_emnlp25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

# Position IDs Matter: An Enhanced Position Layout for Efficient Context Compression in Large Language Models

Runsong Zhao, Xin Liu, Xinyu Liu, `Pengcheng Huang`, Chunyang Xiao, Tong Xiao†, Jingbo Zhu

[![arXiv](https://img.shields.io/badge/arXiv-2409.14364-b31b1b.svg)](https://arxiv.org/abs/2409.14364)

- 本文发现现有 LLM 上下文压缩方法（如 ICAE）在压缩词的位置编码布局上存在缺陷，提出将位置标识符均匀分布并引入专注记忆的"压缩损失"，将压缩比从 4 倍提升至约 15 倍，同时保持重建和下游任务性能。
</div>
</div>

<!-- Forgetting_curve_EMNLP -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2024</div><img src='images/paper/forget_emnlp24.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

# Forgetting curve: A reliable method for evaluating memorization capability for long-context models

Xinyu Liu, Runsong Zhao, `Pengcheng Huang`, Chunyang Xiao, Bei Li, Jingang Wang, Tong Xiao†, Jingbo Zhu

[![arXiv](https://img.shields.io/badge/arXiv-2410.04727-b31b1b.svg)](https://arxiv.org/abs/2410.04727)

- 本文发现现有长上下文模型的记忆能力评估方法（如困惑度、"大海捞针"任务）不够可靠，提出遗忘曲线——一种基于拷贝准确率与语言模型准确率对比的无提示鲁棒指标，更忠实地衡量模型对长上下文的记忆能力。
</div>
</div>


<!-- TAR_CCL -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CCL 2025</div><img src='images/paper/tar_ccl24.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

# Translate-and-Revise: Boosting Large Language Models for Constrained Translation

`Pengcheng Huang`, Yongyu Mu, Yuzhang Wu, Bei Li, Chunyang Xiao, Tong Xiao†, Jingbo Zhu

[**📄PDF**](https://aclanthology.org/2024.ccl-1.82/)

- 本文发现大语言模型在约束翻译中常忽略或违反指定的词汇或结构约束，提出 Translate-and-Revise，通过添加修订过程让模型识别未满足的约束并修正输出，约束翻译准确率提升约 15%，超越神经机器翻译基线。
</div>
</div>
