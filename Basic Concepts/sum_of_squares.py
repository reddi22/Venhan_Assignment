def sum_of_squares(nums_list):
    total = 0
    for i in nums_list:
        total += i ** 2
    return total

# Example usage:
nums_list = [1, 2, 3, 4, 5, 6, 7]
output = sum_of_squares(nums_list)
print(output)  # Output: 140