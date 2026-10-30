from unittest.mock import Mock

from devagent.tools import executor


def test_approved_action_executes(monkeypatch):
    action = Mock()

    monkeypatch.setattr(
        executor,
        "request_approval",
        lambda *args: True,
    )

    result = executor.execute_with_approval(
        action,
        "write_file",
        "Create hello.txt",
    )

    assert result is True
    action.assert_called_once()


def test_rejected_action_does_not_execute(monkeypatch):
    action = Mock()

    monkeypatch.setattr(
        executor,
        "request_approval",
        lambda *args: False,
    )

    result = executor.execute_with_approval(
        action,
        "write_file",
        "Create hello.txt",
    )

    assert result is False
    action.assert_not_called()
