---
permalink: /unmasking-order/
title: "Unmasking Order in Diffusion Language Models"
seo_title: "Unmasking Order in Diffusion Language Models | A Related Work Guide"
description: "Compare confidence-based unmasking, decoding calibration, parallel token commitment, lookahead search, and learned policies in masked diffusion language models."
schema_type: "Article"
microdata_type: "Article"
og_type: "article"
lang: "en"
locale: "en_US"
lang_key: "en"
nav_locale: "en"
author_profile: false
---

# Unmasking Order in Diffusion Language Models

*Pengcheng Huang · November 2026*

A masked diffusion language model predicts tokens at several masked positions in one forward pass. Its sampler still has to decide **which positions to reveal, how many to commit, and whether earlier decisions can be revised**. Papers on unmasking order often change different parts of that decision. This guide separates them so readers can identify the closest prior work and trace each claim to its source.

| Research question | Representative papers | What the method changes |
| --- | --- | --- |
| Which position should be revealed first? | [LLaDA](https://arxiv.org/abs/2502.09992), [UNCODE](https://aclanthology.org/2026.acl-long.311/), [BayesER](https://arxiv.org/abs/2610.05125) | Start from confidence-based remasking, reweight confidence using positional and token-informativeness priors, or estimate uncertainty from a posterior over model parameters. |
| How many positions can be committed together? | [Fast-dLLM](https://arxiv.org/abs/2505.22618), [EB-Sampler](https://arxiv.org/abs/2505.24857) | Accept positions above a confidence threshold, or adapt how many positions to reveal under an entropy budget. Fast-dLLM also studies approximate KV caching. |
| How should the sampler account for the remaining masked intervals? | [Balance-Aware Pivot Decoding](https://arxiv.org/abs/2610.26040) | After confidence-based prefilling, favor central pivots to split masked intervals into shorter intervals that can be processed in parallel. |
| Can extra inference compute help select a better trajectory? | [LookUM](https://arxiv.org/abs/2511.05563) | Propose alternative unmasking paths and select among them using uncertainty over the resulting trajectories. |
| Can a separate policy learn which positions to reveal or revisit? | [Where-to-Unmask](https://arxiv.org/abs/2602.09501), [TIPS](https://arxiv.org/abs/2610.22099) | Train a planner from ground-truth-guided rankings, or train a small controller that can both reveal and remask tokens while keeping the underlying model frozen. |

## Confidence, calibration, and decoding bias

Confidence is an estimate of how likely the current token prediction is at a position. It can favor an easy prediction even when revealing it contributes little to the rest of the sequence. [UNCODE](https://aclanthology.org/2026.acl-long.311/) reports two recurring patterns under the uncertainty-based samplers it studies: a rigid tendency to reveal boundary positions early, and early preference for high-frequency, low-information tokens. Its sampler combines a positional prior and a corpus-based informativeness prior with the model's confidence. The paper's empirical analysis in Section 3 supports claims about **what confidence-first unmasking tends to reveal**. Section 4.2 describes **how to change that ranking without training a planner**. [Paper sections](https://arxiv.org/html/2508.13021v4#S3) · [ACL BibTeX](https://aclanthology.org/2026.acl-long.311.bib)

[BayesER](https://arxiv.org/abs/2610.05125) uses a different notion of calibration. It averages predictions from an approximate parameter posterior and ranks positions by predictive entropy. It is relevant when discussing whether the model's uncertainty estimates track error. The two approaches therefore motivate different comparisons: selecting informative positions versus improving the reliability of uncertainty estimates.

**Version note.** The first two arXiv versions of UNCODE used the name [PC-Sampler](https://arxiv.org/abs/2508.13021v2). The [ACL 2026 version](https://aclanthology.org/2026.acl-long.311/) is titled *Empirical Analysis of Decoding Biases in Masked Diffusion Models*. I am the first author of that paper.

## Position order and parallel commitment

Ranking positions and choosing a commit count can be varied separately. [Fast-dLLM](https://arxiv.org/abs/2505.22618) uses a confidence threshold for parallel commitment, while [EB-Sampler](https://arxiv.org/abs/2505.24857) adjusts the count with an approximate entropy bound. [Balance-Aware Pivot Decoding](https://arxiv.org/abs/2610.26040) explicitly considers how the positions selected now determine the remaining masked intervals. Its depth analysis concerns the balanced splitting rule. End-to-end speed also depends on the model, threshold, and implementation used in the experiment.

Local token dependence is a related question. [CoDiLA](https://arxiv.org/abs/2603.20216) adds a small autoregressive model to account for local dependencies within blocks. This changes how simultaneously proposed tokens are made coherent. A scheduler that changes only the order of positions addresses a different part of the sampler.

## Search and learned policies

The methods differ in where their extra work happens. [LookUM](https://arxiv.org/abs/2511.05563) uses additional forward passes at inference to evaluate candidate unmasking paths. [Where-to-Unmask](https://arxiv.org/abs/2602.09501) uses oracle scores during training to supervise a planner and then ranks positions with that planner during inference. [TIPS](https://arxiv.org/abs/2610.22099) learns a visibility controller that can reveal or remask tokens. These distinctions matter when a manuscript says a method is training-free, keeps the backbone frozen, or allows previously revealed positions to change.

## Citing and comparing results

- **For the rationale for a position policy**, cite the work that identifies the relevant behavior. For example, use [UNCODE §3](https://arxiv.org/html/2508.13021v4#S3) for observed decoding bias and [Where-to-Unmask §3](https://arxiv.org/html/2602.09501#S3) for evidence from controlled oracle orderings.
- **For an inference comparison**, match the model checkpoint, prompt, output budget, number of function evaluations, and what counts as a commitment or remask. If reporting latency, also state the cache configuration, hardware, and batch size. A throughput result and an accuracy result at matched function evaluations answer different questions. The [IJCAI survey on efficient dLLM inference](https://ijcai.org/proceedings/2026/873) discusses practical latency comparisons in more detail.

*Scope.* This is a focused reading guide to position selection and commitment at inference in masked text diffusion. It draws on the papers linked above and the references of the IJCAI survey and UNCODE, checked November 19, 2026. It includes selected preprints and provides no common performance ranking.
