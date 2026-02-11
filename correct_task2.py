import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def count_valid_emails(emails):
    count = 0

    for email in emails:
        if isinstance(email, str) and EMAIL_REGEX.match(email):
            count += 1

    return count