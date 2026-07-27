from agents.hr_agent.hr_agent import HRAgent
from agents.finance_agent.finance_agent import FinanceAgent
from agents.it_agent.it_agent import ITAgent


def test_hr_agent():

    agent = HRAgent()

    result = agent.handle_request(
        "vacation policy"
    )

    assert "answer" in result


def test_finance_agent():

    agent = FinanceAgent()

    result = agent.handle_request(
        "total spending"
    )

    assert "total_amount" in result


def test_it_agent():

    agent = ITAgent()

    result = agent.handle_request(
        "vpn issue"
    )

    assert "solution" in result