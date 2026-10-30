from pathlib import Path

from devagent.tools.executor import execute_with_approval


def write_file(workspace: Path, filename: str, content: str) -> bool:
    workspace = workspace.resolve()
    target = (workspace / filename).resolve()

    if not target.is_relative_to(workspace):
        raise ValueError("File path must stay inside the workspace.")

    def perform_write():
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    return execute_with_approval(
        action=perform_write,
        action_name="write_file",
        description=f"Write to {target}",
    )
