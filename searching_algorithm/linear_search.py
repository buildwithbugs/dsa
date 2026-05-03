def linear_search(arr, target):
    """
    Perform linear search on an array to find the target element.
    
    Args:
        arr: List of elements to search through
        target: Element to search for
        
    Returns:
        Index of target if found, -1 if not found
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    target = 3
    result = linear_search(arr, target)
    
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the array")