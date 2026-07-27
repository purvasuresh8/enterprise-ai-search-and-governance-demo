import re


class PIIDetector:

    @staticmethod
    def detect(text):

        findings = []

        ssn_pattern = r"\d{3}-\d{2}-\d{4}"

        email_pattern = (
            r"[A-Za-z0-9._%+-]+"
            r"@[A-Za-z0-9.-]+"
            r"\.[A-Za-z]{2,}"
        )

        if re.search(ssn_pattern, text):

            findings.append(
                "Potential SSN detected"
            )

        if re.search(email_pattern, text):

            findings.append(
                "Email address detected"
            )

        return findings