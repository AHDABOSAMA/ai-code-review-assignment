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

- An empty list or a list where all orders are cancelled, to confirm the function returns 0.0 without errors.

- A mix of cancelled and non-cancelled orders, to ensure only valid orders affect the average.

- Orders with missing or invalid amount values, to verify they are skipped instead of crashing.

- Unexpected inputs (e.g. None or non-dict values) to confirm the function handles them safely.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- It claims cancelled orders are excluded correctly, but the denominator still includes them.

- It does not mention the division-by-zero case for empty input.


### Rewritten explanation
- This function calculates the average order value using only non-cancelled orders. It adds up valid numeric amounts and divides by the number of orders included in the calculation. Invalid entries are ignored, and the function returns 0.0 when no valid orders are present.

## 4) Final Judgment
- Decision: Request Changes 
- Justification: The original implementation returns an incorrect average and can crash on empty input. The corrected version fixes the core logic and handles common edge cases safely.
- Confidence & unknowns: High confidence in the fix. Handling of malformed orders depends on product requirements, but skipping them is a reasonable default for this task.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Right now it counts anything with an @ as “valid”, even if it’s clearly not an email.

- It also breaks if the list has non-strings (like None or an int), because "@" in email won’t work on those.

### Edge cases & risks
- Strings like "@", "a@", "@b", or "a@b@c" are counted as valid even though they are not.

- Whitespace-only strings or empty values are not handled explicitly.

### Code quality / design issues
- The validation logic is too weak for the claim of counting “valid email addresses”.

- The explanation overstates what the function actually does.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Ensure each entry is a string before validating.

- Require exactly one "@" with non-empty local and domain parts.

- Perform a basic domain check instead of relying on "@" alone.

- Ignore invalid inputs safely.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
I would test:

- An empty list and a list with only invalid values.

- Emails missing a local or domain part.

- Emails with multiple "@" symbols.

- Lists containing non-string values such as None or numbers.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- The function does not actually validate email addresses beyond checking for "@".

- It does not safely handle non-string inputs.

- The explanation claims correctness that the code does not provide.

### Rewritten explanation
- This function counts email addresses that pass a basic sanity check. It ensures each value is a string, contains exactly one "@", and has non-empty local and domain parts. Invalid entries are skipped.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original implementation overcounts invalid emails and can fail on non-string inputs. The corrected version aligns the logic with the intended behavior and handles common edge cases safely.
- Confidence & unknowns: High confidence for basic validation. Full RFC email validation is intentionally out of scope.

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
