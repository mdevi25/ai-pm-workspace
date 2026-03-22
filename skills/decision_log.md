#---------------------------------Log 3-------------------
"""
Date: 03-21-2026
File: pages/Decision_Log.py
Project: PCC (Personal Command Center)
Milestone: PCC.M3.S2 - Session State Foundation

OBJECTIVE:
This page captures important architectural and product decisions.
These decisions are stored in session state for now and will later be stored in a database.

WHY DECISION LOG EXISTS:
In AI systems and product development, decisions are important data.
Later we will track:
- Human overrides
- Architecture changes
- Model changes
- Workflow changes
- Risk decisions
- Governance decisions

For now, we log:
- Decision Title
- Decision Description
- Decision Date
"""

import streamlit as st
from core.session_state import init_session

# Initialize session state
init_session()

st.title("Decision Log")

st.write("This page records important project and system decisions.")


# ---------------------------------------------------
# Input Section — Add New Decision
# ---------------------------------------------------
st.subheader("Add New Decision")

decision_title = st.text_input("Decision Title")
decision_description = st.text_area("Decision Description")

if st.button("Add Decision"):
    if decision_title and decision_description:
        decision_entry = {
            "title": decision_title,
            "description": decision_description
        }

        # Store decision in session state list
        st.session_state.decision_log.append(decision_entry)

        st.success("Decision added to log.")
    else:
        st.warning("Please enter both title and description.")


# ---------------------------------------------------
# Display Section — Show Decision Log
# ---------------------------------------------------
st.subheader("Decision History")

if st.session_state.decision_log:
    for i, decision in enumerate(st.session_state.decision_log, start=1):
        st.write(f"### Decision {i}")
        st.write(f"**Title:** {decision['title']}")
        st.write(f"**Description:** {decision['description']}")
else:
    st.info("No decisions logged yet.")



#------------------------------Log 2------------
# Update decision_log.md for this

Because creating a change management process is a **governance decision**, add this entry:

Date: 03-21-2026
Milestone: PCC.M3.S1
Decision: Establish a formal change management process for PCC using dev → main branch workflow, GitHub Desktop for commits, and Streamlit Cloud for deployment.
Reason: PCC is being developed as a structured platform. A standardized change management process ensures stability, traceability, and controlled deployment.
Impact: All future PCC changes will follow a documented process including validation, commit standards, decision logging, and deployment verification.
                                 
#-----------------------------Log 1-----------

Date: 03-21-2026
Milestone: PCC.M3.S1
Decision: Implement Streamlit multi-page structure as the UI foundation.
Reason: PCC will expand into multiple modules (Dashboard, Workspace, Skills, Projects). 
A multi-page architecture allows modular growth without restructuring the app later.