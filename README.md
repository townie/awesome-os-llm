# Awesome OS LLM

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated open-source and open-weight large language models, plus the stacks people use to run, train, and apply them.

An **open-source LLM**, in this list, is a language model whose weights you can download and run yourself, together with the open code around that. It is not “an LLM that pretends to be an operating system.” That other topic lives in [awesome-llm-os](https://github.com/bilalonur/awesome-llm-os).

Two claims get mixed up, and this list keeps them apart:

- **Open weights** means the parameters are published, so you can self-host, quantize, and fine-tune. The license may still forbid commercial use or add a field-of-use restriction.
- **Open source**, in the [Open Source Initiative’s Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition), means a license that lets you use, study, modify, and share without those restrictions. Apache-2.0 and MIT meet that bar. The Llama Community License, Gemma’s older Terms of Use, and CC BY-NC weights do not, even when the files download.

Both belong here. The blurb says which is which when it matters. A vendor’s “open source” slogan is not treated as the license.

The public record is older than the 2023 Llama moment, and this list does not invent a first. OpenAI shipped GPT-2 weights in 2019. EleutherAI’s GPT-Neo, GPT-J, GPT-NeoX, and Pythia, and BigScience BLOOM, kept research releases going before Meta’s LLaMA (February 2023), a gated non-commercial drop that still seeded a large fine-tune ecosystem. Self-hosting for commercial products became practical with Llama 2 (July 2023, custom community license) and Mistral 7B (September 2023, Apache-2.0). Qwen, Gemma, DeepSeek, Phi, OLMo, and later OpenAI’s own gpt-oss weights followed. None of those sentences is a claim that anyone built the first language model.

Deduplicated by normalized URL (trailing slash, `www.`, query, and fragment stripped).

**285 unique links** · Ingested **2026-09-22 PT** · License for this compilation: [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (linked projects keep their own licenses).

### Start here

- [Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) — What “open source” means for a model, as distinct from downloadable weights.
- [Landmark open models](#landmark-open-models) — Llama, Mistral, Qwen, Gemma, DeepSeek, and the fully open OLMo line.
- [Olmo](https://allenai.org/olmo) — AllenAI’s fully open model flow: weights, data, and code, not weights alone.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) — The usual way to run a GGUF model on a laptop.
- [vLLM](https://github.com/vllm-project/vllm) — The usual way to serve an open model to more than one user.
- [Use cases](#use-cases) — Agents, coding, RAG, local chat, and on-device apps, ahead of the tool pile.
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — The harness most open-model papers still quote.

## Contents

- [Landmark open models](#landmark-open-models) (98)
  - [Early open weights](#early-open-weights) (10)
  - [Llama](#llama) (8)
  - [Mistral](#mistral) (11)
  - [Qwen](#qwen) (11)
  - [Gemma](#gemma) (8)
  - [DeepSeek](#deepseek) (9)
  - [Fully open model flows](#fully-open-model-flows) (7)
  - [Permissive open weights](#permissive-open-weights) (16)
  - [Open weights, restricted licenses](#open-weights-restricted-licenses) (18)
- [Use cases](#use-cases) (42)
  - [Agents](#agents) (11)
  - [Coding](#coding) (7)
  - [RAG and knowledge](#rag-and-knowledge) (11)
  - [Creative and local chat](#creative-and-local-chat) (3)
  - [On-device apps](#on-device-apps) (3)
  - [Research tools](#research-tools) (7)
- [Runtimes and local serving](#runtimes-and-local-serving) (33)
  - [Inference engines](#inference-engines) (15)
  - [Local apps and front ends](#local-apps-and-front-ends) (12)
  - [Edge and in-browser](#edge-and-in-browser) (6)
- [Training, finetune and alignment](#training-finetune-and-alignment) (39)
  - [Pretraining stacks](#pretraining-stacks) (14)
  - [Finetune and alignment](#finetune-and-alignment) (19)
  - [Kernels and efficiency](#kernels-and-efficiency) (6)
- [Evals and papers](#evals-and-papers) (38)
  - [Leaderboards](#leaderboards) (15)
  - [Harnesses](#harnesses) (4)
  - [Papers](#papers) (19)
- [Docs and essays](#docs-and-essays) (11)
- [Datasets](#datasets) (14)
  - [Pretraining data](#pretraining-data) (8)
  - [Post-training data](#post-training-data) (5)
  - [Data tools](#data-tools) (1)
- [Awesome lists and indexes](#awesome-lists-and-indexes) (6)
- [Community](#community) (4)
- [Sources](#sources)
- [Contributing](#contributing)
- [License](#license)

## Landmark open models

Families whose weights you can download. Apache-2.0 and MIT are called out when that is what the model card says; custom and non-commercial licenses are called out too.

### Early open weights

- [GPT-2](https://github.com/openai/gpt-2) — OpenAI's 2019 code and released weights for GPT-2. A real open-weight language model years before LLaMA, not a retroactive slogan.
- [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) — The GPT-2 paper. The PDF is the primary write-up; the GitHub repo is the code and weights.
- [GPT-Neo](https://github.com/EleutherAI/gpt-neo) — EleutherAI's open GPT-3-style models and training code, from the period when the largest GPT-3 weights were not public.
- [GPT-J-6B](https://huggingface.co/EleutherAI/gpt-j-6b) — EleutherAI's 6B model, Apache-2.0 on the Hub, and the model a lot of 2021-2022 open tooling actually ran.
- [Mesh Transformer JAX](https://github.com/kingoflolz/mesh-transformer-jax) — The JAX code used to train GPT-J. The weights live on the Hub; this is the training implementation.
- [GPT-NeoX](https://github.com/EleutherAI/gpt-neox) — EleutherAI's distributed training library, used for GPT-NeoX and Pythia. Still a reference pretraining stack, not just a 2022 artifact.
- [OPT-66B](https://huggingface.co/facebook/opt-66b) — Meta's 2022 66B decoder. Weights are downloadable under a research license, not Apache-2.0 or MIT.
- [Metaseq](https://github.com/facebookresearch/metaseq) — The codebase Meta published with OPT. The models are open-weight research releases, not an OSI-licensed family.
- [BLOOM](https://huggingface.co/bigscience/bloom) — BigScience's 176B multilingual model. The Hub license is the BigScience RAIL, which adds use restrictions on top of the weight release.
- [Pythia](https://github.com/EleutherAI/pythia) — EleutherAI's suite of models trained on the same data in the same order so training dynamics can be studied. Code and weights are Apache-2.0.

### Llama

- [Introducing LLaMA](https://ai.meta.com/blog/large-language-model-llama-meta-ai/) — Meta's February 2023 research release (7B to 65B). Access was gated and non-commercial; it still became the base of the first public fine-tune wave.
- [Llama](https://github.com/meta-llama/llama) — Meta's Llama model repo (the old facebookresearch/llama URL redirects here). Weights are under the Llama community licenses, not Apache-2.0.
- [Llama 2](https://about.fb.com/news/2023/07/llama-2/) — July 2023 release with a custom community license that allowed commercial use under its conditions. Meta called it open source; the license is not OSI-approved.
- [Llama 3.1](https://ai.meta.com/blog/meta-llama-3-1/) — Meta's July 2024 post for the 8B, 70B, and 405B models with a 128K context. Same community-license pattern as Llama 3, not an Apache grant.
- [Llama 3.1 8B Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) — The practical small Llama 3.1 checkpoint. Hub license field is llama3.1, a custom community license.
- [Llama 4 Scout](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) — Meta's 2025 open-weight multimodal MoE (17B active). Hub license is the custom Llama license, which Meta itself now describes as open-weight rather than open source.
- [Llama 4 Maverick](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) — The larger Llama 4 MoE sibling of Scout, also multimodal and under the same custom license.
- [Llama developer docs](https://dev.meta.ai/llama/) — Current Meta docs for the Llama weights and prompt formats. The marketing site and this doc host are both first-party; the license text is still the community license.

### Mistral

- [Mistral 7B](https://mistral.ai/news/announcing-mistral-7b/) — Mistral's September 2023 announcement of a 7.3B model under Apache-2.0. This is the release that made a permissive commercial self-host realistic at laptop size.
- [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) — The original Apache-2.0 checkpoint. Later instruct and v0.3 weights exist; this card is the one the 2023 announcement pointed at.
- [Mixtral of experts](https://mistral.ai/news/mixtral-of-experts/) — December 2023 announcement of Mixtral 8x7B, the sparse MoE that made open mixture-of-experts normal. Apache-2.0.
- [Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) — Apache-2.0 weights for Mixtral 8x7B. About 47B parameters stored, with far fewer active per token.
- [Pixtral 12B](https://huggingface.co/mistralai/Pixtral-12B-2409) — Mistral's first natively multimodal open model, Apache-2.0 on the Hub. A 12B decoder plus a vision encoder, not a text model with a bolted-on captioner.
- [Magistral Small](https://huggingface.co/mistralai/Magistral-Small-2506) — Apache-2.0 reasoning model (24B). Magistral Medium stayed API-only; this card is the open one.
- [Devstral Small](https://huggingface.co/mistralai/Devstral-Small-2505) — Apache-2.0 agentic coding model Mistral released with All Hands. It is a fine-tune line, not a general chat replacement.
- [Mistral Large 3](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512) — Apache-2.0 sparse MoE, 675B total, from the December 2025 Mistral 3 family. Earlier Mistral Large 2 used a research license; this generation's card says Apache-2.0.
- [Mistral Small 4](https://mistral.ai/news/mistral-small-4/) — Mistral's announcement of one Apache-2.0 model meant to cover instruct, reasoning, and coding, instead of three separate checkpoints.
- [Mistral Small 4 119B](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) — The Apache-2.0 weights: a 119B MoE with multimodal input. The card is the artifact; the news post is the framing.
- [mistral-inference](https://github.com/mistralai/mistral-inference) — Official reference inference code for Mistral models. Production serving usually goes through vLLM or llama.cpp instead.

### Qwen

- [Qwen](https://github.com/QwenLM/Qwen) — First-generation Qwen repo. Those early weights used the Tongyi Qianwen license; the code was Apache-2.0. Later generations changed the weight license.
- [Qwen3](https://github.com/QwenLM/Qwen3) — Repo and release notes for Qwen3. From this generation the Qwen team states that the open-weight models are Apache-2.0.
- [Qwen3 blog](https://qwenlm.github.io/blog/qwen3/) — The Qwen3 launch post: hybrid thinking and non-thinking modes, and the Apache-2.0 claim for the open weights.
- [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) — Apache-2.0 Qwen3 mixture-of-experts, 235B total and 22B active. A flagship of that generation, not the 2026 line.
- [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B) — Apache-2.0 open reasoning model from the Qwen team. The preview that started this line was November 2024; this card is the 32B release.
- [Qwen3-Coder-480B-A35B](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct) — Apache-2.0 agentic code MoE, 480B total and 35B active. A specialist checkpoint, not the general Qwen3 chat model.
- [Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) — Apache-2.0 vision-language MoE. Hub repo created 2026-02-16, the first size in the Qwen3.5 line.
- [Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) — Apache-2.0 dense vision-language model. Hub repo created 2026-04-21. The Qwen3.6 GitHub name now redirects to the Qwen3.8 repo.
- [Qwen3.8](https://github.com/QwenLM/Qwen3.8) — Canonical GitHub repo for Qwen3.5, Qwen3.6, and Qwen3.8. Read the license per checkpoint: the 27B is Apache-2.0 and the 2.4T card is not.
- [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) — Apache-2.0 dense vision-language model, Hub repo created 2026-08-05. The size people actually download for a single GPU.
- [Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) — Open-weight text MoE, Hub repo created 2026-08-08. The license field is custom, not Apache-2.0, unlike the 27B.

### Gemma

- [Gemma](https://deepmind.google/models/gemma/) — Google DeepMind's Gemma page. Gemma 1 through 3 shipped under the Gemma Terms of Use; Gemma 4 is the generation that moved to Apache-2.0.
- [Gemma reference code](https://github.com/google-deepmind/gemma) — Official Gemma model code. Inference for real deployments is usually llama.cpp, vLLM, MLX, or the cookbook, not this repo alone.
- [Gemma 3 27B Instruct](https://huggingface.co/google/gemma-3-27b-it) — Vision-language Gemma 3 checkpoint. Hub license is gemma, the older terms, not Apache-2.0.
- [Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) — Google's Gemma 4 announcement. The post says this generation is Apache-2.0, which the Hub license fields for the 31B, 26B-A4B, and E4B cards match.
- [Gemma 4 31B](https://huggingface.co/google/gemma-4-31B-it) — Apache-2.0 dense vision-language Gemma 4. Hub repo created 2026-03-11.
- [Gemma 4 26B-A4B](https://huggingface.co/google/gemma-4-26B-A4B-it) — Apache-2.0 Gemma 4 mixture-of-experts. Fewer parameters active per token than the 31B dense model, so it is the faster of the two mid sizes.
- [Gemma 4 E4B](https://huggingface.co/google/gemma-4-E4B-it) — Apache-2.0 edge Gemma 4. The Hub pipeline tag is any-to-any, which is the small multimodal checkpoint rather than the text-only 31B.
- [Gemma cookbook](https://github.com/google-gemini/gemma-cookbook) — Official notebooks for running and fine-tuning Gemma, including the Apache-2.0 Gemma 4 weights.

### DeepSeek

- [DeepSeek LLM](https://github.com/deepseek-ai/DeepSeek-LLM) — DeepSeek's first open models (2023). Code in that era was MIT; the weight license was the DeepSeek model license, not yet the MIT weights of R1.
- [DeepSeek-V2](https://github.com/deepseek-ai/DeepSeek-V2) — The 2024 MoE that introduced Multi-head Latent Attention. A research and architecture landmark more than a checkpoint you would pick in 2026.
- [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) — 671B-total MoE release repo (December 2024). Later DeepSeek weight releases moved to MIT; read this repo's license instead of assuming that backward.
- [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) — January 2025 reasoning model and the distilled smaller checkpoints, released under MIT. The repo that made open reasoning weights ordinary.
- [DeepSeek-V4 preview](https://www.deepseek.com/en/news/v4-preview/) — DeepSeek's 24 April 2026 post announcing open V4-Pro and V4-Flash weights with a 1M-token context.
- [DeepSeek-V4 on Hugging Face](https://huggingface.co/blog/deepseekv4) — Hugging Face's 24 April 2026 write-up of the V4 checkpoints, including which repos are instruct versus base.
- [DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) — MIT-licensed text MoE. Hub repo created 2026-04-22. The large V4 checkpoint, not the Flash line.
- [DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) — MIT-licensed text checkpoint, Hub repo created 2026-07-31. A later Flash build than the April preview repo.
- [DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) — MIT-licensed multimodal model, Hub repo created 2026-09-10. The newest DeepSeek weight repo confirmed for this ingest.

### Fully open model flows

- [Olmo](https://allenai.org/olmo) — AllenAI's fully open language-model project: weights, training data, and code, which is a stricter bar than open weights alone.
- [OLMo code](https://github.com/allenai/OLMo) — Training and inference code for OLMo. Apache-2.0, and the repo that goes with the Dolma data.
- [OLMo 2 13B](https://huggingface.co/allenai/OLMo-2-1124-13B) — Apache-2.0 OLMo 2 base model. A fully open 13B from the November 2024 line, before Olmo 3.
- [Olmo 3](https://allenai.org/blog/olmo3) — Ai2's write-up of the 7B and 32B Olmo 3 family, including the Think variants whose reasoning traces they tie back to the training data.
- [Olmo 3.1 Think 32B](https://huggingface.co/allenai/Olmo-3.1-32B-Think) — Apache-2.0 thinking model. Hub repo created 2025-12-10. Fully open weights, not a Llama-license clone.
- [Apertus 70B Instruct](https://huggingface.co/swiss-ai/Apertus-70B-Instruct-2509) — Apache-2.0 70B instruct model from the Swiss AI Initiative. Hub repo created 2025-09-01.
- [Marin](https://github.com/marin-community/marin) — Open training stack aimed at reproducing modern language models with public data and code, in the same spirit as OLMo rather than a closed pretrain.

### Permissive open weights

- [gpt-oss](https://github.com/openai/gpt-oss) — OpenAI's open-weight model repo. The 20B and 120B checkpoints on the Hub are Apache-2.0. The openai.com announcement page blocked this ingest, so the repo and cards are the cited sources.
- [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) — Apache-2.0 MoE reasoning model sized to run locally. Hub repo created 2025-08-04.
- [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) — Apache-2.0 larger gpt-oss checkpoint. Hub repo created 2025-08-04. Open weights from OpenAI, not a leaked model.
- [gpt-oss-safeguard-20b](https://huggingface.co/openai/gpt-oss-safeguard-20b) — Apache-2.0 safety classifier that reasons over a policy you supply. Hub repo created 2025-09-18.
- [Phi-2](https://huggingface.co/microsoft/phi-2) — Microsoft's 2.7B model under MIT. The small-model result that made Phi a line rather than a paper.
- [Phi-4](https://huggingface.co/microsoft/phi-4) — MIT-licensed 14B model. Microsoft's data-quality pitch, with weights you can actually download.
- [Phi-4-reasoning](https://huggingface.co/microsoft/Phi-4-reasoning) — MIT-licensed reasoning variant of Phi-4. Hub repo created 2025-04-09.
- [Phi cookbook](https://github.com/microsoft/PhiCookBook) — Microsoft's notebooks for the Phi models, including the MIT-licensed open weights.
- [Yi-34B](https://huggingface.co/01-ai/Yi-34B) — 01.AI's 34B model. Hub license is Apache-2.0. The 2023-2024 bilingual line, not a 2026 flagship.
- [Granite 3.3 8B Instruct](https://huggingface.co/ibm-granite/granite-3.3-8b-instruct) — Apache-2.0 IBM Granite instruct model. Hub repo created 2025-04-09.
- [Grok-1](https://github.com/xai-org/grok-1) — JAX code for xAI's 314B MoE. The README in this repo says the code and the Grok-1 weights are Apache-2.0, and it points at a magnet link plus a Hub download.
- [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) — MIT-licensed multimodal GLM from Z.ai. Hub repo created 2026-08-25. The full GLM-5.3 card is a different, custom license.
- [GLM-5](https://github.com/zai-org/GLM-5) — Z.ai's repo covering GLM-5 through GLM-5.3. Use it to see which sibling is MIT (Flash) and which is the custom-license flagship.
- [Hy4 preview](https://huggingface.co/tencent/Hy4-preview) — Apache-2.0 text model from Tencent's Hy team. Hub repo created 2026-08-27. The card describes a 770B-total MoE preview, not a general Hunyuan product page.
- [SmolLM3 3B](https://huggingface.co/HuggingFaceTB/SmolLM3-3B) — Apache-2.0 3B model from Hugging Face. Hub repo created 2025-07-08. Small on purpose.
- [SmolLM](https://github.com/huggingface/smollm) — Training and data recipes for the SmolLM series, including SmolLM3. Apache-2.0 models with the corpus work published alongside.

### Open weights, restricted licenses

- [Command R+](https://huggingface.co/CohereLabs/c4ai-command-r-plus) — Cohere's Command R+ weights. Hub license is CC BY-NC 4.0, so commercial use is not granted.
- [Aya Expanse 32B](https://huggingface.co/CohereLabs/aya-expanse-32b) — Cohere For AI's multilingual model. Hub license is CC BY-NC 4.0, the same non-commercial limit as Command R+.
- [DBRX](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm) — Databricks' March 2024 announcement of a 132B MoE. The weight host asked this ingest for authorization, so the public citation is the announcement, not a silent Hub mirror.
- [Falcon 180B](https://huggingface.co/tiiuae/falcon-180B) — TII's 180B model. The Hub card does not expose a standard SPDX license id; read the license file on the card before commercial use.
- [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) — Z.ai's text flagship. Hub license is custom, not the MIT license used by GLM-5.3-Flash. Hub repo created 2026-08-25.
- [Kimi K2](https://github.com/MoonshotAI/Kimi-K2) — Moonshot's Kimi K2 code and release repo. Later Kimi K3 weights are a separate card with their own license.
- [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) — Open-weight multimodal model, Hub license name kimi-k3 (custom, not Apache or MIT). Hub repo created 2026-06-13.
- [Nemotron 70B Instruct](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Instruct-HF) — NVIDIA's instruct tune of Llama 3.1 70B. Hub license is llama3.1, so the Llama community terms still apply.
- [OpenELM 3B](https://huggingface.co/apple/OpenELM-3B) — Apple's 3B open-weight model. Hub license is the Apple AMLR research license, not Apache-2.0.
- [OpenELM paper page](https://machinelearning.apple.com/research/openelm) — Apple's research page for OpenELM. The weights are public; the license is Apple's, not an OSI license.
- [LFM2-8B-A1B](https://huggingface.co/LiquidAI/LFM2-8B-A1B) — Liquid AI's 8B mixture model. Hub license is custom. Hub repo created 2025-10-07.
- [StarCoder2 15B](https://huggingface.co/bigcode/starcoder2-15b) — BigCode's 15B code model. Hub license is BigCode OpenRAIL-M, which is a responsible-use license, not plain Apache-2.0.
- [StarCoder2](https://github.com/bigcode-project/starcoder2) — The StarCoder2 release repo. Pair it with the model card so the OpenRAIL-M terms are not missed.
- [StableLM 2 12B](https://huggingface.co/stabilityai/stablelm-2-12b) — Stability AI's 12B model. The Hub license field is a custom Stability license, not Apache-2.0.
- [StableLM](https://github.com/Stability-AI/StableLM) — Stability's language-model repo. Check the checkpoint license; the org name is not a license.
- [InternLM](https://github.com/InternLM/InternLM) — Shanghai AI Lab's InternLM code and model line. Treat the license on the checkpoint you download as the license, not this README's tone.
- [MiniCPM](https://github.com/OpenBMB/MiniCPM) — OpenBMB's small-model line, aimed at edge devices. Confirm the license file in the version you pull.
- [Hunyuan-A13B](https://github.com/Tencent-Hunyuan/Hunyuan-A13B) — Tencent's earlier Hunyuan-A13B MoE. Hy4 preview is the newer Apache-2.0 Hy release; this repo is the prior line.

## Use cases

Applications and libraries that run on open weights. Hosted-only products stay out.

### Agents

- [AutoGen](https://github.com/microsoft/autogen) — Microsoft's multi-agent framework. Model calls go through an OpenAI-compatible client, so a local runtime can sit behind it.
- [browser-use](https://github.com/browser-use/browser-use) — Python library that lets a model drive a real browser. It does not ship a model; you bring an open one.
- [CrewAI](https://github.com/crewAIInc/crewAI) — Role-based multi-agent library. Open code; the model is whichever server you configure.
- [goose](https://github.com/aaif-goose/goose) — Open-source extensible agent from the goose project (the block/goose URL redirects here). It installs, edits, and runs code against any configured LLM.
- [GPT Researcher](https://github.com/assafelovic/gpt-researcher) — Autonomous research agent that plans a query, reads pages, and writes a report. Swap the model endpoint for a local one.
- [LangGraph](https://github.com/langchain-ai/langgraph) — Graph runtime for agent workflows from the LangChain team. Open source library, not a weight release.
- [Open Interpreter](https://github.com/openinterpreter/openinterpreter) — Local-first interpreter that lets a model run code on your machine. Point it at Ollama or llama.cpp rather than assuming a hosted default.
- [OpenHands](https://github.com/OpenHands/OpenHands) — Open-source software-engineering agent that drives a shell, editor, and browser against whatever model you point it at, including a local server.
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) — Typed agent library from the Pydantic team. Useful when the model is local and you still want structured tool calls.
- [smolagents](https://github.com/huggingface/smolagents) — Hugging Face's small agent library. It is code-agent shaped and runs against local model servers, not a hosted product.
- [STORM](https://github.com/stanford-oval/storm) — Stanford's open research agent for writing Wikipedia-style articles with citations. A research system, not a hosted writer.

### Coding

- [Aider](https://github.com/Aider-AI/aider) — Terminal pair-programmer that edits a git repo. It speaks to any OpenAI-compatible server, including a local open model.
- [Cline](https://github.com/cline/cline) — Open-source VS Code coding agent that can run commands in the workspace. You choose the model, including local endpoints.
- [Continue](https://github.com/continuedev/continue) — Open-source IDE extension for chat and edits. Local models via Ollama and llama.cpp are a documented path, not an afterthought.
- [OpenCode](https://github.com/anomalyco/opencode) — Open-source coding agent (the sst/opencode URL redirects here). A terminal UI, not a weight release.
- [Roo Code](https://github.com/RooCodeInc/Roo-Code) — Open-source fork of the Cline-style coding agent, with its own modes. Same caveat: the model is not bundled.
- [Tabby](https://github.com/TabbyML/tabby) — Self-hosted code completion server. It serves open code models; it is not a closed Copilot clone with a key.
- [Void](https://github.com/voideditor/void) — Open-source editor forked toward local and self-hosted models. The editor is the product; you still pick the weights.

### RAG and knowledge

- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) — Desktop and server app for chatting with your documents through Ollama, LM Studio, or another local backend.
- [Dify](https://github.com/langgenius/dify) — Open app builder for RAG and agents. You can point the model provider at a local OpenAI-compatible server.
- [Docling](https://github.com/docling-project/docling) — Document parser that turns PDFs and office files into structured text for a RAG index. It is not itself a language model.
- [FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) — BAAI's embedding and reranker code, including BGE. Open retrieval models, used next to open generators.
- [GraphRAG](https://github.com/microsoft/graphrag) — Microsoft's open graph-based retrieval pipeline. It calls a model you configure; the graph step is the point.
- [Haystack](https://github.com/deepset-ai/haystack) — Open pipeline library for retrieval and question answering. Local generators are a normal backend.
- [Khoj](https://github.com/khoj-ai/khoj) — Self-hosted personal research assistant over your notes and documents, with local model support.
- [LlamaIndex](https://github.com/run-llama/llama_index) — Data framework for retrieval on top of an LLM. The name is historical; it is not tied to Meta's license.
- [PrivateGPT](https://github.com/zylon-ai/private-gpt) — The early local-document QA app. Still a clear example of RAG that never sends the prompt to a hosted model.
- [RAGFlow](https://github.com/infiniflow/ragflow) — Open RAG engine with document parsing and a UI. Aimed at self-hosting, including open models.
- [Sentence Transformers](https://github.com/huggingface/sentence-transformers) — The usual open library for embedding models that sit in front of an open generator.

### Creative and local chat

- [Hugging Face Chat UI](https://github.com/huggingface/chat-ui) — Open chat interface used by HuggingChat. You can run it against your own text-generation server.
- [koboldcpp](https://github.com/LostRuins/koboldcpp) — Single-file llama.cpp distribution aimed at story and roleplay front ends. A runtime and a creative app at once.
- [SillyTavern](https://github.com/SillyTavern/SillyTavern) — Front end for local roleplay and character chat. It connects to koboldcpp, llama.cpp, Ollama, and similar backends.

### On-device apps

- [exo](https://github.com/exo-explore/exo) — Runs a model across a cluster of home machines. An open runtime for machines you already own, not a cloud product.
- [PocketPal AI](https://github.com/a-ghorbani/pocketpal-ai) — Mobile app that runs GGUF models on-device through llama.cpp. The weights are whatever you download into it.
- [WebLLM](https://github.com/mlc-ai/web-llm) — Runs open models in the browser with WebGPU. In-browser weights, not a call to a vendor API.

### Research tools

- [DSPy](https://github.com/stanfordnlp/dspy) — Stanford's framework for programming language models instead of hand-writing prompts. Works with local model clients.
- [Guidance](https://github.com/guidance-ai/guidance) — Constraint and templating library for generation. Useful when an open model has to follow a format.
- [Instructor](https://github.com/567-labs/instructor) — Pydantic structured output on top of model APIs, including local OpenAI-compatible servers.
- [LLMs from Scratch](https://github.com/rasbt/LLMs-from-scratch) — Sebastian Raschka's book-style repo that implements a GPT, then trains and fine-tunes it, in readable PyTorch.
- [Outlines](https://github.com/dottxt-ai/outlines) — Constrained decoding so a model emits JSON or a regex. The outlines-dev URL redirects here.
- [SAELens](https://github.com/decoderesearch/SAELens) — Sparse-autoencoder tooling for open models. The jbloomAus/SAELens URL redirects here.
- [TransformerLens](https://github.com/TransformerLensOrg/TransformerLens) — Mechanistic-interpretability library for looking inside decoder models, including open checkpoints.

## Runtimes and local serving

Engines and apps that load those weights on your own machine. A polished desktop app is not the same thing as an open-source engine.

### Inference engines

- [Candle](https://github.com/huggingface/candle) — Hugging Face's Rust tensor library, with LLM examples. A minimal runtime, not a serving stack.
- [ExLlamaV2](https://github.com/turboderp-org/exllamav2) — GPU inference for EXL2 quantizations of open models. Faster than a naive Transformers load, narrower than vLLM.
- [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp) — A llama.cpp fork focused on quantization and CPU/GPU kernels. Use it when mainline GGUF is not enough; it is not the upstream project.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) — C and C++ inference for GGUF models on CPU and GPU. The ggerganov/llama.cpp URL redirects here. This is the default local runtime.
- [llama2.c](https://github.com/karpathy/llama2.c) — One-file C inference for a Llama 2 architecture. A teaching runtime, not a serving stack.
- [llamafile](https://github.com/mozilla-ai/llamafile) — Runs an open model as a single executable file. The Mozilla-Ocho URL redirects here.
- [LMDeploy](https://github.com/InternLM/lmdeploy) — InternLM's serving toolkit for compressed open models, with a TurboMind backend. Not limited to InternLM weights.
- [MLC LLM](https://github.com/mlc-ai/mlc-llm) — Compiles open models onto native and browser runtimes. The engine behind a lot of on-device and WebGPU demos.
- [MLX LM](https://github.com/ml-explore/mlx-lm) — Apple's MLX library for running and fine-tuning language models on Apple silicon.
- [ONNX Runtime GenAI](https://github.com/microsoft/onnxruntime-genai) — Microsoft's generative runtime on top of ONNX Runtime, used for Windows and on-device open models.
- [SGLang](https://github.com/sgl-project/sglang) — Serving runtime for open models, often faster than a stock vLLM setup on the same GPU. Open code.
- [TabbyAPI](https://github.com/theroyallab/tabbyAPI) — OpenAI-compatible server in front of ExLlamaV2. A server, not a model.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) — NVIDIA's open compiler and runtime for LLM inference on its GPUs. Apache-2.0 code; it runs open weights, it is not a weight license.
- [Text Generation Inference](https://github.com/huggingface/text-generation-inference) — Hugging Face's production serving stack for Hub models. Open code, aimed at GPU servers rather than laptops.
- [vLLM](https://github.com/vllm-project/vllm) — The common open serving engine for open weights: paged attention, continuous batching, and an OpenAI-compatible API.

### Local apps and front ends

- [GPT4All](https://github.com/nomic-ai/gpt4all) — Desktop app for running local chat models, plus its own historically released small models. The app is the reason to list it.
- [Jan](https://github.com/janhq/jan) — Open-source desktop app for downloading and chatting with local models.
- [LiteLLM](https://github.com/BerriAI/litellm) — A proxy that presents many backends, including Ollama and vLLM, as one OpenAI-compatible API.
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) — Python bindings for llama.cpp, including an OpenAI-compatible server. Bindings, not a new engine.
- [llm](https://github.com/simonw/llm) — Simon Willison's CLI for calling models, with plugins for local backends. A client, not a weight file.
- [LM Studio](https://lmstudio.ai/) — Desktop app for running local models. The app itself is not open source; the open pieces are the lms CLI and mlx-engine repos.
- [lms](https://github.com/lmstudio-ai/lms) — Open CLI for LM Studio. This repo is not the closed desktop shell.
- [LocalAI](https://github.com/mudler/LocalAI) — OpenAI-compatible server that wraps local models, including llama.cpp backends. Self-hosted, not a LocalAI cloud.
- [mlx-engine](https://github.com/lmstudio-ai/mlx-engine) — Open MLX inference engine used by LM Studio on Apple silicon.
- [Ollama](https://github.com/ollama/ollama) — Open-source local runner that pulls a model and serves it. The model license is still the license of the weights you pull.
- [Open WebUI](https://github.com/open-webui/open-webui) — Open web interface commonly sat in front of Ollama. A UI, not a model.
- [textgen](https://github.com/oobabooga/textgen) — Open-source desktop app for local LLMs. The old text-generation-webui URL redirects here.

### Edge and in-browser

- [BitNet](https://github.com/microsoft/BitNet) — Microsoft's 1-bit LLM inference code. A research runtime for ternary and bitnet-style models, not a general GGUF server.
- [Cactus](https://github.com/cactus-compute/cactus) — Edge inference stack named in the Gemma 4 launch as a day-one target. Open code for running small models off-server.
- [ExecuTorch](https://github.com/pytorch/executorch) — PyTorch's on-device runtime. Used to ship small open models onto phones, not to serve a 70B.
- [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) — Google's edge LLM runtime, the path Gemma documents for on-device runs.
- [MLX-VLM](https://github.com/Blaizzy/mlx-vlm) — Vision-language inference on Apple MLX. The text-only path is mlx-lm; this is the multimodal one.
- [Transformers.js](https://github.com/huggingface/transformers.js) — Runs Hub models in the browser and Node through ONNX. Practical for small open models, not frontier MoEs.

## Training, finetune and alignment

Open code for pretraining, fine-tuning, and preference optimization. Checkpoints without a training stack live under models.

### Pretraining stacks

- [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) — Microsoft's distributed training library, ZeRO included. The microsoft/DeepSpeed URL redirects here.
- [Levanter](https://github.com/marin-community/levanter) — JAX trainer used by the Marin open-model effort. The stanford-crfm/levanter URL redirects here.
- [Lingua](https://github.com/facebookresearch/lingua) — Meta's research training codebase for language models. Open code; it does not relicense Llama weights.
- [LitGPT](https://github.com/Lightning-AI/litgpt) — Lightning's readable implementation of open model architectures, with pretrain and fine-tune recipes.
- [LLM Foundry](https://github.com/mosaicml/llm-foundry) — Mosaic's training recipes on top of Composer. Open pretraining code; the Composer org is now part of Databricks.
- [llm.c](https://github.com/karpathy/llm.c) — Training a GPT in plain C and CUDA, for people who want the kernels without a framework.
- [Mamba](https://github.com/state-spaces/mamba) — State-space model code, an alternative to the Transformer used by almost everything else in this list.
- [MaxText](https://github.com/AI-Hypercomputer/maxtext) — JAX reference trainer for LLMs on Google's accelerator stack. Open code, not a Gemma weight.
- [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) — NVIDIA's large-model training library. The code many cluster pretrains still fork.
- [modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt) — A speedrun of nanoGPT: the same small training task, with the tricks that actually cut the wall-clock time.
- [nanochat](https://github.com/karpathy/nanochat) — Karpathy's later minimal stack that trains a small chat model end to end, including the tokenization and the fine-tune.
- [nanoGPT](https://github.com/karpathy/nanoGPT) — Andrej Karpathy's small, readable GPT trainer. A teaching codebase, not a cluster stack.
- [nanotron](https://github.com/huggingface/nanotron) — Hugging Face's small 3D-parallelism trainer. A research pretraining stack, lighter than Megatron.
- [TorchTitan](https://github.com/pytorch/torchtitan) — PyTorch's reference distributed trainer for large language models.

### Finetune and alignment

- [Accelerate](https://github.com/huggingface/accelerate) — Hugging Face's device and distributed launcher. Most of the fine-tune tools here sit on it.
- [Alignment Handbook](https://github.com/huggingface/alignment-handbook) — Recipes that reproduce known chat and preference fine-tunes with TRL. A cookbook, not a new algorithm.
- [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) — YAML-driven fine-tune runner used widely on open models. The OpenAccess-AI-Collective URL redirects here.
- [distilabel](https://github.com/argilla-io/distilabel) — Synthetic-data and preference-data pipeline. Open code for building the sets the fine-tune tools consume.
- [FSDP QLoRA](https://github.com/AnswerDotAI/fsdp_qlora) — Answer.AI's code for QLoRA under FSDP, which is how people fine-tune larger open models on more than one GPU.
- [Llama Cookbook](https://github.com/metainternal/llama-cookbook) — Meta's Llama recipes for inference, fine-tuning, and RAG. The meta-llama/llama-cookbook URL redirects here. Recipes, not a new license.
- [LLaMA-Factory](https://github.com/hiyouga/LlamaFactory) — Web and CLI fine-tune tool for a long list of open models. The LLaMA-Factory spelling redirects here.
- [mistral-finetune](https://github.com/mistralai/mistral-finetune) — Mistral's reference fine-tune code for its open models.
- [ms-swift](https://github.com/modelscope/ms-swift) — ModelScope's fine-tune toolkit, commonly used on Qwen and other open checkpoints.
- [NeMo-Aligner](https://github.com/NVIDIA/NeMo-Aligner) — NVIDIA's alignment toolkit (SFT, RLHF, DPO) for its training stack. The NeMo GitHub name now redirects to a speech repo, so this is the alignment link.
- [Open R1](https://github.com/huggingface/open-r1) — Hugging Face's open reproduction of the DeepSeek-R1 training recipe. Code and notes, not a claim of identical weights.
- [open-instruct](https://github.com/allenai/open-instruct) — AllenAI's post-training recipes, including the Tulu line. Fully open fine-tunes, with the data releases that go with them.
- [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) — Open RLHF stack for preference optimization at scale. Built for open weights, not a closed API.
- [PEFT](https://github.com/huggingface/peft) — Parameter-efficient fine-tunes, LoRA included, for open checkpoints.
- [QLoRA](https://github.com/artidoro/qlora) — The original QLoRA code: 4-bit base weights plus LoRA. The paper's repo, still the reference implementation.
- [torchtune](https://github.com/meta-pytorch/torchtune) — PyTorch-native post-training library. The pytorch/torchtune URL redirects here.
- [TRL](https://github.com/huggingface/trl) — Hugging Face's library for SFT, DPO, PPO, and related post-training. The default open alignment toolkit.
- [Unsloth](https://github.com/unslothai/unsloth) — Fine-tune library that patches kernels to use less memory. Open code aimed at LoRA on open weights.
- [verl](https://github.com/verl-project/verl) — RL post-training framework (HybridFlow). The volcengine/verl URL redirects here.

### Kernels and efficiency

- [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) — 8-bit and 4-bit optimizers and quantization used by QLoRA and a lot of Hugging Face fine-tunes.
- [DeepEP](https://github.com/deepseek-ai/DeepEP) — DeepSeek's expert-parallelism communication library. Training infrastructure published with the MoE line.
- [FlashAttention](https://github.com/Dao-AILab/flash-attention) — The fused attention kernel most open training and serving stacks optionally bind. A kernel repo, not a model.
- [FlashMLA](https://github.com/deepseek-ai/FlashMLA) — DeepSeek's Multi-head Latent Attention kernel. Open code that goes with the V2-and-later architecture.
- [Liger Kernel](https://github.com/linkedin/Liger-Kernel) — Triton kernels that drop memory use in open-model training.
- [Triton](https://github.com/triton-lang/triton) — OpenAI's compiler for writing GPU kernels in Python. Underneath many of the kernels above.

## Evals and papers

Boards, harnesses, and papers that are actually used to compare open models. Scores on the boards move; the links are the stable part.

### Leaderboards

- [AIHOT Model Leaderboard](https://aihot.news/leaderboard) — Chinese-language comparison of open-weight and proprietary models using independently measured public benchmarks across reasoning, coding, and other tasks.
- [AlpacaEval](https://github.com/tatsu-lab/alpaca_eval) — Automatic instruction-following eval. Cheap and gameable; useful as a regression check, not as a ranking of record.
- [Arena](https://arena.ai/) — Blind human-preference leaderboard. The lmarena.ai URL redirects here. Open and closed models share the board; read the license column before treating a rank as an open-weight result.
- [Arena leaderboard Space](https://huggingface.co/spaces/lmarena-ai/arena-leaderboard) — Hugging Face Space for the Arena board. The older chatbot-arena-leaderboard path redirects here.
- [Arena-Hard-Auto](https://github.com/lmarena/arena-hard-auto) — Automatic proxy for Arena hard prompts. A benchmark repo from the Arena authors, not the human board itself.
- [Artificial Analysis](https://artificialanalysis.ai/) — Independent index of model quality, speed, and price. Includes open-weight models and says when a number is the vendor's.
- [BigCode Evaluation Harness](https://github.com/bigcode-project/bigcode-evaluation-harness) — BigCode's fork of the eval harness aimed at code models, including StarCoder.
- [EvalPlus](https://github.com/evalplus/evalplus) — Stricter HumanEval and MBPP tests. A code-eval harness, not a leaderboard vendor.
- [Hallucination Leaderboard](https://github.com/vectara/hallucination-leaderboard) — Vectara's public board for summarization hallucinations. A narrow task, which is why it is still useful.
- [HELM](https://github.com/stanford-crfm/helm) — Stanford's Holistic Evaluation of Language Models. A broad eval suite, not a single score.
- [Humanity's Last Exam](https://github.com/centerforaisafety/hle) — The HLE benchmark repo from the Center for AI Safety. A hard closed-book exam used on both open and closed models.
- [LiveCodeBench](https://github.com/LiveCodeBench/LiveCodeBench) — Contamination-resistant coding benchmark that keeps adding problems after models are trained.
- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — Hugging Face Space for the Open LLM Leaderboard. A reproducible eval board for open models; check the Space for whether a given week is still updating.
- [simple-evals](https://github.com/openai/simple-evals) — OpenAI's small eval set, including GPQA and MMLU variants. Open code; it does not make the target model open.
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) — Real GitHub-issue benchmark for coding agents. The princeton-nlp URL redirects here. Used on open code models as well as closed ones.

### Harnesses

- [Inspect](https://github.com/UKGovernmentBEIS/inspect_ai) — UK AI Security Institute's eval framework. Open harness for writing task-based evals, including tool-use.
- [LightEval](https://github.com/huggingface/lighteval) — Hugging Face's eval runner, used by the Open LLM Leaderboard and by groups who do not want to fork the Eleuther harness.
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — EleutherAI's eval harness. The one open-model papers still mean when they say they ran the standard suite.
- [OLMES](https://github.com/allenai/olmes) — AllenAI's standardized eval setup for OLMo and other open models. The point is a fixed protocol, not a new test set.

### Papers

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Vaswani et al., 2017. The Transformer paper. Not an open-weight release; the architecture under every model in this list.
- [DCLM](https://arxiv.org/abs/2406.11794) — DataComp for language models. An open data-curation result, with a public baseline corpus.
- [DeepSeek-R1](https://arxiv.org/abs/2501.12948) — The R1 technical report: reasoning trained on the V3 base, with MIT weights and distilled smaller models.
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) — Architecture and training report for DeepSeek-V3. The weight license is the one in the repo, not this PDF.
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) — The DPO paper. The preference method implemented in TRL and most open alignment recipes.
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) — The GPT-3 paper. The weights were not released; it is here because the open GPT-Neo line was a response to that fact.
- [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288) — The Llama 2 paper, including the community license discussion. Read it next to the license file, not instead of it.
- [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) — The LLaMA paper. The models were a gated research release; the paper is the architecture and data description.
- [LoRA](https://arxiv.org/abs/2106.09685) — Hu et al. on low-rank adaptation. The method behind most open fine-tunes.
- [Mixtral of Experts](https://arxiv.org/abs/2401.04088) — The Mixtral paper. Sparse MoE details for the Apache-2.0 8x7B model.
- [Olmo 3](https://arxiv.org/abs/2512.13961) — The Olmo 3 paper. Fully open 7B and 32B models, including the model-flow claim.
- [ORPO](https://arxiv.org/abs/2402.03300) — Odds-ratio preference optimization without a reference model. One of the post-DPO methods open recipes actually ship.
- [QLoRA](https://arxiv.org/abs/2305.14314) — Dettmers et al. Fine-tuning a quantized open model on one GPU.
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — Kaplan et al. on loss versus compute. The plot people still argue with, including the later Chinchilla correction.
- [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) — The Llama 3 paper. Covers the open-weight 3.1 models, not Llama 4.
- [The RefinedWeb Dataset](https://arxiv.org/abs/2306.01116) — Falcon's public web dataset paper. A pretraining-data release, which is rarer than a weight release.
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) — The Chinchilla paper. Why later open models spent tokens, not just parameters.
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — InstructGPT. Closed weights; the reason the open chat models exist as a category.
- [Tulu 3](https://arxiv.org/abs/2411.15124) — AllenAI's open post-training recipe and the evals that go with it.

## Docs and essays

Explainers worth reading before you pick a license or a runtime.

- [Hugging Face blog](https://huggingface.co/blog) — First-party write-ups when a weight release lands on the Hub, including the DeepSeek-V4 post linked above.
- [Hugging Face Llama 3 blog](https://huggingface.co/blog/llama3) — How Llama 3 was wired into the Hub and the open fine-tune tools on release day. A practical companion to Meta's post.
- [Interconnects](https://www.interconnects.ai/) — Nathan Lambert's newsletter. The open-model and post-training coverage is the reason it is here.
- [Latent Space](https://www.latent.space/) — Swyx and Alessio's podcast and newsletter. Interviews and paper walkthroughs, not a benchmark.
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — Lilian Weng's 2023 survey of agent patterns. The diagram people still copy.
- [Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) — The OSI's definition. The line this list uses between Apache-or-MIT and a custom weight license.
- [Patterns for Building LLM Systems](https://eugeneyan.com/writing/llm-patterns/) — Eugene Yan's notes on production LLM patterns. Pairs with his open-llm index.
- [Simon Willison's weblog](https://simonwillison.net/) — Running notes on local models and the tools around them, usually with the command he actually typed.
- [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) — Rich Sutton's essay on general methods that scale. Background, not a model release.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Jay Alammar's walkthrough of the architecture. Still the clearest single picture.
- [You can now train a 70b language model at home](https://www.answer.ai/posts/2024-03-06-fsdp-qlora.html) — Answer.AI's FSDP-QLoRA write-up. The code is the fsdp_qlora repo in the training section.

## Datasets

High-signal corpora and the tools that build them. Most chat fine-tunes are not here.

### Pretraining data

- [DCLM baseline](https://huggingface.co/datasets/mlfoundations/dclm-baseline-1.0) — The public baseline corpus from the DCLM paper. A data-curation result you can download.
- [Dolma](https://github.com/allenai/dolma) — AllenAI's open corpus toolkit and data, the pretraining source for OLMo.
- [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) — Hugging Face's large cleaned web corpus. The common public pretraining set after RefinedWeb.
- [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) — The education-filtered slice of FineWeb. Smaller, and what a lot of small-model recipes actually train on.
- [RedPajama](https://github.com/togethercomputer/RedPajama-Data) — Together's open reproduction of the Llama training mix. A dataset project, not a model.
- [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb) — TII's filtered web dataset, released with the Falcon models. The paper is in the evals section.
- [The Pile](https://github.com/EleutherAI/the-pile) — EleutherAI's 800GB public corpus, the pretraining set for the early Pythia and GPT-NeoX models.
- [The Stack v2](https://huggingface.co/datasets/bigcode/the-stack-v2) — BigCode's code corpus for StarCoder2. Software-license filtered, which is why it is not 'all of GitHub'.

### Post-training data

- [LMSYS-Chat-1M](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) — A million real conversations collected by LMSYS. Human prompts, with the privacy processing described on the card.
- [Magpie](https://github.com/magpie-align/magpie) — Generates instruction data from an aligned model without a human seed set. A method and a code release.
- [OpenHermes 2.5](https://huggingface.co/datasets/teknium/OpenHermes-2.5) — A widely reused synthetic instruction set. High signal as a historical SFT mix, not as a current frontier recipe.
- [Tulu 3 SFT mixture](https://huggingface.co/datasets/allenai/tulu-3-sft-mixture) — The supervised-fine-tune mix from the Tulu 3 paper. Public post-training data with a paper attached.
- [UltraChat 200k](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k) — A 200k-scale chat set used in open SFT recipes. Synthetic user-assistant turns, not human preference data.

### Data tools

- [datatrove](https://github.com/huggingface/datatrove) — Hugging Face's library for filtering and deduplicating large text corpora. The tool behind FineWeb-style pipelines.

## Awesome lists and indexes

Related indexes. This list does not try to replace a general LLM bibliography.

- [Awesome LLM resources](https://github.com/WangRongsheng/awesome-LLM-resources) — A large Chinese-and-English bookmark list of LLM papers and repos. An index, not a curated open-weight catalog.
- [Awesome Transformer NLP](https://github.com/cedrickchee/awesome-transformer-nlp) — Older awesome list of Transformer papers and code. Useful history, not a 2026 model picker.
- [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) — A broad awesome list of LLM papers, tools, and models. Much wider than open weights.
- [awesome-llm-os](https://github.com/bilalonur/awesome-llm-os) — A list about LLMs as operating systems. A different topic from this repo; linked so the names are not confused.
- [LLM Course](https://github.com/mlabonne/llm-course) — Maxime Labonne's course-shaped list of LLM papers and tooling, with a bias toward things you can run.
- [open-llms](https://github.com/eugeneyan/open-llms) — Eugene Yan's table of open LLMs with licenses and sizes. An index this list consulted, not a mirror of it.

## Community

Places people actually discuss running open weights.

- [EleutherAI](https://www.eleuther.ai/) — The research group behind GPT-Neo, Pythia, the Pile, and the eval harness. Still the closest thing to an institution for open model science.
- [Hugging Face Discord](https://discord.com/invite/huggingface) — The public Discord invite for the Hub. Model-specific channels move; this is the front door.
- [Hugging Face Hub](https://huggingface.co/) — Where the weight files, dataset cards, and licenses actually live. A model is not 'released' for this list until it is here or in a vendor repo.
- [llama.cpp discussions](https://github.com/ggml-org/llama.cpp/discussions) — The practical forum for GGUF, quants, and 'does this checkpoint run'. More useful than a general chat room if you are serving locally.

## Sources

Indexes consulted for this pass. Entries were not bulk-copied; each README link was checked on its own. Machine-readable rows: [`links.json`](links.json). Counts: [`stats.txt`](stats.txt). Recent-launch notes that did not all earn a README line: [`discoveries/`](discoveries/).

- Manual curation — Entries written for this list on 2026-09-22 PT.
- [Hugging Face Hub API](https://huggingface.co/models) — Model id, license field, pipeline tag, and createdAt.
- [eugeneyan/open-llms](https://github.com/eugeneyan/open-llms) — Consulted as an open-weight index; links re-checked.
- [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) — Consulted as a broad LLM index; not bulk-imported.
- [Open-weights release timeline (Hidekazu Konishi)](https://hidekazu-konishi.com/entry/open_weights_llm_release_history_and_timeline.html) — Family history. A date is repeated here only when a first-party page or Hub createdAt agreed.
- [Vendor pages and GitHub orgs](https://github.com/QwenLM/Qwen3.8) — Meta, Mistral, Google DeepMind, DeepSeek, Ai2, Qwen, OpenAI gpt-oss repo.
- [Grok-1 README](https://github.com/xai-org/grok-1) — License sentence quoted from the repo README, not from a secondary recap.

## Contributing

One factual line in the right subsection: `[Name](url) — What it actually is.` Say whether weights are Apache-2.0 or MIT, or a community / research / non-commercial license. Do not invent star counts, release days, benchmark scores, or tweet ids. Prefer a model card or official repo over a roundup. Weak or unverified finds go in [`discoveries/`](discoveries/) instead of the README.

Add the row to [`links.json`](links.json) (url, title, category, subsection, blurb, sources) and run `python3 build.py`. The script dedupes on the normalized URL and rewrites this file.

List text is dedicated to the public domain under [CC0 1.0](LICENSE). Linked projects keep their own licenses.

## License

This compilation is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Individual projects and linked content retain their own licenses and terms.
