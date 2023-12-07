# Python program to calculate the sum of a list of numbers.
def recursive_sum(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0]+recursive_sum(numbers[1:])
    
numbers_list = [1, 2, 3, 4, 5]
result = recursive_sum(numbers_list)
print(f"The sum of the list {numbers_list} is: {result}")    
    
