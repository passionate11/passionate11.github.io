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
paper_authors:
  - Xingjie Gao
  - Pengcheng Huang
  - Zhenghao Liu
  - Yukun Yan
  - Shuo Wang
  - Zulong Chen
  - Chen Qian
  - Ge Yu
  - Yu Gu
citation_fields:
  publication_date: "2026/01/19"
  arxiv_id: "2601.12762"
  doi: "10.48550/arXiv.2601.12762"
citation_bibtex: "https://arxiv.org/bibtex/2601.12762"
---

# Teaching LLMs to Learn Tool Trialing and Execution through Environment Interaction

Xingjie Gao, Pengcheng Huang, Zhenghao Liu, Yukun Yan, Shuo Wang, Zulong Chen, Chen Qian, Ge Yu, Yu Gu

**arXiv preprint**

[arXiv](https://arxiv.org/abs/2601.12762) · [Code](https://github.com/NEUIR/ToolMaster) · [Hugging Face](https://huggingface.co/papers/2601.12762) · [ORKG](https://orkg.org/papers/R1994784) · [Full text (arXiv HTML)](https://arxiv.org/html/2601.12762)

ToolMaster studies how language-model agents learn to use unfamiliar tools by interacting with an environment. A trial phase lets the agent probe available tools and use feedback before executing a task.

## Training for tool trialing and execution

The supervised stage uses teacher trajectories that include explicit tool trials and self-corrections. A subsequent stage uses Group Relative Policy Optimization to train trialing and execution jointly. The paper evaluates whether the learned behavior transfers to previously unseen tools. [Source](https://arxiv.org/html/2601.12762v1)

## Learning to call previously unseen tools

| Approach | Where the agent learns about an unfamiliar tool |
| --- | --- |
| [ToolLLM](https://arxiv.org/abs/2307.16789) | Collects successful multi-step API solutions with a search procedure, then uses the resulting instruction data to train a tool-using model. |
| [Simulated Trial and Error (STE)](https://aclanthology.org/2024.acl-long.570/) | Simulates useful situations for a tool, interacts with it, and stores lessons from the execution feedback for later use. |
| [ToolMaster](https://arxiv.org/html/2601.12762v1#S3) | Trains an explicit trial phase before task execution. Supervised trajectories model tool probes and self-correction, followed by reinforcement learning over trial and execution together. |

The table compares how methods acquire tool experience. Each paper uses its own evaluation setting.

## Evaluating generalization on ToolHop

[ToolHop](https://aclanthology.org/2025.acl-long.150/) pairs multi-hop questions with interdependent, locally executable tools. ToolMaster uses it as an out-of-domain test. Its [Table 2](https://arxiv.org/html/2601.12762v1#S5.T2) reports answer correctness on ToolHop and Solvable Pass Rate on TMDB. The [ToolHop dataset card](https://huggingface.co/datasets/bytedance-research/ToolHop) documents the original benchmark and its evaluation settings.

[Section 5.4 and Figure 4](https://arxiv.org/html/2601.12762v1#S5.SS4) compare ToolMaster with an ablation trained on successful tool-use trajectories. The analysis groups ToolHop tools by how similar their documentation is to that of tools seen during training. A query is treated as unfamiliar if any required tool falls into the low-similarity group, and as familiar if every required tool falls into the high-similarity group.

## Released trajectories and checkpoint

The [released SFT file](https://github.com/NEUIR/ToolMaster/blob/3bd49c8290a1a139b1a12371826f2911afa422e0/data/for_sft/G123_sft_train_data.json) contains 1,444 query records, each with one conversation. [Section 4](https://arxiv.org/html/2601.12762v1#S4) reports selecting 1,500 ToolBench queries to construct the SFT dataset. The two counts refer to the released file and the paper's query selection, respectively. The [ToolMaster-7B checkpoint](https://huggingface.co/Kfkcome/ToolMaster-7B) is linked from the official repository.

DOI [10.48550/arXiv.2601.12762](https://doi.org/10.48550/arXiv.2601.12762) · [BibTeX]({{ page.citation_bibtex }})

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "@id": "https://doi.org/10.48550/arXiv.2601.12762",
  "headline": "Teaching LLMs to Learn Tool Trialing and Execution through Environment Interaction",
  "description": "ToolMaster studies how language-model agents learn to use unfamiliar tools by interacting with an environment. A trial phase lets the agent probe available tools and use feedback before executing a task.",
  "inLanguage": "en",
  "author": [{% for name in page.paper_authors %}{"@type": "Person", "name": {{ name | jsonify }}}{% unless forloop.last %}, {% endunless %}{% endfor %}],
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
