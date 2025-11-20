# Chatgpt

A beginner-friendly Python project scaffold. It includes a simple command-line entry point, 
testing and linting defaults, and instructions to get you running quickly even if you are new 
to coding.

## Quick start
1. **Install Python 3.10 or newer.**
2. **Create a virtual environment** in the project folder:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\\Scripts\\activate
   ```
3. **Install the project in editable mode with development tools**:
   ```bash
   pip install -e .[dev]
   ```

## Using the example CLI
After installation, you can run the packaged command-line script:
```bash
chatgpt --name "Ada"
```
It will print a friendly greeting. The logic lives in `src/chatgpt/cli.py`.

## Code layout
- `src/chatgpt/cli.py`: Main entry point and helper functions.
- `tests/`: Pytest-based unit tests to validate the CLI behavior.
- `pyproject.toml`: Project metadata plus tool configuration (packaging, linting, tests).
- `.gitignore`: Common Python ignores for virtual environments, build files, and editor cache.

## Developing
- **Run tests**:
  ```bash
  pytest
  ```
- **Run linting (Ruff)**:
  ```bash
  ruff check .
  ```
- **Format imports automatically**:
  ```bash
  ruff check --select I --fix .
  ```

## Next steps
- Add real application code inside `src/chatgpt/`.
- Expand tests in `tests/` to cover new features.
- Configure continuous integration (CI) to run `pytest` and `ruff` on every commit.
- Update this README with project-specific documentation as the codebase grows.
