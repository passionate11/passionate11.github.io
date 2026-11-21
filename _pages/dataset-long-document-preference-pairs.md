---
layout: research-dataset
permalink: /research-data/long-document-preference-pairs/
title: LongMab-PO long-document preference pairs
description: The LongMab-PO release provides two JSON Lines files of chosen and rejected responses for long-context preference optimization. The Llama 3 file contains 2,250 pairs and the Qwen 2 file contains 2,112.
dataset_key: long_document_preference_pairs
paper_title: 'Chunks as Arms: Multi-Armed Bandit-Guided Sampling for Long-Context LLM Preference Optimization'
paper_resource: https://aclanthology.org/2026.acl-long.161.bib
paper_resource_label: Official BibTeX
source_label: Authors’ training data folder
lang: en
locale: en_US
lang_key: en
nav_locale: en
reading_page: true
author_profile: false
---

## Which files are ready for preference training?

Both preference files contain `id`, `input`, `prompt`, `chosen` and `rejected`. Select the file for the model family you are studying and keep prompt–response pairs together. The authors also distribute a larger `raw_data_42_8k_16k.jsonl` file in the same folder for constructing training examples.

LongMab-PO samples chunks of the long context to generate candidate responses and uses reward feedback to guide subsequent sampling. The repository documents both generating those candidates and training from the released pairs. [Authors’ training instructions](https://github.com/NEUIR/LongMab-PO#training-longmab-po)
