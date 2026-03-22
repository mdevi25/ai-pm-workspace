# PCC Execution Protocol (Mandatory)

This document defines HOW all Personal Command Center (PCC) tasks must be executed.
All future skills must follow this protocol.

---

## 1. Milestone Structure
All work must follow:

PCC.M# = Milestone
PCC.M#.S# = Step
PCC.M#.S#.1 = Sub-step

Example:
PCC.M3.S1 = Create multi-page Streamlit structure

---

## 2. Every Instruction Must Include

For EVERY step, the following must be specified:

1. Where to run (Cursor / Terminal / GitHub Desktop / Browser / Streamlit)
2. Exact file path
3. Exact file name
4. Exact code to paste
5. Exact command to run
6. What output to expect
7. How to validate success
8. What to do if error happens
9. Do not change syntax 
10. Do not derail the response quality
11. Do not hallucinate
12. Ask question, where not clear
13. Must include inline comments including header in every file
14. Update decision_log
14. Reference changement skills to transition from execution to delivery.

No step should skip these.

---

## 3. Repository Rules

Repo structure must always look like:

ai-pm-workspace/
│
├── app/
├── skills/
├── requirements.txt
├── run_app.py
├── README.md
├── .gitignore
└── .env.example

Rules:
- `.env` must NEVER be committed
- `.env.example` must be committed
- All new features must be built on `dev` branch
- Only stable features go to `main`
- `main` = production
- `dev` = development

---

## 4. Branch Strategy

We follow this workflow:

1. Work in `dev`
2. Commit to `dev`
3. Push `dev`
4. Test locally
5. Test Streamlit Cloud (if UI change)
6. Merge `dev` → `main`
7. Push `main`
8. Streamlit auto-deploys

---

## 5. Commit Message Standard

Format:

Summary:
PCC.M#.S# - Short title

Description:
- What was added
- What was changed
- What was fixed
- What milestone this supports

---

## 6. Definition of Done (DoD)

A step is COMPLETE only if:

- Runs locally
- Runs on Streamlit Cloud
- Code pushed to GitHub
- Documented in README
- Skill updated (if reusable)

---

## 7. Skill Creation Rule

Whenever a repeatable process is created, a new skill must be created in:

skills/

Skill must include:
- Purpose
- When to use
- Steps
- Commands
- Validation
- Common errors

---

## 8. Folder Naming Standard

Use numbering:

01_Projects.py
02_Learning.py
03_AI_Tools.py
04_Resume.py
05_Weekly_Plan.py

This keeps Streamlit sidebar in order.

---

## 9. Never Do These

- Never commit `.env`
- Never work directly on `main`
- Never push broken code to `main`
- Never skip validation
- Never skip README update

---

## 10. PCC Architecture Layers

Layer 1 — Repo + Streamlit Base
Layer 2 — Pages
Layer 3 — Skills
Layer 4 — Database
Layer 5 — n8n Automation
Layer 6 — AI Agents
Layer 7 — Dashboard / Analytics
Layer 8 — Deployment / Domain
Layer 9 — Authentication
Layer 10 — Portfolio Mode

We build layer by layer only.

---

# This is the Master Execution Rulebook for PCC.

---

## 11. Human-in-the-Loop (HITL) Control Layer

PCC is a Human + AI system, not a fully automated system.
The human (owner) must review and approve before major actions.

### HITL Required Before:
- Merging dev → main
- Deploying to Streamlit Cloud
- Changing architecture
- Adding new tools (n8n, DB, APIs, Agents)
- Running automations
- Publishing portfolio content
- Sharing externally
- Deleting or restructuring folders
- Changing environment variables
- Adding cost-incurring services

### HITL Checkpoints

At the end of each milestone:

| Milestone | Human Action Required |
|----------|----------------------|
| PCC.M1 | Approve base structure |
| PCC.M2 | Approve repo & branching |
| PCC.M3 | Approve UI structure |
| PCC.M4 | Approve database |
| PCC.M5 | Approve automation |
| PCC.M6 | Approve AI agents |
| PCC.M7 | Approve dashboard |
| PCC.M8 | Approve deployment |
| PCC.M9 | Approve authentication |
| PCC.M10 | Approve portfolio mode |

Human must explicitly confirm:
"Approved — proceed to next milestone"

---

## 12. Decision Logging (Human Decisions Must Be Recorded)

Create a file:

decision_log.md

This file records important human decisions.

Format:

Date:
Milestone:
Decision:
Options Considered:
Final Decision:
Reason:
Impact:
Next Step:

This becomes your PM documentation and portfolio artifact.

---

## 13. Override Rule

If AI suggests something but human disagrees:

Human decision overrides AI.

But log it in:
decision_log.md

This creates:
Human Override Dataset → Future AI training → Governance artifact.

---

## 14. PCC Operating Model

PCC is built on this model:

AI does:
- Suggest
- Generate
- Automate
- Draft
- Analyze

Human does:
- Decide
- Approve
- Prioritize
- Architect
- Govern
- Publish

This is Human-in-the-Loop Product Management.

---

