---
layout: research-dataset
permalink: /research-data/edge-cloud-agent-tasks/
title: EC²-Bench (EC2-Bench)
description: EC²-Bench contains 128 English and Chinese digital-workspace tasks for evaluating local agents that consult cloud models. The task index connects completion and resource-use measurements with privacy annotations available for 100 tasks.
dataset_key: edge_cloud_agent_tasks
paper_title: 'Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration in LLM Agent Execution'
paper_resource: https://arxiv.org/abs/2610.17816
paper_resource_label: Paper on arXiv
lang: en
locale: en_US
lang_key: en
nav_locale: en
author_profile: false
reading_page: true
---

## Which files does an experiment need?

The task index gives the prompt, grading criteria, language and number of annotated sensitivity units for each task. Use it to select a common set of tasks before comparing local execution, delegation and cloud advice. Report the denominator when computing privacy exposure across annotated tasks.

The executable workspaces and graders are separate from the index. The data repository preserves the `ACE_Bench` workspace name. For running an experiment, record both the dataset revision and the runner commit.

[Browse the workspaces](https://huggingface.co/datasets/chengpingan/EC2-Bench/tree/main/workspace) · [Runner and evaluation instructions](https://github.com/OpenBMB/EC2-Bench#quick-start)
