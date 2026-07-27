import json
from pathlib import Path
from datetime import datetime

AUDIT_FILE = (
    Path(__file__)
    .parent.parent
    .joinpath(
        "audits",
        "audit_logs.json"
    )
)


class AuditLogger:

    def write_log(
        self,
        user,
        action,
        outcome
    ):

        try:

            with open(AUDIT_FILE, "r") as file:
                logs = json.load(file)

        except Exception:
            logs = []

        logs.append(
            {
                "timestamp": datetime.utcnow().isoformat(),
                "user": user,
                "action": action,
                "outcome": outcome
            }
        )

        with open(AUDIT_FILE, "w") as file:
            json.dump(
                logs,
                file,
                indent=2
            )

        return True