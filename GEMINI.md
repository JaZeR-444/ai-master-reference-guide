# Project Context: AI Research Library

## Overview
This repository serves as a **Master Reference Guide** for AI models, platforms, and creative tools. It is a structured research archive designed to track the rapidly evolving AI landscape for a solo builder or researcher.

The project is a hybrid of a **static knowledge base** and a **Python-automated workflow** that enforces consistency across research artifacts.

## Directory Structure
The repository is organized hierarchically:

1.  **Category (Top-Level):** Folders representing AI capabilities (e.g., `General-Purpose-LLMs`, `Image-Generation`, `3D-and-World-Generation`).
2.  **Provider (Mid-Level):** Specific companies or tools (e.g., `OpenAI`, `Midjourney`, `Runway`). **Each provider appears exactly once.**
3.  **Artifacts (Leaf-Level):** A standardized set of subfolders for every provider:
    *   `00_Inbox`: Raw materials and unsorted finds.
    *   `01_Official_Docs`: Manuals, API references.
    *   `02_Reference_and_Writeups`: Articles, blog posts.
    *   `03_Papers_and_Benchmarks`: Academic papers, technical reports.
    *   `04_Pricing_and_Policies`: Cost and usage terms.
    *   `05_Code_and_Examples`: Snippets, SDKs.
    *   `06_Evals_and_Testing`: Personal tests and results.
    *   `07_Assets_and_Media`: Images, videos, outputs.
    *   `08_Notes`: Synthesis and personal thoughts.
    *   `09_Exports`: Final summaries or reports.

## Key Files

*   **`update_ai_research.py`**: The core automation script. It scans the directory tree and:
    *   Creates missing subfolders (scaffolding) for any new provider folders.
    *   Generates a standardized `2026_<Provider>_Deep_Research_Prompt.md` file.
    *   Updates `PROVIDER-INDEX.md` with new entries.
    *   Updates the timestamp in `README.md`.
*   **`RESEARCH-PLAYBOOK.md`**: The standard operating procedure for conducting research, detailing the "Intake Flow" and "Evaluation Dimensions".
*   **`PROVIDER-INDEX.md`**: A manually or automatically curated list of all tracked providers, categorized by domain.
*   **`README.md`**: High-level project status and rules.

## Workflows

### Adding a New Provider
1.  Navigate to the appropriate **Category** folder (e.g., `Image-Generation`).
2.  Create a new folder with the **Provider Name** (e.g., `Flux`).
3.  Run the automation script:
    ```bash
    python update_ai_research.py
    ```
4.  The script will automatically populate the subfolders and generate the research prompt file.

### Conducting Research
Refer to `RESEARCH-PLAYBOOK.md` for the detailed methodology. The general flow is:
1.  **Intake:** Dump links/PDFs into `00_Inbox`.
2.  **Sort:** Move files to specific artifact folders.
3.  **Analyze:** Use the generated `..._Deep_Research_Prompt.md` to guide LLM analysis or personal deep dives.
4.  **Synthesize:** Write conclusions in `08_Notes`.
