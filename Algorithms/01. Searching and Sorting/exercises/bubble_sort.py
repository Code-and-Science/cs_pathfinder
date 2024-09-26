from performance_graphing_bubble import (
    analyze_bubble_sort_performance,
    plot_bubble_sort_performance,
    print_bubble_sort_results,
)


def bubble_sort_iterative(lst):
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


# Bubble Sort Performance Results:
# Size: 10, Time: 0.000006 seconds
# Size: 100, Time: 0.000208 seconds
# Size: 1000, Time: 0.025068 seconds
# Size: 10000, Time: 2.926782 seconds
# Size: 20000, Time: 11.645677 seconds
# Size: 30000, Time: 26.010972 seconds
# Size: 40000, Time: 48.194841 seconds
# Size: 50000, Time: 76.298721 seconds


def bubble_sort_recursive(lst):
    if len(lst) <= 1:
        return lst

    max_idx = lst.index(max(lst))
    left_part = bubble_sort_recursive(lst[:max_idx])
    right_part = bubble_sort_recursive(lst[max_idx + 1 :])

    return left_part + [lst[max_idx]] + right_part


# Bubble Sort Recursive Performance Results:
# Size: 10, Time: 0.000008 seconds
# Size: 100, Time: 0.000036 seconds
# Size: 1000, Time: 0.000432 seconds
# Size: 10000, Time: 0.004736 seconds
# Size: 20000, Time: 0.010177 seconds
# Size: 30000, Time: 0.018509 seconds
# Size: 40000, Time: 0.021627 seconds
# Size: 50000, Time: 0.026160 seconds


if __name__ == "__main__":
    bubble_sizes = [10, 100, 1_000, 10_000, 20_000, 30_000]
    bubble_times = analyze_bubble_sort_performance(bubble_sizes, bubble_sort)
    plot_bubble_sort_performance(bubble_sizes, bubble_times)
    print_bubble_sort_results(bubble_sizes, bubble_times)
