from datetime import datetime


class SearchTool:

    def search(self, query):

        return {
            "query": query,
            "result": f"Knowledge found for '{query}'"
        }


class CalculatorTool:

    def calculate(self, value1, value2):

        return {
            "result": value1 + value2
        }


class DateTool:

    def now(self):

        return datetime.utcnow().isoformat()