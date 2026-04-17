# CI/CD Pipeline Lab Assignment Report


## 1. Requirements Met
-  Created a live, working CI pipeline using GitHub Actions.
-  Used the previously corrected `cart.py` file.
-  **Trigger**: Configured to run on every push to the `develop` branch.
-  **Automated Testing**: Pipeline runs the full suite (`test_cart.py`) automatically using `pytest`.
-  **Branch Protection**: Enabled blocking merges to `main` if tests fail.
-  **Linting Gate**: Integrated `flake8` for syntax checking and code formatting enforcement.

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


