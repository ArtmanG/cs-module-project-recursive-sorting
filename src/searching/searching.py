# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # ok so the problem is that we want to recursively make this function, call the function within itself
    
    
    # base case
    # so any case pretty much starts this as long as the section of the array has a start and end point, even if they are the same, only if the start is somehow higher than the end does it stop.
    while end >= start:
        # mid point set up
        mid = (start + end) // 2
        # to goal we are trying to hit. get the mid point to equal the target
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            # when the midpoint is larger than the target you are looking for you reset the end based on the current midpoint to cut out the unwanted half 
                #  binary_search(arr, target, start, end)
            return binary_search(arr, target, start, mid - 1)
            # call the binary_search again and start the process again from the top with the new end point
        else:
            # when the midpoint is smaller than the target you are looking for you reset the start based on the current midpoint to cut out the unwanted half 
                 # binary_search(arr, target, start, end)
            return binary_search(arr, target, mid + 1, end)
            # call the binary_search again and start the process again from the top with the new start point
    # if the target is not in the array, return -1
    return -1

# Example Test
# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# start = 0
# end = len(arr1) - 1
# binary_search(arr1, -8, start, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

