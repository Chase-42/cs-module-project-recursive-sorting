# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Index pointers for each array 
    arrA_index = 0 
    arrB_index = 0
    merged_index = 0 

    # Start at [0] with arrA & arrB and find smallest value to add to merged_arr at [0]
    # Increment index from taken array and repeat 
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            merged_arr[merged_index] = arrA[arrA_index]
            arrA_index += 1 
        else: 
            merged_arr[merged_index] = arrB[arrB_index]
            arrB_index += 1 

        merged_index += 1

    # Loop through the remaining elements 
    while arrA_index < len(arrA):
        merged_arr[merged_index]  = arrA[arrA_index]
        arrA_index += 1 
        merged_index += 1 

    while arrB_index < len(arrB):
        merged_arr[merged_index]  = arrB[arrB_index]
        arrB_index += 1 
        merged_index += 1    

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # If greater than one then find middle 
    if len(arr) > 1:
        middle = (len(arr) // 2)
        # Grab each side (l & r) and recursively call merge_sort on it
        left_arr = merge_sort(arr[:middle])
        right_arr = merge_sort(arr[middle:])

        # Once each array is one element, call merge to put back together 
        return merge(left_arr, right_arr)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

