# Python program to find the greatest common divisor (GCD) of two integers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))


result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")

