def farewell(name):
    """Return a farewell string for the given name."""
    if not name:
        return "Goodbye, World!"
    return f"Goodbye, {name}!"


def shout_farewell(name):
    """Return an uppercase farewell."""
    return farewell(name).upper()


if __name__ == "__main__":
    print(farewell("Claude"))
