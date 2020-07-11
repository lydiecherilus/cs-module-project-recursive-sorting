# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # check base case
    if start > end:
        return -1
    else: 
        # target is at the middle, return target
        midpoint = (start + end) // 2
        if target == arr[midpoint]:
            return midpoint
        # target is smaller than the midpoint, the element after midpoint is the new start
        elif target > arr[midpoint]:
            return binary_search(arr, target, midpoint+1, end)
        else:
            # target is bigger than midpoint, the element before midpoint is the new end
            target < arr[midpoint]
            return binary_search(arr, target, start, midpoint-1)
 
array1 =  [1, 3, 34, 56, 78, 456]
print(binary_search(array1, 455, 0, len(array1)))
 
array2 =  [1, 3, 5, 6, 8, 155]
print(binary_search(array2, 155, 0, len(array2)))

array3 =  [-101, -98, -57, 2, 20, 30, 49]
print(binary_search(array3, 2, 0, len(array3)))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
# Your code here
    pass