# ============================================================
# Skill: Change Management
# File: skills/change_management.md
# Purpose: Standardize how changes are made, documented,
# committed, merged, and deployed in the PCC platform.
# ============================================================

## Purpose

This skill defines the standard process for managing changes in PCC.

This ensures:
- Changes are documented
- Changes are traceable
- Changes are tested before deployment
- The dev and main branches remain controlled
- The decision log is updated when needed
- Deployment to Streamlit remains stable

This is the PCC Change Management Process.

---

## When To Use This Skill

Use this skill when:
- Adding a new feature
- Modifying an existing feature
- Changing file structure
- Adding a new page
- Adding a new skill
- Updating governance documents
- Fixing a bug
- Renaming files
- Changing deployment configuration

Do NOT skip this process.

---

## Tools Used

| Task | Tool |
|------|------|
| Code editing | Cursor |
| Version control | Git |
| Commit & merge | GitHub Desktop (default) |
| Repository | GitHub |
| Deployment | Streamlit Cloud |
| Documentation | Markdown files |

GitHub Desktop is the default tool for commit, merge, and push.

---

## Branch Strategy

| Branch | Purpose |
|--------|--------|
| dev | Development work |
| main | Production / Streamlit deployment |

### Rule
All changes must be committed to **dev first**, then merged into **main**.

```text
Work → dev → test → merge → main → deploy