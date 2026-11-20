---
permalink: /papers/longmab-po/
title: "Chunks as Arms: Multi-Armed Bandit-Guided Sampling for Long-Context LLM Preference Optimization"
description: "LongMab uses multi-armed bandit sampling to construct preference pairs for long-context language models. A context is divided into chunks, and each chunk is treated as a bandit arm."
og_type: "article"
lang: "en"
locale: "en_US"
lang_key: "en"
nav_locale: "en"
author_profile: false
reading_page: true
---

# Chunks as Arms: Multi-Armed Bandit-Guided Sampling for Long-Context LLM Preference Optimization

Shaohua Duan, Pengcheng Huang, Xinze Li, Zhenghao Liu, Xiaoyuan Yi, Yukun Yan, Shuo Wang, Yu Gu, Ge Yu, Maosong Sun

**ACL 2026**

[Proceedings](https://aclanthology.org/2026.acl-long.161/) · [arXiv](https://arxiv.org/abs/2508.13993) · [Code](https://github.com/NEUIR/LongMab-PO) · [Hugging Face](https://huggingface.co/papers/2508.13993) · [ORKG](https://orkg.org/papers/R1994780)

LongMab uses multi-armed bandit sampling to construct preference pairs for long-context language models. A context is divided into chunks, and each chunk is treated as a bandit arm.

## How the sampling works

During rollouts, an upper-confidence-bound policy balances exploring under-sampled chunks and selecting chunks with higher estimated rewards. Feedback from the generated responses updates the chunk estimates. The sampled responses are then used to build pairs for direct preference optimization. [Source](https://arxiv.org/html/2508.13993v2)

## What the experiments evaluate

The paper evaluates sample construction and downstream performance on long-context tasks with Llama and Qwen models. The evaluation and ablations describe the effect of bandit-guided sampling on the preference data and the trained models. [Source](https://aclanthology.org/2026.acl-long.161/)

DOI [10.18653/v1/2026.acl-long.161](https://doi.org/10.18653/v1/2026.acl-long.161) · [BibTeX](/selected-papers.bib)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "@id": "https://doi.org/10.18653/v1/2026.acl-long.161",
  "headline": "Chunks as Arms: Multi-Armed Bandit-Guided Sampling for Long-Context LLM Preference Optimization",
  "description": "LongMab uses multi-armed bandit sampling to construct preference pairs for long-context language models. A context is divided into chunks, and each chunk is treated as a bandit arm.",
  "inLanguage": "en",
  "author": [
    {
      "@type": "Person",
      "name": "Shaohua Duan"
    },
    {
      "@type": "Person",
      "name": "Pengcheng Huang"
    },
    {
      "@type": "Person",
      "name": "Xinze Li"
    },
    {
      "@type": "Person",
      "name": "Zhenghao Liu"
    },
    {
      "@type": "Person",
      "name": "Xiaoyuan Yi"
    },
    {
      "@type": "Person",
      "name": "Yukun Yan"
    },
    {
      "@type": "Person",
      "name": "Shuo Wang"
    },
    {
      "@type": "Person",
      "name": "Yu Gu"
    },
    {
      "@type": "Person",
      "name": "Ge Yu"
    },
    {
      "@type": "Person",
      "name": "Maosong Sun"
    }
  ],
  "identifier": {
    "@type": "PropertyValue",
    "propertyID": "DOI",
    "value": "10.18653/v1/2026.acl-long.161"
  },
  "sameAs": [
    "https://aclanthology.org/2026.acl-long.161/",
    "https://arxiv.org/abs/2508.13993"
  ],
  "mainEntityOfPage": "https://passionate11.github.io/papers/longmab-po/"
}
</script>
