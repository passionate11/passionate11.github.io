---
layout: research-dataset
permalink: /research-data/tool-trialing-trajectories/
title: ToolMaster supervised tool-use trajectories
description: The ToolMaster supervised fine-tuning release contains 1,444 queries for learning to try tools and execute them from environment feedback. It is stored as a JSON object keyed by query ID.
dataset_key: tool_trialing_trajectories
paper_title: Teaching LLMs to Learn Tool Trialing and Execution through Environment Interaction
paper_resource: https://arxiv.org/abs/2601.12762
paper_resource_label: Paper on arXiv
source_label: Authors’ GitHub data directory
lang: en
locale: en_US
lang_key: en
nav_locale: en
reading_page: true
author_profile: false
---

## How do I read the release?

Read the JSON object and iterate over its values. Each record contains `query`, `query_id`, `tool_doc` and `instances`. Keep the tool descriptions alongside the interactions when comparing how a model responds to an unfamiliar API.

The paper reports selecting 1,500 ToolBench queries during construction. The 1,444 count here describes the public SFT file. [Data construction in Section 4](https://arxiv.org/html/2601.12762v1#S4)
