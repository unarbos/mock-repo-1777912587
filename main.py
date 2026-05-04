"""Entry point for the mock app."""


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"


def main() -> None:
    print(greet("world"))


if __name__ == "__main__":
    main()
