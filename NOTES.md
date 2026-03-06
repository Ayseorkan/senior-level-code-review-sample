# Notes (Optional)
<!-- This file is optional.

Use it only if you want to provide additional context for the reviewer that does not fit cleanly in submission_template.md.

Examples of appropriate use:

Assumptions you made
Known limitations of your solution
Alternative approaches you considered but did not implement
Do not repeat information already included in code_review.md. -->

- Task 1 :
    - If all orders are cancelled or the list is empty, the function returns 0.0.
      This may be misleading from a business perspective, since no valid orders exist to average.
      Returning None or raising an exception could be considered depending on product requirements.

- Task 3 :
    - If the list is empty or contains only invalid values, the function returns 0.0.
      This might not reflect the intended average and could be handled differently based on product rules.
