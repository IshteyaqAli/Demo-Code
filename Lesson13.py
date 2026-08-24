# Dictionary in Python
# A dictionary is a collection of key-value pairs.
# Each key is unique and used to access its corresponding value.
# It is like a real-world dictionary:
# word -> meaning
# Example: "name" -> "Alice"
#
# Dictionaries are very useful when we want to store related data.
# They are mutable, which means we can change them after creation.
# Python dictionaries are ordered by default in Python 3.7+.

# ------------------------------------------------------------
# 1. Creating a dictionary
# ------------------------------------------------------------

student = {
    "name": "Alice",
    "age": 20,
    "course": "Python",
    "grade": "A"
}

print("Example 1: Creating a dictionary")
print(student)
print() 

# Another way to create a dictionary is using the dict() function.
# This is useful when you already have pairs of data.

student2 = dict(name="Bob", age=22, course="Java", grade="B")
print(student2)
print()

# ------------------------------------------------------------
# 2. Accessing dictionary values
# ------------------------------------------------------------

# We access values using their keys.
print("Example 2: Accessing values")
print(student["name"])       # Output: Alice
print(student["course"])     # Output: Python
print()

# If a key does not exist, using student["phone"] will raise an error.
# To avoid this, we use .get()
print("Using .get() to avoid KeyError")
print(student.get("phone", "Not available"))
print()

# ------------------------------------------------------------
# 3. Adding and updating values
# ------------------------------------------------------------

print("Example 3: Adding and updating values")
student["phone"] = "1234567890"   # Add a new key-value pair
print(student)

student["age"] = 21               # Update an existing key value
print(student)
print()

# ------------------------------------------------------------
# 4. Removing items
# ------------------------------------------------------------

# pop() removes and returns the value of a given key
removed_value = student.pop("phone")
print("Removed phone:", removed_value)
print(student)

# popitem() removes the last inserted key-value pair
student.popitem()
print("After popitem:", student)
print()

# del removes a key entirely
# del student["grade"]
# print(student)

# clear() removes all items from the dictionary
# student.clear()
# print(student)

# ------------------------------------------------------------
# 5. Important dictionary methods
# ------------------------------------------------------------

print("Example 4: Common dictionary methods")
print(student.keys())      # Returns all keys
print(student.values())    # Returns all values
print(student.items())     # Returns key-value pairs as tuples
print()

# Looping through keys, values, and items
print("Looping through keys:")
for key in student.keys():
    print(key)

print("\nLooping through values:")
for value in student.values():
    print(value)

print("\nLooping through items:")
for key, value in student.items():
    print(key, "->", value)
print()

# ------------------------------------------------------------
# 6. Checking if a key exists
# ------------------------------------------------------------

print("Example 5: Checking keys")
print("name" in student)      # True
print("phone" in student)     # False
print()

# ------------------------------------------------------------
# 7. Length of a dictionary
# ------------------------------------------------------------

print("Number of items in student:", len(student))
print()

# ------------------------------------------------------------
# 8. Nested dictionaries
# ------------------------------------------------------------

# A dictionary can contain another dictionary.
# This is useful for storing structured data.

students = {
    "student1": {
        "name": "Alice",
        "age": 20
    },
    "student2": {
        "name": "Bob",
        "age": 22
    }
}

print("Example 6: Nested dictionaries")
print(students["student1"]["name"])  # Alice
print(students["student2"]["age"])   # 22
print()

# ------------------------------------------------------------
# 9. Dictionary comprehension
# ------------------------------------------------------------

# Comprehension is a short and clean way to create dictionaries.
# Syntax: {key: value for item in iterable}

squares = {x: x * x for x in range(1, 6)}
print("Example 7: Dictionary comprehension")
print(squares)
print()

# ------------------------------------------------------------
# 10. Updating one dictionary with another dictionary
# ------------------------------------------------------------

info = {"city": "Delhi", "country": "India"}
student.update(info)
print("After update:", student)
print()

# ------------------------------------------------------------
# 11. Copying a dictionary
# ------------------------------------------------------------

student_copy = student.copy()
print("Copied dictionary:", student_copy)
print()

# ------------------------------------------------------------
# 12. Why dictionaries are useful
# ------------------------------------------------------------

# Dictionaries are best used when:
# - You need to store data with labels (keys)
# - You want fast lookup by key
# - You want to represent real-world objects like records
#
# Example: Student record
# {
#   "name": "Rahul",
#   "id": 101,
#   "marks": 95,
#   "city": "Mumbai"
# }

# ------------------------------------------------------------
# 13. Summary
# ------------------------------------------------------------

print("Summary:")
print("- Dictionary stores data in key-value pairs")
print("- Keys are unique")
print("- Values can be of any data type")
print("- We can add, update, delete, and access data easily")
print("- Very useful for storing structured data")

# ------------------------------------------------------------
# 14. Practice example
# ------------------------------------------------------------

# Create a dictionary of a mobile phone specification
phone = {
    "brand": "Samsung",
    "model": "Galaxy A14",
    "storage": "128GB",
    "color": "Black"
}

print("\nPractice example:")
print(phone["brand"])
print(phone.get("model"))
phone["battery"] = "5000mAh"
print(phone)

# End of tutorial
