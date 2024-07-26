

import random
import cProfile
import time


# Use random number withing range as target
target = random.randint(1, 1_000)
def generate_list_sequential():
    return list(range(1_000))
sequential_list = generate_list_sequential()
def binary_search_iterative(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

result = binary_search_iterative(sequential_list, target)

if result != -1:
    print(f"Element search iterative found at index {result}.")
else:
    print("Element search iterative not found.")


def binary_search_recursive(list, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if list[mid] == target:
        return mid
    elif list[mid] < target:
        return binary_search_recursive(list, target, mid + 1, right)
    else:
        return binary_search_recursive(list, target, left, mid - 1)
    
result = binary_search_recursive(sequential_list, target, 0, len(sequential_list) - 1)

if result != -1:
    print(f"Element search recursive found at index {result}.")
else:
    print("Element search recursive not found.")


# Performance analysis

# Profile iterative search
print("\nIterative Binary Search:")
start_time = time.perf_counter()
cProfile.run("binary_search_iterative(sequential_list, target)")
end_time = time.perf_counter()
print(f"Total time: {end_time - start_time:.4f} seconds")

# Profile recursive search
print("\nRecursive Binary Search:")
start_time = time.perf_counter()
cProfile.run("binary_search_recursive(sequential_list, target, 0, len(sequential_list) - 1)")
end_time = time.perf_counter()
print(f"Total time: {end_time - start_time:.4f} seconds")

