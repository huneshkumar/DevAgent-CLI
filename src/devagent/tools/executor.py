from pathlib import Path
from typing import Callable

from devagent.tools.approval import request_approval


def execute_with_approval(
    action: Callable,
    action_name: str,
    description: str,
) -> bool:
    approved = request_approval(action_name, description)

    if not approved:
        print("Execution cancelled.")
        return False

    action()
    print("Execution completed.")
    return True
