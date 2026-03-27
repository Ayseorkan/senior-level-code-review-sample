import re
from typing import List

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def count_valid_emails(emails: List[str]) -> int:
    """
    Counts the number of valid email addresses in a list.

    Args:
        emails (List[str]): A list of strings representing email addresses.

    Returns:
        int: Number of valid emails according to a regex.

    Notes:
        - Ignores non-string entries and invalid formats.
        - Regex checks that the email contains one '@', no spaces, and a domain.
        - For production, consider more robust email validation.
    """
    count = 0

    for email in emails:
        if isinstance(email, str) and EMAIL_REGEX.match(email):
            count += 1

    return count