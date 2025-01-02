'''
Given an array arr[] of size N containing positive integers and an integer X, find the element in the array which is smaller than X and closest to it.

'''

def immediateSmaller(arr,x):
        ans=0
        for i in arr:
            if i < x:
                if i> ans:
                    ans=i
                else:
                    pass
        
        if not ans:
            return -1
        else:
            return ans
        
Sample_List=[2,6,5,7,8,4,12,9]
x=10
print(immediateSmaller(Sample_List,x))