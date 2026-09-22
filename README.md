# Awesome OS LLM

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Open-weight large language models, and the open stack people use to run, train, evaluate, and apply them.

An **open-source LLM**, in this list, is a language model whose **weights you can download**, plus the open runtimes, training code, evals, datasets, and apps built to use those weights. It is not "an LLM that acts as an operating system." That topic has its own catalog, [awesome-llm-os](https://github.com/bilalonur/awesome-llm-os).

Open weights are older than the 2023 Llama moment. GPT-2 (2019) shipped weights and sampling code. EleutherAI's GPT-Neo, GPT-J, GPT-NeoX, and Pythia made training runs something other people could study. BigScience BLOOM (2022) and Meta OPT (2022) were large public checkpoints under research-style or use-restricted licenses. Meta's LLaMA paper (February 2023) described a non-commercial research release whose weights then circulated widely; that license was not an OSI open-source license. Llama 2 replaced it with a custom commercial license. Permissive grants (Apache-2.0 or MIT) on strong models — Mistral 7B, much of Qwen, DeepSeek, OLMo, Phi, Gemma 4, gpt-oss, and Meta's later Muse Glimmer — came later, and they are still uneven across families. **Downloadable weights, published training code, published data, and an OSI license are four different claims.** Each bullet says which claim the linked page actually supports.

**247 unique links** · Ingested **2026-09-22 PT** · This compilation is [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (linked projects keep their own licenses).

Deduplicated by normalized URL. Regenerate with `python3 build.py` from [`links.json`](links.json). Counts: [`stats.txt`](stats.txt). What was consulted: [`SOURCES.md`](SOURCES.md). Notes that did not clear the README bar: [`discoveries/`](discoveries/).

### Start here

- [llama.cpp](https://github.com/ggml-org/llama.cpp) — The C/C++ engine most local GGUF setups actually run.
- [Ollama](https://github.com/ollama/ollama) — The shortest path from a laptop to a local OpenAI-compatible server.
- [Hugging Face Hub](https://huggingface.co/models) — Where the weight files live; read the license on the model card, not the org's reputation.
- [OLMo](https://github.com/allenai/OLMo) — Weights, training code, and pretraining data, which is a higher bar than weights alone.
- [Landmark open models](#landmark-open-models) — Families, with the license stated on the page that was checked.
- [gpt-oss](https://github.com/openai/gpt-oss) — OpenAI's Apache-2.0 open-weight models (20B and 120B), if you want a permissive checkpoint from a lab that mostly ships closed models.
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — The harness behind a large share of open-model numbers.
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) — The forum where local-model practice shows up before it shows up in papers.

## Contents

- [Landmark open models](#landmark-open-models) (92)
  - [Early open weights](#early-open-weights) (8)
  - [Meta Llama](#meta-llama) (10)
  - [Mistral](#mistral) (7)
  - [Qwen](#qwen) (12)
  - [Google Gemma](#google-gemma) (7)
  - [DeepSeek](#deepseek) (7)
  - [Microsoft Phi](#microsoft-phi) (4)
  - [Allen Institute OLMo](#allen-institute-olmo) (6)
  - [Other families](#other-families) (31)
- [Runtimes and local serving](#runtimes-and-local-serving) (33)
  - [Inference engines](#inference-engines) (16)
  - [Local apps and front ends](#local-apps-and-front-ends) (11)
  - [On-device and edge](#on-device-and-edge) (6)
- [Training, finetune and alignment](#training-finetune-and-alignment) (35)
  - [Finetune and post-training](#finetune-and-post-training) (12)
  - [Pretraining](#pretraining) (13)
  - [Preference, RL and data](#preference-rl-and-data) (10)
- [Use cases](#use-cases) (30)
  - [Agents and coding](#agents-and-coding) (13)
  - [RAG and knowledge](#rag-and-knowledge) (9)
  - [Creative and local chat](#creative-and-local-chat) (1)
  - [Voice](#voice) (3)
  - [Structured output](#structured-output) (4)
- [Evals and papers](#evals-and-papers) (29)
  - [Leaderboards and harnesses](#leaderboards-and-harnesses) (16)
  - [Papers](#papers) (13)
- [Datasets](#datasets) (12)
- [Docs and essays](#docs-and-essays) (8)
- [Awesome lists and indexes](#awesome-lists-and-indexes) (5)
- [Community](#community) (3)
- [Sources](#sources)
- [Contributing](#contributing)
- [License](#license)

## Landmark open models

Families with public weights. A bullet names the license on the linked card or repo. Open weights are not the same thing as an OSI license, and a finetune keeps the base model's terms.

### Early open weights

Public checkpoints from before the Llama license era. Several are research-licensed or use-restricted.

- [GPT-2](https://github.com/openai/gpt-2) — OpenAI's 2019 weight-and-code release for GPT-2; the repo is archived, and later GPT models were not released this way.
- [GPT-Neo](https://github.com/EleutherAI/gpt-neo) — Archived EleutherAI code for GPT-2- and GPT-3-style models, MIT-licensed, from the effort that made open GPT reproductions a research project.
- [GPT-J-6B](https://huggingface.co/EleutherAI/gpt-j-6b) — EleutherAI's 6B checkpoint, Apache-2.0, trained with the mesh-transformer-jax codebase and widely used before Llama.
- [GPT-NeoX-20B](https://huggingface.co/EleutherAI/gpt-neox-20b) — EleutherAI's 20B checkpoint, Apache-2.0; the training stack is the separate gpt-neox repo.
- [Pythia](https://github.com/EleutherAI/pythia) — Apache-2.0 suite of models trained in public so scaling and training dynamics can be compared on the same data order.
- [BLOOM](https://huggingface.co/bigscience/bloom) — BigScience's 176B multilingual model under the BigScience RAIL license, which is open access with use restrictions, not Apache-2.0 or MIT.
- [OPT-66B](https://huggingface.co/facebook/opt-66b) — Meta's 2022 Open Pretrained Transformer checkpoint; the model card marks the license as non-commercial.
- [GLM-130B](https://github.com/zai-org/GLM-130B) — Apache-2.0 code repo for the 2022 bilingual 130B model from Tsinghua, published as an ICLR 2023 open bilingual pretrained model.

### Meta Llama

Meta's Llama line. Every shipping generation here uses a Llama community license, not Apache-2.0 or MIT.

- [LLaMA paper](https://arxiv.org/abs/2302.13971) — The February 2023 paper for Meta's original LLaMA release, whose weights shipped under a non-commercial research license rather than an OSI license.
- [Llama inference code](https://github.com/meta-llama/llama) — Meta's inference code for Llama models; it is not a grant to ignore the license on the checkpoint you download.
- [Llama 2 7B](https://huggingface.co/meta-llama/Llama-2-7b-hf) — 7B base weights under the Llama 2 Community License, a custom license with a monthly-active-user threshold, not Apache-2.0.
- [Llama 3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B) — 8B base model under the Llama 3.1 Community License.
- [Llama 3.2 1B](https://huggingface.co/meta-llama/Llama-3.2-1B) — Small Llama 3.2 text model under the Llama 3.2 license, in a size people actually run on a laptop.
- [Llama 3.3 70B Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) — 70B instruction model under the Llama 3.3 Community License.
- [Llama 4 Scout](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) — Multimodal instruct Mixture-of-Experts (17B-16E in the model id) under the Llama 4 license named on the card, not an OSI license.
- [Llama 4 Maverick](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) — Larger-expert Llama 4 multimodal instruct model (17B-128E in the model id), same Llama 4 license family as Scout.
- [Llama.com](https://www.llama.com) — Meta's Llama site for current docs and license terms; the page is the place to re-read the grant before you ship.
- [Code Llama](https://github.com/meta-llama/codellama) — Meta's inference repo for Code Llama; weight terms follow the Llama license on the checkpoint, and the repository's last push was 2024-08-12.

### Mistral

Mistral's open-weight line. Apache-2.0 and the Mistral Research License both appear; the bullet says which.

- [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-v0.1) — Apache-2.0 7B pretrained model whose 2023 release made permissive local weights a default choice rather than a research exception.
- [Mixtral 8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) — Apache-2.0 sparse mixture-of-experts model, eight experts with two active per token.
- [Mistral Small 24B Instruct](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) — Apache-2.0 24B instruct model in the size range a single high-memory GPU can hold.
- [Devstral Small](https://huggingface.co/mistralai/Devstral-Small-2505) — Apache-2.0 coding model in Mistral's Small line.
- [Magistral Small](https://huggingface.co/mistralai/Magistral-Small-2506) — Apache-2.0 reasoning model in Mistral's Small line.
- [Ministral 8B Instruct](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410) — 8B instruct model under the Mistral Research License (MRL-0.1), not Apache-2.0.
- [Mistral Large 3](https://huggingface.co/mistralai/Mistral-Large-3) — Apache-2.0 multimodal mixture-of-experts instruct model, 675B total and 41B active, with FP8 and NVFP4 checkpoints called out on the card for single-node serving.

### Qwen

Alibaba's Qwen line. Many dense and small MoE checkpoints are Apache-2.0; the largest Qwen3.8 release is not.

- [Qwen](https://github.com/QwenLM/Qwen) — Apache-2.0 repo for the original Qwen chat and pretrained models from Alibaba Cloud.
- [Qwen2.5](https://github.com/QwenLM/Qwen2.5) — Official Qwen2.5 repo; the 7B base weights on Hugging Face are Apache-2.0.
- [Qwen2.5-7B](https://huggingface.co/Qwen/Qwen2.5-7B) — Apache-2.0 dense base model from the Qwen2.5 generation.
- [Qwen2.5-Coder 32B Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) — Apache-2.0 code instruct model that is still a practical local coder.
- [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) — Apache-2.0 dense model from the Qwen3 generation.
- [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) — Apache-2.0 mixture-of-experts Qwen3 model, 235B total with 22B active.
- [Qwen3-Coder 480B-A35B Instruct](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct) — Apache-2.0 code instruct mixture-of-experts model, 480B total with 35B active.
- [Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B) — Apache-2.0 vision-language model; the Qwen3.8 repo's news log dates the 27B weights in this generation to 2026-02-24.
- [Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) — Apache-2.0 vision-language model in the Qwen3.6 line.
- [Qwen3.8](https://github.com/QwenLM/Qwen3.8) — Official repo covering Qwen3.5 through Qwen3.8; the repo is Apache-2.0, while the 2.4T-A95B weights use a separate license named qwen3.8-max.
- [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) — Apache-2.0 27B checkpoint; the project news log dates these weights to 2026-08-14.
- [Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) — The large Qwen3.8 checkpoint under the license named qwen3.8-max on the card, which is separate from the Apache-2.0 grant on the 27B weights; the project news log dates it to 2026-08-12.

### Google Gemma

Gemma 1 through 3 use the Gemma license. Gemma 4's model cards checked here say Apache-2.0.

- [Gemma library](https://github.com/google-deepmind/gemma) — Google DeepMind's Apache-2.0 library for running Gemma; the library license is not the license of every Gemma checkpoint.
- [Gemma 7B](https://huggingface.co/google/gemma-7b) — First-generation Gemma 7B under the Gemma license, not Apache-2.0.
- [Gemma 2 9B](https://huggingface.co/google/gemma-2-9b) — Gemma 2 9B base model under the Gemma license.
- [Gemma 3 27B IT](https://huggingface.co/google/gemma-3-27b-it) — Multimodal Gemma 3 instruct model under the Gemma license.
- [Gemma 3n E4B](https://huggingface.co/google/gemma-3n-E4B-it) — Mobile-oriented Gemma 3n checkpoint under the Gemma license.
- [Gemma 4 31B IT](https://huggingface.co/google/gemma-4-31b-it) — Gemma 4 multimodal instruct model whose card states Apache-2.0, a change from the Gemma terms used on Gemma 1 through 3.
- [Gemma 4 E4B](https://huggingface.co/google/gemma-4-e4b-it) — Smaller Apache-2.0 Gemma 4 model; the family card says the E2B, E4B, and 12B sizes also take audio, unlike the text-and-image-only larger sizes.

### DeepSeek

DeepSeek publishes weights. MIT on a GitHub repo is not automatically the license file sitting next to every checkpoint.

- [DeepSeek-V2](https://github.com/deepseek-ai/DeepSeek-V2) — Mixture-of-experts model that introduced the MLA and DeepSeekMoE designs later reused in V3; the Hugging Face card's license tag is other, so do not assume the V3 MIT grant applies.
- [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) — MIT-licensed repo for the 671B mixture-of-experts model (37B activated) with weights on Hugging Face and a public technical report.
- [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) — MIT-licensed reasoning-model release trained with large-scale reinforcement learning; the paper is arXiv:2501.12948.
- [DeepSeek-V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2) — MIT-licensed DeepSeek-V3.2 weights on Hugging Face.
- [DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) — MIT-licensed V4-Pro weights; the card links the technical report arXiv:2606.19348, and there is no deepseek-ai/DeepSeek-V4 GitHub repository.
- [DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) — MIT-licensed code-model repository; the Lite instruct checkpoint on Hugging Face carries a file named deepseek-license, so read that file before redistributing the weights.
- [DeepSeek-Math](https://github.com/deepseek-ai/DeepSeek-Math) — MIT-licensed math models and the accompanying training code.

### Microsoft Phi

Microsoft's small models. The cards checked here are MIT.

- [Phi-2](https://huggingface.co/microsoft/phi-2) — MIT-licensed small model from Microsoft's Phi line.
- [Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) — MIT-licensed Phi-3 mini instruct model in the 4k-context variant.
- [Phi-4](https://huggingface.co/microsoft/phi-4) — MIT-licensed Phi-4 weights.
- [Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct) — MIT-licensed smaller Phi-4 instruct model.

### Allen Institute OLMo

The rare stack that releases weights, training code, and pretraining data under Apache-2.0 / ODC-By rather than weights alone.

- [OLMo project](https://allenai.org/olmo) — Allen Institute project page for OLMo, the family released with weights, code, and data rather than weights alone.
- [OLMo](https://github.com/allenai/OLMo) — Apache-2.0 modeling, training, eval, and inference code for the original OLMo release.
- [OLMo-7B](https://huggingface.co/allenai/OLMo-7B) — Apache-2.0 original OLMo 7B checkpoint.
- [OLMo 2 7B](https://huggingface.co/allenai/OLMo-2-1124-7B) — Apache-2.0 OLMo 2 7B checkpoint.
- [OLMo 2 32B](https://huggingface.co/allenai/OLMo-2-0325-32B) — Apache-2.0 OLMo 2 32B checkpoint.
- [OLMoE-1B-7B](https://huggingface.co/allenai/OLMoE-1B-7B-0924) — Apache-2.0 open mixture-of-experts model, 1B active and 7B total, with the training recipe published alongside the weights.

### Other families

Other real open-weight families. Sorted alphabetically. License caveats are the point of the line.

- [Baichuan 2](https://github.com/baichuan-inc/Baichuan2) — Apache-2.0 code for Baichuan's bilingual models; confirm the weight license on the checkpoint you download.
- [Command A](https://huggingface.co/CohereLabs/c4ai-command-a-03-2025) — Cohere Command A weights under CC-BY-NC-4.0, which is not a commercial-use license.
- [Command R+](https://huggingface.co/CohereForAI/c4ai-command-r-plus) — Command R+ weights under CC-BY-NC-4.0; open weights here means non-commercial.
- [Falcon 3 10B Instruct](https://huggingface.co/tiiuae/Falcon3-10B-Instruct) — Instruct model under the Falcon LLM license linked from the card, not Apache-2.0.
- [Falcon-7B](https://huggingface.co/tiiuae/falcon-7b) — Apache-2.0 7B model from TII; Falcon-180B is a different checkpoint and is not Apache-2.0.
- [GLM-4](https://github.com/zai-org/GLM-4) — Apache-2.0 code repository for the GLM-4 series of multilingual multimodal chat models.
- [GLM-4.5](https://huggingface.co/zai-org/GLM-4.5) — MIT-licensed GLM-4.5 weights aimed at agent, reasoning, and coding use.
- [GLM-5](https://github.com/zai-org/GLM-5) — Apache-2.0 repository for GLM-5; its homepage link points at the GLM-5.2 blog post.
- [GLM-5.2](https://huggingface.co/zai-org/GLM-5.2) — MIT-licensed GLM-5.2 weights; the card points at a newer GLM-5.3 checkpoint published under a license named glm-5.3, not MIT.
- [gpt-oss](https://github.com/openai/gpt-oss) — OpenAI's Apache-2.0 open-weight models, gpt-oss-120b and gpt-oss-20b, with weights on Hugging Face and a project site at gpt-oss.com.
- [Granite 3.1 8B Instruct](https://huggingface.co/ibm-granite/granite-3.1-8b-instruct) — IBM Granite instruct model under Apache-2.0.
- [Grok-1](https://github.com/xai-org/grok-1) — Apache-2.0 weight release of xAI's 314B mixture-of-experts; a research artifact, not a practical local chat model.
- [Hermes 3 Llama 3.1 8B](https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B) — Community finetune whose card is under the Llama 3 license, so the base model's restrictions still apply.
- [InternLM](https://github.com/InternLM/InternLM) — Apache-2.0 code for the InternLM series; the internlm2.5 7B chat card checked on ingest uses a non-Apache license tag, so read the checkpoint you download.
- [Jamba v0.1](https://huggingface.co/ai21labs/Jamba-v0.1) — Apache-2.0 hybrid Transformer-Mamba model; later Jamba cards use other licenses, and this entry is only v0.1.
- [Kimi K2 Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct) — Moonshot's open-weight K2 instruct model under a modified MIT license.
- [Kimi K2.5](https://github.com/MoonshotAI/Kimi-K2.5) — Open-weight visual and agentic Kimi model under a modified MIT license.
- [Kimi K3](https://github.com/MoonshotAI/Kimi-K3) — Open-weight 2.8T multimodal mixture-of-experts under the Kimi K3 License, which adds a Model-as-a-Service revenue clause and an attribution clause above 100 million monthly users or 20 million dollars of monthly revenue.
- [LFM2.5 1.2B Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct) — Small Liquid AI instruct model for edge hardware, under the license named lfm1.0 on the card, not Apache-2.0 or MIT.
- [Mamba](https://github.com/state-spaces/mamba) — Apache-2.0 implementation of the Mamba state-space architecture used by some open language models.
- [MiniCPM4-8B](https://huggingface.co/openbmb/MiniCPM4-8B) — Apache-2.0 on-device-oriented model from OpenBMB.
- [MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1) — Apache-2.0 hybrid-attention reasoning model from MiniMax.
- [Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) — Apache-2.0 30B multimodal model from Meta Superintelligence Lab; the card dates the release to August 2026 and describes it as distilled from Muse Spark.
- [Nemotron 70B Instruct](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Instruct-HF) — Llama-3.1-based Nemotron instruct model; the card stays on the Llama 3.1 license.
- [Nemotron Nano 9B v2](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2) — NVIDIA's 9B open model under the NVIDIA Open Model License, not Apache-2.0.
- [RWKV](https://github.com/BlinkDL/RWKV-LM) — Apache-2.0 linear-time RNN language-model line; the repository is at the RWKV-7 generation.
- [SmolLM2 1.7B Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct) — Apache-2.0 small instruct model from Hugging Face, sized to run without a datacenter GPU.
- [SmolLM3 3B](https://huggingface.co/HuggingFaceTB/SmolLM3-3B) — Apache-2.0 3B model with a public training recipe in the SmolLM repository.
- [Stable LM 2 12B](https://huggingface.co/stabilityai/stablelm-2-12b) — 12B Stability model whose card sends commercial use to Stability's own license rather than Apache-2.0.
- [StarCoder2](https://github.com/bigcode-project/starcoder2) — BigCode's code-model release; the 15B weights use the BigCode OpenRAIL-M license, which adds use restrictions on top of an open grant.
- [Yi-1.5](https://github.com/01-ai/Yi-1.5) — Apache-2.0 upgrade of 01.AI's Yi models, with the project describing stronger coding, math, reasoning, and instruction following than Yi.

## Runtimes and local serving

Ways to run weights on hardware you control. Hosted-only APIs are left out.

### Inference engines

Servers and libraries that load weights and produce tokens.

- [candle](https://github.com/huggingface/candle) — Apache-2.0 minimalist ML framework in Rust, with LLM inference examples in-tree.
- [ExLlamaV2](https://github.com/turboderp-org/exllamav2) — MIT-licensed GPU inference library for running quantized LLMs on consumer NVIDIA cards.
- [gemma.cpp](https://github.com/google/gemma.cpp) — Apache-2.0 standalone C++ inference engine for Gemma models.
- [LightLLM](https://github.com/ModelTC/LightLLM) — Apache-2.0 Python serving framework aimed at high-throughput GPU inference.
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) — MIT-licensed Python bindings for llama.cpp, including an OpenAI-compatible server.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) — MIT-licensed C/C++ inference engine and the GGUF ecosystem most local setups are built on; the canonical repo is ggml-org, not the older ggerganov mirror.
- [llamafile](https://github.com/mozilla-ai/llamafile) — Single-file local LLM runner; the LICENSE text is Apache-2.0 even though GitHub's SPDX field is unset.
- [LMDeploy](https://github.com/InternLM/lmdeploy) — Apache-2.0 toolkit for compressing, deploying, and serving LLMs, from the InternLM project.
- [mistral.rs](https://github.com/EricLBuehler/mistral.rs) — MIT-licensed Rust inference engine for LLMs.
- [MLX-LM](https://github.com/ml-explore/mlx-lm) — MIT-licensed library for running LLMs on Apple silicon through MLX.
- [Ollama](https://github.com/ollama/ollama) — MIT-licensed local runner and OpenAI-compatible server; the library tag is not a license, so check the upstream model card.
- [SGLang](https://github.com/sgl-project/sglang) — Apache-2.0 serving framework for language and multimodal models, used when vLLM-style throughput is the goal.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) — NVIDIA's Python and C++ stack for LLM inference on NVIDIA GPUs; the LICENSE text says Apache-2.0.
- [Text Generation Inference](https://github.com/huggingface/text-generation-inference) — Hugging Face's LLM server; the repository is archived.
- [Transformers](https://github.com/huggingface/transformers) — Apache-2.0 model-definition library that both loads open checkpoints for inference and defines them for training.
- [vLLM](https://github.com/vllm-project/vllm) — Apache-2.0 high-throughput inference and serving engine, and the usual server for large open MoE models.

### Local apps and front ends

Desktop and web apps in front of a local engine. Some are permissively licensed; Open WebUI is not plain BSD.

- [chat-ui](https://github.com/huggingface/chat-ui) — Apache-2.0 codebase behind HuggingChat, self-hostable against an OpenAI-compatible local server.
- [exo](https://github.com/exo-explore/exo) — Apache-2.0 runtime for splitting a model across machines you already have.
- [GPT4All](https://github.com/nomic-ai/gpt4all) — MIT-licensed desktop app for running local LLMs, including commercial use as stated by the project.
- [Jan](https://github.com/janhq/jan) — Desktop app for offline chat; the LICENSE file is Apache-2.0 and asks for attribution in user-facing docs.
- [koboldcpp](https://github.com/LostRuins/koboldcpp) — AGPL-3.0 single-file app that serves GGUF models behind a KoboldAI-compatible UI.
- [LM Studio CLI](https://github.com/lmstudio-ai/lms) — MIT-licensed command-line tool for LM Studio; the desktop app itself is a separate closed product.
- [LM Studio Python SDK](https://github.com/lmstudio-ai/lmstudio-python) — MIT-licensed Python SDK for talking to a local LM Studio server.
- [LocalAI](https://github.com/mudler/LocalAI) — MIT-licensed OpenAI-compatible server for local models across text, vision, and audio.
- [Ollama library](https://ollama.com/library) — Ollama's model index; a tag here is a packaging choice, and the weight license is whatever the upstream card says.
- [Open WebUI](https://github.com/open-webui/open-webui) — Self-hosted chat UI for Ollama and OpenAI-compatible servers, under a custom license that forbids removing Open WebUI branding above 50 end users.
- [textgen](https://github.com/oobabooga/textgen) — AGPL-3.0 desktop app from the text-generation-webui author for local text and vision models.

### On-device and edge

Runtimes aimed at phones, browsers, and single-file or laptop deployment.

- [BitNet](https://github.com/microsoft/BitNet) — MIT-licensed official inference framework for 1-bit LLMs.
- [ExecuTorch](https://github.com/pytorch/executorch) — PyTorch runtime for on-device inference across mobile and embedded; read the repo license file, which GitHub does not map to an SPDX id.
- [LlamaEdge](https://github.com/LlamaEdge/LlamaEdge) — Apache-2.0 path for running LLMs as WasmEdge applications on a local machine or at the edge.
- [MLC LLM](https://github.com/mlc-ai/mlc-llm) — Apache-2.0 compiler stack for deploying LLMs onto phones, browsers, and other edge targets.
- [MLX-VLM](https://github.com/Blaizzy/mlx-vlm) — MIT-licensed inference and finetune package for vision-language models on Apple silicon.
- [WebLLM](https://github.com/mlc-ai/web-llm) — Apache-2.0 in-browser LLM engine; the model still has to be an open checkpoint the runtime can fetch.

## Training, finetune and alignment

Open code for training and adapting language models. A library that only calls a closed API is not listed.

### Finetune and post-training

- [Alignment Handbook](https://github.com/huggingface/alignment-handbook) — Apache-2.0 recipes from Hugging Face for aligning models with human and AI preferences.
- [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) — Apache-2.0 finetune framework configured by YAML, widely used for QLoRA and full finetunes of open checkpoints.
- [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) — MIT-licensed k-bit quantization used to finetune and load large models on smaller GPUs.
- [LitGPT](https://github.com/Lightning-AI/litgpt) — Apache-2.0 recipes to pretrain, finetune, and serve a set of open LLM implementations.
- [LLaMA-Factory](https://github.com/hiyouga/LlamaFactory) — Apache-2.0 web UI and CLI for finetuning open LLMs and vision-language models.
- [llm-compressor](https://github.com/vllm-project/llm-compressor) — Apache-2.0 compression library for producing checkpoints that vLLM can serve.
- [ms-swift](https://github.com/modelscope/ms-swift) — Apache-2.0 finetune toolkit covering CPT, SFT, DPO, and GRPO across hundreds of open models.
- [open-instruct](https://github.com/allenai/open-instruct) — Apache-2.0 post-training codebase from the Allen Institute, used for the Tülu line.
- [PEFT](https://github.com/huggingface/peft) — Apache-2.0 parameter-efficient finetuning, including LoRA, on top of Transformers.
- [torchtune](https://github.com/meta-pytorch/torchtune) — BSD-3-Clause PyTorch-native post-training library, now under the meta-pytorch org.
- [TRL](https://github.com/huggingface/trl) — Apache-2.0 library for SFT, DPO, PPO, and GRPO on transformer language models.
- [Unsloth](https://github.com/unslothai/unsloth) — Apache-2.0 library and local UI for faster finetuning of open LLMs, including the 2026 open-weight families the README names.

### Pretraining

- [ColossalAI](https://github.com/hpcaitech/ColossalAI) — Apache-2.0 parallel-training library aimed at making large models cheaper to train.
- [Composer](https://github.com/mosaicml/composer) — Apache-2.0 training library from Mosaic, used under llm-foundry.
- [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) — Apache-2.0 optimization library for distributed training and inference; the maintained org is deepspeedai.
- [GPT-NeoX](https://github.com/EleutherAI/gpt-neox) — Apache-2.0 training stack EleutherAI used for GPT-NeoX and Pythia, built on Megatron and DeepSpeed.
- [Lingua](https://github.com/facebookresearch/lingua) — BSD-3-Clause research codebase from Meta for training LLMs without a framework-sized dependency tree.
- [llm-foundry](https://github.com/mosaicml/llm-foundry) — Apache-2.0 training code Databricks used for its open foundation models, including the DBRX-era stack.
- [llm.c](https://github.com/karpathy/llm.c) — MIT-licensed training implementation in C and CUDA, written to show the algorithm without a framework.
- [MaxText](https://github.com/AI-Hypercomputer/maxtext) — Apache-2.0 JAX stack for training LLMs on Google Cloud TPUs and GPUs.
- [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) — NVIDIA's research codebase for training transformers with model parallelism.
- [nanochat](https://github.com/karpathy/nanochat) — MIT-licensed end-to-end training of a small ChatGPT-style model on a budget the README puts around 100 dollars.
- [nanoGPT](https://github.com/karpathy/nanoGPT) — MIT-licensed minimal GPT trainer, still the clearest place to read a training loop.
- [nanotron](https://github.com/huggingface/nanotron) — Apache-2.0 minimal 3D-parallel training code from Hugging Face.
- [OLMo-core](https://github.com/allenai/OLMo-core) — Apache-2.0 PyTorch training library for the current OLMo stack.

### Preference, RL and data

- [Argilla](https://github.com/argilla-io/argilla) — Apache-2.0 tool for humans and engineers to review and label data used in alignment.
- [datatrove](https://github.com/huggingface/datatrove) — Apache-2.0 data-processing pipelines for large text corpora.
- [distilabel](https://github.com/argilla-io/distilabel) — Apache-2.0 framework for synthetic data and AI feedback pipelines.
- [NeMo Curator](https://github.com/NVIDIA-NeMo/Curator) — Apache-2.0 data curation toolkit for LLM pretraining corpora.
- [Open R1](https://github.com/huggingface/open-r1) — Apache-2.0 effort to reproduce DeepSeek-R1 with public data and training code.
- [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) — Apache-2.0 RLHF and agentic-RL framework built on Ray and vLLM.
- [OpenThoughts](https://github.com/open-thoughts/open-thoughts) — Apache-2.0 open data-curation effort for reasoning models.
- [TRLX](https://github.com/CarperAI/trlx) — MIT-licensed earlier distributed RLHF library; new work has mostly moved to TRL and OpenRLHF, and the repo is quiet.
- [verifiers](https://github.com/PrimeIntellect-ai/verifiers) — MIT-licensed library of RL environments and evals from Prime Intellect.
- [verl](https://github.com/verl-project/verl) — Apache-2.0 reinforcement-learning post-training framework, the maintained home of the HybridFlow codebase.

## Use cases

Apps and libraries people use on top of open weights. A project that cannot point at a local or open model is not a fit.

### Agents and coding

- [Aider](https://github.com/Aider-AI/aider) — Apache-2.0 terminal pair-programmer that can talk to a local OpenAI-compatible server as well as hosted APIs.
- [browser-use](https://github.com/browser-use/browser-use) — MIT-licensed browser agent; point it at an open model through an OpenAI-compatible endpoint if you do not want a hosted model.
- [Cline](https://github.com/cline/cline) — Apache-2.0 coding agent shipped as an SDK, IDE extension, or CLI, able to use local models.
- [Continue](https://github.com/continuedev/continue) — Apache-2.0 coding agent with first-class config for local OpenAI-compatible backends.
- [goose](https://github.com/aaif-goose/goose) — Apache-2.0 extensible agent that installs, edits, and runs code against any LLM, including local ones.
- [Kimi Code](https://github.com/MoonshotAI/kimi-code) — MIT-licensed terminal coding agent from Moonshot; it is an agent harness, not the Kimi K3 weights.
- [OpenCode](https://github.com/anomalyco/opencode) — MIT-licensed terminal coding agent.
- [OpenHands](https://github.com/OpenHands/OpenHands) — MIT-licensed software-engineering agent, the project formerly called OpenDevin, that can run against open models.
- [Qwen Code](https://github.com/QwenLM/qwen-code) — Apache-2.0 terminal coding agent from the Qwen team.
- [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) — Apache-2.0 agent framework for Qwen models, including function calling, code interpreter, RAG, and MCP.
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) — MIT-licensed agent that takes a GitHub issue and tries to patch it with a language model of your choice.
- [Tabby](https://github.com/TabbyML/tabby) — Self-hosted coding assistant; code outside the ee directory is Apache-2.0, and ee has a separate license.
- [UI-TARS](https://github.com/bytedance/UI-TARS) — Apache-2.0 desktop and GUI agent stack from ByteDance, built to drive native interfaces.

### RAG and knowledge

- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) — MIT-licensed local-first app for chatting with your documents against a local model.
- [Chroma](https://github.com/chroma-core/chroma) — Apache-2.0 embedding store used as the retrieval layer under local RAG apps.
- [Dify](https://github.com/langgenius/dify) — Workflow and RAG studio you can self-host and point at open models; the GitHub license field is unset, so read LICENSE before you embed it.
- [Haystack](https://github.com/deepset-ai/haystack) — Apache-2.0 framework for retrieval pipelines and agents, with explicit control over which model generates.
- [LlamaIndex](https://github.com/run-llama/llama_index) — MIT-licensed document-processing and retrieval library that sits in front of whatever model you serve.
- [PrivateGPT](https://github.com/zylon-ai/private-gpt) — Apache-2.0 API for private RAG over local, OpenAI-compatible inference servers.
- [Qdrant](https://github.com/qdrant/qdrant) — Apache-2.0 vector database commonly paired with local embedding and chat models.
- [RAGFlow](https://github.com/infiniflow/ragflow) — Apache-2.0 RAG engine with document parsing, meant to sit in front of an LLM you choose.
- [sentence-transformers](https://github.com/huggingface/sentence-transformers) — Apache-2.0 library for open embedding and reranker models, which is the retrieval half of a local RAG stack.

### Creative and local chat

Front ends aimed at roleplay and long-context chat. General local chat shells are listed under local apps.

- [SillyTavern](https://github.com/SillyTavern/SillyTavern) — AGPL-3.0 front end for roleplay and long-context chat, almost always pointed at a local model such as llama.cpp or Ollama.

### Voice

- [Moshi](https://github.com/kyutai-labs/moshi) — Apache-2.0 full-duplex speech-text model and streaming audio codec from Kyutai.
- [speech-to-speech](https://github.com/huggingface/speech-to-speech) — Apache-2.0 pipeline for voice agents built from open speech and language models.
- [Ultravox](https://github.com/fixie-ai/ultravox) — MIT-licensed multimodal model for real-time voice, with weights published for local use.

### Structured output

- [DSPy](https://github.com/stanfordnlp/dspy) — MIT-licensed framework for programming language models with typed modules instead of one-off prompts, including local backends.
- [Guidance](https://github.com/guidance-ai/guidance) — MIT-licensed language for constraining generation, including against local models.
- [Outlines](https://github.com/dottxt-ai/outlines) — Apache-2.0 structured-generation library.
- [XGrammar](https://github.com/mlc-ai/xgrammar) — Apache-2.0 grammar-constrained decoding engine used by serving stacks such as vLLM.

## Evals and papers

Harnesses and papers that still matter when the model is open-weight. Leaderboard ranks move; the link is the method, not a score.

### Leaderboards and harnesses

- [AlpacaEval](https://tatsu-lab.github.io/alpaca_eval) — Automatic evaluator for instruction following; cheap and widely cited, and not a substitute for a held-out task you care about.
- [Arena-Hard-Auto](https://github.com/lmarena/arena-hard-auto) — Apache-2.0 automatic benchmark built to approximate LMSYS-style arena judgments.
- [Artificial Analysis](https://artificialanalysis.ai) — Independent site that reports quality, speed, and price, with an open-weight slice; treat any rank as a snapshot.
- [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) — Leaderboard for tool and function calling, which is the failure mode that matters for open models used as agents.
- [HELM](https://crfm.stanford.edu/helm) — Stanford CRFM's holistic evaluation site for foundation models; the harness itself is the separate Apache-2.0 repository stanford-crfm/helm.
- [LightEval](https://github.com/huggingface/lighteval) — MIT-licensed evaluation toolkit from Hugging Face that runs the same tasks across several inference backends.
- [LiveBench](https://livebench.ai) — Contamination-resistant benchmark with frequently refreshed questions.
- [LiveCodeBench](https://github.com/LiveCodeBench/LiveCodeBench) — MIT-licensed contamination-resistant coding benchmark; the site is livecodebench.github.io.
- [LM Arena](https://lmarena.ai) — Blind pairwise chat arena; open and closed models share the board, so filter to open weights before quoting a rank.
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — MIT-licensed few-shot evaluation harness behind a large share of open-model benchmark tables.
- [OLMES](https://github.com/allenai/olmes) — Apache-2.0 evaluation setup the Allen Institute uses for reproducible OLMo numbers.
- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — Hugging Face space that ranked open models on a fixed harness; confirm it is still updating before you cite a position.
- [OpenCompass](https://github.com/open-compass/opencompass) — Apache-2.0 evaluation platform covering knowledge, reasoning, coding, and long context, with many open-model backends.
- [RewardBench](https://github.com/allenai/reward-bench) — Apache-2.0 benchmark for reward models, which is the piece open preference-tuning actually depends on.
- [simple-evals](https://github.com/openai/simple-evals) — MIT-licensed small eval suite OpenAI published, useful as a shared script rather than as a leaderboard.
- [SWE-bench](https://www.swebench.com) — Benchmark of real GitHub issues; the MIT-licensed harness is SWE-bench/SWE-bench, and the score depends on the agent as well as the model.

### Papers

- [BLOOM paper](https://arxiv.org/abs/2211.05100) — BigScience report on training the 176B BLOOM model in the open.
- [OPT paper](https://arxiv.org/abs/2205.01068) — Meta's paper on the Open Pretrained Transformer models and what they released.
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) — The DPO paper, which is the method most open preference-tuning recipes still implement.
- [Llama 2 paper](https://arxiv.org/abs/2307.09288) — Meta's paper on Llama 2, including the custom license and the safety finetune, separate from the original non-commercial LLaMA release.
- [Mistral 7B paper](https://arxiv.org/abs/2310.06825) — Technical report for the Apache-2.0 Mistral 7B model.
- [OLMo paper](https://arxiv.org/abs/2402.00838) — Allen Institute paper on releasing a competitive model together with its training data and code.
- [FineWeb paper](https://arxiv.org/abs/2406.17557) — Hugging Face paper on filtering web data into the FineWeb and FineWeb-Edu corpora.
- [Llama 3 paper](https://arxiv.org/abs/2407.21783) — Meta's herd paper for Llama 3, covering the models released under the Llama 3 community licenses.
- [Qwen2.5 technical report](https://arxiv.org/abs/2412.15115) — Alibaba's technical report for the Qwen2.5 family.
- [DeepSeek-V3 technical report](https://arxiv.org/abs/2412.19437) — Technical report for DeepSeek-V3, including the auxiliary-loss-free load balancer and multi-token prediction.
- [DeepSeek-R1 paper](https://arxiv.org/abs/2501.12948) — Paper on training DeepSeek-R1's reasoning behavior with reinforcement learning, and on the distilled open checkpoints.
- [DeepSeek-V4 technical report](https://arxiv.org/abs/2606.19348) — Technical report linked from the MIT-licensed DeepSeek-V4-Pro model card.
- [Gemma 4 technical report](https://arxiv.org/abs/2607.02770) — Technical report linked from the Apache-2.0 Gemma 4 model cards.

## Datasets

High-signal corpora for pretraining and post-training. Licenses are uneven; ODC-By and CC-BY are not the same as the model license you ship.

- [DCLM baseline](https://huggingface.co/datasets/mlfoundations/dclm-baseline-1.0) — DataComp for Language Models baseline corpus, CC-BY-4.0 on the Hub card.
- [Dolma](https://huggingface.co/datasets/allenai/dolma) — Allen Institute pretraining corpus released with OLMo, under ODC-By.
- [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) — Hugging Face web-text corpus under ODC-By, built to be a cleaner Common-Crawl-derived pretraining set.
- [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) — Educational subset of FineWeb, also ODC-By, used heavily for small open models.
- [Infinity-Instruct](https://huggingface.co/datasets/BAAI/Infinity-Instruct) — Instruction mixture from BAAI under CC-BY-SA-4.0, which is share-alike and not the same as Apache-2.0.
- [RedPajama-1T](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T) — Together's open reproduction of a LLaMA-style pretraining mix; the Hub API did not return a SPDX id, so read the dataset card before redistributing.
- [SmolTalk](https://huggingface.co/datasets/HuggingFaceTB/smoltalk) — Supervised-finetune mixture published with the SmolLM line; the Hub API did not return a SPDX id on ingest, so read the card.
- [The Pile](https://huggingface.co/datasets/EleutherAI/pile) — EleutherAI's pretraining corpus; the Hub license is other, and the original full dump is not something you should assume is still redistributable.
- [The Stack v2](https://huggingface.co/datasets/bigcode/the-stack-v2) — BigCode's code pretraining corpus with per-file license metadata; the dataset license tag is other, not a blanket Apache grant.
- [Tülu 3 SFT mixture](https://huggingface.co/datasets/allenai/tulu-3-sft-mixture) — Allen Institute supervised-finetune mixture for Tülu 3, under ODC-By.
- [UltraChat 200k](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k) — MIT-licensed multi-turn dialogue set used in many open chat finetunes.
- [UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback) — MIT-licensed preference dataset used to train reward models and DPO mixes.

## Docs and essays

Short readings that explain the stack without pretending to be a benchmark.

- [EleutherAI](https://www.eleuther.ai) — Home of the lab behind GPT-NeoX, Pythia, and the evaluation harness.
- [Gemma docs](https://ai.google.dev/gemma/docs/core) — Google's current Gemma documentation, including the pointer from Gemma 4 cards to the Apache-2.0 grant.
- [gpt-oss.com](https://gpt-oss.com) — Project site linked from the Apache-2.0 gpt-oss model card.
- [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) — Free course that walks from Transformer basics through the Hub, finetuning, and evaluation.
- [LLM course](https://github.com/mlabonne/llm-course) — Apache-2.0 roadmap and notebooks for learning LLMs, with an emphasis on open models.
- [Qwen3 blog](https://qwenlm.github.io/blog/qwen3) — Qwen team's blog post introducing the Qwen3 generation.
- [SmolLM repo](https://github.com/huggingface/smollm) — Apache-2.0 home for the SmolLM and SmolVLM families, including the training recipes the model cards point at.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer) — Jay Alammar's visual walkthrough of the Transformer, still the best single explanation of the architecture these models share.

## Awesome lists and indexes

Related catalogs. None of these is a substitute for checking a weight's license, and awesome-llm-os is a different topic.

- [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) — DeepSeek's own list of integrations; useful for apps, not a substitute for the model license.
- [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) — Broad CC0 list of LLM papers, training frameworks, and tools; last pushed 2025-07-31, and not limited to open weights.
- [awesome-llm-os](https://github.com/bilalonur/awesome-llm-os) — CC0 list of LLM-as-operating-system projects; a different topic from this catalog, listed so the two are not merged.
- [open-llms](https://github.com/eugeneyan/open-llms) — Apache-2.0 short list of open LLMs the author marks as available for commercial use; last pushed 2025-02-13, so re-check anything it recommends.
- [Qwen3.8 collection](https://huggingface.co/collections/Qwen/qwen38) — Hugging Face collection the Qwen3.8 README points at for the 27B and 2.4T-A95B weights.

## Community

Places where open-weight work is actually discussed.

- [EleutherAI Discord](https://discord.gg/eleutherai) — Discord invite for the EleutherAI community.
- [Hugging Face](https://huggingface.co) — Hub, forums, and model cards where open-weight releases are actually posted.
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA) — The main public forum for running open weights locally; an automated fetch from this ingest was blocked by Reddit, and the subreddit itself is long-standing.

## Sources

This list was checked against official model cards, GitHub repos, dataset cards, and a few existing indexes. It is not a bulk merge of those indexes. The map is [`SOURCES.md`](SOURCES.md). The machine-readable dump is [`links.json`](links.json).

## Contributing

Add or edit an object in [`links.json`](links.json), then run `python3 build.py`. One factual sentence, a URL that loads, and a license note when the weights are public but the grant is not Apache-2.0 or MIT. Do not invent star counts, tweet ids, or release dates. Within a subsection, leave `pin` unset to sort alphabetically; set `pin` only to keep a deliberate chronological order. Normalized URLs must be unique.

## License

This compilation is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Model weights, code, datasets, and essays linked from here keep their own licenses and use restrictions.
