# ======================================================================
"""
File: core/session_state.py
Project: PCC (Personal Command Center)
Milestone: PCC.M3.S2 - Session State Foundation

OBJECTIVE:
This file manages session state (memory) for the entire PCC application.

WHAT IS SESSION STATE:
Session state is Streamlit's way of storing data while the user is using the app.
It allows the app to remember:
- Who is logged in
- Which project is selected
- Which job is active
- Decision logs
- User preferences (future)

WHY THIS FILE EXISTS:
Instead of writing session logic in every page,
we centralize session logic here so it is reusable and consistent.

SESSION VARIABLES MANAGED HERE:
- user
- authenticated
- active_project
- active_job
- decision_log

FUNCTIONS PROVIDED:
- init_session() → Initializes session variables
- login(user_name) → Logs user in
- logout() → Logs user out and resets session variables

PAGES THAT USE THIS FILE:
- main.py
- pages/Home.py
- pages/Dashboard.py (future)
- pages/Project_Workspace.py (future)
- pages/Decision_Log.py (future)
- pages/Settings.py (future)
"""
# ======================================================================

import streamlit as st  # Imports Streamlit so we can use session_state


def init_session():
    """
    Initialize all required session state variables.

    Why this exists:
    Streamlit reruns the script often.
    If a variable does not already exist in st.session_state,
    we create it with a safe default value.
    """

    # Stores the current user's name or identifier.
    # None means no user is logged in yet.
    if "user" not in st.session_state:
        st.session_state.user = None

    # Tracks whether the user is authenticated.
    # False means not logged in.
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    # Stores which project is currently selected in the app.
    # None means nothing has been selected yet.
    if "active_project" not in st.session_state:
        st.session_state.active_project = None

    # Stores which job/task is currently selected.
    # This is useful later when you add workflows/jobs.
    if "active_job" not in st.session_state:
        st.session_state.active_job = None

    # Stores decision log entries in memory for the session.
    # Starting with an empty list means no decisions yet.
    if "decision_log" not in st.session_state:
        st.session_state.decision_log = []


def login(user_name: str):
    """
    Simulates a login action.

    What it does:
    - saves the user name
    - marks the session as authenticated
    """

    st.session_state.user = user_name
    st.session_state.authenticated = True


def logout():
    """
    Logs the user out and clears session-specific selections.

    What it resets:
    - user
    - authenticated flag
    - active project
    - active job

    What it keeps:
    - decision_log for now, unless you want full reset behavior later
    """

    st.session_state.user = None
    st.session_state.authenticated = False
    st.session_state.active_project = None
    st.session_state.active_job = None