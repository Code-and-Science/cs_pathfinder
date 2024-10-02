from performance_graphing_bubble import (
    analyze_sort_performance,
    plot_sort_performance,
    print_sort_results,
)


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


# Time complexity wise this algorithm takes quadratic time.
# Complexity of the outer loop is n, complexity of the inner loop is sort of 1/2n, (n * n/2) = n^2/2

# Worst case: Sorted List in descending order: O(n^2)
# Average case: Random List: O(n^2)
# Best case: Sorted List in Ascending order: O(n)

if __name__ == "__main__":
    sizes = [10, 100, 1000, 2000, 3000, 4000, 5000, 7000, 10000]
    times = analyze_sort_performance(sizes, bubble_sort)
    print_sort_results(sizes, times)
    plot_sort_performance(sizes, times)
