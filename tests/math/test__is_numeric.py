import numpy as np

from util_functions.math import is_numeric


def test__int():
    int_value = 3
    assert is_numeric(int_value) is True


def test__float():
    float_value = 2.534
    assert is_numeric(float_value) is True


def test__np_int():
    int_value = np.int_(4)
    assert is_numeric(int_value) is True


def test__np_float():
    float_value = np.float_(4.234)
    assert is_numeric(float_value) is True


def test__string():
    string_value = "2"
    assert is_numeric(string_value) is False


def test__list():
    list_value = [1, 2, 3]
    assert is_numeric(list_value) is False


def test__boolean():
    boolean_value = True
    assert is_numeric(boolean_value) is True
