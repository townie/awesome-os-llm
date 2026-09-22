#!/usr/bin/env python3
"""Regenerate README.md and stats.txt from links.json.

Edit links.json, then run `python3 build.py`. The script deduplicates by
normalized URL, orders sections from OUTLINE, and sorts each subsection
alphabetically unless an entry sets `pin` (used for landmark chronology).
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse, urlunparse

ROOT = Path(__file__).resolve().parent
LINKS_PATH = ROOT / "links.json"
README_PATH = ROOT / "README.md"
STATS_PATH = ROOT / "stats.txt"

INGEST_DATE = "2026-09-22 PT"

# (category, [subsections], category blurb or "")
OUTLINE: list[tuple[str, list[str], str]] = [
    (
        "Landmark open models",
        [
            "Early open weights",
            "Meta Llama",
            "Mistral",
            "Qwen",
            "Google Gemma",
            "DeepSeek",
            "Microsoft Phi",
            "Allen Institute OLMo",
            "Other families",
        ],
        "Families with public weights. A bullet names the license on the linked card or repo. Open weights are not the same thing as an OSI license, and a finetune keeps the base model's terms.",
    ),
    (
        "Runtimes and local serving",
        [
            "Inference engines",
            "Local apps and front ends",
            "On-device and edge",
        ],
        "Ways to run weights on hardware you control. Hosted-only APIs are left out.",
    ),
    (
        "Training, finetune and alignment",
        [
            "Finetune and post-training",
            "Pretraining",
            "Preference, RL and data",
        ],
        "Open code for training and adapting language models. A library that only calls a closed API is not listed.",
    ),
    (
        "Use cases",
        [
            "Agents and coding",
            "RAG and knowledge",
            "Creative and local chat",
            "Voice",
            "Structured output",
        ],
        "Apps and libraries people use on top of open weights. A project that cannot point at a local or open model is not a fit.",
    ),
    (
        "Evals and papers",
        [
            "Leaderboards and harnesses",
            "Papers",
        ],
        "Harnesses and papers that still matter when the model is open-weight. Leaderboard ranks move; the link is the method, not a score.",
    ),
    (
        "Datasets",
        [],
        "High-signal corpora for pretraining and post-training. Licenses are uneven; ODC-By and CC-BY are not the same as the model license you ship.",
    ),
    (
        "Docs and essays",
        [],
        "Short readings that explain the stack without pretending to be a benchmark.",
    ),
    (
        "Awesome lists and indexes",
        [],
        "Related catalogs. None of these is a substitute for checking a weight's license, and awesome-llm-os is a different topic.",
    ),
    (
        "Community",
        [],
        "Places where open-weight work is actually discussed.",
    ),
]

SUBSECTION_BLURB: dict[tuple[str, str], str] = {
    ("Landmark open models", "Early open weights"): "Public checkpoints from before the Llama license era. Several are research-licensed or use-restricted.",
    ("Landmark open models", "Meta Llama"): "Meta's Llama line. Every shipping generation here uses a Llama community license, not Apache-2.0 or MIT.",
    ("Landmark open models", "Mistral"): "Mistral's open-weight line. Apache-2.0 and the Mistral Research License both appear; the bullet says which.",
    ("Landmark open models", "Qwen"): "Alibaba's Qwen line. Many dense and small MoE checkpoints are Apache-2.0; the largest Qwen3.8 release is not.",
    ("Landmark open models", "Google Gemma"): "Gemma 1 through 3 use the Gemma license. Gemma 4's model cards checked here say Apache-2.0.",
    ("Landmark open models", "DeepSeek"): "DeepSeek publishes weights. MIT on a GitHub repo is not automatically the license file sitting next to every checkpoint.",
    ("Landmark open models", "Microsoft Phi"): "Microsoft's small models. The cards checked here are MIT.",
    ("Landmark open models", "Allen Institute OLMo"): "The rare stack that releases weights, training code, and pretraining data under Apache-2.0 / ODC-By rather than weights alone.",
    ("Landmark open models", "Other families"): "Other real open-weight families. Sorted alphabetically. License caveats are the point of the line.",
    ("Runtimes and local serving", "Inference engines"): "Servers and libraries that load weights and produce tokens.",
    ("Runtimes and local serving", "Local apps and front ends"): "Desktop and web apps in front of a local engine. Some are permissively licensed; Open WebUI is not plain BSD.",
    ("Runtimes and local serving", "On-device and edge"): "Runtimes aimed at phones, browsers, and single-file or laptop deployment.",
    ("Use cases", "Creative and local chat"): "Front ends aimed at roleplay and long-context chat. General local chat shells are listed under local apps.",
}


def normalize_url(url: str) -> str:
    url = (url or "").strip()
    if not url or url.startswith(("#", "mailto:")):
        return ""
    url = url.split("#", 1)[0].split("?", 1)[0].rstrip("/")
    if url.endswith(".git"):
        url = url[:-4]
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return ""
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = parsed.path or ""
    path = path.rstrip("/")
    while "//" in path:
        path = path.replace("//", "/")
    return urlunparse((parsed.scheme.lower(), host, path, "", "", ""))


def github_slug(text: str) -> str:
    """Match GitHub's heading anchors: drop punctuation, keep spaces as hyphens."""
    cleaned = []
    for ch in text.lower():
        if ch.isalnum() or ch in "-_ ":
            cleaned.append(ch)
    return "".join(cleaned).strip().replace(" ", "-")


def load_entries() -> list[dict]:
    raw = json.loads(LINKS_PATH.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise SystemExit("links.json must be a list")
    seen: dict[str, dict] = {}
    duplicates: list[str] = []
    required = ("url", "title", "category", "blurb", "sources")
    known_cats = {cat for cat, _, _ in OUTLINE}
    known_subs = {(cat, sub) for cat, subs, _ in OUTLINE for sub in subs}
    for item in raw:
        for key in required:
            if not item.get(key):
                raise SystemExit(f"missing {key}: {item.get('url') or item}")
        if not isinstance(item["sources"], list) or not item["sources"]:
            raise SystemExit(f"sources must be a non-empty list: {item['url']}")
        if item["category"] not in known_cats:
            raise SystemExit(f"unknown category {item['category']!r} for {item['url']}")
        sub = item.get("subsection") or ""
        if sub and (item["category"], sub) not in known_subs:
            raise SystemExit(f"unknown subsection {item['category']} / {sub} for {item['url']}")
        if not sub and any(subs for cat, subs, _ in OUTLINE if cat == item["category"]):
            raise SystemExit(f"subsection required for {item['url']}")
        norm = normalize_url(item["url"])
        if not norm:
            raise SystemExit(f"bad url: {item['url']}")
        if norm in seen:
            duplicates.append(norm)
            continue
        entry = dict(item)
        entry["_norm"] = norm
        seen[norm] = entry
    if duplicates:
        raise SystemExit("duplicate normalized URLs:\n" + "\n".join(duplicates))
    return list(seen.values())


def sort_entries(entries: list[dict]) -> list[dict]:
    def key(entry: dict) -> tuple:
        pin = entry.get("pin")
        if isinstance(pin, int):
            return (0, pin, entry["title"].casefold())
        return (1, 0, entry["title"].casefold())

    return sorted(entries, key=key)


def render_readme(entries: list[dict]) -> str:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        by_cat[entry["category"]].append(entry)

    def cat_count(cat: str) -> int:
        return len(by_cat.get(cat, []))

    def sub_count(cat: str, sub: str) -> int:
        return sum(1 for e in by_cat.get(cat, []) if (e.get("subsection") or "") == sub)

    lines: list[str] = []
    lines.append("# Awesome OS LLM")
    lines.append("")
    lines.append("[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append("")
    lines.append(
        "> Open-weight large language models, and the open stack people use to run, train, evaluate, and apply them."
    )
    lines.append("")
    lines.append(
        "An **open-source LLM**, in this list, is a language model whose **weights you can download**, plus the open runtimes, training code, evals, datasets, and apps built to use those weights. It is not \"an LLM that acts as an operating system.\" That topic has its own catalog, [awesome-llm-os](https://github.com/bilalonur/awesome-llm-os)."
    )
    lines.append("")
    lines.append(
        "Open weights are older than the 2023 Llama moment. GPT-2 (2019) shipped weights and sampling code. EleutherAI's GPT-Neo, GPT-J, GPT-NeoX, and Pythia made training runs something other people could study. BigScience BLOOM (2022) and Meta OPT (2022) were large public checkpoints under research-style or use-restricted licenses. Meta's LLaMA paper (February 2023) described a non-commercial research release whose weights then circulated widely; that license was not an OSI open-source license. Llama 2 replaced it with a custom commercial license. Permissive grants (Apache-2.0 or MIT) on strong models — Mistral 7B, much of Qwen, DeepSeek, OLMo, Phi, Gemma 4, gpt-oss, and Meta's later Muse Glimmer — came later, and they are still uneven across families. **Downloadable weights, published training code, published data, and an OSI license are four different claims.** Each bullet says which claim the linked page actually supports."
    )
    lines.append("")
    lines.append(
        f"**{len(entries)} unique links** · Ingested **{INGEST_DATE}** · This compilation is [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (linked projects keep their own licenses)."
    )
    lines.append("")
    lines.append("Deduplicated by normalized URL. Regenerate with `python3 build.py` from [`links.json`](links.json). Counts: [`stats.txt`](stats.txt). What was consulted: [`SOURCES.md`](SOURCES.md). Notes that did not clear the README bar: [`discoveries/`](discoveries/)."
    )
    lines.append("")
    lines.append("### Start here")
    lines.append("")
    lines.append(
        "- [llama.cpp](https://github.com/ggml-org/llama.cpp) — The C/C++ engine most local GGUF setups actually run."
    )
    lines.append(
        "- [Ollama](https://github.com/ollama/ollama) — The shortest path from a laptop to a local OpenAI-compatible server."
    )
    lines.append(
        "- [Hugging Face Hub](https://huggingface.co/models) — Where the weight files live; read the license on the model card, not the org's reputation."
    )
    lines.append(
        "- [OLMo](https://github.com/allenai/OLMo) — Weights, training code, and pretraining data, which is a higher bar than weights alone."
    )
    lines.append(
        "- [Landmark open models](#landmark-open-models) — Families, with the license stated on the page that was checked."
    )
    lines.append(
        "- [gpt-oss](https://github.com/openai/gpt-oss) — OpenAI's Apache-2.0 open-weight models (20B and 120B), if you want a permissive checkpoint from a lab that mostly ships closed models."
    )
    lines.append(
        "- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — The harness behind a large share of open-model numbers."
    )
    lines.append(
        "- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) — The forum where local-model practice shows up before it shows up in papers."
    )
    lines.append("")
    lines.append("## Contents")
    lines.append("")
    for cat, subs, _blurb in OUTLINE:
        lines.append(f"- [{cat}](#{github_slug(cat)}) ({cat_count(cat)})")
        for sub in subs:
            lines.append(f"  - [{sub}](#{github_slug(sub)}) ({sub_count(cat, sub)})")
    lines.append(f"- [Sources](#{github_slug('Sources')})")
    lines.append(f"- [Contributing](#{github_slug('Contributing')})")
    lines.append(f"- [License](#{github_slug('License')})")
    lines.append("")

    for cat, subs, blurb in OUTLINE:
        lines.append(f"## {cat}")
        lines.append("")
        if blurb:
            lines.append(blurb)
            lines.append("")
        grouped: dict[str, list[dict]] = defaultdict(list)
        for entry in by_cat.get(cat, []):
            grouped[entry.get("subsection") or ""].append(entry)
        if subs:
            for sub in subs:
                lines.append(f"### {sub}")
                lines.append("")
                sub_blurb = SUBSECTION_BLURB.get((cat, sub))
                if sub_blurb:
                    lines.append(sub_blurb)
                    lines.append("")
                bucket = sort_entries(grouped.get(sub, []))
                if not bucket:
                    lines.append("_None yet._")
                    lines.append("")
                    continue
                for entry in bucket:
                    lines.append(f"- [{entry['title']}]({entry['url']}) — {entry['blurb']}")
                lines.append("")
        else:
            for entry in sort_entries(grouped.get("", [])):
                lines.append(f"- [{entry['title']}]({entry['url']}) — {entry['blurb']}")
            lines.append("")

    lines.append("## Sources")
    lines.append("")
    lines.append(
        "This list was checked against official model cards, GitHub repos, dataset cards, and a few existing indexes. It is not a bulk merge of those indexes. The map is [`SOURCES.md`](SOURCES.md). The machine-readable dump is [`links.json`](links.json)."
    )
    lines.append("")
    lines.append("## Contributing")
    lines.append("")
    lines.append(
        "Add or edit an object in [`links.json`](links.json), then run `python3 build.py`. One factual sentence, a URL that loads, and a license note when the weights are public but the grant is not Apache-2.0 or MIT. Do not invent star counts, tweet ids, or release dates. Within a subsection, leave `pin` unset to sort alphabetically; set `pin` only to keep a deliberate chronological order. Normalized URLs must be unique."
    )
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append(
        "This compilation is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Model weights, code, datasets, and essays linked from here keep their own licenses and use restrictions."
    )
    lines.append("")
    return "\n".join(lines)


def render_stats(entries: list[dict]) -> str:
    by_cat: dict[str, int] = defaultdict(int)
    by_sub: dict[str, int] = defaultdict(int)
    by_source: dict[str, int] = defaultdict(int)
    for entry in entries:
        by_cat[entry["category"]] += 1
        sub = entry.get("subsection") or "(none)"
        by_sub[f"{entry['category']} / {sub}"] += 1
        for source in entry["sources"]:
            by_source[source] += 1
    lines = [f"unique_links {len(entries)}", "", "by_category"]
    for cat, _subs, _blurb in OUTLINE:
        lines.append(f"{cat} {by_cat[cat]}")
    lines.append("")
    lines.append("by_subsection")
    for cat, subs, _blurb in OUTLINE:
        if subs:
            for sub in subs:
                lines.append(f"{cat} / {sub} {by_sub[f'{cat} / {sub}']}")
        else:
            lines.append(f"{cat} / (none) {by_sub[f'{cat} / (none)']}")
    lines.append("")
    lines.append("by_source_appearance_count")
    lines.append("# a link counted once per source tag on that entry")
    for source, count in sorted(by_source.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"{source} {count}")
    lines.append("")
    lines.append("json_count_matches_unique True")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    entries = load_entries()
    README_PATH.write_text(render_readme(entries), encoding="utf-8")
    STATS_PATH.write_text(render_stats(entries), encoding="utf-8")
    print(f"wrote {README_PATH.name} and {STATS_PATH.name} ({len(entries)} links)")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
