def greet(name):
    """Return a greeting string for the given name."""
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"


def shout(name):
    """Return an uppercase greeting."""
    return greet(name).upper()


if __name__ == "__main__":
    print(greet("Claude"))
