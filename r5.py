#Python program to solve the Fibonacci sequence using recursion
def fibonacci(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


while True:
    try:
        terms = int(input("Enter the number of Fibonacci terms to generate: "))
        if terms < 0:
            print("Please enter a non-negative integer.")
        else:
           
            print("Fibonacci sequence:")
            for i in range(terms):
                print(fibonacci(i), end=" ")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
