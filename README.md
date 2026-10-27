# Lab 5: Static Code Analysis - Museum Artifact Catalog

This lab uses Pylint, Bandit, and Flake8 to improve `museum_catalog.py`.
The program registers museum artifacts in an in-memory SQLite database,
moves them onto display, and totals their value by era.

## Setup on Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

The recorded environment uses Python 3.11.9, Pylint 4.1.3, Bandit 1.9.4,
and Flake8 7.4.1. `requirements-dev.txt` pins the installed tool dependencies.
The catalog itself uses only the Python standard library.

## Run and check

```powershell
.\.venv\Scripts\python.exe museum_catalog.py
.\.venv\Scripts\python.exe -m pylint museum_catalog.py
.\.venv\Scripts\python.exe -m bandit -r museum_catalog.py -f txt
.\.venv\Scripts\python.exe -m flake8 museum_catalog.py test_museum_catalog.py
.\.venv\Scripts\python.exe -m unittest -v test_museum_catalog
```

Expected demonstration output:

```text
on display
135000
catalog backup complete
```

The backup message is a notice only. It does not create a backup file.
The database exists only for the life of the process. The original captured
output printed the shell's backup notice first because of buffering; the
updated version prints all three lines in the order they are called.

## Results and deliverables

| Check | Original | Final |
|-------|----------|-------|
| Pylint | 4.85/10 | 10.00/10 |
| Bandit | 1 medium, 4 low findings | No findings |
| Flake8, catalog script | 8 findings | No findings |
| Regression tests | Not present | 7 passing |

- `museum_catalog.py`: cleaned script, with more than four issues fixed.
- `issues.md`: original line references, findings, fix approaches, and status.
- `reflection.md`: four provisional reflection topics. The handout omits the
  actual reflection questions.
- `reports/before/`: untouched baseline tool reports and program output.
- `reports/security/`: Bandit verification for the security commit.
- `reports/quality/`: Pylint and test verification for the code quality commit.
- `reports/after/`: final tool reports, program output, and test results.
- `test_museum_catalog.py`: behavior and security regression checks.
- `requirements-dev.txt`: reproducible analysis tool dependencies.

An empty final Flake8 report means the tool found no violations. Static
analysis targets the assigned catalog script; the final Flake8 check also
includes the test file. Reports contain the tools' actual output.

The work is organized into three commits: Bandit security fixes, Pylint code
quality fixes, and Flake8 formatting fixes with final documentation. No PDF
or Word report is required by the handout; the written deliverables use plain
Markdown without added colors or font styling.
