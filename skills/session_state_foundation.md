# Skill: Session State Foundation

# Milestone Reference: PCC.M3.S2

# Project: PCC (Personal Command Center)

---

## OBJECTIVE

Implement a session state (memory layer) in a multi-page Streamlit application so the system can remember:

* Logged-in user
* Authentication status
* Active project
* Active job
* Decision log entries

This is required before implementing:

* Authentication
* Project context
* Job workflows
* Decision governance
* AI agent orchestration

---

## WHEN TO USE THIS SKILL

Use this skill when:

* Building a multi-page Streamlit app
* The app needs memory across pages
* The app needs login/session behavior
* The app needs project tracking
* The app needs decision tracking

---

## REQUIRED FOLDER STRUCTURE

The application must follow this structure:

app/
│
├── main.py                 # Application boot layer
├── pages/                  # UI pages
│   ├── Home.py
│   ├── Dashboard.py
│   ├── Project_Workspace.py
│   ├── Decision_Log.py
│   └── Settings.py
│
├── core/                   # Shared logic layer
│   └── session_state.py
│
├── data/                   # Data files
├── memory/                 # Logs / decision memory
└── docs/                   # Documentation

---

## STEP 1 — Create Session State Manager

Create file:
app/core/session_state.py

Add the following code:

```python
"""
File: session_state.py
Purpose: Manage session state (memory) for the entire application.
This file ensures the app remembers user, project, job, and decision data across pages.
"""

import streamlit as st  # Streamlit library for session state


def init_session():
    """
    Initialize session state variables.
    This function must run at the start of every page.
    It ensures required session variables exist.
    """

    # Stores logged-in user name
    if "user" not in st.session_state:
        st.session_state.user = None

    # Tracks login status
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    # Tracks which project is currently active
    if "active_project" not in st.session_state:
        st.session_state.active_project = None

    # Tracks which job is currently active
    if "active_job" not in st.session_state:
        st.session_state.active_job = None

    # Stores decision log entries
    if "decision_log" not in st.session_state:
        st.session_state.decision_log = []


def login(user_name: str):
    """
    Simulates user login.
    Updates session state with user information.
    """

    st.session_state.user = user_name
    st.session_state.authenticated = True


def logout():
    """
    Logs the user out and resets session variables.
    """

    st.session_state.user = None
    st.session_state.authenticated = False
    st.session_state.active_project = None
    st.session_state.active_job = None
```

---

## STEP 2 — Update main.py (Boot Layer)

File location:
app/main.py

Purpose:

* Configure Streamlit app
* Initialize session state
* Display system initialization message

Add:

```python
"""
File: main.py
Purpose: Application boot layer.
This file runs first when the app starts.
It initializes session state and prepares the system.
"""

import streamlit as st
from app.core.session_state import init_session  # Import session initializer

# Configure Streamlit page
st.set_page_config(
    page_title="PCC - Personal Command Center",
    layout="wide"
)

# Initialize session memory
init_session()

# Display initialization message
st.title("PCC System Initialization")
st.success("System initialized successfully.")
st.info("Use the sidebar to navigate to Home, Dashboard, or Project Workspace.")

# Debug view (temporary)
st.subheader("Session State (Debug View)")
st.write(st.session_state)
```

---

## STEP 3 — Update Home Page

File location:
app/pages/Home.py

Purpose:

* Acts as landing page
* Provides login/logout test
* Displays session state

Add:

```python
"""
File: Home.py
Purpose: Landing page of PCC.
This page tests login and session persistence.
"""

import streamlit as st
from app.core.session_state import init_session, login, logout

# Initialize session state
init_session()

st.title("Home - Personal Command Center")
st.write("Welcome to PCC. This is your central control panel.")

# Login / Logout logic
if not st.session_state.authenticated:
    st.info("Status: Logged Out")

    if st.button("Login (Test User)"):
        login("Madhu")
        st.success("Login successful. Session state updated.")
else:
    st.success(f"Welcome, {st.session_state.user}")

    if st.button("Logout"):
        logout()
        st.warning("You have been logged out.")

# Debug session state
st.subheader("Session State (Debug View)")
st.write(st.session_state)
```

---

## STEP 4 — How to Run the App

Open terminal and run:

If you are in project root:

```
streamlit run app/main.py
```

If you are inside app folder:

```
streamlit run main.py
```

---

## STEP 5 — VALIDATION CHECKLIST

After running the app, confirm:

| Test                      | Expected Result  |
| ------------------------- | ---------------- |
| App loads                 | No import errors |
| Home page loads           | Yes              |
| Login button works        | Yes              |
| Logout button works       | Yes              |
| Navigate pages            | Session persists |
| Session variables visible | Yes              |
| decision_log exists       | Yes              |

Session state should look like:

{
"user": "Madhu",
"authenticated": true,
"active_project": null,
"active_job": null,
"decision_log": []
}

---

## STEP 6 — Update Decision Log

Update file:
app/docs/decision_log.md

Add entry for:
PCC.M3.S2 — Session State Foundation

---

## STEP 7 — Commit Using GitHub Desktop

Commit Summary:
PCC.M3.S2 - Session State Foundation

Commit Description:
Implemented session state memory layer for PCC multi-page Streamlit app.
Added session_state.py to manage user, project, job, and decision memory.
Updated main.py as boot layer and Home.py as landing page.
Validated session persistence across pages.

---

## EXPECTED OUTCOME

After completing this skill, the application will have:

| Capability             | Status  |
| ---------------------- | ------- |
| Multi-page navigation  | Enabled |
| User session           | Enabled |
| Project context ready  | Enabled |
| Job tracking ready     | Enabled |
| Decision logging ready | Enabled |
| Memory layer           | Enabled |

This completes the Memory Layer of the PCC architecture.
