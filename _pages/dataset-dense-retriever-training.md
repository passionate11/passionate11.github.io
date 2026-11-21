---
layout: research-dataset
permalink: /research-data/dense-retriever-training/
title: ExpandR dense retriever training data
description: This dataset contains 708,740 contrastive training examples for dense passage retrieval. Each row pairs a search query and its generated pseudo-document with positive and negative retrieval examples used by ExpandR.
dataset_key: dense_retriever_training
paper_title: 'ExpandR: Teaching Dense Retrievers Beyond Queries with LLM Guidance'
paper_resource: https://aclanthology.org/2025.emnlp-main.963.bib
paper_resource_label: Official BibTeX
lang: en
locale: en_US
lang_key: en
nav_locale: en
author_profile: false
reading_page: true
---

## What can be compared with the same examples?

The release stores `query` and `pseudo_doc` in separate fields. A retriever experiment can therefore vary whether the expansion is supplied while retaining the same `pos` and `neg` examples. Use the same evaluation queries, corpus and retrieval cutoff to compare the resulting rankings.

For a generator experiment that needs two competing expansions for one prompt, use the [companion preference pairs](/research-data/query-expansion-preferences/).
