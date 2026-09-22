# Sources consulted

Ingest date: **2026-09-22 PT** (America/Los_Angeles).

This catalog is a manual check of primary pages. It is not a bulk import of the indexes below. Every README bullet comes from [`links.json`](links.json), and every URL in that file was requested on the ingest date except [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/), which answered HTTP 403 to this environment's client (Reddit's bot wall, not a 404).

| Source | URL | How it was used |
| --- | --- | --- |
| Hugging Face model and dataset API | https://huggingface.co | Existence, `license` / `license_name`, and README frontmatter for weight and dataset entries. |
| GitHub REST API (`gh api`) | https://github.com | Repository existence, SPDX field, archive bit, and LICENSE or README text where the SPDX field was empty or the grant was easy to misread. |
| Hannibal046/Awesome-LLM | https://github.com/Hannibal046/Awesome-LLM | Consulted for milestone papers, training frameworks, and inference tools. Last push seen: 2025-07-31. Not bulk-imported. |
| eugeneyan/open-llms | https://github.com/eugeneyan/open-llms | Consulted as a short commercial-use list. Last push seen: 2025-02-13. Not bulk-imported. |
| QwenLM/Qwen3.8 README news log | https://github.com/QwenLM/Qwen3.8 | Dates for Qwen3.5, Qwen3.6, and Qwen3.8 weight posts are quoted from that file. |
| Kimi K3 LICENSE | https://github.com/MoonshotAI/Kimi-K3/blob/main/LICENSE | Model-as-a-Service and attribution clauses quoted from the license text. |
| Open WebUI LICENSE | https://github.com/open-webui/open-webui/blob/main/LICENSE | Branding clause above 50 end users, read from the license text. |
| Gemma 4 model card | https://huggingface.co/google/gemma-4-31b-it | Apache-2.0 statement and the note that Gemma 4's grant differs from earlier Gemma terms. |
| DeepSeek-V4-Pro model card | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro | MIT frontmatter and the link to arXiv:2606.19348. Confirmed there is no `deepseek-ai/DeepSeek-V4` GitHub repo. |
| Muse Glimmer model card | https://huggingface.co/meta-models/Muse-Glimmer-30B | Apache-2.0, August 2026 release date, and the distillation note, taken from the card. |
| bilalonur/awesome-llm-os | https://github.com/bilalonur/awesome-llm-os | Read only to keep this list from covering LLM-as-operating-system. |

Normalization: strip the fragment and query, strip a trailing slash and a trailing `.git`, lowercase the scheme and host, and drop a leading `www.` URLs that match after that are duplicates and `build.py` refuses to render them.

Items that were real enough to notice and too uncertain for the README are in [`discoveries/2026-09-22.md`](discoveries/2026-09-22.md).
