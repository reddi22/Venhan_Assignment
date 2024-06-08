def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    lower = []
    higher = []
    equal = []

    for item in lst:
        if item < pivot:
            lower.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            higher.append(item)

    return quick_sort(lower) + equal + quick_sort(higher)


arr = [7, 18, 2, 15, 12, 8, 26, 1]
print(quick_sort(arr))  # Output: [1, 2, 7, 8, 12, 15, 18, 26]