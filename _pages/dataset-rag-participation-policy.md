---
layout: research-dataset
permalink: /research-data/rag-participation-policy/
title: SPARK training data for context–memory conflicts
description: SPARK releases two sets of training and validation records for a policy that regulates how much an LLM relies on parametric knowledge during retrieval-augmented generation. The two archives correspond to Qwen3-1.7B and Qwen3-8B.
dataset_key: rag_participation_policy
paper_title: 'SPARK: Adaptive Parametric Knowledge Participation for Faithful Retrieval-Augmented Generation'
paper_resource: https://arxiv.org/abs/2606.27786
paper_resource_label: Paper on arXiv
source_label: Authors’ Hugging Face dataset card
lang: en
locale: en_US
lang_key: en
nav_locale: en
reading_page: true
author_profile: false
---

## Which examples are in each archive?

Both ZIPs contain `train.json` and `valid.json`. The Qwen3-1.7B release has 9,407 training and 2,351 validation records. The Qwen3-8B release has 14,265 and 3,565. Each example includes a question, context, a counterfactual context, the model's parametric answer and a context answer. The field `is_parametric_answer_right` records whether the parametric answer is correct.

The authors used FlashRAG and MRQA to synthesize the training data. Use the archive corresponding to the model whose parametric answers you want to study. [Data preparation in the authors' repository](https://github.com/OpenBMB/SPARK#readme)
