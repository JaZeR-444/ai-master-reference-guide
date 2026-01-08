import argparse
from datetime import datetime
from pathlib import Path
import re
import sys

SUBFOLDERS = [
    "00_Inbox",
    "01_Official_Docs",
    "02_Reference_and_Writeups",
    "03_Papers_and_Benchmarks",
    "04_Pricing_and_Policies",
    "05_Code_and_Examples",
    "06_Evals_and_Testing",
    "07_Assets_and_Media",
    "08_Notes",
    "09_Exports",
]

CATEGORY_TITLE_MAP = {
    "General-Purpose-LLMs": "General-Purpose LLMs",
    "Image-Generation": "Image Generation",
    "Video-Generation": "Video Generation",
    "Music-Generation": "Music Generation",
    "Voice-and-Speech": "Voice / Speech (TTS & Cloning)",
    "3D-and-World-Generation": "3D / World / Asset Generation",
    "Model-Hosting-and-Inference": "Model Hosting / Inference Platforms",
    "Creative-and-Productivity-Apps": "Creative / Productivity Apps with AI",
}

PROMPT_TEMPLATE = """# 2026 <ProviderName> Deep Research Prompt

You are a senior AI research analyst conducting a **foundational, source-driven deep research review** of <ProviderName>.

This research is for **a single, technically capable user** who uses AI tools to:
- accelerate learning and research
- build applications, scripts, and workflows
- create useful or creative software products
- explore opportunities for a future AI-powered services or product business

This analysis is **private, internal, and unsanitized**.
Assume the reader is technically literate, skeptical, and optimizing for personal leverage-not vendor marketing alignment.

Avoid hype and marketing language.

---

## RESEARCH OBJECTIVES

Produce a comprehensive, evidence-based analysis that helps determine:

- What <ProviderName> actually offers today (not aspirationally)
- Where it is genuinely strong, weak, and differentiated
- How it compares to its closest alternatives for a solo builder
- What risks, limitations, or hidden costs exist
- Whether it is worth investing **time, learning effort, and dependency** into

---

## REQUIRED SECTIONS (DO NOT SKIP)

### 1. Provider Overview & Positioning
- What problem(s) <ProviderName> is solving
- Who it is primarily built for (developers, enterprises, creatives, consumers)
- Core value proposition in plain language
- Where it sits in the broader AI ecosystem

---

### 2. Model Catalog (Complete Inventory)  **(NEW - REQUIRED)**
Produce a **complete, current list** of all models offered by <ProviderName> that are accessible via:
- API(s)
- first-party apps/products
- enterprise offerings (if distinct)

For each model, include a table with the following columns:
- Model Name (exact)
- Family / Tier (if applicable)
- Primary Modality (text/image/video/audio/multimodal/3D/etc.)
- Intended Use (as <ProviderName> positions it; paraphrase precisely and cite source)
- Key Strengths (1-3 bullets)
- Key Constraints / Known Weaknesses (1-3 bullets)
- Availability (API/app/enterprise; public vs gated; regions if relevant)
- Status (GA/Beta/Preview/Deprecated)
- Release / Last Update (if known)
- Sources (official preferred)

Rules:
- Do not guess model names.
- If the catalog is incomplete due to limited public info, state exactly what is missing and why.
- Clearly separate "current" models from "deprecated/legacy" models.

---

### 3. Core Capabilities & Modalities
- Supported modalities (text, image, video, audio, multimodal, etc.)
- Key features and technical capabilities
- How capabilities map to the models listed in the Model Catalog
- Known strengths and known gaps relevant to building and experimentation

---

### 4. Technical Architecture (High-Level)
- Publicly known or reasonably inferred architecture details
- Training approach (if disclosed)
- Inference characteristics (latency, throughput, scaling assumptions)
- Deployment model (API, hosted app, local, hybrid)

Explicitly label what is **known**, **inferred**, or **unknown**.

---

### 5. Performance, Quality, and Benchmarks
- Available benchmark results (with sources), ideally tied to specific models from the catalog
- Real-world performance observations from credible users
- Consistency, reliability, and failure modes
- Where benchmarks do or do not reflect real usage

Avoid single-number conclusions; focus on context and variance.

---

### 6. Pricing, Limits, and Economic Model
- Pricing structure and tiers, tied to specific models where applicable
- Rate limits, quotas, or usage constraints
- Cost predictability for experimentation and small-scale production
- Cost-efficiency relative to comparable alternatives

---

### 7. Safety, Policy, and Governance
- Content policies and enforcement mechanisms
- Safety systems (if disclosed)
- Constraints that materially affect experimentation or product building
- Known incidents, controversies, or regulatory exposure

---

### 8. Adoption, Ecosystem, and Real-World Usage
- Evidence of real-world adoption (especially by developers or small teams)
- Signals of production vs experimental usage
- Notable case studies or public deployments
- Gaps between claimed and observed adoption

---

### 9. Competitive Landscape
- Closest competitors (name them)
- Model-by-model comparison where appropriate (anchored to the Model Catalog)
- Clear advantages vs alternatives
- Clear disadvantages vs alternatives
- Scenarios where <ProviderName> is a poor choice for a solo builder

Be direct and critical.

---

### 10. Operational Risks, Unknowns, and Watch Areas
- Technical or platform risks
- Operational friction (outages, breaking changes, churn)
- Lock-in or migration concerns
- Unknowns that could materially impact long-term usefulness

---

### 11. Strategic Assessment (Personal Leverage Focused)
Provide a concise synthesis addressing:

- When <ProviderName> is worth investing learning time into
- When it is not worth the cognitive or dependency cost
- Best-fit use cases for solo projects, tools, or client work
- Near-term viability (0-12 months)
- Medium-term outlook (12-24 months)

Provide an overall confidence level (Low / Medium / High) and explicitly state:
- What evidence would increase this confidence
- What evidence would reduce it

---

## SOURCE REQUIREMENTS
- Prefer primary sources (official docs, model lists, pricing pages, release notes)
- Use credible third-party analysis where necessary
- Clearly distinguish fact from inference
- Cite sources inline or as a reference list

---

## OUTPUT FORMAT
- Clear section headers
- Concise but thorough
- No marketing copy
- No speculative hype
- Favor clarity over verbosity
"""


def normalize_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def title_for_category(category_name: str) -> str:
    return CATEGORY_TITLE_MAP.get(category_name, category_name.replace("-", " "))


def load_provider_index(index_path: Path):
    if not index_path.exists():
        return "", [], {}

    text = index_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    section_order = []
    sections = {}
    display_map = {}
    current = None

    for line in lines:
        if line.startswith("## "):
            current = line[3:].strip()
            section_order.append(current)
            sections.setdefault(current, [])
            continue
        if current and line.startswith("- "):
            name = line[2:].strip()
            sections[current].append(name)
            display_map[normalize_key(name)] = name

    return text, section_order, {"sections": sections, "display_map": display_map}


def write_provider_index(index_path: Path, root: Path, changed: bool):
    original_text, section_order, parsed = load_provider_index(index_path)
    sections = parsed.get("sections", {})
    display_map = parsed.get("display_map", {})

    category_dirs = [d for d in root.iterdir() if d.is_dir()]

    for category in category_dirs:
        section_title = title_for_category(category.name)
        if section_title not in sections:
            sections[section_title] = []
            section_order.append(section_title)

        existing = {normalize_key(n): n for n in sections[section_title]}

        providers = [p for p in category.iterdir() if p.is_dir()]
        new_names = []
        for provider in providers:
            key = normalize_key(provider.name)
            if key in existing:
                continue
            display_name = display_map.get(key, provider.name.replace("-", " "))
            new_names.append(display_name)

        if new_names:
            sections[section_title].extend(sorted(new_names, key=lambda s: s.lower()))

    new_lines = ["# Provider Index", ""]
    for section in section_order:
        new_lines.append(f"## {section}")
        for name in sections.get(section, []):
            new_lines.append(f"- {name}")
        new_lines.append("")

    new_text = "\n".join(new_lines).rstrip() + "\n"

    if new_text != original_text:
        index_path.write_text(new_text, encoding="utf-8")
        return True

    return False


def update_readme(readme_path: Path):
    if not readme_path.exists():
        return False

    text = readme_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    updated = False

    status_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## Status":
            status_idx = i
            break

    if status_idx is None:
        return False

    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    last_line = f"Last updated: {ts}"

    last_idx = None
    for i in range(status_idx + 1, len(lines)):
        if lines[i].startswith("## "):
            break
        if lines[i].startswith("Last updated:"):
            last_idx = i
            break

    if last_idx is not None:
        if lines[last_idx] != last_line:
            lines[last_idx] = last_line
            updated = True
    else:
        insert_at = status_idx + 1
        while insert_at < len(lines) and lines[insert_at].strip() == "":
            insert_at += 1
        if insert_at < len(lines):
            insert_at += 1
        lines.insert(insert_at, last_line)
        updated = True

    if updated:
        readme_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    return updated


def scan_folder_contents(provider_path: Path) -> dict:
    """
    Scan all 10 subfolders and return file counts.
    Exclude README.md templates from counts.
    """
    contents = {}
    for subfolder in SUBFOLDERS:
        folder_path = provider_path / subfolder
        if folder_path.exists():
            files = [f for f in folder_path.iterdir()
                    if f.is_file() and f.name != "README.md"]
            contents[subfolder] = {
                "file_count": len(files),
                "has_content": len(files) > 0
            }
        else:
            contents[subfolder] = {"file_count": 0, "has_content": False}
    return contents


def extract_research_summary(export_file: Path) -> dict:
    """
    Extract executive summary and key metadata from research markdown.
    Returns dict with: executive_summary, strategic_assessment, confidence
    """
    if not export_file.exists():
        return {}

    try:
        text = export_file.read_text(encoding="utf-8")
    except Exception:
        return {}

    # Extract executive summary (first paragraph after "## 1. Provider Overview")
    summary_match = re.search(
        r"## 1\. Provider Overview & Positioning\n\n(.*?)(?=\n##|\n---|\Z)",
        text,
        re.DOTALL
    )
    executive_summary = ""
    if summary_match:
        summary_text = summary_match.group(1).strip()
        # Take first 300 characters
        executive_summary = summary_text[:300] + "..." if len(summary_text) > 300 else summary_text

    # Extract strategic assessment
    verdict_match = re.search(
        r"##\s*11\..*Strategic Assessment.*?\n.*?(?:Verdict|Recommendation)[:\s]*\*\*([^*]+)\*\*",
        text,
        re.DOTALL | re.IGNORECASE
    )
    strategic_assessment = verdict_match.group(1).strip() if verdict_match else "Unknown"

    # Extract confidence
    confidence_match = re.search(r"Confidence(?:\s+Score)?[:\s]*\*?\*?([^*\n]+)", text, re.IGNORECASE)
    confidence = confidence_match.group(1).strip() if confidence_match else "Unknown"

    return {
        "executive_summary": executive_summary,
        "strategic_assessment": strategic_assessment,
        "confidence": confidence
    }


def determine_provider_status(contents: dict, exports_path: Path) -> str:
    """
    Determine if provider is: completed, in_progress, or not_started
    """
    has_exports = contents.get("09_Exports", {}).get("has_content", False)
    has_any_content = any(v.get("has_content", False) for k, v in contents.items() if k != "09_Exports")

    if has_exports:
        return "completed"
    elif has_any_content:
        return "in_progress"
    else:
        return "not_started"


def generate_dashboard_data(root: Path, output_path: Path):
    """
    Scan entire directory structure and generate dashboard-data.json
    """
    import json

    data = {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "total_providers": 0,
            "completed_count": 0,
            "in_progress_count": 0,
            "not_started_count": 0
        },
        "categories": []
    }

    category_dirs = [d for d in root.iterdir() if d.is_dir() and not d.name.startswith('.') and d.name != "templates"]

    for category in sorted(category_dirs, key=lambda x: x.name):
        category_data = {
            "name": category.name,
            "display_name": title_for_category(category.name),
            "provider_count": 0,
            "completed_count": 0,
            "providers": []
        }

        provider_dirs = [p for p in category.iterdir() if p.is_dir()]
        category_data["provider_count"] = len(provider_dirs)

        for provider in sorted(provider_dirs, key=lambda x: x.name):
            contents = scan_folder_contents(provider)
            status = determine_provider_status(contents, provider / "09_Exports")

            provider_data = {
                "name": provider.name,
                "folder_path": f"{category.name}/{provider.name}",
                "absolute_path": str(provider.resolve()),
                "status": status,
                "folder_contents": contents,
                "research_files": [],
                "last_updated": None
            }

            # Extract research file details if completed
            exports_path = provider / "09_Exports"
            if status == "completed" and exports_path.exists():
                research_files = [f for f in exports_path.iterdir()
                                 if f.is_file() and f.suffix == ".md" and "Analysis" in f.name]

                for research_file in research_files:
                    summary_data = extract_research_summary(research_file)
                    provider_data["research_files"].append({
                        "filename": research_file.name,
                        "path": f"09_Exports/{research_file.name}",
                        "last_modified": datetime.fromtimestamp(
                            research_file.stat().st_mtime
                        ).isoformat(),
                        **summary_data
                    })

                if provider_data["research_files"]:
                    provider_data["last_updated"] = provider_data["research_files"][0]["last_modified"]

            category_data["providers"].append(provider_data)

            # Update counts
            data["metadata"]["total_providers"] += 1
            if status == "completed":
                data["metadata"]["completed_count"] += 1
                category_data["completed_count"] += 1
            elif status == "in_progress":
                data["metadata"]["in_progress_count"] += 1
            else:
                data["metadata"]["not_started_count"] += 1

        data["categories"].append(category_data)

    # Write JSON file
    output_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print("Dashboard data generated: dashboard-data.json")
    print(f"  Total providers: {data['metadata']['total_providers']}")
    print(f"  Completed: {data['metadata']['completed_count']}")
    print(f"  In progress: {data['metadata']['in_progress_count']}")
    print(f"  Not started: {data['metadata']['not_started_count']}")

    return data


def deploy_templates(root: Path, templates_dir: Path):
    """
    Deploy README.md templates to all provider subfolders.
    Only deploys if README.md doesn't exist (non-destructive).
    """
    deployed_count = 0

    template_files = {
        "00_Inbox": templates_dir / "00_Inbox_README.md",
        "01_Official_Docs": templates_dir / "01_Official_Docs_README.md",
        "02_Reference_and_Writeups": templates_dir / "02_Reference_and_Writeups_README.md",
        "03_Papers_and_Benchmarks": templates_dir / "03_Papers_and_Benchmarks_README.md",
        "04_Pricing_and_Policies": templates_dir / "04_Pricing_and_Policies_README.md",
        "05_Code_and_Examples": templates_dir / "05_Code_and_Examples_README.md",
        "06_Evals_and_Testing": templates_dir / "06_Evals_and_Testing_README.md",
        "07_Assets_and_Media": templates_dir / "07_Assets_and_Media_README.md",
        "08_Notes": templates_dir / "08_Notes_README.md",
        "09_Exports": templates_dir / "09_Exports_README.md",
    }

    category_dirs = [d for d in root.iterdir() if d.is_dir() and not d.name.startswith('.') and d.name != "templates"]

    for category in category_dirs:
        provider_dirs = [p for p in category.iterdir() if p.is_dir()]
        for provider in provider_dirs:
            for subfolder, template_file in template_files.items():
                target_folder = provider / subfolder
                target_readme = target_folder / "README.md"

                if target_folder.exists() and not target_readme.exists():
                    if template_file.exists():
                        # Copy template with timestamp
                        content = template_file.read_text(encoding="utf-8")
                        content = content.replace(
                            "[Auto-generated timestamp]",
                            datetime.now().strftime("%Y-%m-%d %H:%M")
                        )
                        target_readme.write_text(content, encoding="utf-8")
                        deployed_count += 1

    print(f"Templates deployed: {deployed_count} README files")
    return deployed_count


def main():
    parser = argparse.ArgumentParser(description="Sync AI-Research provider scaffolding.")
    parser.add_argument("--root", default=".", help="Root AI-Research directory.")
    parser.add_argument("--generate-dashboard", action="store_true",
                       help="Generate dashboard-data.json")
    parser.add_argument("--deploy-templates", action="store_true",
                       help="Deploy README templates to all providers")
    parser.add_argument("--templates-dir", default="./templates",
                       help="Directory containing template files")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"Root not found: {root}", file=sys.stderr)
        return 1

    created_folders = []
    created_prompts = []

    category_dirs = [d for d in root.iterdir() if d.is_dir()]

    index_path = root / "PROVIDER-INDEX.md"
    readme_path = root / "README.md"

    _, _, parsed = load_provider_index(index_path)
    display_map = parsed.get("display_map", {})

    for category in category_dirs:
        provider_dirs = [p for p in category.iterdir() if p.is_dir()]
        for provider in provider_dirs:
            for subfolder in SUBFOLDERS:
                target = provider / subfolder
                if not target.exists():
                    target.mkdir(parents=True, exist_ok=True)
                    created_folders.append(target)

            prompt_name = f"2026_{provider.name}_Deep_Research_Prompt.md"
            prompt_path = provider / prompt_name
            if not prompt_path.exists():
                display_name = display_map.get(
                    normalize_key(provider.name), provider.name.replace("-", " ")
                )
                content = PROMPT_TEMPLATE.replace("<ProviderName>", display_name)
                prompt_path.write_text(content, encoding="utf-8")
                created_prompts.append(prompt_path)

    index_updated = write_provider_index(index_path, root, changed=bool(created_folders or created_prompts))
    readme_updated = False
    if created_folders or created_prompts or index_updated:
        readme_updated = update_readme(readme_path)

    print("Created folders:", len(created_folders))
    print("Created prompts:", len(created_prompts))
    print("Provider index updated:", "yes" if index_updated else "no")
    print("README updated:", "yes" if readme_updated else "no")

    # New dashboard generation
    if args.generate_dashboard:
        output_path = root / "dashboard-data.json"
        generate_dashboard_data(root, output_path)

    # New template deployment
    if args.deploy_templates:
        templates_dir = Path(args.templates_dir).resolve()
        if not templates_dir.exists():
            print(f"Templates directory not found: {templates_dir}", file=sys.stderr)
            return 1
        deploy_templates(root, templates_dir)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
