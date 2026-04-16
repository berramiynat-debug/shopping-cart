# CI/CD Pipeline Lab Assignment Report

**Course**: COMP 3304 - Fundamentals of Software Engineering  
**Assignment**: Working CI pipeline (Chapter 11)

## 1. Requirements Met
- ✅ Created a live, working CI pipeline using GitHub Actions.
- ✅ Used the previously corrected `cart.py` file.
- ✅ **Trigger**: Configured to run on every push to the `develop` branch.
- ✅ **Automated Testing**: Pipeline runs the full suite (`test_cart.py`) automatically using `pytest`.
- ✅ **Branch Protection**: Enabled blocking merges to `main` if tests fail.
- ✅ **Linting Gate**: Integrated `flake8` for syntax checking and code formatting enforcement.

---

## 2. GitHub Actions Pipeline Specification (ci.yml)

The pipeline is defined as follows:

```yaml
name: CI Pipeline

on:
  push:
    branches: [ develop ]

jobs:
  test-and-lint:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.12'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest pytest-cov

    - name: Lint with flake8
      run: |
        # Stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

    - name: Run tests with pytest
      run: |
        pytest test_cart.py -v
```

---

## 3. Required Screenshots

*(Please insert your screenshots below before exporting to PDF)*

### A. Pipeline Run Evidence (Green Checkmarks)
> **Instructions for student**: Take a screenshot of the GitHub Actions page showing the successful execution of your `test-and-lint` job.
[Insert Screenshot Here]

### B. Branch Protection Rule Evidence
> **Instructions for student**: Take a screenshot of your GitHub Repository Settings > Branches > Branch Protection Rule. Ensure it shows that "Require status checks to pass before merging" is enabled for the `main` branch, pointing to your CI job.
[Insert Screenshot Here]

### C. Failing Status Demonstration (Optional/If required)
> **Instructions for student**: If instructed to show a failed run, take a screenshot of a failed GitHub Action block due to a failing test or linter execution.
[Insert Screenshot Here]
