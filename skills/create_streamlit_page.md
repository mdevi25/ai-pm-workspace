# Skill: Create Streamlit Page

## Purpose
Use this skill when adding a new PCC page to the multi-page Streamlit application.

## File Location
Create new page files under:

app/pages/

The landing page remains:

app/Home.py

## Naming Convention
Use numeric prefixes to control sidebar order.

Examples:
- 1_Dashboard.py
- 2_Project_Workspace.py
- 3_Skills.py
- 4_Governance.py

## Required File Structure
Each page must include:
- file header comments
- purpose comments
- page title
- short caption
- current state section
- future enhancements section

## Required Inline Documentation
Every page must contain:
- file-level purpose header
- section separators
- comments explaining why each section exists

## Validation
Run locally from project root:

streamlit run app/Home.py

Confirm:
- page appears in sidebar
- page loads without error
- navigation works

## Git Workflow
1. Work on dev branch
2. Commit changes to dev
3. Push dev
4. Merge dev into main only after validation
5. Push main for Streamlit deployment

## Expected Outcome
New page is added consistently, documented clearly, and deployed through the standard PCC workflow.