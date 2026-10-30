from pathlib import Path

import pytest

from devagent.tools import file_tools


def test_write_file_when_approved(tmp_path, monkeypatch):
    monkeypatch.setattr(
        file_tools,
        "execute_with_approval",
        lambda action, **kwargs: (action() or True),
    )

    result = file_tools.write_file(
        tmp_path,
        "hello.txt",
        "Hello from DevAgent",
    )

    assert result is True
    assert (tmp_path / "hello.txt").read_text() == "Hello from DevAgent"


def test_write_file_when_rejected(tmp_path, monkeypatch):
    monkeypatch.setattr(
        file_tools,
        "execute_with_approval",
        lambda *args, **kwargs: False,
    )

    result = file_tools.write_file(
        tmp_path,
        "hello.txt",
        "Hello from DevAgent",
    )

    assert result is False
    assert not (tmp_path / "hello.txt").exists()


def test_write_file_rejects_path_outside_workspace(tmp_path):
    with pytest.raises(ValueError, match="inside the workspace"):
        file_tools.write_file(
            tmp_path,
            "../outside.txt",
            "This should not be written",
        )