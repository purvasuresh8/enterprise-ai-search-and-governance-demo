import pandas as pd

from pathlib import Path
from agents.core.agent_framework import BaseAgent

DATA = (
    Path(__file__)
    .parent
    .joinpath("transactions_sample.csv")
)


class FinanceAgent(BaseAgent):

    def __init__(self):
        super().__init__("Finance Agent")

        self.data = pd.read_csv(DATA)

    def handle_request(self, query):

        query = query.lower()

        if "total" in query:

            total = self.data["amount"].sum()

            return {
                "agent": self.name,
                "total_amount": float(total)
            }

        if "average" in query:

            avg = self.data["amount"].mean()

            return {
                "agent": self.name,
                "average_amount": round(float(avg), 2)
            }

        return {
            "agent": self.name,
            "answer": "Unable to process finance request."
        }