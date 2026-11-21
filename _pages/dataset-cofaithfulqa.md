---
layout: research-dataset
permalink: /research-data/cofaithfulqa/
title: CoFaithfulQA
description: CoFaithfulQA contains 8,529 question–passage examples from six QA sources. It supports evaluation of retrieval-augmented generation when an accurate passage conflicts with the answer a language model gives from memory.
dataset_key: cofaithfulqa
paper_title: 'ParamMute: Suppressing Knowledge-Critical FFNs for Faithful Retrieval-Augmented Generation'
paper_resource: https://openreview.net/forum?id=CyUq9D99vE
paper_resource_label: Paper on OpenReview
lang: en
locale: en_US
lang_key: en
nav_locale: en
author_profile: false
reading_page: true
---

## What does one row measure?

The passage in `context` supports an answer in `answers`. The `parametric_answer` field records the answer the model used to construct the benchmark gave without that passage. Its frequency across repeated generations is recorded in `parametric_answer_freq`.

For a new model, first answer the same `question` without the passage. A disagreement identified for the original model may disappear for yours. Report how many disagreements remain before measuring how often the retrieved passage resolves them. The Hub groups the six files under a split called `train`. The paper uses the examples for evaluation. The download counts below describe the raw public files. Table 1 in the paper reports counts after deduplication.

[Benchmark construction and evaluation in the paper](https://arxiv.org/html/2502.15543v4#S4)
