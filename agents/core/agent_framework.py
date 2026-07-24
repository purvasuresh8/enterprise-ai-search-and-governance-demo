from abc import ABC, abstractmethod


class BaseAgent(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def handle_request(self, query):
        pass

    def info(self):
        return {
            "agent_name": self.name
        }