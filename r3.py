#Python program to sum recursion lists
def recursive_sum(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += recursive_sum(element)
        else:
            total += element
    return total


nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]
result = recursive_sum(nested_list)
print(f"The sum of the nested list is: {result}")
