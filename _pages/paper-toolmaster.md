---
permalink: /papers/toolmaster/
title: "Teaching LLMs to Learn Tool Trialing and Execution through Environment Interaction"
description: "ToolMaster studies how language-model agents learn to use unfamiliar tools by interacting with an environment. A trial phase lets the agent probe available tools and use feedback before executing a task."
og_type: "article"
lang: "en"
locale: "en_US"
lang_key: "en"
nav_locale: "en"
author_profile: false
reading_page: true
---

# Teaching LLMs to Learn Tool Trialing and Execution through Environment Interaction

Xingjie Gao, Pengcheng Huang, Zhenghao Liu, Yukun Yan, Shuo Wang, Zulong Chen, Chen Qian, Ge Yu, Yu Gu

**arXiv preprint**

[arXiv](https://arxiv.org/abs/2601.12762) · [Code](https://github.com/NEUIR/ToolMaster) · [Hugging Face](https://huggingface.co/papers/2601.12762) · [ORKG](https://orkg.org/papers/R1994784)

ToolMaster studies how language-model agents learn to use unfamiliar tools by interacting with an environment. A trial phase lets the agent probe available tools and use feedback before executing a task.

## Training for tool trialing and execution

The supervised stage uses teacher trajectories that include explicit tool trials and self-corrections. A subsequent stage uses Group Relative Policy Optimization to train trialing and execution jointly. The paper evaluates whether the learned behavior transfers to previously unseen tools. [Source](https://arxiv.org/html/2601.12762v1)

## Learning to call previously unseen tools

| Approach | Where the agent learns about an unfamiliar tool |
| --- | --- |
| [ToolLLM](https://arxiv.org/abs/2307.16789) | Collects successful multi-step API solutions with a search procedure, then uses the resulting instruction data to train a tool-using model. |
| [Simulated Trial and Error (STE)](https://aclanthology.org/2024.acl-long.570/) | Simulates useful situations for a tool, interacts with it, and stores lessons from the execution feedback for later use. |
| [ToolMaster](https://arxiv.org/html/2601.12762v1#S3) | Trains an explicit trial phase before task execution. Supervised trajectories model tool probes and self-correction, followed by reinforcement learning over trial and execution together. |

For out-of-domain tool use, [Section 5.3 and Table 2](https://arxiv.org/html/2601.12762v1#S5.SS3) report results on TMDB and ToolHop. [Section 5.4](https://arxiv.org/html/2601.12762v1#S5.SS4) breaks ToolHop results down by similarity to tools seen during training. The table above compares how methods acquire tool experience. Each paper uses its own evaluation setting.

DOI [10.48550/arXiv.2601.12762](https://doi.org/10.48550/arXiv.2601.12762) · [BibTeX](/selected-papers.bib)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "@id": "https://doi.org/10.48550/arXiv.2601.12762",
  "headline": "Teaching LLMs to Learn Tool Trialing and Execution through Environment Interaction",
  "description": "ToolMaster studies how language-model agents learn to use unfamiliar tools by interacting with an environment. A trial phase lets the agent probe available tools and use feedback before executing a task.",
  "inLanguage": "en",
  "author": [
    {
      "@type": "Person",
      "name": "Xingjie Gao"
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
      "name": "Yukun Yan"
    },
    {
      "@type": "Person",
      "name": "Shuo Wang"
    },
    {
      "@type": "Person",
      "name": "Zulong Chen"
    },
    {
      "@type": "Person",
      "name": "Chen Qian"
    },
    {
      "@type": "Person",
      "name": "Ge Yu"
    },
    {
      "@type": "Person",
      "name": "Yu Gu"
    }
  ],
  "identifier": {
    "@type": "PropertyValue",
    "propertyID": "DOI",
    "value": "10.48550/arXiv.2601.12762"
  },
  "sameAs": [
    "https://arxiv.org/abs/2601.12762"
  ],
  "mainEntityOfPage": "https://passionate11.github.io/papers/toolmaster/",
  "datePublished": "2026-01-19"
}
</script>
