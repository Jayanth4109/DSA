#Finding largest element in a list

#Method1: Using max() function
Sample_List=[5,3,8,6,1,9,2,7]
print("Largest element in the list: ",max(Sample_List))

#Method2: Using sort() function
Sample_List.sort()
print("Largest element in the list: ",Sample_List[-1])

#Method3: Using loop
for i in range(1,len(Sample_List)):
    max=Sample_List[0]
    if Sample_List[i]>max:
        max=Sample_List[i]
    else:
        continue
print("Largest element in the list: ",max)