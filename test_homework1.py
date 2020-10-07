import pytest
import random


class TestData:
    def test_int_class_param(self):
        with pytest.raises(ZeroDivisionError):
            assert 1 / 0

    def test_string_class(self):
        prosto = 'prosto'
        with pytest.raises(TypeError):
            prosto[2] = 'k'

    def test_list_class(self):
        s = list()
        assert bool(s) is False

    def test_set_class(self):
        num_set = {1, 2, 3}
        with pytest.raises(KeyError):
            num_set.remove(10)

    def test_dictionary_class(self):
        table = {'monday': 'nothing', 'tuesday': 'something'}
        'monday' in table


@pytest.mark.parametrize('i', list(range(3)))
def test_int_param(i):
    bool(i)


listik = ['p', 't', 'o']


@pytest.mark.parametrize('i', list(range(3)))
def test_list_param(i):
    listik[i]


set_of_something = {1, 2, 3}


@pytest.mark.parametrize('i', list(range(5)))
def test_set_param(i):
    set_of_something.discard(i)


di = {a: a for a in range(3)}


@pytest.mark.parametrize('i', list(range(3)))
def test_dict_param(i):
    assert di[i] != 9


@pytest.mark.parametrize('i', list(i for i in 'ri'))
def test_string_param(i):
    with pytest.raises(ValueError):
        int(i)


def test_list3():
    bool(listik.count('p'))


def test_list4():
    with pytest.raises(ValueError):
        listik.index('we')


def test_list5():
    with pytest.raises(TypeError):
        int(listik)


def test_set3():
    set_little = {1, 2}
    set_little.isdisjoint(set_of_something)


def test_set4():
    set_wrong = set()
    with pytest.raises(TypeError):
        set_wrong = {1, 2, 3, [3, 4, 5]}


def test_set5():
    s = set()
    assert bool(s) is False


def test_dict3():
    dictionary = {1: False}
    assert dictionary[1] is False


def test_dict4():
    dict_small = {1: 1}
    assert dict_small[1] != 0


def test_dict5():
    with pytest.raises(TypeError):
        float(di)


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






