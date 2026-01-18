# AI Code Review Assignment (Python)

## Candidate
- Name: Ahdab kasim
- Approximate time spent: 60 minute

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The numerator ignores cancelled orders, but the denominator doesn’t — so the math is off.
- Empty input blows up because of a divide-by-zero.

### Edge cases & risks
- If all orders are cancelled, the function still divides by the full list length and returns a misleading result.

- The code assumes each item is a dictionary with status and amount fields, which can cause runtime errors for malformed inputs.

### Code quality / design issues
- The denominator does not reflect the stated business rule (“average over non-cancelled orders”).

- There is no validation or safe handling for unexpected input types.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Track only non-cancelled orders and divide by their count instead of len(orders).

- Return 0.0 when no valid orders exist to avoid division by zero.

- Skip malformed entries and ignore non-numeric amounts to keep the function safe.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
I would focus on cases that affect correctness and stability:

An empty list or a list where all orders are cancelled, to confirm the function returns 0.0 without errors.

A mix of cancelled and non-cancelled orders, to ensure only valid orders affect the average.

Orders with missing or invalid amount values, to verify they are skipped instead of crashing.

Unexpected inputs (e.g. None or non-dict values) to confirm the function handles them safely.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- It claims cancelled orders are excluded correctly, but the denominator still includes them.

- It does not mention the division-by-zero case for empty input.


### Rewritten explanation
- This function calculates the average order value using only non-cancelled orders. It adds up valid numeric amounts and divides by the number of orders included in the calculation. Invalid entries are ignored, and the function returns 0.0 when no valid orders are present.

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
