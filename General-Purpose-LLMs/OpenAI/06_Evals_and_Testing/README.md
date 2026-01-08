# 06_Evals_and_Testing - Personal Evaluation Results

## Purpose
This folder contains **your own testing results, evaluation notes, and quality assessments** of the provider's models and services.

## Content Types

### Test Results
- [ ] Model output samples
- [ ] Performance measurements
- [ ] Quality assessments
- [ ] Comparison tests
- [ ] Edge case explorations

### Testing Protocols
- [ ] Test prompts and datasets
- [ ] Evaluation rubrics
- [ ] Reproducible test scripts
- [ ] Benchmark methodologies

### Observations
- [ ] Failure mode documentation
- [ ] Consistency checks
- [ ] Latency measurements
- [ ] Cost tracking

## Test Report Template
```markdown
# Test Report - [Test Name]

## Date
YYYY-MM-DD

## Objective
[What you're testing and why]

## Models Tested
- Model A: [version/tier]
- Model B: [version/tier] (comparison)

## Test Methodology
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Test Cases
| Case ID | Input | Expected Output | Actual Output | Pass/Fail | Notes |
|---------|-------|-----------------|---------------|-----------|-------|
| TC-01 | [input] | [expected] | [actual] | ✓/✗ | [notes] |

## Quantitative Results
- Metric 1: [value]
- Metric 2: [value]
- Cost: $[amount]
- Latency: [time]

## Qualitative Observations
- Observation 1
- Observation 2

## Failure Modes Discovered
- Failure 1: [description and trigger]
- Failure 2: [description and trigger]

## Comparative Analysis
Compared to [Alternative]:
- Better at: [specific tasks]
- Worse at: [specific tasks]
- Cost difference: [analysis]

## Conclusions
- [Key takeaway 1]
- [Key takeaway 2]

## Reproducibility
- Test script: [filename]
- Dataset: [filename/description]
- Random seed: [if applicable]
```

## File Naming Convention
- `YYYY-MM-DD_Test_[Description].md`
- `YYYY-MM-DD_Eval_[ModelName]_[Task].md`

Examples:
- `2025-12-15_Test_Claude_Code_Generation.md`
- `2025-12-20_Eval_GPT4o_vs_Claude_Reasoning.md`

## Testing Best Practices
- Test multiple times (statistical significance)
- Document exact prompts and parameters
- Track costs for each test run
- Compare against baseline/alternatives
- Note non-reproducible behaviors

---
*Last Updated: 2026-01-08 01:45*
