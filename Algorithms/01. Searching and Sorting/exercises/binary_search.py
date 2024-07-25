# Generate a list of one million elements, which are unique integers in the range of 0 to 10^6-1.
## Implement binary search using recursion
## Implement binary search using iteration
## Measure the time taken with timenow() function at the beginning and end of the search
## Use c-profile for performance analysis

## How long does it take when the numbers are not random but already sorted?


import random

def generate_list_random():
    return random.sample(range(1000000), 100)
random_list = generate_list_random()
print(f"Random list: {random_list}")


def generate_list_sequential():
    return list(range(100))
sequential_list = generate_list_sequential()
print(f"Sequential list: {sequential_list}")


target = 27


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
    print(f"Element found at index {result}.")
else:
    print("Element not found.")