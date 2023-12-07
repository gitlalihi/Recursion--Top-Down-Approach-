#Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...
def sum_of_positive_integers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_positive_integers(n - 2)


n = int(input("Enter a positive integer (n): "))


if n > 0:
    result = sum_of_positive_integers(n)
    print(f"The sum of positive integers in the sequence is: {result}")
else:
    print("Please enter a positive integer.")
