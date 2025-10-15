import sys
import time

import pytest


# Funktionen, die getestet werden sollen
def add_correct(a, b):
    return a + b


def add_with_bug(a, b):
    return [a - b]  # Hier ist der Bug: sollte 'a + b' sein, nicht '[a - b]'


def test_add_correct():
    result = add_correct(3, 5)
    assert result == 8
    assert type(result) == int


def test_add_correct_datatype():
    result = add_correct(3, 5)
    assert type(result) == int


def test_add_with_bug():
    result = add_with_bug(3, 5)
    assert result == 8


@pytest.mark.parametrize("test_input, expected", [((3, 5), 8), ((6, 9), 15)])
def test_add_with_bug_with_parameter(test_input, expected):
    result = add_with_bug(test_input[0], test_input[1])
    assert result == expected


skip_on_windows = pytest.mark.skipif(sys.platform == "win32", reason="Nicht auf Windows ausführen")
skip_on_non_windows = pytest.mark.skipif(
    sys.platform != "win32", reason="Nur auf Windows ausführen"
)


@skip_on_windows
def test_add_correct_skip_on_windows():
    result = add_correct(3, 5)
    assert result == 8


@skip_on_non_windows
def test_add_correct_skip_on_not_windows():
    result = add_correct(3, 5)
    assert result == 8


@pytest.mark.slow
def test_add_correct_slow():
    result = add_correct(3, 5)
    time.sleep(5)  # Simuliert eine langsame Operation
    assert result == 8
