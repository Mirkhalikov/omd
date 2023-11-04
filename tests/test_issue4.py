import sys
import os
sys.path.append(os.getcwd())
from one_hot_encoder import fit_transform


def test_fit_transform_single_argument():
    result = fit_transform('a', 'b', 'c')
    expected = [('a', [0, 0, 1]), ('b', [0, 1, 0]), ('c', [1, 0, 0])]
    assert result == expected


def test_fit_transform_empty_argument():
    try:
        result = fit_transform()
    except TypeError as e:
        assert str(e) == 'expected at least 1 arguments, got 0'
    else:
        assert False, 'Expected TypeError to be raised'


def test_fit_transform_duplicate_arguments():
    result = fit_transform('a', 'b', 'c', 'a')
    expected = [('a', [0, 0, 1]), ('b', [0, 1, 0]),
                ('c', [1, 0, 0]), ('a', [0, 0, 1])]
    assert result == expected


def test_fit_transform_duplicate_categories():
    result = fit_transform('cat', 'dog', 'cat', 'dog')
    expected = [
        ('cat', [0, 1]),
        ('dog', [1, 0]),
        ('cat', [0, 1]),
        ('dog', [1, 0])
    ]
    assert result == expected
