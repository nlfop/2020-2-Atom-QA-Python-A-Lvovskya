import pytest
import random


@pytest.mark.parametrize('i', list(range(-1, 2, 1)))
def test_int_param(i):
    if i == 0:
        assert bool(i) is False
    else:
        assert bool(i) is True


listik = ['0', '1', 'A']


@pytest.mark.parametrize('i', list(range(3)))
def test_list_param(i):
    assert bool(listik[i]) is True


set_of_something = {-1, 0, 1}
a = set()


@pytest.mark.parametrize('i', list(range(5)))
def test_set_param(i):
    a.add(i)
    if i < 2:
        assert (a < set_of_something) is True
    else:
        assert (a < set_of_something) is False


di = {a: a for a in range(3)}


@pytest.mark.parametrize('i', list(range(3)))
def test_dict_param(i):
    assert di[i] != 9


@pytest.mark.parametrize('i', list(i for i in 'ri'))
def test_string_param(i):
    with pytest.raises(ValueError):
        int(i)
