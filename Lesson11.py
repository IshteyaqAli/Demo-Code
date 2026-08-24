# Tupples in python
T1 = (1, 2, 3, 4, 5) # It's a tuple of integers
T2 = (1, "hello", 3.4, True) # It's a tuple of mixed data types
# Now to make a tuple with one element we need to add a comma after the element
T3 = (1,) # It's a tuple with one element
print(type(T3)) # It prints the type of class :- <clas tuple>
T4 = tuple("Gujarat")
print(T4) # We get output as : ('G', 'u', 'j,....)
T5 = tuple([1,2,3]) # It's a tuple from a list
                    # It's output is: (1,2,3)

# Now how to access the items from tuple

print(T1[0]) # Output : 1
print(T1[:4])  # Output : (1,2,3,4)
# It works and operates mostly as lists
# The difference is Tuples will not be changed once created
# Tuples are immutable & Lists are mutable

del T1
print(T1) # It will throw an error as it is deleted
del T1[0] # We cannot delete a single entity as we cannot edit tuples once built

# Operation & Functions of tuples :- Mostly same as Lists

# Tuples are read only data type



