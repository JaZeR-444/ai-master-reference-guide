# AI Models Master Reference Guide

A comprehensive research tracking system for 66+ AI providers across 8 major categories. This system includes standardized templates, automated indexing, and an interactive dashboard for organizing and tracking AI model research.

![Dashboard Preview](logo.svg)

## Features

### 📊 Interactive Dashboard
- Real-time search and filtering across all providers
- Status tracking (Completed, In Progress, Not Started)
- Category organization with progress bars
- Direct links to folders and research documents
- Dark/light theme toggle
- Responsive design for all devices

### 📁 Organized Research Structure
10 standardized subfolders for each provider:
- **00_Inbox** - Temporary holding area for new materials
- **01_Official_Docs** - Primary source documentation
- **02_Reference_and_Writeups** - Third-party articles and analysis
- **03_Papers_and_Benchmarks** - Academic research and benchmarks
- **04_Pricing_and_Policies** - Cost structures and terms
- **05_Code_and_Examples** - Code samples and implementations
- **06_Evals_and_Testing** - Personal evaluation results
- **07_Assets_and_Media** - Visual assets and media
- **08_Notes** - Personal synthesis and analysis
- **09_Exports** - Final research outputs

### 🤖 Automated Management
- Python script for scaffolding new providers
- Automatic dashboard data generation
- Template deployment to all providers
- Provider index maintenance

## Categories

- **General-Purpose LLMs** (17 providers)
- **Image Generation** (11 providers)
- **Video Generation** (8 providers)
- **Music Generation** (7 providers)
- **Voice & Speech** (7 providers)
- **3D & World Generation** (4 providers)
- **Model Hosting & Inference** (7 providers)
- **Creative & Productivity Apps** (5 providers)

## Quick Start

### 1. View the Dashboard

Start a local web server:
```bash
python -m http.server 8000
```

Then open: http://localhost:8000/dashboard.html

### 2. Add New Providers

```bash
# Create provider folder in appropriate category
mkdir "Category-Name/New-Provider"

# Run automation script
python update_ai_research.py --root . --deploy-templates --generate-dashboard
```

### 3. Conduct Research

Follow the workflow:
1. **Discover** - Add materials to 00_Inbox
2. **Organize** - Sort into appropriate folders (01-08)
3. **Research** - Use templates as guides
4. **Export** - Write final analysis in 09_Exports
5. **Update** - Regenerate dashboard data

## Commands

### Update Dashboard
```bash
python update_ai_research.py --root . --generate-dashboard
```

### Deploy Templates
```bash
python update_ai_research.py --root . --deploy-templates
```

### Full Update
```bash
python update_ai_research.py --root . --deploy-templates --generate-dashboard
```

## Current Status

- **66 Total Providers** across 8 categories
- **43 Completed** research reports
- **660 Template READMEs** deployed
- **Interactive Dashboard** fully operational

## File Structure

```
AI-Research/
├── dashboard.html              # Main dashboard interface
├── dashboard-data.json         # Generated provider data
├── logo.svg                    # Logo graphic
├── favicon.svg                 # Browser favicon
├── update_ai_research.py       # Automation script
├── templates/                  # Template README files
│   ├── 00_Inbox_README.md
│   ├── 01_Official_Docs_README.md
│   └── ... (10 templates)
│
├── General-Purpose-LLMs/
│   ├── Anthropic/
│   ├── OpenAI/
│   └── ... (17 providers)
│
├── Image-Generation/
│   ├── Midjourney/
│   ├── Stability-AI/
│   └── ... (11 providers)
│
└── ... (8 categories total)
```

## Documentation

- **DASHBOARD-GUIDE.md** - Comprehensive usage guide
- **RESEARCH-PLAYBOOK.md** - Research methodology
- **PROVIDER-INDEX.md** - Complete provider list

## Research Workflow

1. **Capture** everything in 00_Inbox
2. **Triage** weekly - move to appropriate folders
3. **Collect** official docs, articles, benchmarks
4. **Test** and document results
5. **Synthesize** insights in 08_Notes
6. **Export** final analysis following research prompt template

## Technologies

- **Frontend**: Pure HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python 3.x
- **Storage**: Local filesystem with JSON data
- **Version Control**: Git

## Requirements

- Python 3.x
- Modern web browser
- Git (for version control)

## License

Personal research project - all rights reserved.

## Credits

Built with Claude Code (Anthropic Claude Sonnet 4.5)
- Template system design
- Interactive dashboard development
- Automation scripting
- Logo and favicon design

---

**Last Updated**: January 8, 2026

**Maintained by**: JaZeR
