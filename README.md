# String Calculator – TDD Kata (Python)

This repository contains a Python implementation of the classic **String Calculator TDD Kata**, extended to meet both the [Incubyte Assessment](https://blog.incubyte.co/blog/tdd-assessment) and additional requirements.

All functionality has been built using **Test-Driven Development (TDD)** principles, with clear commit history, unit tests, and screenshots.

## 🧪 TDD Principles Followed

This project was developed using core TDD principles:

- **Red-Green-Refactor cycle** was followed for each user story.
- **Tests were always written first** before implementing the actual logic.
- Code was written in **small, incremental steps**, starting from the simplest case.
- **Only the minimal code** was written to make each test pass.
- Refactoring was done after all tests passed to ensure clean, maintainable code.
- **Each case was committed separately**, ensuring a clear development history.


---

## ✅ Features Implemented

| Feature Description | Example Input | Expected Output |
|---------------------|---------------|-----------------|
| Return 0 for empty string | `""` | `0` |
| Return number if only one provided | `"6"` | `6` |
| Sum two numbers | `"4,2"` | `6` |
| Handle unknown number of comma-separated numbers | `"1,2,3,4,5"` | `15` |
| Handle newline (`\n`) as delimiter | `"1\n2,3\n4,5"` | `15` |
| Support custom single-character delimiter | `"//;\n1;5"` | `6` |
| Raise exception on negative numbers | `"2,-4,3,-5"` | `Exception: Negatives not allowed: -4, -5` |
| Ignore numbers greater than 1000 | `"2,1001"` | `2` |
| Support custom delimiters of any length | `"//[***]\n1***2***3"` | `6` |
| Track how many times `add()` is called | Called 3 times | `get_called_count() → 3` |

---

## 🧪 How to Run the Tests

Make sure you're using Python 3.x.

```bash
python test.py
```
You should see output like:
```
Ran 12 tests in 0.000s
OK
```
This project was developed as part of the **Incubyte TDD Assessment** and to practice clean, test-driven software development using Python.
