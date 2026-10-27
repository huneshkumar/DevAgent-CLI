import os
from dataclasses import dataclass


@dataclass(frozen=True)
class ProviderSettings:
    name: str
    api_key: str
    model: str
    base_url: str | None = None


def get_provider_settings(provider: str) -> ProviderSettings:
    provider = provider.lower()

    if provider == "deepseek":
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY is missing from .env")

        return ProviderSettings(
            name="deepseek",
            api_key=api_key,
            model=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
            base_url="https://api.deepseek.com",
        )

    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing from .env")

        model = os.getenv("OPENAI_MODEL")
        if not model:
            raise ValueError("OPENAI_MODEL is missing from .env")

        return ProviderSettings(
            name="openai",
            api_key=api_key,
            model=model,
        )

    raise ValueError(
        f"Unsupported provider: {provider}. "
        "Choose deepseek or openai."
    )