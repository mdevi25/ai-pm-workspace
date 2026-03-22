"""
File: main.py
Project: PCC (Personal Command Center)
Milestone: PCC.M3.S2 - Session State Foundation

OBJECTIVE:
This file acts as the application initializer (system boot layer).
It is NOT a user-facing page. It prepares the app environment before any page loads.

WHAT THIS FILE DOES:
1. Sets Streamlit page configuration (title, layout).
2. Initializes session state variables for the entire app.
3. Confirms system initialization.
4. Displays session debug info (temporary for development).

WHEN THIS FILE RUNS:
This file runs FIRST when the command below is executed:
    streamlit run main.py

DEPENDENCIES:
- core/session_state.py → provides session initialization logic

PAGES THAT DEPEND ON THIS:
- pages/Home.py
- pages/Dashboard.py
- pages/Project_Workspace.py
- pages/Decision_Log.py
- pages/Settings.py

NOTE:
Do NOT put page-specific UI here.
All UI pages must live inside /pages folder.
"""

import streamlit as st  # Streamlit framework
from core.session_state import init_session  # Import session initialization function


# ---------------------------------------------------
# STEP 1 — Configure Streamlit Page
# This must be one of the first Streamlit commands.
# It controls browser tab name and layout.
# ---------------------------------------------------
st.set_page_config(
    page_title="PCC - Personal Command Center",
    layout="wide"
)


# ---------------------------------------------------
# STEP 2 — Initialize Session State
# This prepares memory variables used across all pages.
# Without this, pages may crash due to missing variables.
# ---------------------------------------------------
init_session()


# ---------------------------------------------------
# STEP 3 — System Initialization Message
# This tells the user the system is ready.
# Navigation should be done using the sidebar.
# ---------------------------------------------------
st.title("PCC System Initialization")
st.success("System initialized successfully.")
st.info("Use the sidebar to navigate to Home, Dashboard, or Project Workspace.")


# ---------------------------------------------------
# STEP 4 — Debug Section (Development Only)
# Shows current session state so we can verify memory is working.
# This can be removed in later milestones.
# ---------------------------------------------------
st.subheader("Session State (Debug View)")
st.write(st.session_state)