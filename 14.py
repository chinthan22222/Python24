def linear_search(arr, target):
    """
    Perform linear search on an array.

    Parameters:
    arr (list): The list to search through.
    target: The element to search for.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
arr = [2, 3, 4, 10, 40]
target = 10
result = linear_search(arr, target)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")