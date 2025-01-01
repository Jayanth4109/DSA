Sample_List=[1,2,3,4,5,6,7,8,9,10]

# List properties:
Sample_List.append(11) # Append 11 to the list
print(Sample_List)

Sample_List.insert(0,0) # Insert 0 at the beginning of the list
print(Sample_List)

Sample_List.remove(0) # Remove 0 from the list
print(Sample_List)

Sample_List.pop() # Remove the last element from the list
print(Sample_List)

Sample_List.pop(0) # Remove the first element from the list
print(Sample_List)

Sample_List.reverse() # Reverse the list
print(Sample_List)

Sample_List.sort() # Sort the list
print(Sample_List)

# More List properties:
print("Length of the list: ",len(Sample_List))

print("Maximum value in the list: ",max(Sample_List))

print("Minimum value in the list: ",min(Sample_List))

print("Sum of the list: ",sum(Sample_List))

print("Index of 5 in the list: ",Sample_List.index(5))

print("Count of 5 in the list: ",Sample_List.count(5))

# List slicing:

print("First 5 elements of the list: ",Sample_List[:5])

print("Last 5 elements of the list: ",Sample_List[-5:])

print("Elements from 3rd to 7th index: ",Sample_List[3:8])

print("Elements from 3rd to 7th index with step 2: ",Sample_List[3:8:2])

print("Elements from 3rd to 7th index with step 2 in reverse order: ",Sample_List[7:2:-2])

# List comprehension:

# List of squares of numbers from 1 to 10
Squares=[i**2 for i in range(1,11)]
print("List of squares of numbers from 1 to 10: ",Squares)

# List of even numbers from 1 to 10
Even_Numbers=[i for i in range(1,11) if i%2==0]
print("List of even numbers from 1 to 10: ",Even_Numbers)

# List of odd numbers from 1 to 10
Odd_Numbers=[i for i in range(1,11) if i%2!=0]
print("List of odd numbers from 1 to 10: ",Odd_Numbers)

# List of squares of even numbers from 1 to 10
Squares_of_Even_Numbers=[i**2 for i in range(1,11) if i%2==0]
print("List of squares of even numbers from 1 to 10: ",Squares_of_Even_Numbers)

# List of squares of odd numbers from 1 to 10
Squares_of_Odd_Numbers=[i**2 for i in range(1,11) if i%2!=0]
print("List of squares of odd numbers from 1 to 10: ",Squares_of_Odd_Numbers)

