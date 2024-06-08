def find_duplicates(arr):
    duplicates = []
    count_map = {}

    for num in arr:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    for num, count in count_map.items():
        if count > 1:
            duplicates.append(num)

    return duplicates

# Example usage
arr = [1, 2, 3, 4, 5, 2, 7, 8, 3, 10, 1]
duplicates = find_duplicates(arr)
print(duplicates)   #output : [1, 2, 3]
