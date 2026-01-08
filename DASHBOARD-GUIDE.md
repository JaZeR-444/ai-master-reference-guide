# AI Models Reference Guide - Dashboard Usage Guide

## Overview

Your AI Research system now includes:
- **10 Template Files** for organizing research across all providers
- **Interactive HTML Dashboard** for browsing and tracking research
- **Automated Python Script** for maintaining the system

## Quick Start

### 1. View the Dashboard

Open `dashboard.html` in your web browser:
```
C:\Users\JaZeR\OneDrive\Desktop\2026 → JaZeR Mainframe\2026 → AI Models Master Reference Guide\AI-Research\dashboard.html
```

The dashboard displays:
- **66 providers** across 8 categories
- **43 completed** research reports
- **Search & filter** capabilities
- **Direct links** to folders and research documents

### 2. Using the Templates

Each provider now has README.md templates in all 10 subfolders:

**00_Inbox** - Drop new materials here temporarily
- URLs, PDFs, screenshots, quick notes
- Sort weekly into appropriate folders

**01_Official_Docs** - Primary source documentation
- API references, user guides, release notes
- Official documentation snapshots

**02_Reference_and_Writeups** - Third-party analysis
- Articles, blog posts, tutorials
- Industry analysis and reviews

**03_Papers_and_Benchmarks** - Academic research
- Research papers, technical reports
- Benchmark results and leaderboards

**04_Pricing_and_Policies** - Economics and terms
- Pricing tiers, rate limits
- Terms of service, policies

**05_Code_and_Examples** - Implementation references
- Code samples, SDK examples
- Integration patterns

**06_Evals_and_Testing** - Personal evaluations
- Test results, quality assessments
- Performance measurements

**07_Assets_and_Media** - Visual assets
- Screenshots, diagrams, videos
- Model outputs and examples

**08_Notes** - Personal synthesis
- Analysis notes, observations
- Ideas and questions

**09_Exports** - Final research outputs
- Completed research reports
- Executive summaries

## Dashboard Features

### Statistics Dashboard
- Total providers tracked
- Completed research count
- In-progress research
- Overall completion rate

### Search & Filter
- **Search Box**: Search by provider name, summary text, or category
- **Category Filter**: Show only specific categories
- **Real-time Results**: Updates as you type

### Provider Cards
Each provider card shows:
- **Status Badge**: ✓ Completed, ⏳ In Progress, ○ Not Started
- **Folder Badges**: 10 numbered badges (00-09) showing which folders have content
- **Research Summary**: Excerpt from completed research
- **Quick Actions**:
  - "Open Folder" - Opens provider directory in File Explorer
  - "View Research" - Opens completed research document

### Theme Toggle
- Click "Toggle Theme" to switch between light and dark modes
- Preference is saved automatically

### Category Organization
- Click any category header to expand/collapse
- Shows provider count and completion progress bar
- Expanded state is remembered

## Maintaining the System

### Adding New Research

When you complete research for a provider:

1. Save the final report to `09_Exports/2026_[ProviderName]_Deep_Research_Analysis.md`

2. Regenerate the dashboard:
```bash
cd "C:\Users\JaZeR\OneDrive\Desktop\2026 → JaZeR Mainframe\2026 → AI Models Master Reference Guide\AI-Research"
python update_ai_research.py --root . --generate-dashboard
```

3. Refresh `dashboard.html` in your browser

### Adding New Providers

When you add a new provider:

1. Create the provider folder in the appropriate category
2. Run the automation script:
```bash
python update_ai_research.py --root . --deploy-templates --generate-dashboard
```

This will:
- Create all 10 subfolders
- Deploy README templates
- Generate research prompt
- Update dashboard data
- Update provider index

### Regular Updates

Run this command weekly to keep everything in sync:
```bash
python update_ai_research.py --root . --generate-dashboard
```

## Research Workflow

### Standard Research Process

1. **Discovery** (00_Inbox)
   - Find interesting articles, docs, or resources
   - Drop everything into 00_Inbox
   - Don't organize yet - just capture

2. **Triage** (Weekly)
   - Review 00_Inbox contents
   - Move items to appropriate folders (01-08)
   - Follow the sorting guidelines in 00_Inbox README

3. **Deep Research** (01-08)
   - Collect official docs in 01_Official_Docs
   - Save articles in 02_Reference_and_Writeups
   - Run tests, save results in 06_Evals_and_Testing
   - Take synthesis notes in 08_Notes

4. **Export** (09_Exports)
   - Use the generated research prompt as a guide
   - Write comprehensive analysis
   - Save as `2026_[ProviderName]_Deep_Research_Analysis.md`
   - Update dashboard

### Template Guidelines

Each README template includes:
- **Purpose** - What belongs in this folder
- **Content Types** - Specific items to save
- **Organization Guidelines** - How to structure content
- **File Naming Conventions** - Consistent naming patterns
- **Best Practices** - Tips and workflows

Follow these templates to maintain consistency across all 66 providers.

## Tips & Tricks

### Efficient Research
- Use 00_Inbox liberally - better to capture than forget
- Set weekly reminder to triage inbox
- Reference other providers for examples
- Cross-link related notes in 08_Notes

### Dashboard Usage
- Bookmark dashboard.html for quick access
- Use search to find providers by capability (e.g., "image generation")
- Filter by category when focusing on specific domains
- Check folder badges to see research coverage gaps

### Quality Control
- Follow the research prompt template in 09_Exports
- Include confidence levels in assessments
- Cite sources from other folders
- Update research when pricing or features change

## File Structure

```
AI-Research/
├── dashboard.html                    # Main dashboard interface
├── dashboard-data.json               # Generated provider data
├── update_ai_research.py             # Automation script
├── templates/                        # Template README files
│   ├── 00_Inbox_README.md
│   ├── 01_Official_Docs_README.md
│   └── ... (10 templates total)
│
├── General-Purpose-LLMs/
│   ├── Anthropic/
│   │   ├── 00_Inbox/
│   │   │   └── README.md            # Template deployed
│   │   ├── 01_Official_Docs/
│   │   │   └── README.md
│   │   └── ... (10 folders total)
│   └── ... (17 providers)
│
└── ... (8 categories total)
```

## Commands Reference

### View Dashboard
Double-click `dashboard.html` or open in browser

### Update Dashboard Data
```bash
python update_ai_research.py --root . --generate-dashboard
```

### Deploy Templates (already done, but can re-run safely)
```bash
python update_ai_research.py --root . --deploy-templates
```

### Full Update (recommended for new providers)
```bash
python update_ai_research.py --root . --deploy-templates --generate-dashboard
```

## Troubleshooting

### Dashboard shows "Error loading dashboard data"
- Ensure `dashboard-data.json` exists in the same folder as `dashboard.html`
- Run: `python update_ai_research.py --root . --generate-dashboard`

### "Open Folder" button doesn't work
- This uses the `file://` protocol
- Some browsers may block local file access
- Try a different browser or manually navigate to the path

### Templates not appearing
- Run: `python update_ai_research.py --root . --deploy-templates`
- Templates only deploy to folders without existing README.md files

### Research not showing as "completed"
- Ensure the research file is in `09_Exports/`
- Filename must contain "Analysis" (e.g., `2026_Anthropic_Deep_Research_Analysis.md`)
- Regenerate dashboard data after adding research

## Next Steps

1. **Explore the Dashboard**
   - Open dashboard.html
   - Try searching and filtering
   - Click through to provider folders

2. **Review the Templates**
   - Open a few README files
   - Familiarize yourself with the structure
   - Use them as guides when organizing research

3. **Start Research**
   - Pick a provider with "not started" status
   - Use the generated research prompt
   - Follow the workflow: Inbox → Organize → Research → Export

4. **Maintain Regularly**
   - Weekly: Triage 00_Inbox folders
   - Monthly: Update dashboard data
   - Quarterly: Review and update existing research

## Support

For issues or questions:
- Check the README templates for folder-specific guidance
- Review RESEARCH-PLAYBOOK.md for methodology
- Examine completed research (e.g., Anthropic) as examples

---

**Last Updated**: 2026-01-08

**System Status**:
- 66 providers tracked
- 43 completed research reports
- 660 template READMEs deployed
- Dashboard fully operational
