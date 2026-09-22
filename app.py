def greet(name):
    if name is None:
        return "Hello, World!"
    return f"Hello, {name}!"


def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    print(greet("CI/CD"))