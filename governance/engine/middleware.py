from governance.engine.policy_checker import (
    PolicyChecker
)

from governance.engine.audit_logger import (
    AuditLogger
)

from governance.engine.pii_detector import (
    PIIDetector
)


class GovernanceMiddleware:

    def __init__(self):

        self.policy_checker = PolicyChecker()

        self.audit_logger = AuditLogger()

    def inspect(
        self,
        user,
        prompt
    ):

        valid, message = (
            self.policy_checker
            .validate(prompt)
        )

        pii_findings = (
            PIIDetector.detect(prompt)
        )

        outcome = "approved"

        if not valid:
            outcome = "blocked"

        self.audit_logger.write_log(
            user=user,
            action=prompt,
            outcome=outcome
        )

        return {
            "approved": valid,
            "message": message,
            "pii_findings": pii_findings
        }