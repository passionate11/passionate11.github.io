---
layout: research-dataset
permalink: /research-data/lexically-constrained-translation-scores/
title: BLEU and constraint completion on IATE and Wiktionary
description: This CSV transcribes Table 2 of Translate-and-Revise. It gives BLEU and constraint completion rate for eight systems or prompting settings on two English-to-German lexically constrained translation test sets.
dataset_key: lexically_constrained_translation_scores
paper_title: 'Translate-and-Revise: Boosting Large Language Models for Constrained Translation'
paper_resource: https://aclanthology.org/2024.ccl-1.82.bib
paper_resource_label: Official BibTeX
source_label: null
lang: en
locale: en_US
lang_key: en
nav_locale: en
reading_page: true
author_profile: false
---

## How did revision affect translation quality and constraint completion?

With GPT-3.5-turbo-0613 on IATE, adding revision to the constrained prompt raises constraint completion from 96.2% to 98.9% at the same BLEU of 32.0. On Wiktionary, completion rises from 97.2% to 98.9% while BLEU changes from 32.1 to 32.0. Both metrics are included for all eight settings, so a gain on one can be examined alongside its effect on the other.

Each row is one reported system–test-set result. This author-prepared transcription uses the paper's absolute scores and includes all five neural machine translation baselines. [Table 2 in the CCL paper](https://aclanthology.org/2024.ccl-1.82.pdf#page=5)
