import os
from typing import List


class GitContext(object):
    """Temporarily force GIT_TERMINAL_PROMPT to 0 for private repositories."""
    V = "GIT_TERMINAL_PROMPT"

    def __init__(self, repo: str, private_repos: List[str]):
        self.value = None
        self.save_value = repo in private_repos

    def __enter__(self):
        if self.save_value:
            self.value = os.environ.get(__class__.V, None)
            os.environ[__class__.V] = "0"

    def __exit__(self, exception_type, exception_value, traceback):
        if self.save_value:
            if self.value:
                os.environ[__class__.V] = self.value
            else:
                del os.environ[__class__.V]
