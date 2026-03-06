# AI Code Review Assignment (Python)

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The original implementation divides the total of non-cancelled orders by the total number of orders.
- It assumes that every order has a valid numeric "amount" field, which can raise runtime errors.

### Edge cases & risks
- If all orders are cancelled, the function will divide by zero.
- Orders with missing, None, or non-numeric "amount" values are not safely handled.
- Orders missing the "status" key may cause unexpected behavior.

### Code quality / design issues
- The variable count does not accurately represent the number of valid orders being averaged.
- The function incorrectly assumes that all input data is valid, mixing business logic with unsafe data assumptions.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only non-cancelled orders instead of all orders.
- Safely convert order amounts to float and ignore invalid values.
- Prevent division by zero by explicitly checking the valid order count.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations
<!-- If you were to test this function, what areas or scenarios would you focus on, and why? -->
Key test cases include:
- A mix of cancelled and non-cancelled orders 
- All orders cancelled 
- Orders with missing or invalid "amount" values  
- Empty input list 


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The explanation claims cancelled orders are excluded.
- It ignores potential runtime errors resulting from invalid or incomplete order amounts.


### Rewritten explanation
- This function calculates the average order value by summing the amounts of all non-cancelled orders and dividing by the number of valid, non-cancelled orders. It safely ignores cancelled orders and invalid amount values, and returns 0.0 if there are no valid orders.

## 4) Final Judgment
- Decision: Reject
- Justification: The core business logic produces incorrect averages and may raise runtime errors. The implementation cannot be approved in its current state.
- Confidence & unknowns: High confidence. Return-value semantics may depend on requirements.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The original implementation assumes every item in the list is a string, which can cause runtime errors when encountering None or non-string values.
- It treats any string containing "@" as a valid email.

### Edge cases & risks
- Empty strings, whitespace-only strings, or strings like "@", "user@", or "@domain" are incorrectly counted as valid.
- Non-string values are not safely handled.
- Emails with multiple @ characters are not filtered out.

### Code quality / design issues
- Email validation logic is overly simplistic.
- The function does not document what “valid” means.
- No input type checking is performed.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Add type checking to ensure only string values are processed.
- Replace the naive "@" check with a regular expression for proper email validation.


### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
Key test cases include:
- Valid and invalid email formats.
- Non-string inputs.
- Empty lists and lists containing empty strings.
- Edge cases like multiple @ symbols or missing domain parts.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- The explanation claims that invalid inputs are safely ignored, which is not true for non-string values.
- It does not mention the simplistic nature of the validation.


### Rewritten explanation
- This function counts the number of valid email addresses in the given list by validating only string inputs against a regular expression. Invalid formats, non-string values, and empty entries are safely ignored.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original validation logic was overly simplistic and did not align with realistic email validation requirements.
- Confidence & unknowns: High confidence. Validation rules must be clarified.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The original implementation divides the sum of valid values by the total length of the list, including invalid and missing entries, which results in an incorrect average.
- It assumes all non-None values can be safely converted to float, which can raise runtime errors.

### Edge cases & risks
- If the list contains only None or invalid values, the function will divide by zero.
- Non-numeric types such as strings or objects can cause exceptions.
- Empty input lists are not handled safely.

### Code quality / design issues
- The variable count does not represent the number of valid measurements.
- The function lacks defensive programming practices.
- Input validation and aggregation logic are tightly coupled without safeguards.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only successfully parsed numeric values.
- Safely convert values to float and ignore invalid entries.
- Prevent division by zero by returning 0.0 when no valid measurements exist.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
Key test cases include:
- Mixed valid and invalid numeric values.
- Inputs containing only non-numeric values.
- Empty input lists.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- The explanation claims missing values are ignored, but the original code still includes them in the division.
- It does not mention potential runtime errors from invalid types.


### Rewritten explanation
- This function computes the average of valid measurements by summing only values that can be safely converted to numbers and dividing by the count of those valid values. Missing and invalid inputs are ignored, and the function returns 0.0 when no valid measurements are present.

## 4) Final Judgment
- Decision: Reject
- Justification: The function produces mathematically incorrect results and lacks necessary defensive checks. This makes it unsafe for production use.
- Confidence & unknowns: High confidence. The mathematical issue is obvious. Final behavior may depend on product expectations.
