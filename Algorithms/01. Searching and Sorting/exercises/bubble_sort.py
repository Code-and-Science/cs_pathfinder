# generate unsorted list of random integers

# use same interface for different sorting algorithms:


# use matplot library for plotting test results


def bubble_sort(lst):
    n = len(lst)
    needs_sorting = False

    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                needs_sorting = True

        if not needs_sorting:
            break

    return lst


lst = [64, 34, 25, 12, 22, 11, 90]
sorted_lst = bubble_sort(lst)
print(f"Sorted list: {sorted_lst}")
