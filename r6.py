#Python program to get the sum of a non-negative integer.
def sum_of_digits(n):
    if n < 0:
        return "Please enter a non-negative integer."
    str_n = str(n)
    digit_sum = 0
    for digit in str_n:
        digit_sum += int(digit)

    return digit_sum


number = int(input("Enter a non-negative integer: "))


result = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {result}")
