def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

# Example usage:
num = int(input("Enter a number: ")) # 22
if is_prime(num):
    print(f"{num} is a prime number.") 
else:
    print(f"{num} is not a prime number.") # 22 is not a prime number
