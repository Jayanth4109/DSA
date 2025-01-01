''' 
You are given an array arr(0-based indexing). The size of the array is given by n. You need to delete an element at given index and modify given array. The arr[i] of array is initially set to i+1.
Deletion means you need to shift all the elements after that index to the left by 1 position and set the last element as zero.

Example :

Input:
n = 5
index = 0
Output: 
2 3 4 5 0

'''
def deleteFromList(l,idx):
    n=len(l)
    for i in range(idx,n-1):
        l[i]=l[i+1]
    l[n-1]=0
    return l

Sample_List=[1,2,3,4,5,6,7,8,9]
x=5

print(deleteFromList(Sample_List,x))