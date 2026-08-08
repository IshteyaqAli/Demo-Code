# String in python
# Strings are the sequence of characters. In python, strings are represented by str class. Strings are immutable in python. Strings are enclosed in single quotes or double quotes. Strings can be created by using single quotes, double quotes or triple quotes. Triple quotes are used to create multi-line strings.
# Strings can be concatenated by using + operator.
#  Strings can be repeated by using * operator.
#  Strings can be indexed and sliced.
#  Strings can be formatted by using format() method.
#  Strings can be converted to upper case, lower case, title case, etc.
#  by using upper(), lower(), title(), etc. methods. 
# Strings can be stripped of whitespace by using strip() method. 
# Strings can be split into a list of substrings by using split() method. 
# Strings can be joined into a single string by using join() method. 
# Strings can be searched for a substring by using find() method. 
# Strings can be replaced by using replace() method.

# Concept of indexing
s = "Hello, World!"
print(s[0])  # Output: H
print(s[7])  # Output: W
print(s[-1])  # Output: !

# Concept of slicing
print(s[0:4])  # Output: Hell
print(s[0:5])  # Output: Hello
print(s[2:7])  # Output: llo, W
print(s[:5])  # Output: Hello
print(s[:])  # Output: Hello, World!
print(s[2:7:2])  # Output: lo as we are taking every 2nd character from index 2 to 7

# Editing and deleting in strings
s = "Hello, World!"
# Editing strings
s=s.replace("world","Python") # Output: Hello, Python!
print(s) # Output: Hello, Python!
# Deleting strings
s = "Hello, World!"
s = s.replace("World!", "") # Output: Hello,
print(s) # Output: Hello,
#OR
s="Hello, World!"
del s # Output: NameError: name 's' is not defined
print(s) # Output: NameError: name 's' is not defined


# Operations in strings

print("Hello" + " " + "World!") # Output: Hello World! it's concatenation of strings

print("Hello " * 3) # Output: Hello Hello Hello it's repetition of strings

s="hello"
"h" in s # Output: True it's checking if "h" is present in s or not
print("h" in s) # Output: True it's checking if "h" is present  
"H" not in s # Output: True it's checking if "H" is not present in s or not
print("H" not in s) # Output: True it's checking if "H" is not present in s or not
