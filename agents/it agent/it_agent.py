import json

from pathlib import Path
from agents.core.agent_framework import BaseAgent

DATA = (
    Path(__file__)
    .parent
    .joinpath(
        "troubleshooting_knowledge_base.json"
    )
)


class ITAgent(BaseAgent):

    def __init__(self):

        super().__init__("IT Agent")

        with open(DATA, "r") as f:
            self.kb = json.load(f)

    def handle_request(self, query):

        query = query.lower()

        for article in self.kb:

            if article["keyword"].lower() in query:

                return {
                    "agent": self.name,
                    "solution": article["solution"]
                }

        return {
            "agent": self.name,
            "solution": "No solution found."
        }