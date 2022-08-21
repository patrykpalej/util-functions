import pytest
import pandas as pd
import numpy as np

from util_functions.math import gini_coefficient


def test__numeric_list():
    numeric_list = [1, 2, 3.5, 4, 5.1]
    expected_gini = 0.2615384615384615
    assert gini_coefficient(numeric_list) == expected_gini
    assert gini_coefficient(numeric_list, 3) == 0.262


def test__pandas_series():
    pandas_series = pd.Series([1, 2, 3.5, 4, 5.1])
    expected_gini = 0.2615384615384615
    assert gini_coefficient(pandas_series) == expected_gini
    assert gini_coefficient(pandas_series, 0) == 0


def test__numpy_array():
    numpy_array = np.array([1, 2, 3.5, 4, 5.1])
    expected_gini = 0.2615384615384615
    assert gini_coefficient(numpy_array) == expected_gini
    assert gini_coefficient(numpy_array, 1) == 0.3


def test__mixed_list():
    mixed_list = [1, '2', 3.5, 4, 5.1]
    with pytest.raises(TypeError, match="'collection' should .* numeric values"):
        gini_coefficient(mixed_list)


def test__invalid_precision():
    mixed_list = [1, 2, 3.5, 4, 5.1]
    with pytest.raises(TypeError, match="'precision' should be an integer"):
        gini_coefficient(mixed_list, 3.1)
