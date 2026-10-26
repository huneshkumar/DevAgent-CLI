
import os

from openai import OpenAI


def get_client(provider: str) -> tuple[OpenAI, str]:
    provider = provider.lower()

    if provider == "deepseek":
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY is missing.")

        return (
            OpenAI(
                api_key=api_key,
                base_url="https://api.deepseek.com",
            ),
            "deepseek-chat",
        )

    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing.")

        model = os.getenv("OPENAI_MODEL")
        if not model:
            raise ValueError("OPENAI_MODEL is missing.")

        return OpenAI(api_key=api_key), model

    raise ValueError(
        f"Unsupported provider: {provider}. "
        "Choose deepseek or openai."
    )


def ask_llm(provider: str, prompt: str) -> str:
    client, model = get_client(provider)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are DevAgent, a helpful AI assistant "
                    "for software developers."
                ),
            },
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content or ""
