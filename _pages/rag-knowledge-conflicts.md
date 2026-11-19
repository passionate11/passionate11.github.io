---
permalink: /rag-knowledge-conflicts/
title: "RAG Knowledge Conflicts: When Retrieval Disagrees with Model Memory"
seo_title: "RAG Knowledge Conflicts: Model Memory vs. Retrieved Evidence"
description: "How to evaluate naturally occurring context–memory conflicts in retrieval-augmented generation and compare feed-forward network interventions for contextual faithfulness."
schema_type: "Article"
microdata_type: "Article"
og_type: "article"
lang: "en"
locale: "en_US"
lang_key: "en"
nav_locale: "en"
author_profile: false
---

# RAG Knowledge Conflicts: When Retrieval Disagrees with Model Memory

*Pengcheng Huang · November 2026*

A retrieval-augmented language model can give its usual closed-book answer even after reading a passage that supports a different answer. **Context–memory conflict** is the disagreement between that parametric answer and the retrieved evidence. When the passage is accurate, test whether the model adopts the supported answer. When the model is right and the passage is misleading, adopting the retrieved answer is itself an error. Report those cases separately when evaluating a method that changes how much the model relies on retrieval. [ParamMute, §4](https://proceedings.neurips.cc/paper_files/paper/2025/file/90d1e515d74686ad148b469a3cecbbaa-Paper-Conference.pdf#page=5) · [SPARK, §6.3](https://arxiv.org/html/2606.27786v2#S6.SS3)

## How can I test a naturally occurring conflict between retrieval and memory?

Start with an existing question, its supporting passage, and a reference answer. Check that a model gives a stable, different answer without the passage. Then supply the original passage and measure how often the output follows the supported answer or repeats the earlier answer. This tests what happens once reliable evidence is available. A separate retrieval evaluation can measure whether the evidence would be found in the first place. [CoFaithfulQA in ParamMute, §4 and Appendix A.5–A.7](https://proceedings.neurips.cc/paper_files/paper/2025/file/90d1e515d74686ad148b469a3cecbbaa-Paper-Conference.pdf#page=5) · [Knowledge Conflicts with Real Documents, §3.1](https://arxiv.org/html/2404.16032#S3.SS1)

| Research question | Representative work and what it measures |
| --- | --- |
| Does a model follow accurate evidence when its memory gives a different answer? | CoFaithfulQA identifies a conflict subset within six existing QA datasets by verifying disagreement between a model's stable closed-book answer and the answer supported by the original passage. The real-documents study derives disagreements using existing gold passages as a proxy for successful retrieval. [ParamMute, §4 and Table 1](https://proceedings.neurips.cc/paper_files/paper/2025/file/90d1e515d74686ad148b469a3cecbbaa-Paper-Conference.pdf#page=5) · [Knowledge Conflicts with Real Documents, §3.1](https://arxiv.org/html/2404.16032#S3.SS1) |
| How should an answer handle two passages that contradict each other? | WikiContradict pairs contradictory Wikipedia passages and evaluates whether answers account for the differing perspectives. [WikiContradict, §3–4](https://arxiv.org/html/2406.13805#S3) |
| What happens when the supplied passages include misleading or irrelevant material? | Tug-of-War tests conflicts with model memory and between different kinds of evidence. Its contrastive decoder compares predictions conditioned on different evidence. [Tug-of-War, §4–6](https://aclanthology.org/2024.lrec-main.1466/) |

## What changes when intervening on feed-forward layers?

**ParamMute** identifies mid-to-deep feed-forward networks with a higher fraction of active neurons during unfaithful generation, then combines selective activation suppression with knowledge-preference adaptation. The main experiments report **context recall** and **memory recall** to distinguish recovery of the supplied answer from persistence of the model's closed-book answer. [NeurIPS 2025 paper, §3–6 and Table 2](https://doi.org/10.52202/085713-3356) · [CoFaithfulQA dataset](https://huggingface.co/datasets/chengpingan/CoFaithfulQA)

**SPARK** trains a lightweight policy that gates the contribution of FFN residuals by layer and decoding step while freezing the backbone. Its gates can suppress or amplify those contributions. The standard MRQA and ConFiQA results use different evaluation protocols from CoFaithfulQA's filtered conflict subset. Section 6.3 reports a separate breakdown for cases where the context is correct and cases where the closed-book answer is correct. [SPARK, §4, §6.1 and §6.3](https://arxiv.org/html/2606.27786v2)

**ProbeRAG** classifies hidden states to detect conflicting evidence and marks the detected statements at inference. Its fine-tuning uses an auxiliary loss to guide attention toward those statements. Its main experiments include ParamMute as a baseline, giving a setting for comparing the two kinds of intervention. [ProbeRAG](https://aclanthology.org/2026.findings-acl.1499/) · [Table 2](https://arxiv.org/html/2510.12460v3#S4.T2)

Earlier preprints used different titles. **[PIP-KAG](https://arxiv.org/abs/2502.15543v1)** is the earlier version of [ParamMute](https://arxiv.org/abs/2502.15543) and **SHIFT** is the first version of [SPARK](https://arxiv.org/abs/2606.27786v1). I am the first author of ParamMute and a co-first author of SPARK.
