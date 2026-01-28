# AtlasLogix Automation Suite

## What We Covered
- Login flow validation
- Shipments list retrieval + schema validation
- Shipment details retrieval + schema validation
- Compliance approval (success + locked cases)
- Audit logs validation
- Smoke suite combining all flows
- HTML reporting via pytest-html
- Modular test design with reusable fixtures and schemas

## What We Didn’t Cover (and Why)
- Performance / load testing → out of scope for functional QA
- Negative scenarios beyond compliance lock → limited by API sandbox data
- UI testing → API-only assessment
- Multi-tenant scenarios → only `TENANT-01` provided in assessment

## Assumptions
- Credentials: `auditor@atlaslogix.test / password`
- Tenant: `TENANT-01`
- Base URL: `https://nexus-atlaslogix-assessment.vast-soft.com/api/v1`
- Compliance approval may return either **shipment object** or **error object** (locked case)
- Audit logs always return JSON with `data` array
- Tests are run from project root (`atlaslogix-automation`) using provided `.bat` / `.sh` scripts

```markdown
# Automation Sample — AtlasLogix Assessment API

## Overview
Pytest-based automation suite covering critical flows:
- Login
- Fetch shipments list
- Fetch shipment details
- Attempt compliance approve (success or locked)
- Check audit logs

Includes both **modular tests** (per feature) and a **smoke suite** (`test_smoke_atlaslogix.py`).

---

## Setup

### Step 1: Install Python
Ensure you have **Python 3.9+** installed.  
Verify installation:

- **Windows CMD**
  ```cmd
  python --version
  ```
- **Mac/Linux Terminal**
  ```bash
  python3 --version
  ```

---

### Step 2: Install Dependencies
Install required packages:

```bash
pip install -r requirements.txt
```

Recommended packages in `requirements.txt`:
- pytest
- requests
- pytest-html
- jsonschema
- pytest-metadata
- python-dotenv

---

## Running Tests

You can run tests in two ways:  
1. **Directly from the command line**  
2. **Using the provided `.bat` (Windows) or `.sh` (Mac/Linux) files** (located in the `automation/` folder)

---

### 🔹 Option 1: Run Tests via Command Line

- **Windows CMD**
  ```cmd
  python -m pytest -v automation/tests --html=report.html --self-contained-html && start report.html
  ```

- **Mac/Linux Terminal**
  ```bash
  python3 -m pytest -v automation/tests --html=report.html --self-contained-html && open report.html
  ```
  *(On Linux replace `open` with `xdg-open`)*

---

### 🔹 Option 2: Run Tests via Provided Files

- **Windows (`automation/run_tests.bat`)**
  ```bat
  @echo off
  REM Move up to project root
  cd ..

  REM Run pytest and generate HTML report
  python -m pytest -v automation/tests --html=report.html --self-contained-html

  REM Open the report automatically
  start report.html
  ```

- **Mac/Linux (`automation/run_tests.sh`)**
  ```bash
  #!/bin/bash
  # Move up to project root
  cd ..

  # Run pytest and generate HTML report
  python3 -m pytest -v automation/tests --html=report.html --self-contained-html

  # Open the report automatically
  if [[ "$OSTYPE" == "darwin"* ]]; then
      open report.html
  else
      xdg-open report.html
  fi
  ```

---

## Notes
- Credentials: `auditor@atlaslogix.test / password`  
- Tenant: `TENANT-01`  
- Base URL and credentials can be loaded from `.env` if using `python-dotenv`.  
- Handles both success and locked compliance approval cases.  
- HTML report (`report.html`) is generated after every run and opened automatically.  
- You can run subsets of tests with markers, e.g.:
  ```bash
  pytest -m login
  pytest -m compliance
  pytest -m audit
  ```
```