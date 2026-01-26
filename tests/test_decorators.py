from fileinput import filename

import pytest
from mypy.types import NoneTyp

from src.decorators import log
import os

PATCH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src", "mylog.txt")

print(PATCH_TO_FILE)

@log(filename = None)
def my_function(x, y):
        return x + y


@log(filename = None)
def dev_function(x, y):
        return x / y


def test_log(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == 'my_function ok\n'


def test_log_wrong_type(capsys):
    my_function(1, "3")
    captured = capsys.readouterr()
    assert captured.out  == "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '3'), {}\n"


def test_log_wrong_divide(capsys):
    dev_function(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: division by zero. Inputs: (1, 0), {}\n"