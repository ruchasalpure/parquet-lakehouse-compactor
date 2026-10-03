# Parquet Lakehouse Compactor Agent

[![OpenGAP Compliant](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](https://opengap.org)
[![Visa Count](https://img.shields.io/badge/Visas-15%2F15-brightgreen.svg)](https://app.hidevs.xyz)
[![Score](https://img.shields.io/badge/Score-1675%20%2F%201675-success.svg)](https://app.hidevs.xyz)

> Optimizes Apache Iceberg and Delta Lake table footprints through Z-order clustering, bloom filter synthesis, and small-file row-group compaction

## Key Highlights
- **Category**: `data-analytics`
- **Dual-Control Roles**: Maker (`row-group-compactor`) & Checker (`query-speedup-verifier`)
- **Core Skill**: `z-order-clustering-compaction` (Computes Morton space-filling curves across high-cardinality predicate columns to maximize parquet row-group skipping)
- **Compliance**: OpenGAP Standard v0.1.0 with 15 Framework Export Visas

## Multi-Framework Export Visas Supported
This repository exports to all 15 industry-standard agent frameworks:
1. System Prompt (`system_prompt.txt`)
2. Claude Code Subagent (`claude_subagent.json`)
3. OpenAI Assistant (`openai_assistant.json`)
4. CrewAI Agent (`crewai_agent.py`)
5. OpenClaw Module (`openclaw_module.py`)
6. Nanobot Spec (`nanobot.yaml`)
7. Lyzr Agent (`lyzr_agent.py`)
8. GitHub Copilot Workspace (`github_copilot_instructions.md`)
9. Microsoft Copilot Studio (`copilot-instructions.md`)
10. OpenCode Protocol (`opencode_agent.json`)
11. Cursor IDE Rules (`.cursorrules`)
12. Google Gemini CLI (`gemini_system_prompt.txt`)
13. OpenAI Codex Rules (`codex_instructions.md`)
14. AWS Kiro Assistant (`kiro_agent.json`)
15. GitClaw Architecture (`gitclaw_spec.json`)

## Architecture
See [`agent.yaml`](agent.yaml), [`DUTIES.md`](DUTIES.md), and [`EXPLAINABILITY.md`](EXPLAINABILITY.md) for complete structural specifications.
