import pytest

from src.decorators import log

# def division_numbers(a, b):
#    """Функция для отработки ошибок декоратора log"""
#    return a / b


def test_decorators_log(capsys):
    """Проверка отработки функции"""

    @log("logs.txt")
    def division_numbers(a, b):
        return a / b

    print(division_numbers(10, 5))
    captured = capsys.readouterr()
    assert str(captured.out) == (
        "--> Function: test_decorators_log.<locals>.division_numbers started OK!; " "result: (2.0)\n" "\n" "None\n"
    )


def test_decorators_log1(capsys):
    """Проверка отработки ошибки вычисления"""

    @log("logs.txt")
    def division_numbers(a: float, b: float):
        return a / b

    print(division_numbers(10, 0))
    captured = capsys.readouterr()
    assert str(captured.out) == (
        "(10, 0)\n"
        "--> Function: test_decorators_log1.<locals>.division_numbers started-> "
        "ERROR!: division by zero  при входных данных: (10, 0), {}\n"
        "\n"
        "None\n"
    )


def test_decorators_log2(capsys):
    """Проверка отработки пустого значения"""

    @log("logs.txt")
    def division_numbers(a, b):
        return a / b

    print(division_numbers())
    captured = capsys.readouterr()
    assert str(captured.out) == (
        "()\n"
        "--> Function: test_decorators_log2.<locals>.division_numbers started-> "
        "ERROR!: test_decorators_log2.<locals>.division_numbers() missing 2 required "
        "positional arguments: 'a' and 'b'  при входных данных: (), {}\n"
        "\n"
        "None\n"
    )
