import unittest
from binary_search import (
    binary_search_iterative,
    binary_search_recursive,
)
import random


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        print(f"This is our sorted list for testing: {self.sorted_list}")

    def test_existing_element(self):
        target = 11
        expected_index = 5
        iterative_result = binary_search_iterative(self.sorted_list, target)
        recursive_result = binary_search_recursive(self.sorted_list, target)

        print(f"Searching for {target} in the list:")
        print(f"Iterative search result: {iterative_result}")
        print(f"Recursive search result: {recursive_result}")

        self.assertEqual(iterative_result, expected_index)
        self.assertEqual(recursive_result, expected_index)

    def test_non_existing_element(self):
        target = 10
        expected_result = -1
        iterative_result = binary_search_iterative(self.sorted_list, target)
        recursive_result = binary_search_recursive(self.sorted_list, target)

        print(f"Searching for non-existing element {target} in the list:")
        print(f"Iterative search result: {iterative_result}")
        print(f"Recursive search result: {recursive_result}")

        self.assertEqual(iterative_result, expected_result)
        self.assertEqual(recursive_result, expected_result)

    def test_first_element(self):
        target = 1
        expected_index = 0
        iterative_result = binary_search_iterative(self.sorted_list, target)
        recursive_result = binary_search_recursive(self.sorted_list, target)

        print(f"Searching for first element {target} in the list:")
        print(f"Iterative search result: {iterative_result}")
        print(f"Recursive search result: {recursive_result}")

        self.assertEqual(iterative_result, expected_index)
        self.assertEqual(recursive_result, expected_index)

    def test_last_element(self):
        target = 19
        expected_index = 9
        iterative_result = binary_search_iterative(self.sorted_list, target)
        recursive_result = binary_search_recursive(self.sorted_list, target)

        print(f"Searching for last element {target} in the list:")
        print(f"Iterative search result: {iterative_result}")
        print(f"Recursive search result: {recursive_result}")

        self.assertEqual(iterative_result, expected_index)
        self.assertEqual(recursive_result, expected_index)

    def test_empty_list(self):
        empty_list = []
        target = 5
        expected_result = -1
        iterative_result = binary_search_iterative(empty_list, target)
        recursive_result = binary_search_recursive(empty_list, target)

        print(f"Searching for {target} in an empty list:")
        print(f"Iterative search result: {iterative_result}")
        print(f"Recursive search result: {recursive_result}")

        self.assertEqual(iterative_result, expected_result)
        self.assertEqual(recursive_result, expected_result)

    def test_single_element_list(self):
        single_element_list = [1]
        target = 1
        expected_index = 0
        iterative_result = binary_search_iterative(single_element_list, target)
        recursive_result = binary_search_recursive(single_element_list, target)

        print(f"Searching for {target} in a single-element list {single_element_list}:")
        print(f"Iterative search result: {iterative_result}")
        print(f"Recursive search result: {recursive_result}")

        self.assertEqual(iterative_result, expected_index)
        self.assertEqual(recursive_result, expected_index)

    def test_left_right_condition(self):
        two_element_list = [1, 2]
        target = 2
        expected_index = 1
        iterative_result = binary_search_iterative(two_element_list, target)
        recursive_result = binary_search_recursive(two_element_list, target)

        print(f"Searching for {target} in a two-element list {two_element_list}:")
        print(f"Iterative search result: {iterative_result}")
        print(f"Recursive search result: {recursive_result}")

        self.assertEqual(iterative_result, expected_index)
        self.assertEqual(recursive_result, expected_index)


if __name__ == "__main__":
    unittest.main()
