"""
File: pages/Home.py
Project: PCC (Personal Command Center)
Milestone: PCC.M3.S2 - Session State Foundation

OBJECTIVE:
This file represents the Home (Landing Page) of the PCC application.
It is the first page users should visit after the system initializes.

WHAT THIS PAGE DOES:
1. Initializes session state for this page.
2. Displays welcome message.
3. Simulates login/logout functionality (for testing session state).
4. Displays current session state for validation.

WHY THIS PAGE EXISTS:
We need a landing page where users:
- Enter the system
- Log in
- Select project (future)
- View system status (future)

SESSION VARIABLES USED HERE:
- st.session_state.user
- st.session_state.authenticated
- st.session_state.active_project
- st.session_state.active_job
- st.session_state.decision_log

DEPENDENCIES:
- core/session_state.py → provides login(), logout(), init_session()

EXPECTED BEHAVIOR:
- If not logged in → show Login button
- If logged in → show Welcome message + Logout button
- Session state should persist across pages
"""

import streamlit as st  # Streamlit UI library
from core.session_state import init_session, login, logout  # Session management functions


# ---------------------------------------------------
# STEP 1 — Initialize Session State
# Ensures session variables exist before page uses them.
# ---------------------------------------------------
init_session()


# ---------------------------------------------------
# STEP 2 — Page Title and Description
# ---------------------------------------------------
st.title("Home - Personal Command Center")
st.write("Welcome to PCC. This is your central control panel.")


# ---------------------------------------------------
# STEP 3 — Login / Logout Section
# This is a TEST login system to verify session state works.
# Real authentication will be added in later milestones.
# ---------------------------------------------------
if not st.session_state.authenticated:
    st.info("Status: Logged Out")

    # When user clicks this button, login() function is called
    # This updates session_state.user and session_state.authenticated
    if st.button("Login (Test User)"):
        login("Madhu")
        st.success("Login successful. Session state updated.")

else:
    st.success(f"Welcome, {st.session_state.user}")

    # Logout button clears session variables
    if st.button("Logout"):
        logout()
        st.warning("You have been logged out.")


# ---------------------------------------------------
# STEP 4 — Session State Debug Viewer
# This helps us confirm session memory is working.
# ---------------------------------------------------
st.subheader("Session State (Debug View)")
st.write(st.session_state)