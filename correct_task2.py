# Write your corrected implementation for Task 2 here.
def count_valid_emails(emails):
    count = 0

    for email in emails:
        if not isinstance(email, str):
            continue

        email = email.strip()

        if not email:
            continue

        if email.count("@") != 1:
            continue

        local, domain = email.split("@")

        if not local or not domain:
            continue

        if "." not in domain:
            continue

        count += 1

    return count

# Do not modify `task2.py`.
