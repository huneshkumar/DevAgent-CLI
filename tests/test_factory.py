
from unittest.mock import Mock

import pytest

from devagent.providers import factory


def test_deepseek_provider_is_selected(monkeypatch):
    fake_provider = Mock()
    monkeypatch.setattr(
        factory, "DeepSeekProvider", lambda: fake_provider
    )

    result = factory.get_provider("deepseek")

    assert result is fake_provider


def test_openai_provider_is_selected(monkeypatch):
    fake_provider = Mock()
    monkeypatch.setattr(
        factory, "OpenAIProvider", lambda: fake_provider
    )

    result = factory.get_provider("openai")

    assert result is fake_provider


def test_unsupported_provider_raises_error():
    with pytest.raises(ValueError, match="Unsupported provider"):
        factory.get_provider("unsupported")
