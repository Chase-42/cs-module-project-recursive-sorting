# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # If starting index is less than ending index, return -1 and exit
    if end < start: 
        return -1 
    else: 
        # Find the midpoint of array
        mid = (start + end) // 2 
        # If midpoint is the target return that
        if target == arr[mid]:
            return mid 
        # If target is less than mid move left
        elif target < arr[mid]:
            # return recursive call with midpoint -1 
            return binary_search(arr, target, start, mid-1)
        else: 
            # Else we move right, return recursive call with midpoint + 1
            return binary_search(arr, target, mid+1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here8
    pass