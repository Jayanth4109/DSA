''' 
Given an unsorted array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

'''

def rotateArr(arr, d):
    n = len(arr)
    if d>n:
        d = d % n  # Handle cases where d >= n
        
    arr[:] = arr[d:] + arr[:d]   # Concatenate and modify in-place

    return arr

Sample_List=[1,2,3,4,5]
x=3

print(rotateArr(Sample_List,x))