# ============================================================
# PCC - Personal Command Center
# File: Home.py
# Purpose: Main landing page of the PCC application
# This file acts as the entry point for the Streamlit multi-page app.
# ============================================================

import streamlit as st

# ------------------------------------------------------------
# Page configuration (must be the first Streamlit command)
# ------------------------------------------------------------
st.set_page_config(
    page_title="PCC - Personal Command Center",  # Browser tab title
    page_icon="🧭",                              # Browser tab icon
    layout="wide"                                # Use full screen width
)

# ------------------------------------------------------------
# Main Page Content
# ------------------------------------------------------------
st.title("PCC - Personal Command Center")
st.caption("Base multi-page application shell")

# ------------------------------------------------------------
# Section: Welcome
# ------------------------------------------------------------
st.markdown("## Welcome")
st.write(
    "This is the main entry page for PCC. "
    "Use the left sidebar to navigate across modules."
)

# ------------------------------------------------------------
# Section: Current Milestone
# This helps track platform build progress inside the UI
# ------------------------------------------------------------
st.markdown("## Current Milestone")
st.info("PCC.M3.S1 - Multi-page structure is being established.")

# ------------------------------------------------------------
# Section: Available Sections (Navigation Guidance)
# ------------------------------------------------------------
st.markdown("## Available Sections")
st.write("- Dashboard")
st.write("- Project Workspace")

# ------------------------------------------------------------
# Section: Next Intent
# Explains why this layer exists in the architecture
# ------------------------------------------------------------
st.markdown("## Next Intent")
st.write(
    "This layer creates the navigational foundation so future features "
    "can be added page by page without restructuring the app."
)