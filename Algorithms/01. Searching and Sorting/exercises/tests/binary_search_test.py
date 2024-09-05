import unittest
from binary_search import (
    binary_search_iterative,
    binary_search_recursive,
)
import random
import unittest


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_binary_search_iterative(self):
        self.assertEqual(binary_search_iterative(self.test_list, 5), 4)
        self.assertEqual(binary_search_iterative([1, 2, 3], 2), 1)
        self.assertEqual(binary_search_iterative([], 5), -1)
        self.assertEqual(
            binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), -1
        )
        self.assertEqual(
            binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1
        )

    def test_binary_search_recursive(self):
        self.assertEqual(binary_search_recursive(self.test_list, 5), 4)
        self.assertEqual(binary_search_recursive([1, 2, 3], 2), 1)
        self.assertEqual(binary_search_recursive([], 5), -1)
        self.assertEqual(
            binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), -1
        )
        self.assertEqual(
            binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1
        )

    def test_edge_cases(self):

        self.assertEqual(binary_search_iterative([1, 1, 1, 1, 1], 1), 0)
        self.assertEqual(binary_search_recursive([1, 1, 1, 1, 1], 1), 0)

        self.assertEqual(binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 4)
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 4)

    def test_large_lists(self):
        large_list = list(range(10000))
        self.assertEqual(binary_search_iterative(large_list, 5000), 5000)
        self.assertEqual(binary_search_recursive(large_list, 5000), 5000)
