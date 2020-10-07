import pytest
import random


def test_int3():
    i = 0
    assert type(i) == int


def test_int4():
    line = 'error'
    i = 23
    with pytest.raises(TypeError):
        i > line


def test_int5():
    i = 3+4
    assert i == 7