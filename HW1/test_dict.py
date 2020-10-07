import pytest
import random


di = {a: a for a in range(3)}


def test_dict3():
    dictionary = {1: False}
    assert dictionary[1] is False


def test_dict4():
    dict_small = {1: 1}
    assert dict_small[1] != 0


def test_dict5():
    with pytest.raises(TypeError):
        float(di)