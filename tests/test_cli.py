import os
import subprocess
import sys
from pathlib import Path

from chatgpt import cli


def test_greet_trims_whitespace():
    assert cli.greet("  Ada  ") == "Hello, Ada!"


def test_greet_defaults_to_placeholder():
    assert cli.greet("   ") == "Hello, there!"


def test_main_outputs_greeting(capsys):
    # Execute the CLI via the Python entry point for Windows-friendly testing
    exit_code = cli.main(["--name", "Tester"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "Hello, Tester!"


def test_command_line_script_invocation():
    """Integration check for the installed console script.

    Running the module with `python -m chatgpt.cli` should print the greeting and exit cleanly.
    """

    env = {**os.environ, "PYTHONPATH": str(Path(__file__).resolve().parents[1] / "src")}

    result = subprocess.run(
        [sys.executable, "-m", "chatgpt.cli", "--name", "CLI"],
        check=True,
        capture_output=True,
        text=True,
        env=env,
    )

    assert result.stdout.strip() == "Hello, CLI!"
