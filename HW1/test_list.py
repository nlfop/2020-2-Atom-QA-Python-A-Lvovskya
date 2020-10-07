import pytest
import random


listik = ['0', '1', 'A']


def test_list3():
    assert bool(listik.count('p')) is False


def test_list4():
    with pytest.raises(ValueError):
        listik.index('we')


def test_list5():
    with pytest.raises(TypeError):
        int(listik)