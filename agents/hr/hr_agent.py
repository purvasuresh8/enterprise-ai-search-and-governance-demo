import json
from pathlib import Path

from agents.core.agent_framework import BaseAgent

DATA = (
    Path(__file__)
    .parent
    .joinpath("hr_policy_data.json")
)


class HRAgent(BaseAgent):

    def __init__(self):

        super().__init__("HR Agent")

        with open(DATA, "r") as f:
            self.policies = json.load(f)

    def handle_request(self, query):

        query = query.lower()

        for item in self.policies:

            if item["topic"].lower() in query:
                return {
                    "agent": self.name,
                    "answer": item["answer"]
                }

        return {
            "agent": self.name,
            "answer": "No HR policy found."
        }