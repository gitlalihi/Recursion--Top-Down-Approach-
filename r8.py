#Python program to calculate the harmonic sum of n-1.
def harmonic_sum(n):
    result = 0.0
    for i in range(1, n):
        result += 1.0 / i
    
    return result


n = int(input("Enter a positive integer (n): "))


if n > 0:
    result = harmonic_sum(n)
    print(f"The harmonic sum of {n-1} is: {result}")
else:
    print("Please enter a positive integer.")
