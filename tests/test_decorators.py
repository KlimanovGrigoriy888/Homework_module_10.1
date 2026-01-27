import os

from src.decorators import log

PATCH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src", "mylog.txt")

print(PATCH_TO_FILE)


@log(filename=None)
def my_function(x, y):
    return x + y


@log(filename=None)
def dev_function(x, y):
    return x / y


@log(filename=None)
def print_function():
    return "Я Функция"


def test_log(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_wrong_type(capsys):
    my_function(1, "3")

    captured = capsys.readouterr()
    assert captured.out == (
        "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '3'), " "{}\n"
    )


def test_log_wrong_divide(capsys):
    dev_function(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: division by zero. Inputs: (1, 0), {}\n"


def test_log_not_parameters(capsys):
    dev_function()
    captured = capsys.readouterr()
    assert (
        captured.out == "my_function error: dev_function() missing 2 required positional arguments: "
        "'x' and 'y'. Inputs: (), {}\n"
    )


def test_log_printing(capsys):
    print_function()
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
