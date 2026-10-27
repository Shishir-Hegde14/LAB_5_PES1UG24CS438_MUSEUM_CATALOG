# Reflection

The supplied three-page handout asks for reflection answers, and the README
mentions four questions, but neither includes the actual questions. The four
topics below are provisional and cover the lab's learning outcomes. They can
be matched to the instructor's questions if those are supplied later.

## 1. What did the tools reveal?

The original program ran, but that did not mean its implementation was sound.
Pylint gave it 4.85/10 and flagged missing documentation, inconsistent function
names, unused code, and unnecessary branching. Flake8 reported eight findings,
including long lines and spacing problems. Bandit reported five security
findings: one medium severity SQL construction issue and four low severity
findings involving an unused password and subprocess usage.

The SQL issue was the most useful example. The program inserted artifact
fields by joining strings into a query. Even an ordinary title containing an
apostrophe could break it. Binding the values with SQLite placeholders fixed
that problem and kept SQL-like text from becoming part of the statement.

## 2. How were the fixes prioritized?

The medium severity SQL finding came first. The remaining Bandit findings
were then resolved by removing the unused password and replacing the shell
command with a direct print statement. The backup function only announces
completion; it does not perform a backup, so it did not need a subprocess.

The next changes improved readability: snake_case names, short docstrings,
removal of the unused import and parameter, and simpler return logic. The
remaining line wrapping and spacing changes were completed last. Keeping
these stages in three commits makes the work easier to review.

## 3. How were the changes verified?

Reports from the original file were preserved before editing. After the fixes,
Pylint scored the script 10.00/10, Bandit reported no findings, and Flake8
reported no violations. No warning suppressions were added.

Seven regression tests also passed. They cover quoted and SQL-like titles,
storage-to-display changes, an initially displayed artifact, era totals and
empty results, missing artifact IDs, the backup notice, and importing without
running the demonstration. The demonstration still reports an artifact on
display and a Chola collection value of 135000. Its three output lines are now
printed in call order; the original shell command could appear first in
captured output because of buffering.

## 4. What are the limits of static analysis?

The three tools complement one another, but clean reports do not prove the
program is correct or secure in every situation. For example, manual reading
showed that requesting an unknown artifact caused an unclear exception and
that importing the module ran the demonstration. Those were addressed with a
clear ValueError and a main guard, then checked with tests.

The final program remains a small teaching example. Its database is in memory,
there is no authentication feature, and its backup notice does not save data.
The lab improves the existing program without turning it into a production
museum system. Static analysis helps find common problems, while code review
and behavior checks are still needed to understand what the program does.
