from openai import OpenAI

from devagent.config import get_provider_settings


class OpenAIProvider:
    def __init__(self):
        self.settings = get_provider_settings("openai")

        self.client = OpenAI(
            api_key=self.settings.api_key,
            base_url=self.settings.base_url,
        )

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.settings.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are DevAgent, a helpful assistant "
                        "for software developers."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response.choices[0].message.content or ""