# Skill: Project Bootstrap — Streamlit + GitHub + Deployment

## Purpose

Set up a new project with GitHub, local development, Streamlit app, and Streamlit Cloud deployment.

---

## Pre-Requisites (Install Once Per Machine)

Install the following:

1. Git → https://git-scm.com/
2. Python 3.10–3.11 → https://python.org
3. Cursor → https://cursor.sh
4. GitHub Desktop → https://desktop.github.com/

Verify installations:

```
git --version
python --version
pip --version
```

---

## Step 1 — Create GitHub Repository

* Create new repository on GitHub
* Add README
* Add .gitignore (Python)
* Set branch = main

---

## Step 2 — Clone Repository Locally

Using GitHub Desktop:

* Clone repo
* Save inside:
  OneDrive/Documents/Projects/<project-name>

Open folder in Cursor.

---

## Step 3 — Create Project Structure

```
app/
pages/
agents/
skills/
memory/
data/
docs/
tests/

requirements.txt
run_app.py
.env.example
```

---

## Step 4 — requirements.txt

```
streamlit
openai
langchain
python-dotenv
pandas
```

---

## Step 5 — Streamlit App

app/main.py

```python
import streamlit as st

st.set_page_config(page_title="App")

st.title("App Running")
st.sidebar.title("Navigation")
```

---

## Step 6 — Run Locally

```
pip install -r requirements.txt
python run_app.py
```

---

## Step 7 — Commit and Push

GitHub Desktop:

* Commit
* Push / Publish branch

---

## Step 8 — Deploy to Streamlit Cloud

* share.streamlit.io
* New App
* Repo
* Branch = main
* File = app/main.py
* Deploy

---

## Output

* Local app
* GitHub repo
* Live Streamlit URL
* Modular project structure
