import sys
from unittest.mock import Mock

import pytest
from openai import AuthenticationError

import devagent.main as main_module


def test_main_prints_provider_response(monkeypatch, capsys):
    fake_provider = Mock()
    fake_provider.generate.return_value = "Hello from DevAgent"

    monkeypatch.setattr(main_module, "get_provider", lambda _: fake_provider)
    monkeypatch.setattr(
        sys, "argv",
        ["devagent", "--provider", "deepseek", "Say hello"],
    )

    main_module.main()

    output = capsys.readouterr().out
    assert "Hello from DevAgent" in output
    assert "deepseek" in output
    fake_provider.generate.assert_called_once_with("Say hello")


def test_main_handles_invalid_configuration(monkeypatch, capsys):
    def raise_config_error(_):
        raise ValueError("API key is missing")

    monkeypatch.setattr(main_module, "get_provider", raise_config_error)
    monkeypatch.setattr(
        sys, "argv",
        ["devagent", "--provider", "deepseek", "Say hello"],
    )

    with pytest.raises(SystemExit) as error:
        main_module.main()

    assert error.value.code == 1
    assert "Configuration error" in capsys.readouterr().out


def test_main_handles_authentication_error(monkeypatch, capsys):
    fake_provider = Mock()
    fake_provider.generate.side_effect = AuthenticationError(
        message="Invalid API key",
        response=Mock(status_code=401),
        body=None,
    )

    monkeypatch.setattr(main_module, "get_provider", lambda _: fake_provider)
    monkeypatch.setattr(
        sys, "argv",
        ["devagent", "--provider", "deepseek", "Say hello"],
    )

    with pytest.raises(SystemExit) as error:
        main_module.main()

    assert error.value.code == 1
    assert "Authentication failed" in capsys.readouterr().out
