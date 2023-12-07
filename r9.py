#Python program to calculate the geometric sum of n-1.
def geometric_sum(a, r, n):
    if r == 1:
        return a * (n - 1)
    else:
        return a * (1 - r**(n-1)) / (1 - r)
a = float(input("Enter the first term (a): "))
r = float(input("Enter the common ratio (r): "))
n = int(input("Enter the number of terms (n): "))
result = geometric_sum(a, r, n)
print(f"The geometric sum of the first {n-1} terms is: {result}")

