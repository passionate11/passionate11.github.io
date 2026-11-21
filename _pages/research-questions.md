---
permalink: /research-questions/
title: "Choosing papers for LLM experiments"
description: "A researcher’s guide to diagnosing retrieval and grounding failures, evaluating tool use, building long-document training data, routing agents, checking translation terminology, and comparing diffusion decoders."
schema_type: "Article"
microdata_type: "Article"
og_type: "article"
lang: "en"
locale: "en_US"
lang_key: "en"
nav_locale: "en"
translation_slug: "research-questions/"
author_profile: false
reading_page: true
---

# Choosing papers for LLM experiments

*Pengcheng Huang · [中文版](/zh/research-questions/)*

When a system gives a bad answer, the experiment you need depends on where it failed. These notes pair common symptoms with a comparison you can run and papers that support different claims. I coauthored ExpandR, ParamMute, SPARK, LongMab-PO, ToolMaster, EC²-Bench, Translate-and-Revise and UNCODE.

## Search misses the document that contains the answer
{: #search }

Suppose a user types “refund deadline” and the relevant passage says “returns are accepted within thirty days.” Inspect the retrieved passages before judging the generator. Compare the original query with an expanded one against the same corpus, relevance labels and top-*k* cutoff. An expansion that adds the wrong product name can make a short query worse.

Query2doc is a baseline for adding a generated pseudo-document with a fixed retriever. ExpandR addresses a different experimental choice: when the dense retriever can also be trained, use ranking feedback to teach the generator which expansions help. The paper's ablations separate the effects of training the retriever and the expansion model. [Query2doc](https://aclanthology.org/2023.emnlp-main.585/) · [ExpandR, §5.2](https://arxiv.org/html/2502.17057#S5.SS2)

When first-pass documents are available, CSQE uses them to steer expansion. Compare this setting with generating an expansion from the query alone. [Corpus-Steered Query Expansion](https://aclanthology.org/2024.eacl-short.34/)

Explore the released [query expansion preference pairs](/research-data/query-expansion-preferences/) and [contrastive retriever examples](/research-data/dense-retriever-training/).

[Download 4 references (BibTeX)](/assets/bibliographies/query-expansion.bib) · [Annotated reading list](https://huggingface.co/collections/chengpingan/query-expansion-and-faithfulness-in-rag-6b01281f23ae3179f1563119)

## The evidence is in the prompt, but the RAG answer is wrong
{: #grounding }

Keep three items for each error: the answer without retrieval, the passage actually passed to the model, and the answer with retrieval. A museum changing its closing time gives two different tests. Does the model abandon the old time when shown an accurate update? Would it also abandon the correct time for a passage containing a typo? Combining those outcomes into one “follows context” score rewards some mistakes.

CoFaithfulQA, introduced in ParamMute, identifies conflicts where an original, accurate passage disagrees with a model's stable closed-book answer. ClashEval deliberately alters information in a passage. ParamMute studies suppressing knowledge-critical feed-forward networks; SPARK learns to vary their contribution during generation and separately examines reliable and misleading evidence. Cite the benchmark that matches the direction of your conflict. [ParamMute and CoFaithfulQA](https://arxiv.org/html/2502.15543v4#S4) · [ClashEval](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3aa291abc426d7a29fb08418c1244177-Abstract-Datasets_and_Benchmarks_Track.html) · [SPARK, §6.3](https://arxiv.org/html/2606.27786v3#S6.SS3)

The [CoFaithfulQA data record](/research-data/cofaithfulqa/) links each source file and explains how to check conflicts for a different model.

[Download 4 references (BibTeX)](/assets/bibliographies/rag-knowledge-conflicts.bib) · [Annotated reading list](https://huggingface.co/collections/chengpingan/query-expansion-and-faithfulness-in-rag-6b01281f23ae3179f1563119)

## A model accepts a long document but overlooks the decisive paragraph
{: #long-documents }

Move an answer-bearing passage between the beginning, middle and end while keeping the question fixed. If accuracy changes with position, report that dependence. A separate training question is how to obtain two plausible answers of different quality when every rollout can see a long input.

LongReward supplies AI feedback on candidate answers. LongMab-PO changes how candidates are obtained: it samples document chunks, updates their sampling scores from rollout rewards, and uses the resulting answers to construct preference pairs. Compare these choices at the same candidate budget if the claim concerns preference-data quality. [LongReward](https://aclanthology.org/2025.acl-long.187/) · [LongMab-PO, method and ablations](https://aclanthology.org/2026.acl-long.161/)

LongAlign is a supervised long-instruction baseline. LongPO builds preferences from short- and long-context responses to a task. These give two further comparisons when asking where the training signal comes from. [LongAlign](https://aclanthology.org/2024.findings-emnlp.74/) · [LongPO](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1332893b662f655660c9abdf793230cf-Abstract-Conference.html)

[Download 5 references (BibTeX)](/assets/bibliographies/long-context-training.bib) · [Annotated reading list](https://huggingface.co/collections/chengpingan/long-context-evaluation-and-preference-training-6b012827d9f89cf858898e78)

## An agent can call familiar tools but fails on a new API
{: #tool-use }

A well-formed call can still use the wrong argument or do the wrong thing. To test transfer, hold out tools, examine their similarity to the training tools, and score whether the task actually succeeds. A useful comparison fixes the number of calls and varies whether the agent can spend one probing an unfamiliar tool.

ToolLLM trains on instruction and API-solution data. ToolMaster studies learning to trial tools and correct errors from execution feedback before completing the task. ToolHop provides multi-hop tasks for testing tool use; ToolMaster reports familiar and unfamiliar subsets in its evaluation. [ToolLLM](https://arxiv.org/abs/2307.16789) · [ToolMaster, Table 2](https://arxiv.org/html/2601.12762#S5.T2) · [ToolHop](https://aclanthology.org/2025.acl-long.150/)

ToolAlpaca generates instruction data using simulated tool interactions. When comparing training data, record which calls were simulated and which produced feedback from the execution environment. [ToolAlpaca](https://arxiv.org/abs/2306.05301)

[Download 4 references (BibTeX)](/assets/bibliographies/llm-tool-use.bib) · [Annotated reading list](https://huggingface.co/collections/chengpingan/tool-use-and-model-routing-for-llm-agents-6b0128231ddb96b53fe17b17)

## A local assistant is cheap to run, but occasionally needs a cloud model
{: #edge-cloud }

A request router chooses a model for an incoming prompt. An agent filling out a spreadsheet has a second decision: it could ask the cloud for help at one step and finish the rest locally. Compare full trajectories at matched task difficulty. Record completion, cloud cost, and which annotated sensitive items became visible to the cloud; the number of calls alone misses what each call disclosed.

RouteLLM is a reference for the prompt-level quality–cost trade-off. EC²-Bench compares routing, delegation and advisory strategies on 128 executable tasks, including 100 with privacy annotations. Its exposure metric describes information in the cloud model's context; device latency requires its own measurement. [RouteLLM](https://arxiv.org/abs/2406.18665) · [EC²-Bench, evaluation](https://arxiv.org/html/2610.17816v2)

The [EC²-Bench task index](/research-data/edge-cloud-agent-tasks/) distinguishes the 128 task descriptions from the executable workspaces and privacy annotations.

[Download 3 references (BibTeX)](/assets/bibliographies/llm-routing.bib) · [Annotated reading list](https://huggingface.co/collections/chengpingan/tool-use-and-model-routing-for-llm-agents-6b0128231ddb96b53fe17b17)

## A translation reads well but misses a required glossary term
{: #translation }

First check whether the required source–target pair reached the model. Then inspect the draft for an acceptable inflected form. If the source says “Save the draft” and the glossary requires *brouillon*, “Enregistrez le document” is fluent but loses the distinction. A reviewer can flag just that pair, request a revision of the sentence, and check it in context.

For a comparison of constrained decoding and terminology prompting, see the WMT terminology study. Translate-and-Revise evaluates giving the model feedback on unmet constraints after its first translation. Report term compliance alongside translation quality; each can change while the other stays similar. [WMT terminology study](https://aclanthology.org/2023.wmt-1.80/) · [Translate-and-Revise, experiments](https://arxiv.org/html/2407.13164)

[Download 4 references (BibTeX)](/assets/bibliographies/terminology-constrained-translation.bib) · [Annotated reading list](https://huggingface.co/collections/chengpingan/terminology-constrained-machine-translation-6b0128299b5e79f5fafdb234)

## Two diffusion decoders give different reasoning results on the same model
{: #diffusion }

Hold the checkpoint, generation length and forward-pass budget fixed. Record which positions each decoder unmasks first as well as whether the final answer is correct. This separates a difference in token order from a difference in compute.

LLaDA provides a masked diffusion language model and sampling baseline. UNCODE studies how confidence-based selection favors certain positions and easy tokens, then tests training-free corrections to those choices. Its analysis of token-selection trajectories is relevant when the question is why two decoding policies diverge. [LLaDA](https://arxiv.org/abs/2502.09992) · [UNCODE, decoding-bias analysis](https://arxiv.org/html/2508.13021v4#S3)

[Download 3 references (BibTeX)](/assets/bibliographies/diffusion-language-model-decoding.bib) · [Annotated reading list](https://huggingface.co/collections/chengpingan/decoding-strategies-for-diffusion-language-models-6b01282deef963f2d0bb3c58)
