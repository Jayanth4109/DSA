def immediateGreatest(arr,x):
    ans=float('inf')
    for i in arr:
        if i >x and i<ans:
            ans=i
    
    return ans if ans!=float('inf') else -1

Sample_List=[1,3,5,7,9,11,13]
x=12
print(immediateGreatest(Sample_List,x))



