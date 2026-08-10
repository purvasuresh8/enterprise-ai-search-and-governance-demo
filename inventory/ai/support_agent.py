import ollama


class SupportAgent:

    def __init__(self, model="llama3.1"):
        self.model = model

    def generate_response(self, question: str) -> str:

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """
You are a professional customer support assistant.

Provide:
- Clear answers
- Helpful troubleshooting steps
- Professional tone
- Concise responses

If you are unsure, recommend creating a support ticket.
"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response["message"]["content"]
        