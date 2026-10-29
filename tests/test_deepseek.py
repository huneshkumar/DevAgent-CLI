
from types import SimpleNamespace
from unittest.mock import Mock

from devagent.providers import deepseek


def test_generate_returns_model_response(monkeypatch):
    settings = SimpleNamespace(
        api_key="test-key",
        base_url="https://example.com",
        model="test-model",
    )

    monkeypatch.setattr(
        deepseek, "get_provider_settings", lambda _: settings
    )

    fake_client = Mock()
    fake_client.chat.completions.create.return_value = (
        SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content="Hello from a mock")
                )
            ]
        )
    )

    monkeypatch.setattr(
        deepseek, "OpenAI", lambda **kwargs: fake_client
    )

    provider = deepseek.DeepSeekProvider()
    result = provider.generate("Say hello")

    assert result == "Hello from a mock"
    fake_client.chat.completions.create.assert_called_once()
