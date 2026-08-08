# some common functions in python
# Capitalize/Title/Upper/Lower/Swapcase

"it's a testing statement".capitalize() # It's output : "It's a testing statement" # It capitalizes the first character of the string
"it's a testiing statement".title() # It's output is : "It's A Testing Statement" # It capitalizes the first character of each word in the string
"it's a testing statement".upper() # It's output is : "IT'S A TESTING STATEMENT" # It converts all the  
"it's a testing statement".lower() # It's output is : "it's a testing statement" #
"it's a testing statement".swapcase() # It's output is : "IT'S A TESTING STATEMENT" 

#Count/Find/Index
"it's a testing statement".count("t") # It's output is : 5 # It counts the number of occurrences of the substring in the string
"it's a testing statement".index("t") # It's output is : 1 # It returns the index of the first occurrence of the substring in the string
"it's a testing statement".find("t") # It's output is : 1 # It returns the index of the first occurrence of the substring in the string

# endswith/startswith
"it's a  testing statement".endswith("statement") # It's output is : True # It checks if the string ends with the specified suffix
"it's a testing statement".startswith("it's") # It's output is : True # It checks if the string starts with the specified prefix

# format
"My name is {} and I am {} years old".format("Ishteyaq",20) # It's output is : "My name is Ishteyaq and I am 20 years old" # It formats the string by replacing the placeholders with the specified values
"My name is {0} and I am {1} years old".format("Ishteyaq",20) # It's output is : "My name is Ishteyaq and I am 20 years old" # It formats the string by replacing the placeholders with the specified values

# isalnum/isalpha/isdecimal/isdigit/isidentifier
"Hello123".isalnum() # It's output is : True # It checks if all characters in the string are alphanumeric
"Hello".isalpha() # It's output is : True # It checks if all characters in the string are alphabetic
"123".isdecimal() # It's output is : True # It checks if all characters in the string are decimal
"123".isdigit() # It's output is : True # It checks if all characters in the string are digits
"my_var".isidentifier() # It's output is : True # It checks if the string is a valid identifier

# Split/Join
"Hello, World!".split(",") # It's output is : ['Hello', ' World!'] # It splits the string into a list of substrings based on the specified delimiter
" ".join(["Hello", "World!"]) # It's output is : "Hello World!" # It joins the list of strings into a single string with the specified delimiter

# Replace
"Hello, World!".replace("World", "Python") # It's output is : "Hello, Python!" # It replaces all occurrences of the specified substring with the new substring

# Strip
"   Hello, World!   ".strip() # It's output is : "Hello, World!" # It removes leading and trailing whitespace from the string
"   Hello, World!   ".lstrip() # It's output is : "Hello, World!   " # It removes leading whitespace from the string
"   Hello, World!   ".rstrip() # It's output is : "   Hello, World!" # It removes trailing whitespace from the string