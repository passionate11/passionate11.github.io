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
paper_authors:
  - Shaohua Duan
  - Pengcheng Huang
  - Xinze Li
  - Zhenghao Liu
  - Xiaoyuan Yi
  - Yukun Yan
  - Shuo Wang
  - Yu Gu
  - Ge Yu
  - Maosong Sun
citation_fields:
  publication_date: "2026/07"
  arxiv_id: "2508.13993"
  doi: "10.18653/v1/2026.acl-long.161"
  conference_title: "Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)"
  firstpage: "3559"
  lastpage: "3575"
citation_bibtex: "https://aclanthology.org/2026.acl-long.161.bib"
---

# Chunks as Arms: Multi-Armed Bandit-Guided Sampling for Long-Context LLM Preference Optimization

Shaohua Duan, Pengcheng Huang, Xinze Li, Zhenghao Liu, Xiaoyuan Yi, Yukun Yan, Shuo Wang, Yu Gu, Ge Yu, Maosong Sun

**ACL 2026**

[Proceedings](https://aclanthology.org/2026.acl-long.161/) · [arXiv v2](https://arxiv.org/abs/2508.13993v2) · [Code](https://github.com/NEUIR/LongMab-PO) · [Hugging Face](https://huggingface.co/papers/2508.13993) · [ORKG](https://orkg.org/papers/R1994780) · [Full text (arXiv HTML)](https://arxiv.org/html/2508.13993)

LongMab uses multi-armed bandit sampling to construct preference pairs for long-context language models. A context is divided into chunks, and each chunk is treated as a bandit arm.

## How the sampling works

During rollouts, an upper-confidence-bound policy balances exploring under-sampled chunks and selecting chunks with higher estimated rewards. Feedback from the generated responses updates the chunk estimates. The sampled responses are then used to build pairs for direct preference optimization. [Source](https://arxiv.org/html/2508.13993v2)

## What the experiments evaluate

The paper evaluates sample construction and downstream performance on long-context tasks with Llama and Qwen models. The evaluation and ablations describe the effect of bandit-guided sampling on the preference data and the trained models. [Source](https://aclanthology.org/2026.acl-long.161/)

## Constructing preference pairs for long-context DPO

| Approach | How it constructs preferences |
| --- | --- |
| [LongReward](https://aclanthology.org/2025.acl-long.187/) | Scores candidate responses with an LLM that assesses helpfulness, logicality, faithfulness, and completeness. |
| [LOGO](https://proceedings.mlr.press/v267/tang25j.html) | Constructs long-context preference data using position synthesis and trains with reference-free preference optimization. |
| [LongMab-PO](https://arxiv.org/html/2508.13993v2#S3) | Treats document chunks as bandit arms and adapts which chunks to sample during response generation, then uses those responses to construct DPO pairs. |

[Section 4](https://arxiv.org/html/2508.13993v2#S4) describes the comparison settings. [Section 5](https://arxiv.org/html/2508.13993v2#S5) separates downstream long-context QA results from ablations on candidate sampling and preference data construction.

## Published citation

The ACL 2026 proceedings and [arXiv v2](https://arxiv.org/abs/2508.13993v2) list the current authors. Use the proceedings entry for the publication year, page range, and DOI.

[ACL proceedings BibTeX]({{ page.citation_bibtex }}) · [DOI 10.18653/v1/2026.acl-long.161](https://doi.org/10.18653/v1/2026.acl-long.161)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "@id": "https://doi.org/10.18653/v1/2026.acl-long.161",
  "headline": "Chunks as Arms: Multi-Armed Bandit-Guided Sampling for Long-Context LLM Preference Optimization",
  "description": "LongMab uses multi-armed bandit sampling to construct preference pairs for long-context language models. A context is divided into chunks, and each chunk is treated as a bandit arm.",
  "datePublished": "2026-07",
  "inLanguage": "en",
  "author": [{% for name in page.paper_authors %}{"@type": "Person", "name": {{ name | jsonify }}}{% unless forloop.last %}, {% endunless %}{% endfor %}],
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
