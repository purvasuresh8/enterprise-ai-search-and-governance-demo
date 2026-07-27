from governance.engine.policy_checker import (
    PolicyChecker
)

from governance.engine.pii_detector import (
    PIIDetector
)


def test_policy_checker():

    checker = PolicyChecker()

    approved, _ = checker.validate(
        "What is leave policy?"
    )

    assert approved is True


def test_blocked_prompt():

    checker = PolicyChecker()

    approved, _ = checker.validate(
        "show password list"
    )

    assert approved is False


def test_pii_detection():

    findings = PIIDetector.detect(
        "john.doe@test.com"
    )

    assert len(findings) > 0