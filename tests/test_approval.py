from devagent.tools.approval import request_approval


def test_approval_granted(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")

    result = request_approval("delete_file", "Delete old.py")

    assert result is True


def test_approval_rejected(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")

    result = request_approval("delete_file", "Delete old.py")

    assert result is False


def test_invalid_input_then_approval(monkeypatch, capsys):
    responses = iter(["abc", "y"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    result = request_approval("delete_file", "Delete old.py")

    assert result is True
    assert "Invalid choice" in capsys.readouterr().out