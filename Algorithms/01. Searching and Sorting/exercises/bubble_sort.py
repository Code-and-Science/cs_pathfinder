from performance_graphing_bubble import (
    analyze_bubble_sort_performance,
    plot_bubble_sort_performance,
    print_bubble_sort_results,
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


if __name__ == "__main__":
    bubble_sizes = [10, 100, 1_000, 10_000]
    bubble_times = analyze_bubble_sort_performance(bubble_sizes, bubble_sort)
    plot_bubble_sort_performance(bubble_sizes, bubble_times)
    print_bubble_sort_results(bubble_sizes, bubble_times)
