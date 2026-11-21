---
layout: research-dataset
permalink: /research-data/masked-diffusion-decoder-scores/
title: Masked diffusion decoder scores on seven benchmarks
description: This CSV transcribes the complete first results table from the UNCODE paper. It contains 19 model or sampler rows, seven benchmark scores per row and the averages reported in the ACL proceedings.
dataset_key: masked_diffusion_decoder_scores
paper_title: Empirical Analysis of Decoding Biases in Masked Diffusion Models
paper_resource: https://aclanthology.org/2026.acl-long.311.bib
paper_resource_label: Official BibTeX
source_label: null
lang: en
locale: en_US
lang_key: en
nav_locale: en
reading_page: true
author_profile: false
---

## Compare samplers on the same backbone

Filter `model_group` to LLaDA-8B-Instruct or LLaDA-1.5-8B before comparing an unmasking rule. Each group includes uniform, confidence, entropy, margin, EB-Sampler, Semi-AR, Fast-dLLM and UNCODE results. Three autoregressive reference models appear in their own group. The dagger column preserves the table's marking for Semi-AR strategies.

The shot count varies by task. HumanEval and MBPP use zero shots, Countdown uses three, GSM8K and MATH500 use four, and GPQA and Sudoku use five. This author-prepared transcription preserves the published scores, including the reported averages. [Table 1 in the ACL paper](https://aclanthology.org/2026.acl-long.311.pdf#page=7)
