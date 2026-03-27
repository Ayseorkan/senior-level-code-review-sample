# Notes / Considerations

These notes provide additional context for the reviewer regarding the implementation choices and known limitations. 

## Function: calculate_average_order_value
- If all orders are cancelled or the input list is empty, the function returns `0.0`.
  - This is a defensive default, but business logic may prefer `None` or raising a specific exception to indicate no valid orders exist.
- Amount values that are missing, `None`, or invalid are ignored.
  - This prevents runtime errors but may hide data quality issues in production.
- Future improvements:
  - Consider logging skipped invalid orders for monitoring.
  - Consider validating order schema before aggregation.

## Function: count_valid_emails
- The regex used is a simplified validation: one `@`, no whitespace, and a domain present.
  - This is sufficient for general filtering but may reject valid internationalized emails or accept some edge cases.
- Non-string entries are ignored silently.
  - In production, you might log or raise warnings if unexpected types are encountered.
- Future improvements:
  - Use a more robust email validation library (e.g., `email-validator`) for stricter compliance.

## Function: average_valid_measurements
- Empty input lists or lists with only invalid values return `0.0`.
  - This avoids division by zero but may not reflect intended averages.
  - Business logic could return `None` or raise a `ValueError` to indicate no valid data.
- Non-numeric or malformed values are skipped silently.
  - Consider logging skipped entries to detect potential data issues.
- Future improvements:
  - Input schema validation before aggregation.
  - Optional parameter to decide behavior when no valid measurements exist.