import unittest
import sys
import os
sys.path.append(os.getcwd())
from one_hot_encoder import fit_transform


class FitTransformTestCase(unittest.TestCase):
    def test_fit_transform_single_arg(self):
        result = fit_transform('apple', 'orange', 'banana')
        expected = [
            ('apple', [0, 0, 1]),
            ('orange', [0, 1, 0]),
            ('banana', [1, 0, 0])
        ]
        self.assertEqual(result, expected)

    def test_fit_transform_multiple_args(self):
        result = fit_transform(['cat', 'dog', 'cat'])
        expected = [
            ('cat', [0, 1]),
            ('dog', [1, 0]),
            ('cat', [0, 1])
        ]
        self.assertEqual(result, expected)

    def test_fit_transform_no_args(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_fit_transform_empty_string(self):
        result = fit_transform('')
        expected = [('', [1])]
        self.assertEqual(result, expected)

    def test_fit_transform_one_category(self):
        result = fit_transform('a', 'a', 'a', 'a')
        self.assertNotIn(('a', [0]), result)

    def test_fit_transform_duplicate_categories(self):
        result = fit_transform('cat', 'dog', 'cat', 'dog')
        expected = [
            ('cat', [0, 1]),
            ('dog', [1, 0]),
            ('cat', [0, 1]),
            ('dog', [1, 0])
        ]
        self.assertTrue(result == expected)


if __name__ == '__main__':
    unittest.main()
