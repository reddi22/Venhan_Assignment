def is_palindrome(string):
    reverse_str = ""
    for char in string:
        reverse_str = char + reverse_str
    return reverse_str == string

s = 'level'
output = is_palindrome(s)

if output:
    print(s, ' is a' + ' Palindrome') #output = level is a Palindrome
else:
    print(s, ' is not a' + ' Palindrome')
