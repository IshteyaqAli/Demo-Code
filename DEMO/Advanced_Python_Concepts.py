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


# 3. Dictionary Comprehension (Short way to create dictionaries)
# Key-Value pairs ko ek line me generate karna.
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(f"Name Lengths: {name_lengths}")


# 4. Exception Handling (Error se bachne ke liye)
# Jab code me error aaye toh program crash na ho, isliye try-except use karte hain.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Zero se divide nahi kar sakte!")
finally:
    print("Ye hamesha chalega (Execution complete).")


# 5. Class & Object with Constructor
# Blueprint (Class) aur uska real instance (Object).
class Student:
    def __init__(self, name, age): # Constructor: Object bante hi call hota hai
        self.name = name
        self.age = age

    def show(self):
        print(f"Student: {self.name}, Age: {self.age}")

s1 = Student("Rahul", 20)
s1.show()


# 6. Inheritance (Virasat)
# Jab ek class dusri class ki properties ko use karti hai.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal): # Dog class Animal class ko inherit kar rahi hai
    def bark(self):
        print("Dog barks")

my_dog = Dog()
my_dog.speak() # Parent ka method
my_dog.bark()  # Khud ka method


# 7. Polymorphism (Ek naam, alag kaam)
# Same function name but different behavior.
class Cat:
    def sound(self): print("Meow")

class Cow:
    def sound(self): print("Moo")

def make_sound(animal):
    animal.sound()

make_sound(Cat())
make_sound(Cow())


# 8. Encapsulation (Data ko hide karna)
# Variable ko private banane ke liye double underscore (__) use karte hain.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private variable

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(f"Balance: {account.get_balance()}")
# print(account.__balance) # Ye error dega (Access restricted)


# 9. Abstraction (Details chupana)
# Sirf zaroori cheezein dikhana (Interface provide karna).
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side * self.side

sq = Square(5)
print(f"Area: {sq.area()}")


# 10. Decorator (Function ko modify karna)
# Bina original function ko change kiye usme extra functionality add karna.
def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# 11. Generator (Memory bachane ke liye)
# 'yield' use karke ek-ek karke value return karna.
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen)) # 1
print(next(gen)) # 2


# 12. Iterator (Looping mechanism)
# __iter__ aur __next__ use karke custom loop banana.
nums = [10, 20]
it = iter(nums)
print(next(it)) # 10


# 13. Closure (Function ke andar function)
# Nested function jo bahar wale variables ko yaad rakhta hai.
def outer_func(msg):
    def inner_func():
        print(f"Message is: {msg}")
    return inner_func

my_closure = outer_func("Hinglish Python!")
my_closure()
