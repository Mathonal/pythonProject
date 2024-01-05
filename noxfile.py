from pathlib import Path
from typing import List

import nox

MODULE_NAME = "template_python"

nox.options.reuse_existing_virtualenvs = True
nox.options.error_on_missing_interpreters = True
PYTHON_VERSIONS: List[str] = ["3.9"]

@nox.session(venv_backend="virtualenv", python=PYTHON_VERSIONS[-1])
def dev(session):
    """Set up an environment for a developer, which can be used by an IDE as all in one.

    Usage
    -----
    > nox -s dev
    """
    session.install("-r", "dev-requirements.txt")
    session.install("-e", ".")