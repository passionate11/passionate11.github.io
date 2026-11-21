---
layout: research-dataset
permalink: /research-data/rag-adaptation-training/
title: ParamMute RAG training examples
description: The ParamMute release contains 32,580 JSON Lines records for training retrieval-augmented language models. Each record includes a retrieval-conditioned input, a plain input and an output.
dataset_key: rag_adaptation_training
paper_title: 'ParamMute: Suppressing Knowledge-Critical FFNs for Faithful Retrieval-Augmented Generation'
paper_resource: https://openreview.net/forum?id=CyUq9D99vE
paper_resource_label: Paper on OpenReview
source_label: Hugging Face dataset card
lang: en
locale: en_US
lang_key: en
nav_locale: en
reading_page: true
author_profile: false
---

## Which input contains retrieval?

The file uses `rag_input` for the retrieval-conditioned prompt, `raw_input` for the plain prompt and `output` for the target text. The filename retains the method's earlier name, PIP-KAG. When training and evaluating the same model, keep these adaptation examples separate from the [CoFaithfulQA evaluation files](/research-data/cofaithfulqa/).
