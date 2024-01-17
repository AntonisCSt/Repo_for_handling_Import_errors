# Modular Coding in Python: A Guide for Handling Import Errors

This is a repository for the code that the medium article: [link] contains.

Requirements: Python 3.9+

## Intro

When our code becomes large or complex, breaking it down into smaller, more manageable parts through modular programming is crucial. This practice enhances organization, reusability, and maintainability. However, Python developers often face challenges like ModuleNotFoundError and ImportError.

In this article, we provide a foundation, solutions, and explanations to tackle these issues effectively.

## Code outline

* /Example_1: Contains the one-script application `app.py` referenced in Section 1.

* /Example_2: Contains the modular version of Example_1. It contains a `helper_functions.py` that depends on `config.py` in the folder/directory and the `app.py` depends on `helper_functions.py`.

* /Example_3: Shares a similar structure with Example_2, but helper_functions.py imports config.py using both relative and absolute imports within a try/except block. Solution 1 in the article pertains to the relative import of helper_functions.py.

* /Solution 2: Contains the solution to run `app.py` successfully with an absolute import of config.py by helper_functions.py.

* /Solution 3: Has the solution using the `sys` library (not recommended).