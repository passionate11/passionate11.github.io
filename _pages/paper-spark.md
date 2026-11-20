---
permalink: /papers/spark/
title: "SPARK: Adaptive Parametric Knowledge Participation for Faithful Retrieval-Augmented Generation"
description: "SPARK studies how a retrieval-augmented language model handles conflicts between retrieved evidence and its parametric knowledge. A lightweight policy adjusts the contribution of feed-forward network states during decoding while the backbone stays frozen."
og_type: "article"
lang: "en"
locale: "en_US"
lang_key: "en"
nav_locale: "en"
author_profile: false
reading_page: true
paper_authors:
  - Ruochang Li
  - Pengcheng Huang
  - Zhenghao Liu
  - Yukun Yan
  - Huiyuan Xie
  - Yu Gu
  - Ge Yu
  - Maosong Sun
citation_fields:
  publication_date: "2026/06/26"
  arxiv_id: "2606.27786"
  doi: "10.48550/arXiv.2606.27786"
citation_bibtex: "https://arxiv.org/bibtex/2606.27786v3"
---

# SPARK: Adaptive Parametric Knowledge Participation for Faithful Retrieval-Augmented Generation

Ruochang Li, Pengcheng Huang, Zhenghao Liu, Yukun Yan, Huiyuan Xie, Yu Gu, Ge Yu, Maosong Sun

**arXiv preprint**

[arXiv](https://arxiv.org/abs/2606.27786) · [Code](https://github.com/OpenBMB/SPARK) · [Hugging Face](https://huggingface.co/papers/2606.27786) · [ORKG](https://orkg.org/papers/R1994772) · [Full text (arXiv HTML)](https://arxiv.org/html/2606.27786)

SPARK studies how a retrieval-augmented language model handles conflicts between retrieved evidence and its parametric knowledge. A lightweight policy adjusts the contribution of feed-forward network states during decoding while the backbone stays frozen.

## How the participation policy works

The policy learns to regulate feed-forward contributions with a faithfulness-oriented reward. The experiments report contextual faithfulness across six datasets. A separate analysis compares cases where the retrieved evidence is accurate with cases where the model's closed-book answer is accurate. [Source](https://arxiv.org/html/2606.27786v3)

## Adapting to reliable and misleading retrieval

| Approach | Where it intervenes |
| --- | --- |
| [ParamMute](https://doi.org/10.52202/085713-3356) | Identifies feed-forward layers associated with unfaithful answers and combines activation suppression with preference-based adaptation. |
| [FIDES](https://arxiv.org/abs/2606.05644) | Uses signals from the output, hidden representations, and prediction trajectory to set intervention strength during decoding. |
| [SPARK](https://arxiv.org/html/2606.27786v3#S4) | Learns a lightweight policy that adjusts feed-forward contributions by layer and decoding step while keeping the backbone frozen. |

When comparing these interventions, distinguish inaccurate parametric memory with correct retrieved context from correct memory with misleading retrieved context. [Section 6.3](https://arxiv.org/html/2606.27786v3#S6.SS3) reports the cases separately. The papers use different conflict subsets and evaluation protocols.

## Earlier preprint

The first arXiv version was titled *SHIFT: Gate-Modulated Activation Steering for Knowledge Conflict Mitigation in Retrieval-Augmented Generation*. [Source](https://arxiv.org/abs/2606.27786v1)

DOI [10.48550/arXiv.2606.27786](https://doi.org/10.48550/arXiv.2606.27786) · [BibTeX]({{ page.citation_bibtex }})

[Research guide on conflicts between model memory and retrieved evidence](/rag-knowledge-conflicts/)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "@id": "https://doi.org/10.48550/arXiv.2606.27786",
  "headline": "SPARK: Adaptive Parametric Knowledge Participation for Faithful Retrieval-Augmented Generation",
  "description": "SPARK studies how a retrieval-augmented language model handles conflicts between retrieved evidence and its parametric knowledge. A lightweight policy adjusts the contribution of feed-forward network states during decoding while the backbone stays frozen.",
  "inLanguage": "en",
  "author": [{% for name in page.paper_authors %}{"@type": "Person", "name": {{ name | jsonify }}}{% unless forloop.last %}, {% endunless %}{% endfor %}],
  "identifier": {
    "@type": "PropertyValue",
    "propertyID": "DOI",
    "value": "10.48550/arXiv.2606.27786"
  },
  "sameAs": [
    "https://arxiv.org/abs/2606.27786"
  ],
  "mainEntityOfPage": "https://passionate11.github.io/papers/spark/",
  "datePublished": "2026-06-26"
}
</script>
