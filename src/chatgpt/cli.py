"""Command-line entry point for the Chatgpt demo app."""

from __future__ import annotations

import argparse

DEFAULT_NAME = "there"


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI."""
    parser = argparse.ArgumentParser(description="Simple greeting CLI")
    parser.add_argument(
        "-n",
        "--name",
        default=DEFAULT_NAME,
        help="Name to greet (default: %(default)s)",
    )
    return parser


def greet(name: str) -> str:
    """Return a friendly greeting for the provided name."""
    clean_name = name.strip() or DEFAULT_NAME
    return f"Hello, {clean_name}!"


def main(argv: list[str] | None = None) -> int:
    """Parse CLI arguments and print the greeting."""
    parser = build_parser()
    args = parser.parse_args(argv)
    message = greet(args.name)
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
