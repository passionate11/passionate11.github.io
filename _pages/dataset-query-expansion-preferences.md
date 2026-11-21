---
layout: research-dataset
permalink: /research-data/query-expansion-preferences/
title: ExpandR query expansion preference data
description: This dataset contains 30,000 preference pairs for training a language model to expand search queries. Each conversation is paired with a preferred and a rejected response for direct preference optimization in ExpandR.
dataset_key: query_expansion_preferences
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

## How is an expansion represented?

One row contains `conversations`, `chosen` and `rejected`. The conversation holds the input to the generator. The latter two fields give alternative responses to that input. Use their order as the preference label when training a query expansion model.

To evaluate whether an expansion helps search, compare retrieval with the original query and the expanded query against the same corpus and relevance judgments. For examples that supply relevant and negative passages alongside a generated expansion, use the [companion retriever data](/research-data/dense-retriever-training/).
