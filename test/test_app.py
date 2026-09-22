import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import greet, add_numbers


def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet(None) == "Hello, World!"


def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0