import unittest
import random

from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_element(self):
        self.assertEqual(bubble_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(
            bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),
            [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9],
        )

    def test_list_with_duplicates(self):
        self.assertEqual(bubble_sort([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8])

    def test_large_random_list(self):
        random_list = [random.randint(1, 1000) for _ in range(1000)]
        sorted_list = sorted(random_list)
        self.assertEqual(bubble_sort(random_list), sorted_list)


if __name__ == "__main__":
    unittest.main()
