import pytest
import random


def test_string3():
    line = 'Hello'
    assert line.isdigit() is False


def test_string4():
    line = 'error'
    assert line[3] != 'e'


def test_string5():
    line = 'error'
    with pytest.raises(ValueError):
        float(line[1])