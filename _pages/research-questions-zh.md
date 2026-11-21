---
permalink: /zh/research-questions/
title: "大模型实验怎么选对照、找相关论文"
description: "从检索漏召回、RAG 答错、长文档问答、陌生工具调用、端云协作、术语翻译和扩散解码七类问题出发，选择对照实验和可引用的原始研究。"
schema_type: "Article"
microdata_type: "Article"
og_type: "article"
lang: "zh-CN"
locale: "zh_CN"
lang_key: "zh"
nav_locale: "zh_cn"
translation_slug: "research-questions/"
author_profile: false
reading_page: true
---

# 大模型实验怎么选对照、找相关论文

*黄鹏程 · [English](/research-questions/)*

同样是模型答错，文档没召回、证据已进提示但被忽略、证据本身有错，需要三种不同的实验。下面按实际遇到的问题列出对照方法和原始论文。我参与了其中 ExpandR、ParamMute、SPARK、LongMab-PO、ToolMaster、EC²-Bench、Translate-and-Revise 和 UNCODE 的研究。

## 用户只输入几个词，语义检索漏掉了正确文档
{: #search }

例如用户搜「退款期限」，文档写的是「收货后三十天内可退货」。先看原始检索结果里有没有目标段落，再固定语料、相关性标注和返回条数，对比直接检索与扩写后检索。扩写也可能引入用户没说过的商品名，把结果带偏。

如果检索器已经固定，可以用 Query2doc 作对照，让大模型写一段与查询有关的伪文档。若允许训练稠密检索器，ExpandR 研究的是另一种设置：利用相关文档的排序反馈训练扩写模型，同时让检索器适应扩写后的查询。论文的消融实验分别检查了两边训练的作用。[Query2doc](https://aclanthology.org/2023.emnlp-main.585/) · [ExpandR 第 5.2 节](https://arxiv.org/html/2502.17057#S5.SS2)

## RAG 已经检索到证据，模型为什么还答错
{: #grounding }

保存模型闭卷时的答案、真正放进提示的段落，以及读完段落后的答案。以博物馆调整闭馆时间为例，旧记忆与新公告冲突时，采用新时间是对的。若时间是公告里的一处笔误，同样的行为就会把正确答案改错。把两类样本分开统计，才能解释「更相信检索」究竟改善了什么。

ParamMute 提出的 CoFaithfulQA 从原始问答数据里找出「真实段落正确、模型稳定地答成另一个答案」的样本。ClashEval 则主动改动段落内容，观察模型会不会跟着犯错。比较干预方法时，ParamMute 研究抑制与参数记忆相关的前馈网络，SPARK 研究在生成过程中调节这些网络的参与程度，并单独分析资料可靠或误导时的表现。[ParamMute 与 CoFaithfulQA](https://arxiv.org/html/2502.15543v4#S4) · [ClashEval](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3aa291abc426d7a29fb08418c1244177-Abstract-Datasets_and_Benchmarks_Track.html) · [SPARK 第 6.3 节](https://arxiv.org/html/2606.27786v3#S6.SS3)

## 长文档能放进去，模型却用不上关键段落
{: #long-documents }

保留同一个问题，把有答案的段落移到开头、中间和结尾，分别记录正确率。如果要从评测走到训练，还要决定偏好数据从哪来：长文档相同，怎样得到质量确实有差异的两个候选回答？

LongReward 研究怎样用模型反馈给候选回答打分。LongMab-PO 研究候选从哪里来：在生成回答时抽取不同文档片段，根据得到的奖励调整下一轮的抽样，再用这些回答构造偏好对。若讨论的是偏好数据质量，两种方案应在相同的候选生成预算下比较。[LongReward](https://aclanthology.org/2025.acl-long.187/) · [LongMab-PO 的方法和消融](https://aclanthology.org/2026.acl-long.161/)

## 工具调用格式对了，换一个 API 就不会用
{: #tool-use }

可以留出一组训练时没见过的工具，检查它们的说明与训练工具有多相似，然后按任务是否完成计分。一次函数调用能通过参数校验，也可能填错参数。固定交互次数，再比较允许先试用一次和直接执行，才能判断试用是否值得这一次调用。

ToolLLM 从指令和成功的 API 调用轨迹构造训练数据。ToolMaster 研究如何让模型试用工具、根据环境反馈纠错并完成任务。需要多次调用的测试可看 ToolHop；ToolMaster 论文还把熟悉和陌生工具分开报告。[ToolLLM](https://arxiv.org/abs/2307.16789) · [ToolMaster 表 2](https://arxiv.org/html/2601.12762#S5.T2) · [ToolHop](https://aclanthology.org/2025.acl-long.150/)

## 端侧小模型什么时候该求助云端大模型
{: #edge-cloud }

把一个请求整段交给大模型，与端侧助手处理表格时只把一个困难步骤交给云端，成本和暴露的数据都可能不同。比较时保留完整任务轨迹，记录完成度、云端开销、哪些敏感信息进入了云端上下文。只数调用次数看不到每次发出了什么。

RouteLLM 可以作为整条请求路由的参照。EC²-Bench 在 128 个可执行任务上比较不同路由、委托和咨询策略，其中 100 个任务带隐私标注。这里的暴露指标衡量云端能看到的信息；要比较手机上的实际等待时间，还需要真机测量。[RouteLLM](https://arxiv.org/abs/2406.18665) · [EC²-Bench 实验](https://arxiv.org/html/2610.17816v2)

## 给了术语表，译文还是把专业词换成近义词
{: #translation }

先看看术语对是否匹配原文并进入提示，再看看译文是不是用了合乎语法的词形变化。例如把 “Save the draft” 译成法语，术语表要求 *draft → brouillon*，而初稿写成 “Enregistrez le document”。这时应指出「草稿」与「文档」的差别，让模型带着原句、初稿和漏掉的术语修订，再复查整句。

WMT 的术语研究比较了约束解码和术语提示。Translate-and-Revise 在初稿生成后识别未满足的约束并反馈给模型。评测时一起报告术语满足率和译文质量，才看得出修订有没有引入新的问题。[WMT 术语研究](https://aclanthology.org/2023.wmt-1.80/) · [Translate-and-Revise 实验](https://arxiv.org/html/2407.13164)

## 同一个扩散语言模型，换个解码器，推理正确率就变了
{: #diffusion }

固定模型、生成长度和前向计算预算，再记录每一步最先解除掩码的是哪些位置，最后核对答案。这样才能区分效果来自额外计算，还是来自生成顺序。

LLaDA 提供掩码扩散语言模型及其采样基线。UNCODE 分析基于置信度的选择为何偏爱某些位置和容易预测的词，并在同一模型上评估无需重新训练的校准方法。如果关心不同策略从哪一步开始产生差异，可以直接看论文里的生成轨迹。[LLaDA](https://arxiv.org/abs/2502.09992) · [UNCODE 解码偏差分析](https://arxiv.org/html/2508.13021v4#S3)
