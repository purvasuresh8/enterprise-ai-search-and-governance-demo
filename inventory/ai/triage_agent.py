import ollama


class TriageAgent:

    def __init__(self, model="llama3.1"):
        self.model = model

    def classify(self, issue: str):

        prompt = f"""
Classify the customer issue into exactly one category:

- Technical
- Billing
- Account
- Product
- General

Customer Issue:
{issue}

Return only the category name.
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        category = response["message"]["content"].strip()

        return {
            "issue": issue,
            "category": category
        }
        