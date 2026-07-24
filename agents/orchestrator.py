from agents.hr_agent.hr_agent import HRAgent
from agents.finance_agent.finance_agent import FinanceAgent
from agents.it_agent.it_agent import ITAgent


class AgentOrchestrator:

    def __init__(self):

        self.hr_agent = HRAgent()
        self.finance_agent = FinanceAgent()
        self.it_agent = ITAgent()

    def route(self, query):

        q = query.lower()

        if any(
            word in q
            for word in [
                "leave",
                "vacation",
                "benefits",
                "hr"
            ]
        ):
            return self.hr_agent.handle_request(query)

        if any(
            word in q
            for word in [
                "expense",
                "finance",
                "budget",
                "total",
                "average"
            ]
        ):
            return self.finance_agent.handle_request(query)

        if any(
            word in q
            for word in [
                "vpn",
                "password",
                "laptop",
                "computer"
            ]
        ):
            return self.it_agent.handle_request(query)

        return {
            "message": "No matching agent found."
        }