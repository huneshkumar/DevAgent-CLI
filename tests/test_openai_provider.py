
from types import SimpleNamespace
from unittest.mock import Mock

from devagent.providers import openai_provider


def test_generate_returns_model_response(monkeypatch):
    settings = SimpleNamespace(
        api_key="test-key",
        base_url=None,
        model="test-model",
    )

    monkeypatch.setattr(
        openai_provider,
        "get_provider_settings",
        lambda _: settings,
    )

    fake_client = Mock()
    fake_client.chat.completions.create.return_value = (
        SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content="Hello from OpenAI mock")
                )
            ]
        )
    )

    monkeypatch.setattr(
        openai_provider,
        "OpenAI",
        lambda **kwargs: fake_client,
    )

    provider = openai_provider.OpenAIProvider()
    result = provider.generate("Say hello")

    assert result == "Hello from OpenAI mock"
    fake_client.chat.completions.create.assert_called_once()
