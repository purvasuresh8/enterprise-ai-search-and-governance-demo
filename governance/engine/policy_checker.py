import yaml
from pathlib import Path

POLICY_FILE = (
    Path(__file__)
    .parent.parent
    .joinpath("policies", "ai_policy.yaml")
)


class PolicyChecker:

    def __init__(self):

        with open(POLICY_FILE, "r") as file:
            policy = yaml.safe_load(file)

        self.policy = policy["ai_policy"]

    def validate(self, prompt):

        if len(prompt) > self.policy["max_prompt_length"]:
            return False, "Prompt exceeds allowed limit."

        prompt_lower = prompt.lower()

        for keyword in self.policy["blocked_keywords"]:

            if keyword.lower() in prompt_lower:
                return (
                    False,
                    f"Blocked keyword detected: {keyword}"
                )

        return True, "Approved"