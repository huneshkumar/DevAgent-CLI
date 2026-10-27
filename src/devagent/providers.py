from openai import OpenAI
from devagent.config import get_provider_settings


def ask_llm(provider: str, prompt: str) -> str:
    settings = get_provider_settings(provider)

    client = OpenAI(
        api_key=settings.api_key,
        base_url=settings.base_url,
    )

    response = client.chat.completions.create(
        model=settings.model,
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