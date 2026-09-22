#!/usr/bin/env python3
"""Regenerate README.md, SOURCES.md, and stats.txt from links.json.

The JSON file is the catalog. This script does not fetch the network.
It dedupes by normalized URL, refuses unknown sections, and rewrites the
README so a hand-edit to the markdown cannot drift from the data.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse, urlunparse

ROOT = Path(__file__).resolve().parent
LINKS_PATH = ROOT / "links.json"
README_PATH = ROOT / "README.md"
SOURCES_PATH = ROOT / "SOURCES.md"
STATS_PATH = ROOT / "stats.txt"

INGEST_DATE = "2026-09-22 PT"

CAT_MODELS = "Landmark open models"
CAT_USE = "Use cases"
CAT_RUNTIME = "Runtimes and local serving"
CAT_TRAIN = "Training, finetune and alignment"
CAT_EVALS = "Evals and papers"
CAT_DOCS = "Docs and essays"
CAT_DATA = "Datasets"
CAT_LISTS = "Awesome lists and indexes"
CAT_COMMUNITY = "Community"

DISPLAY_ORDER = [
    CAT_MODELS,
    CAT_USE,
    CAT_RUNTIME,
    CAT_TRAIN,
    CAT_EVALS,
    CAT_DOCS,
    CAT_DATA,
    CAT_LISTS,
    CAT_COMMUNITY,
]

SUB_ORDER = {
    CAT_MODELS: [
        "Early open weights",
        "Llama",
        "Mistral",
        "Qwen",
        "Gemma",
        "DeepSeek",
        "Fully open model flows",
        "Permissive open weights",
        "Open weights, restricted licenses",
    ],
    CAT_USE: [
        "Agents",
        "Coding",
        "RAG and knowledge",
        "Creative and local chat",
        "On-device apps",
        "Research tools",
    ],
    CAT_RUNTIME: [
        "Inference engines",
        "Local apps and front ends",
        "Edge and in-browser",
    ],
    CAT_TRAIN: [
        "Pretraining stacks",
        "Finetune and alignment",
        "Kernels and efficiency",
    ],
    CAT_EVALS: [
        "Leaderboards",
        "Harnesses",
        "Papers",
    ],
    CAT_DOCS: [],
    CAT_DATA: [
        "Pretraining data",
        "Post-training data",
        "Data tools",
    ],
    CAT_LISTS: [],
    CAT_COMMUNITY: [],
}

BLURBS = {
    CAT_MODELS: "Families whose weights you can download. Apache-2.0 and MIT are called out when that is what the model card says; custom and non-commercial licenses are called out too.",
    CAT_USE: "Applications and libraries that run on open weights. Hosted-only products stay out.",
    CAT_RUNTIME: "Engines and apps that load those weights on your own machine. A polished desktop app is not the same thing as an open-source engine.",
    CAT_TRAIN: "Open code for pretraining, fine-tuning, and preference optimization. Checkpoints without a training stack live under models.",
    CAT_EVALS: "Boards, harnesses, and papers that are actually used to compare open models. Scores on the boards move; the links are the stable part.",
    CAT_DOCS: "Explainers worth reading before you pick a license or a runtime.",
    CAT_DATA: "High-signal corpora and the tools that build them. Most chat fine-tunes are not here.",
    CAT_LISTS: "Related indexes. This list does not try to replace a general LLM bibliography.",
    CAT_COMMUNITY: "Places people actually discuss running open weights.",
}

# Indexes consulted while building the first catalog. Not every row was bulk-imported.
SOURCE_ROWS = [
    (
        "seed-manual",
        "Manual curation",
        "(this repository)",
        "Entries written for this list on 2026-09-22 PT",
    ),
    (
        "hf-api",
        "Hugging Face Hub API",
        "https://huggingface.co/models",
        "Model id, license field, pipeline tag, and createdAt",
    ),
    (
        "eugeneyan/open-llms",
        "eugeneyan/open-llms",
        "https://github.com/eugeneyan/open-llms",
        "Consulted as an open-weight index; links re-checked",
    ),
    (
        "Hannibal046/Awesome-LLM",
        "Hannibal046/Awesome-LLM",
        "https://github.com/Hannibal046/Awesome-LLM",
        "Consulted as a broad LLM index; not bulk-imported",
    ),
    (
        "konishi-timeline",
        "Open-weights release timeline (Hidekazu Konishi)",
        "https://hidekazu-konishi.com/entry/open_weights_llm_release_history_and_timeline.html",
        "Family history. A date is repeated here only when a first-party page or Hub createdAt agreed",
    ),
    (
        "vendor-pages",
        "Vendor pages and GitHub orgs",
        "https://github.com/QwenLM/Qwen3.8",
        "Meta, Mistral, Google DeepMind, DeepSeek, Ai2, Qwen, OpenAI gpt-oss repo",
    ),
    (
        "grok-readme",
        "Grok-1 README",
        "https://github.com/xai-org/grok-1",
        "License sentence quoted from the repo README, not from a secondary recap",
    ),
]


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


def gh_anchor(text: str) -> str:
    chars: list[str] = []
    for ch in text.lower():
        if ch.isalnum() or ch in "-_ ":
            chars.append(ch)
    return "".join(chars).strip().replace(" ", "-")


def load_entries() -> list[dict]:
    raw = json.loads(LINKS_PATH.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        sys.exit("links.json must be a list")
    seen: dict[str, dict] = {}
    for row in raw:
        for key in ("url", "title", "category", "blurb", "sources"):
            if key not in row:
                sys.exit(f"missing {key} on {row.get('url')}")
        url = row["url"].strip()
        norm = normalize_url(url)
        if not norm:
            sys.exit(f"bad url: {url}")
        cat = row["category"]
        sub = row.get("subsection") or ""
        if cat not in SUB_ORDER:
            sys.exit(f"unknown category: {cat}")
        allowed = SUB_ORDER[cat]
        if allowed:
            if sub not in allowed:
                sys.exit(f"unknown subsection {cat!r} / {sub!r} for {url}")
        elif sub:
            sys.exit(f"{cat} does not use subsections: {url}")
        blurb = " ".join(str(row["blurb"]).split())
        if not blurb.endswith("."):
            sys.exit(f"blurb must end with a period: {url}")
        if "—" in blurb or "–" in blurb:
            sys.exit(f"blurb must not contain a dash used as a separator: {url}")
        sources = row["sources"]
        if not isinstance(sources, list) or not sources:
            sys.exit(f"sources must be a non-empty list: {url}")
        pin = row.get("pin")
        if pin is not None and not isinstance(pin, int):
            sys.exit(f"pin must be an int: {url}")
        entry = {
            "url": url,
            "title": str(row["title"]).strip(),
            "category": cat,
            "subsection": sub,
            "blurb": blurb,
            "sources": sources,
            "pin": pin,
        }
        if not entry["title"]:
            sys.exit(f"empty title: {url}")
        if norm in seen:
            sys.exit(f"duplicate normalized URL:\n  {seen[norm]['url']}\n  {url}")
        seen[norm] = entry
    return list(seen.values())


def sort_entries(entries: list[dict]) -> None:
    def key(entry: dict):
        pin = entry["pin"]
        title = entry["title"].casefold()
        if pin is None:
            return (1, 0, title, entry["url"])
        return (0, pin, title, entry["url"])

    entries.sort(key=key)


def intro(n: int) -> list[str]:
    return [
        "# Awesome OS LLM",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        "> Curated open-source and open-weight large language models, plus the stacks people use to run, train, and apply them.",
        "",
        "An **open-source LLM**, in this list, is a language model whose weights you can download and run yourself, together with the open code around that. It is not “an LLM that pretends to be an operating system.” That other topic lives in [awesome-llm-os](https://github.com/bilalonur/awesome-llm-os).",
        "",
        "Two claims get mixed up, and this list keeps them apart:",
        "",
        "- **Open weights** means the parameters are published, so you can self-host, quantize, and fine-tune. The license may still forbid commercial use or add a field-of-use restriction.",
        "- **Open source**, in the [Open Source Initiative’s Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition), means a license that lets you use, study, modify, and share without those restrictions. Apache-2.0 and MIT meet that bar. The Llama Community License, Gemma’s older Terms of Use, and CC BY-NC weights do not, even when the files download.",
        "",
        "Both belong here. The blurb says which is which when it matters. A vendor’s “open source” slogan is not treated as the license.",
        "",
        "The public record is older than the 2023 Llama moment, and this list does not invent a first. OpenAI shipped GPT-2 weights in 2019. EleutherAI’s GPT-Neo, GPT-J, GPT-NeoX, and Pythia, and BigScience BLOOM, kept research releases going before Meta’s LLaMA (February 2023), a gated non-commercial drop that still seeded a large fine-tune ecosystem. Self-hosting for commercial products became practical with Llama 2 (July 2023, custom community license) and Mistral 7B (September 2023, Apache-2.0). Qwen, Gemma, DeepSeek, Phi, OLMo, and later OpenAI’s own gpt-oss weights followed. None of those sentences is a claim that anyone built the first language model.",
        "",
        "Deduplicated by normalized URL (trailing slash, `www.`, query, and fragment stripped).",
        "",
        f"**{n} unique links** · Ingested **{INGEST_DATE}** · License for this compilation: [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (linked projects keep their own licenses).",
        "",
        "### Start here",
        "",
        "- [Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) — What “open source” means for a model, as distinct from downloadable weights.",
        "- [Landmark open models](#landmark-open-models) — Llama, Mistral, Qwen, Gemma, DeepSeek, and the fully open OLMo line.",
        "- [Olmo](https://allenai.org/olmo) — AllenAI’s fully open model flow: weights, data, and code, not weights alone.",
        "- [llama.cpp](https://github.com/ggml-org/llama.cpp) — The usual way to run a GGUF model on a laptop.",
        "- [vLLM](https://github.com/vllm-project/vllm) — The usual way to serve an open model to more than one user.",
        "- [Use cases](#use-cases) — Agents, coding, RAG, local chat, and on-device apps, ahead of the tool pile.",
        "- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — The harness most open-model papers still quote.",
        "",
    ]


def render_contents(by_cat: dict, by_sub: dict) -> list[str]:
    lines = ["## Contents", ""]
    for cat in DISPLAY_ORDER:
        items = by_cat.get(cat, [])
        if not items:
            continue
        lines.append(f"- [{cat}](#{gh_anchor(cat)}) ({len(items)})")
        for sub in SUB_ORDER[cat]:
            sub_items = by_sub[cat].get(sub, [])
            if sub_items:
                lines.append(f"  - [{sub}](#{gh_anchor(sub)}) ({len(sub_items)})")
    lines += [
        "- [Sources](#sources)",
        "- [Contributing](#contributing)",
        "- [License](#license)",
        "",
    ]
    return lines


def render_body(by_cat: dict, by_sub: dict) -> list[str]:
    lines: list[str] = []
    for cat in DISPLAY_ORDER:
        items = by_cat.get(cat, [])
        if not items:
            continue
        lines += [f"## {cat}", "", BLURBS[cat], ""]
        subs = [sub for sub in SUB_ORDER[cat] if by_sub[cat].get(sub)]
        if subs:
            for sub in subs:
                lines += [f"### {sub}", ""]
                for entry in by_sub[cat][sub]:
                    lines.append(f"- [{entry['title']}]({entry['url']}) — {entry['blurb']}")
                lines.append("")
        else:
            for entry in items:
                lines.append(f"- [{entry['title']}]({entry['url']}) — {entry['blurb']}")
            lines.append("")
    return lines


def render_tail() -> list[str]:
    lines = [
        "## Sources",
        "",
        "Indexes consulted for this pass. Entries were not bulk-copied; each README link was checked on its own. Machine-readable rows: [`links.json`](links.json). Counts: [`stats.txt`](stats.txt). Recent-launch notes that did not all earn a README line: [`discoveries/`](discoveries/).",
        "",
    ]
    for _key, name, url, note in SOURCE_ROWS:
        if url.startswith("http"):
            lines.append(f"- [{name}]({url}) — {note}.")
        else:
            lines.append(f"- {name} — {note}.")
    lines += [
        "",
        "## Contributing",
        "",
        "One factual line in the right subsection: `[Name](url) — What it actually is.` Say whether weights are Apache-2.0 or MIT, or a community / research / non-commercial license. Do not invent star counts, release days, benchmark scores, or tweet ids. Prefer a model card or official repo over a roundup. Weak or unverified finds go in [`discoveries/`](discoveries/) instead of the README.",
        "",
        "Add the row to [`links.json`](links.json) (url, title, category, subsection, blurb, sources) and run `python3 build.py`. The script dedupes on the normalized URL and rewrites this file.",
        "",
        "List text is dedicated to the public domain under [CC0 1.0](LICENSE). Linked projects keep their own licenses.",
        "",
        "## License",
        "",
        "This compilation is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Individual projects and linked content retain their own licenses and terms.",
        "",
    ]
    return lines


def write_sources() -> None:
    lines = [
        "# Sources consulted",
        "",
        f"Ingest date: **{INGEST_DATE}** (America/Los_Angeles).",
        "",
        "This first pass is a curated catalog, not a merge of every awesome-list bullet. The indexes below were read. A link appears in the README only after its own URL returned a successful page, and license claims for Hub models were taken from the Hub API license field.",
        "",
        "| Key | Source | URL | How it was used |",
        "| --- | --- | --- | --- |",
    ]
    for key, name, url, note in SOURCE_ROWS:
        lines.append(f"| {key} | {name} | {url} | {note} |")
    lines += [
        "",
        "Normalization: strip the fragment, query, trailing slash, and a leading `www.`; drop a trailing `.git`.",
        "",
        "Not ingested as open-source LLMs: [bilalonur/awesome-llm-os](https://github.com/bilalonur/awesome-llm-os) (LLM-as-operating-system, a different topic). It is listed under awesome lists only so people do not confuse the two.",
        "",
    ]
    SOURCES_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_stats(entries: list[dict], by_cat: dict, by_sub: dict) -> None:
    source_counts: Counter[str] = Counter()
    for entry in entries:
        for source in entry["sources"]:
            source_counts[source] += 1
    lines = [f"unique_links\t{len(entries)}", "", "by_category"]
    for cat in DISPLAY_ORDER:
        lines.append(f"{cat}\t{len(by_cat.get(cat, []))}")
    lines += ["", "by_subsection"]
    for cat in DISPLAY_ORDER:
        if not SUB_ORDER[cat]:
            lines.append(f"{cat} / (none)\t{len(by_cat.get(cat, []))}")
            continue
        for sub in SUB_ORDER[cat]:
            count = len(by_sub[cat].get(sub, []))
            if count:
                lines.append(f"{cat} / {sub}\t{count}")
    lines += ["", "by_source_appearance_count", "# a link counted once per source tag"]
    for source, count in sorted(source_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"{source}\t{count}")
    on_disk = json.loads(LINKS_PATH.read_text(encoding="utf-8"))
    lines += ["", f"json_count_matches_unique\t{len(on_disk) == len(entries)}", ""]
    STATS_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_readme(entries: list[dict]) -> None:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    by_sub: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for entry in entries:
        by_cat[entry["category"]].append(entry)
        by_sub[entry["category"]][entry["subsection"]].append(entry)
    for cat in by_cat:
        sort_entries(by_cat[cat])
        for sub in by_sub[cat]:
            sort_entries(by_sub[cat][sub])
    lines = intro(len(entries))
    lines += render_contents(by_cat, by_sub)
    lines += render_body(by_cat, by_sub)
    lines += render_tail()
    text = "\n".join(lines)
    README_PATH.write_text(text, encoding="utf-8")
    # TOC anchors must exist as headings.
    for line in lines:
        if line.startswith("- [") or line.startswith("  - ["):
            if "](#" not in line:
                continue
            anchor = line.split("](#", 1)[1].split(")", 1)[0]
            if f"#{anchor}" not in text and f"{{#{anchor}}}" not in text:
                # Headings are not explicit anchors; GitHub derives them.
                # Confirm some heading lowercases to this slug.
                headings = [
                    ln[3:] if ln.startswith("### ") else ln[2:]
                    for ln in lines
                    if ln.startswith("## ") or ln.startswith("### ")
                ]
                if anchor not in {gh_anchor(h) for h in headings} and anchor not in {
                    "sources",
                    "contributing",
                    "license",
                }:
                    sys.exit(f"TOC anchor missing: {anchor}")
    write_stats(entries, by_cat, by_sub)


def main() -> None:
    entries = load_entries()
    write_readme(entries)
    write_sources()
    print(f"Wrote {len(entries)} links")


if __name__ == "__main__":
    main()
