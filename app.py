import os
import sys


def greet(name):
    if name==None:
        return "Hello, World!"
    return f"Hello, {name}!"


def add_numbers(a,b):
    result = a+b
    unused_variable = 42
    return result


if __name__ == "__main__":
    print(greet("CI/CD"))