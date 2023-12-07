#Python program to get the factorial of a non-negative integer.
def factorial(n):
    
    if n == 0:
        return 1
    
    else:
        return n * factorial(n - 1)


while True:
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            result = factorial(num)
            print(f"The factorial of {num} is: {result}")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
