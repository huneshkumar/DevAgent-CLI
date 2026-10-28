
from devagent.providers.base import LLMProvider
from devagent.providers.deepseek import DeepSeekProvider
from devagent.providers.openai_provider import OpenAIProvider


def get_provider(provider_name: str) -> LLMProvider:
    if provider_name == "deepseek":
        return DeepSeekProvider()

    if provider_name == "openai":
        return OpenAIProvider()

    raise ValueError(f"Unsupported provider: {provider_name}")
