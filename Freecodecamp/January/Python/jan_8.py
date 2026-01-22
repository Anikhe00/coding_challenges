# Given an array of numbers, determine if the numbers are sorted in ascending order, descending order, or neither.

# If the given array is:

# In ascending order (lowest to highest), return "Ascending".
# In descending order (highest to lowest), return "Descending".
# Not sorted in ascending or descending order, return "Not sorted".

def is_sorted(arr):
    if arr == sorted(arr):
        return "Ascending"
    elif arr == sorted(arr, reverse = True):
        return "Descending"
    else:
        return "Not sorted"
    
print(is_sorted([1, 2, 3, 4, 5]))