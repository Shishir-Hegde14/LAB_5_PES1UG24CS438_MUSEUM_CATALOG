# Issues found in the museum catalog

Line numbers below refer to the original file at commit `7c1fc2f`. Findings
come from the saved reports in `reports/before/`. Bandit reported one medium
and four low severity findings; it reported no high severity findings.
Pylint and Flake8 findings are listed after the security findings and do not
use Bandit's severity scale.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| B608: SQL built with concatenation | Security, medium | 11 | Artifact fields become part of the SQL text. An apostrophe can break the query, and crafted input can alter its meaning. | Bind all four values through SQLite `?` placeholders. |
| B105: Hardcoded password | Security, low | 7 | An unused curator password is stored in source control. | Remove the unused constant. The program has no authentication feature that needs it. |
| B602: Shell execution | Security, low | 37 | Printing a fixed notice launches a shell unnecessarily. Bandit rates this fixed command low severity. | Use `print()` for the same notice. |
| B607: Partial executable path | Security, low | 37 | The shell command relies on resolving `echo` through the execution environment. | Remove the external command when replacing it with `print()`. |
| B404: Subprocess import | Security, low | 3 | Bandit flags the subprocess import for security review. | Remove the import after eliminating the shell call. |
| W0611 / F401: Unused import | Code quality | 2 | `datetime` is imported but never used. | Remove the import. |
| W0613: Unused parameter | Code quality | 15 | `curator` is accepted but has no effect on display status. | Remove the parameter and update the demonstration call. |
| C0114 / C0116: Missing documentation | Maintainability | 1, 10, 15, 24, 31, 36, 40 | The module and functions have no docstrings. | Add short descriptions of their purpose and relevant behavior. |
| C0103: Function names | Naming | 10, 15, 24, 31, 36 | Function names use camelCase instead of Python's snake_case convention. | Rename the functions and update all callers. |
| R1705: Unnecessary else | Code quality | 17-20 | An `else` follows a branch that already returns. | Return the storage status directly after the display branch. |
| C0301 / E501: Long lines | Formatting | 6, 11, 16, 26, 32 | SQL statements and expressions exceed the line limits. | Wrap statements using parentheses and adjacent string literals. |
| E303: Extra blank line | Formatting | 24 | Three blank lines separate top-level functions. | Use two blank lines. |
| E225: Missing spaces | Formatting | 25 | `total=0` has no spaces around the assignment operator. | Change it to `total = 0`. |

Additional observations from manual inspection, separate from tool findings:

- Looking up a missing artifact subscripts `None` and raises an unclear
  `TypeError`. Return a clear `ValueError` for an unknown ID.
- Importing the module runs the demonstration. Add a main guard so importing
  functions does not add sample artifacts or print output.
