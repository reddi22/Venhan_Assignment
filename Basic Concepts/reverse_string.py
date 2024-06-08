def reverse_string(s: str) -> str:
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


input_string = "mango"
reversed_string = reverse_string(input_string)
print(reversed_string) #output: ognam