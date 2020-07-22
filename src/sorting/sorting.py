# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    num_elements = len(arrA) + len(arrB)
    merged_arr = [] * num_elements

    # Your code here
    # pointers for each separate array
    a = 0
    b = 0
    # while the pointers are less than the length of each array, there is something to add to the merged array.
    while a < len(arrA) and b < len(arrB):
        # if the value of arrA at index [a] is less than the arrB at index [b] run this 
        if arrA[a] < arrB[b]:
            # add the value of arrA at index [a]
            merged_arr.append(arrA[a])
            # then increase the pointer so it points to the next index
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    # at this point, we've merged in all of the elements from one of the arrays, but not the other 
    
    # check both arrays to see if the pointer is still in range of its array 
    if a < len(arrA):
        # arrA still has leftover elements, push them all to the merged array 
        merged_arr.extend(arrA[a:])

    if b < len(arrB):
        merged_arr.extend(arrB[b:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case: stop splitting the arrays in half when the arrays reach a length of 1 
    if len(arr) > 1:
    # otherwise, keep splitting them in half 
        left = merge_sort(arr[0 : len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2 : ])

        arr = merge(left, right)

    return arr

# Example Test
arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

