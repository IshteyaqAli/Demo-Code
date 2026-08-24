# Lesson 14: Lambda Functions in Python

"""
SYNTAX:
lambda arguments : expression

DEEP DIVE (Hinglish Notes):
1. Anonymous (Bina naam wala): Lambda functions ka koi naam nahi hota, inhe bina 'def' keyword 
   ke define kiya jata hai.
2. Single Expression: Inme sirf ek hi expression (ek line ka logic) ho sakta hai. Isme loops 
   ya multiple statements use nahi kar sakte.
3. Implicit Return: Isme 'return' keyword likhne ki zarurat nahi hoti. Expression ka result 
   apne aap return ho jata hai.
4. Lexical Scoping: Ye apne surrounding scope (bahar wale variables) ko access kar sakte hain.
5. Best Use Case: Inhe tab use karna chahiye jab function ka kaam chhota ho aur use sirf 
   ek baar hi kaam me lena ho (jaise map(), filter(), or sorted() ke andar).
6. Debugging: Inhe debug karna thoda mushkil ho sakta hai kyunki error aane par stack trace 
   me sirf '<lambda>' likha aata hai, koi specific name nahi.
"""
from functools import reduce

# 1. Basic Lambda Function

# A lambda function that adds 10 to the input argument
add_ten = lambda x: x + 10
print(f"Basic Add: {add_ten(5)}") # Output: 15

# 2. Lambda with Multiple Arguments
# A lambda function that multiplies two numbers
multiply = lambda a, b: a * b
print(f"Multiplication: {multiply(10, 5)}") # Output: 50

# 3. Using Lambda with filter()
# filter() takes a function and a list, returning items that evaluate to True
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filtered (Evens): {even_numbers}") # Output: [2, 4, 6]

# 4. Using Lambda with map()
# map() applies the lambda function to every item in the list
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Mapped (Squared): {squared_numbers}") # Output: [1, 4, 9, 16, 25, 36]

# 5. Using Lambda with reduce()
# reduce() applies a rolling computation to sequential pairs of values
# Note: In Python 3, reduce is in the 'functools' module
product = reduce(lambda x, y: x * y, numbers)
print(f"Reduced (Product): {product}") # Output: 720 (1*2*3*4*5*6)

# 6. Using Lambda with sorted()
# Sorting a list of tuples based on the second value
points = [(1, 9), (4, 1), (5, -3), (10, 2)]
sorted_points = sorted(points, key=lambda x: x[1])
print(f"Sorted by second value: {sorted_points}")

# 7. Why use Lambda?
# They are best used inside other functions for short, one-time logic.
def my_multiplier(n):
    return lambda a : a * n

doubler = my_multiplier(2)
print(f"Function factory (Double 11): {doubler(11)}") # Output: 22


# Advanced Python Concepts - Quick Reference

# 1. Higher-Order Function (Bahar se function pass karna)
# Wo function jo dusre function ko as an argument leta hai.
def greet(name):
    return f"Hello, {name}!"

def display_message(func, name):
    # func yahan ek function hai jo bahar se aaya hai
    print(func(name))

display_message(greet, "Alice")


# 2. List Comprehension (Short way to create lists)
# Ek hi line me list banane ka asaan tareeka.
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers] 
print(f"Squares: {squares}")

# and without creeaating any list 
L1=[i**2 for i in range(10) if i%2!=0]
print(f"Odd squares: {L1}")


# 3. Dictionary Comprehension (Short way to create dictionaries)
# Key-Value pairs ko ek line me generate karna.
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(f"Name Lengths: {name_lengths}")

# another example of dictionary comprehension
L2=[1,2,3,4,5,6,7]
D2 = {item:item**2 for item in L2 if item%2==0}
print(f" A dictionary of even sqaures: {D2}")








