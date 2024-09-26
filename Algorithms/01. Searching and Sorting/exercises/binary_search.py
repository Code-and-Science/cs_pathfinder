import random
from performance_graphing_binary import run_performance_analysis


def generate_list_sequential(size):
    return list(range(size))


def binary_search_iterative(lst, target):
    if not lst:
        return -1

    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            if mid == 0 or lst[mid - 1] != target:
                return mid
            right = mid - 1
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(lst, target):
    if not lst:
        return -1

    def _recursive(left, right):
        if left > right:
            return -1

        mid = (left + right) // 2
        if lst[mid] == target:
            if mid == 0 or lst[mid - 1] != target:
                return mid
            return _recursive(left, mid - 1)
        elif lst[mid] < target:
            return _recursive(mid + 1, right)
        else:
            return _recursive(left, mid - 1)

    return _recursive(0, len(lst) - 1)


if __name__ == "__main__":
    sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
    algorithms = [binary_search_iterative, binary_search_recursive]
    algorithm_names = ["Iterative Binary Search", "Recursive Binary Search"]
    run_performance_analysis(
        algorithms, sizes, generate_list_sequential, algorithm_names
    )
