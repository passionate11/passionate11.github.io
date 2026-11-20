---
permalink: /papers/expandr/
title: "ExpandR: Teaching Dense Retrievers Beyond Queries with LLM Guidance"
description: "ExpandR studies how a language model and a dense retriever can learn query expansion together. The retriever learns from queries augmented by the generator. The generator learns which expansions the retriever finds useful."
og_type: "article"
lang: "en"
locale: "en_US"
lang_key: "en"
nav_locale: "en"
author_profile: false
reading_page: true
---

# ExpandR: Teaching Dense Retrievers Beyond Queries with LLM Guidance

Sijia Yao, Pengcheng Huang, Zhenghao Liu, Yu Gu, Yukun Yan, Shi Yu, Ge Yu

**EMNLP 2025**

[Proceedings](https://aclanthology.org/2025.emnlp-main.963/) · [arXiv](https://arxiv.org/abs/2502.17057) · [Code](https://github.com/NEUIR/ExpandR) · [Hugging Face](https://huggingface.co/papers/2502.17057) · [ORKG](https://orkg.org/papers/R1994776)

ExpandR studies how a language model and a dense retriever can learn query expansion together. The retriever learns from queries augmented by the generator. The generator learns which expansions the retriever finds useful.

## How query expansion is trained

The retriever is trained contrastively on expanded queries. The language model is optimized with direct preference optimization using preferences informed by retrieval effectiveness and generation consistency. Training the two components together lets the expansion policy adapt to the ranking model. [Source](https://aclanthology.org/2025.emnlp-main.963/)

## Query expansion with a fixed or jointly trained retriever

| Approach | What is optimized |
| --- | --- |
| [Query2doc](https://aclanthology.org/2023.emnlp-main.585/) | A few-shot prompt generates a pseudo-document to expand the query, which is passed to a sparse or dense retriever. The expansion is applied without fine-tuning. |
| [ExpandR](https://arxiv.org/html/2502.17057#S3) | Expanded queries train the dense retriever contrastively. Retrieval effectiveness and response consistency inform the preference pairs used to train the expansion generator. |

For evidence on how retriever training and generator preference alignment contribute, see the [ExpandR ablations](https://arxiv.org/html/2502.17057#S5.SS2) and [BEIR results](https://aclanthology.org/2025.emnlp-main.963/). Compare the retriever and query representation used at evaluation time when reading results on query expansion.

## Earlier preprint

The arXiv preprint first appeared under the title *LLM-QE: Improving Query Expansion by Aligning Large Language Models with Ranking Preferences*. The EMNLP proceedings publish it as ExpandR. [Source](https://arxiv.org/abs/2502.17057v1)

DOI [10.18653/v1/2025.emnlp-main.963](https://doi.org/10.18653/v1/2025.emnlp-main.963) · [BibTeX](/selected-papers.bib)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "@id": "https://doi.org/10.18653/v1/2025.emnlp-main.963",
  "headline": "ExpandR: Teaching Dense Retrievers Beyond Queries with LLM Guidance",
  "description": "ExpandR studies how a language model and a dense retriever can learn query expansion together. The retriever learns from queries augmented by the generator. The generator learns which expansions the retriever finds useful.",
  "inLanguage": "en",
  "author": [
    {
      "@type": "Person",
      "name": "Sijia Yao"
    },
    {
      "@type": "Person",
      "name": "Pengcheng Huang"
    },
    {
      "@type": "Person",
      "name": "Zhenghao Liu"
    },
    {
      "@type": "Person",
      "name": "Yu Gu"
    },
    {
      "@type": "Person",
      "name": "Yukun Yan"
    },
    {
      "@type": "Person",
      "name": "Shi Yu"
    },
    {
      "@type": "Person",
      "name": "Ge Yu"
    }
  ],
  "identifier": {
    "@type": "PropertyValue",
    "propertyID": "DOI",
    "value": "10.18653/v1/2025.emnlp-main.963"
  },
  "sameAs": [
    "https://aclanthology.org/2025.emnlp-main.963/",
    "https://arxiv.org/abs/2502.17057"
  ],
  "mainEntityOfPage": "https://passionate11.github.io/papers/expandr/"
}
</script>
