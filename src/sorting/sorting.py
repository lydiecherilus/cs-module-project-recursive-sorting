# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # merge the 2 arrays into a single one
    # Your code here
    count_arrA = 0 # current index for arrA
    count_arrB = 0 # current index for arrB
    #
    # for each index in the merged array elements
    # find the smallest firts item between aarA and ArrB
    # add that item to element at the given index and increment count_arrA/count_arraB
    for i in range(elements):
        if count_arrA >= len(arrA):
            # arrA is empty, arrB is not
            merged_arr[i] = arrB[count_arrB]
            count_arrB += 1

        elif count_arrB >= len(arrB):
            # arrB is empty, arrA is not
            merged_arr[i] = arrA[count_arrA]
            count_arrA += 1
           
        elif arrA[count_arrA] < arrB[count_arrB]:
            # arrA has the smallest element
            merged_arr[i] = arrA[count_arrA]
            count_arrA += 1
        else:
            arrA[count_arrA] >= arrB[count_arrB]
            # arrB has the smallest element
            merged_arr[i] = arrB[count_arrB]
            count_arrB += 1
    return merged_arr
 
array1 =  [1, 4, 6]
array2 =  [2, 3, 5]
print(merge(array1, array2))
 
 
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # while the array contains more than 1 element, split in half
    if len(arr) > 1:
        # split array in 2
        midpoint = len(arr) // 2
        left_arr = arr[0 :midpoint]
        right_arr = arr[midpoint:]
        # sort the split arrays
        left = merge_sort(left_arr)
        right = merge_sort(right_arr)
        # merge the sorted arrays
        arr = merge(left, right)

    return arr
 
array3 =  [21, 18, 4, 100, 8, 50, 7, 12, 9, 11]
print(merge_sort(array3))
 
 
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass
 
 
def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
 