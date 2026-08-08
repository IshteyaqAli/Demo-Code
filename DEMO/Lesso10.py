# List in  python

L1 = [1, 2, 3, 4, 5] # It's a list of integers
L2 = [1,"hello",3.4,True] # It's a list of mixed data types

# multidimensional list
#2D list
L3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # It's a 2D list 
#3D list
L4 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]] # It's a 3D list

L5 = list("Hello") # It's output will be ['H', 'e', 'l', 'l', 'o'] # It converts a string into a list of characters

# Editing and accessing in lists
L1[0] # It's output will be 1 # It accesses the first element of the list
L1[0] = 10 # It changes the first element of the list to 10

L3[2][1] # It's output will be 8 # It accesses the second element of the third list in the 2D list  
L4[1][0][2] # It's output will be 9 # It accesses the third element of the first list in the second list of the 3D list

# append/extend/insert
L1.append(6) # It adds 6 to the end of the list L1
L1.extend([7, 8, 9]) # It adds multiple items like 7, 8, 9 to the end of the list L1
L1.insert(0, 0) # It adds 0 to the beginning of the list L1

# Methods to remove items from a list
# del/remove/pop/clear
del L2[0] # It removes the first element from the list L2
del L2[:3] # It removes the first three elements from the list L2
L2.remove("hello") # It removes the first occurrence of "hello" from the list L2
L2.pop() # It removes the last element from the list L2
L2.pop(0) # It removes the first element from the list L2
L2.clear() # It removes all elements from the list L2

# Operations in  lists
L = [1,2,3,4]
print(L+L1) # It's output will be [1, 2, 3, 4, 10, 2, 3, 4, 5, 6, 7, 8, 9] # It concatenates two lists
print(L*3) # It's output will be [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4] # It repeats the list three times

for i in L:
    print(i) # It prints each element of the list L
    
