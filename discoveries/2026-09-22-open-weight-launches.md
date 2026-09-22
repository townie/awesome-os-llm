# Open-weight launches checked 2026-09-22

Hunt date: **2026-09-22 PT**. This shard is the working note for the first catalog pass. It is not a second README. Stars, benchmark scores, and tweet ids were not recorded, because this pass did not have a clean primary source for them.

Method: Hugging Face Hub API (`createdAt`, `license`, `pipeline_tag`) plus an HTTP check of the page that would be linked. A secondary roundup was only a pointer. If the Hub or the vendor page did not confirm the claim, the claim stayed here or was dropped.

## Folded into the README

These are the recent weight repos the README actually cites. Dates are Hub `createdAt`, not a blog's announced day, unless a first-party post was also checked.

| Hub repo | createdAt | License field | Pipeline | Where it landed |
| --- | --- | --- | --- | --- |
| [deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) | 2026-09-10 | mit | image-text-to-text | DeepSeek |
| [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | 2026-08-05 | apache-2.0 | image-text-to-text | Qwen |
| [Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) | 2026-08-08 | other | text-generation | Qwen (custom license, called out) |
| [tencent/Hy4-preview](https://huggingface.co/tencent/Hy4-preview) | 2026-08-27 | apache-2.0 | text-generation | Permissive open weights |
| [zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) | 2026-08-25 | other | text-generation | Restricted licenses |
| [zai-org/GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) | 2026-08-25 | mit | image-text-to-text | Permissive open weights |
| [moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) | 2026-06-13 | other (`kimi-k3`) | image-text-to-text | Restricted licenses |
| [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it) | 2026-03-11 | apache-2.0 | image-text-to-text | Gemma |
| [mistralai/Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) | 2026-01-23 | apache-2.0 | (unset on the API) | Mistral, next to the [news post](https://mistral.ai/news/mistral-small-4/) |

Also checked and folded, older than this month but easy to miss: [openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) and [openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) (Apache-2.0, Hub `createdAt` 2025-08-04). The `openai.com` announcement URLs returned **403** to this checker, so they are not the cited links. The GitHub repo is [openai/gpt-oss](https://github.com/openai/gpt-oss).

DeepSeek's own V4 preview post was HTTP 200: [deepseek.com/en/news/v4-preview](https://www.deepseek.com/en/news/v4-preview/). The April Flash repo and the 2026-07-31 Flash repo are separate Hub ids; the README cites Pro, Flash-0731, and V4.1 rather than every shard.

## Checked, not given a README line

- **Llama 4 Behemoth.** No public weight repo turned up. Scout and Maverick are the Llama 4 entries. Secondary posts still call Behemoth unreleased; that was not re-proven from a 2026 Meta page, so the README simply does not list it.
- **DBRX weights.** `huggingface.co/databricks/dbrx-instruct` returned **401**. The README links the [Databricks announcement](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm) only.
- **SlimPajama and Nemotron-CC dataset cards** returned **401**. RedPajama, FineWeb, DCLM, and Dolma are the pretraining entries instead.
- **r/LocalLLaMA** returned **403** to this checker. It is the obvious forum and it is not linked, because the URL could not be confirmed from here. llama.cpp discussions and the Hub are the community entries.
- **Aphrodite.** `PygmalionAI/aphrodite-engine` and `aphrodite-engine/aphrodite-engine` redirect to [dphnAI/sonar](https://github.com/dphnAI/sonar), whose title is "Large-scale LLM inference engine." Not listed. The redirect was not read far enough to say Sonar is the same project.
- **NVIDIA/NeMo** redirects to `NVIDIA-NeMo/Speech`. The alignment toolkit that still resolves is [NeMo-Aligner](https://github.com/NVIDIA/NeMo-Aligner), which is in the README. The old NeMo name is not used as an LLM link.
- **Ranking blogs** ([one September 2026 comparison](https://zyvop.com/best-open-weight-llms-september-2026-d4ujd), [a license timeline](https://hidekazu-konishi.com/entry/open_weights_llm_release_history_and_timeline.html)). Used to find Hub ids. Their score tables were not copied. Where a timeline date and a Hub `createdAt` disagreed (gpt-oss-safeguard), the README omits the day.

## Out of scope on purpose

[awesome-llm-os](https://github.com/bilalonur/awesome-llm-os) is about LLMs as operating systems. It is one line in the awesome-list section so the names are not confused. Metaphor-only "LLM OS" posts were not collected.
