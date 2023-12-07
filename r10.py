# Python program to calculate the value of 'a' to the power of 'b'.
def power(a, b):
    if b == 0:
        return 1
    
    else:
        return a * power(a, b - 1)


base = float(input("Enter the base (a): "))
exponent = int(input("Enter the exponent (b): "))


result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
