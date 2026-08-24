# SETs in Python:
# Following are the 4 Rules of SETs:-
print(" 1- Sets do not allow duplicates\n" \
" 2- Sets have no indexing/Slicing It has Hashing \n" \
" 3- Sets dont allow mutable datatypes\n" \
" 4- Sets itself a mutable datatype")

# Create SEts

s1 = {} # its ouput will be : class 'dict'
s1 = set() # now it gives or creates an empty set
s2 = {"Hello",4.5,True}
print(s2)

s3 = {1,1,2,2,3,3} 
print(s3) # Output : {1,2,3} it won't allow duplicating

#s4 = {[1,2,3],"Hello"}
#print(s4) # it gives an error as list is itself a mutable datatype so it cant be in itself

# Hashing: Its 

# Access items

print(s1[0]) # it throw an error as it doesn't supports indexing
s5 = {1,2,3}
print(s5) # output : same
s5.add(4)  
print(s5) # output : {1,2,3,4} This proves that sets is mutable datatype

# Three ways of deleting: Delete, del, remove, pop
# all same as we learn them before

# sets Operations
# it cannot "concatenate" and cannot "multiply"
# but looping  and membership operatorrs are available

# Funtions
print(len(s5))
print(min(s5)) # min and max can be used only for same data
print(max(s5))
print(sum(s5))
print(sorted(s5)) # Output : [1,2,3,4] ouput is list 
print(sorted(s5,reverse=True)) # Output : [4,3,2,1]

s6 = {3,4,5}

print(s5.union(s6)) # Output : {1,2,3,4,5}
print(s5.intersection(s6)) # Output : {3,4}
print(s5.difference(s6)) # Output : {5}
print(s6.difference(s5)) # Output : {1,2}
# Such as we have "symmetric_differnce" "isdisjoint" "issubset" "issuperset"
 