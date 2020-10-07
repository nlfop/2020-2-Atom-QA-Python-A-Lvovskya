import pytest
import random


class TestData:
    def test_int_class_param(self):
        with pytest.raises(ZeroDivisionError):
             1 / 0

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
        assert ('monday' in table) is True
