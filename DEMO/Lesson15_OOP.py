# OOP (Object-Oriented Programming) in Python
# ============================================================
# OOP ka matlab hai program ko objects ke around design karna.
# Object ke paas data (attributes) aur behaviour (methods) hota hai.
# Real-life example: Car ke attributes color, brand, speed ho sakte hain,
# aur methods start(), stop(), accelerate() ho sakte hain.
#
# OOP ke important concepts:
# - Class: object banane ka blueprint/template.
# - Object: class ka actual instance.
# - Encapsulation: data aur methods ko ek unit mein rakhna.
# - Inheritance: parent class ke features child class mein reuse karna.
# - Polymorphism: same method name, lekin objects ke hisaab se alag behaviour.
# - Abstraction: unnecessary details hide karke important interface dikhana.
#
# Is file ko run karke har example ka output dekha ja sakta hai.


# ============================================================
# 1. EASY EXAMPLE: Class, Object, __init__ aur method
# ============================================================
class Student:
	# __init__ constructor hota hai. Object create hote hi automatically chalta hai.
	def __init__(self, name, age):
		# self current object ko refer karta hai.
		# self.name aur self.age object ke instance attributes hain.
		self.name = name
		self.age = age

	def introduce(self):
		# Method object ka behaviour define karta hai.
		return f"Mera naam {self.name} hai aur meri age {self.age} hai."


student_one = Student("Aman", 20)
student_two = Student("Sara", 21)
print("EASY 1:", student_one.introduce())
print("EASY 2:", student_two.introduce())


# ============================================================
# 2. EASY EXAMPLE: Instance attribute vs class attribute
# ============================================================
class Dog:
	# Class attribute sabhi Dog objects ke liye common hota hai.
	species = "Canis familiaris"

	def __init__(self, name):
		# Instance attribute har object ka alag ho sakta hai.
		self.name = name

	def bark(self):
		return f"{self.name} bolta hai: Woof!"


dog_one = Dog("Bruno")
dog_two = Dog("Milo")
print("EASY 3:", dog_one.name, dog_one.species)
print("EASY 4:", dog_two.bark())


# ============================================================
# 3. MODERATE EXAMPLE: Encapsulation aur properties
# ============================================================
class BankAccount:
	def __init__(self, owner, opening_balance=0):
		self.owner = owner
		# Double underscore attribute ko name-mangling ke through private jaisa banata hai.
		self.__balance = opening_balance

	@property
	def balance(self):
		# Read-only style getter: user balance dekh sakta hai.
		return self.__balance

	def deposit(self, amount):
		if amount <= 0:
			raise ValueError("Deposit amount positive hona chahiye.")
		self.__balance += amount

	def withdraw(self, amount):
		if amount <= 0:
			raise ValueError("Withdraw amount positive hona chahiye.")
		if amount > self.__balance:
			raise ValueError("Insufficient balance.")
		self.__balance -= amount


account = BankAccount("Neha", 1000)
account.deposit(500)
account.withdraw(250)
print("MODERATE 1:", account.owner, "ka balance =", account.balance)

# Explanation: Balance ko direct modify karne ke bajaye deposit/withdraw use kiya gaya.
# Isse class invalid values ko reject karke apna data protect kar sakti hai.


# ============================================================
# 4. MODERATE EXAMPLE: Inheritance aur method overriding
# ============================================================
class Vehicle:
	def __init__(self, brand):
		self.brand = brand

	def move(self):
		return f"{self.brand} vehicle move kar raha hai."


class Car(Vehicle):
	# Car, Vehicle ki properties aur methods inherit karti hai.
	def move(self):
		# Same method ko child class apne tareeke se redefine kar rahi hai.
		return f"{self.brand} car road par drive kar rahi hai."


class Boat(Vehicle):
	def move(self):
		return f"{self.brand} boat water par sail kar rahi hai."


car = Car("Toyota")
boat = Boat("Yamaha")
print("MODERATE 2:", car.move())
print("MODERATE 3:", boat.move())

# Explanation: Vehicle parent/base class hai. Car aur Boat child classes hain.
# move() ka naam same hai, par output alag hai. Is behaviour ko polymorphism kehte hain.


# ============================================================
# 5. MODERATE EXAMPLE: Class method aur static method
# ============================================================
class Employee:
	company = "Tech Solutions"

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	@classmethod
	def from_text(cls, text):
		# Class method cls ke through class par operate karta hai.
		# Factory method ke roop mein text se Employee object banaya ja raha hai.
		name, salary = text.split(",")
		return cls(name.strip(), int(salary.strip()))

	@staticmethod
	def is_valid_salary(salary):
		# Static method ko self ya cls ki zarurat nahi hoti.
		return salary >= 0


employee = Employee.from_text("Ravi, 60000")
print("MODERATE 4:", employee.name, employee.salary)
print("MODERATE 5:", Employee.is_valid_salary(employee.salary))


# ============================================================
# 6. DIFFICULT EXAMPLE: Abstraction aur polymorphism
# ============================================================
from abc import ABC, abstractmethod


class Payment(ABC):
	# ABC abstract base class banane mein help karta hai.
	# Payment ka exact process har payment type khud define karega.
	def __init__(self, amount):
		if amount <= 0:
			raise ValueError("Payment amount positive hona chahiye.")
		self.amount = amount

	@abstractmethod
	def pay(self):
		# Child class ko pay() implement karna compulsory hai.
		raise NotImplementedError


class CardPayment(Payment):
	def pay(self):
		return f"Card se Rs. {self.amount} ka payment successful."


class UpiPayment(Payment):
	def __init__(self, amount, upi_id):
		super().__init__(amount)
		self.upi_id = upi_id

	def pay(self):
		return f"UPI {self.upi_id} se Rs. {self.amount} ka payment successful."


def process_payment(payment):
	# Function ko concrete payment type pata nahi; use sirf pay() interface chahiye.
	print("DIFFICULT 1:", payment.pay())


process_payment(CardPayment(1500))
process_payment(UpiPayment(750, "aman@upi"))

# Explanation: Abstraction implementation details hide karti hai.
# process_payment() dono payment classes ke saath same tarah kaam karta hai.


# ============================================================
# 7. DIFFICULT EXAMPLE: Composition aur shopping cart
# ============================================================
class Product:
	def __init__(self, name, price, quantity=1):
		if price < 0 or quantity <= 0:
			raise ValueError("Price negative ya quantity zero nahi ho sakti.")
		self.name = name
		self.price = price
		self.quantity = quantity

	def total_price(self):
		return self.price * self.quantity


class ShoppingCart:
	def __init__(self):
		# Cart ke andar Product objects hain: is relationship ko composition kehte hain.
		self.products = []

	def add_product(self, product):
		if not isinstance(product, Product):
			raise TypeError("Sirf Product object add kar sakte hain.")
		self.products.append(product)

	def subtotal(self):
		return sum(product.total_price() for product in self.products)

	def discount(self, percentage):
		if not 0 <= percentage <= 100:
			raise ValueError("Discount 0 se 100 ke beech hona chahiye.")
		return self.subtotal() * (1 - percentage / 100)

	def summary(self):
		lines = ["Cart summary:"]
		for product in self.products:
			lines.append(
				f"- {product.name}: {product.quantity} x Rs. {product.price}"
			)
		lines.append(f"Subtotal: Rs. {self.subtotal():.2f}")
		return "\n".join(lines)


cart = ShoppingCart()
cart.add_product(Product("Keyboard", 2000, 1))
cart.add_product(Product("Mouse", 800, 2))
print("DIFFICULT 2:\n" + cart.summary())
print("DIFFICULT 3: 10% discount ke baad =", f"Rs. {cart.discount(10):.2f}")

# Explanation: ShoppingCart Product se inherit nahi karta; uske paas Product objects hain.
# Isliye yeh 'has-a' relationship hai, jabki inheritance 'is-a' relationship hota hai.
# Composition real projects mein flexible design banane ke liye useful hoti hai.


# ============================================================
# QUICK REVISION
# ============================================================
# Class -> Blueprint; Object -> class se bana actual item.
# Attribute -> Object ka data; Method -> Object ka behaviour.
# Inheritance -> Existing class ka code reuse.
# Polymorphism -> Same interface, different implementation.
# Encapsulation -> Data ko controlled methods ke through access karna.
# Abstraction -> Complex implementation hide karke simple interface dena.
# Composition -> Ek class ke andar doosri class ke objects rakhna.
