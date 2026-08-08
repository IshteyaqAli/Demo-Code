import math


def get_number(message):
	while True:
		try:
			return float(input(message))
		except ValueError:
			print("Please enter a valid number.")


def main():
	print("Simple Student Calculator")

	while True:
		print("\nChoose an operation:")
		print("1. Addition")
		print("2. Subtraction")
		print("3. Multiplication")
		print("4. Division")
		print("5. Percentage")
		print("6. Square a number")
		print("7. Square root")
		print("8. Exit")

		choice = input("Enter your choice (1-8): ").strip()

		if choice == "8":
			print("Goodbye!")
			break

		if choice in {"1", "2", "3", "4", "5"}:
			first = get_number("Enter the first number: ")
			second = get_number("Enter the second number: ")

			if choice == "1":
				result = first + second
			elif choice == "2":
				result = first - second
			elif choice == "3":
				result = first * second
			elif choice == "4":
				if second == 0:
					print("A number cannot be divided by zero.")
					continue
				result = first / second
			else:
				result = (first / 100) * second

		elif choice == "6":
			number = get_number("Enter a number: ")
			result = number ** 2
		elif choice == "7":
			number = get_number("Enter a number: ")
			if number < 0:
				print("A negative number has no real square root.")
				continue
			result = math.sqrt(number)
		else:
			print("Please choose a number from 1 to 8.")
			continue

		print(f"Answer: {result:g}")


if __name__ == "__main__":
	main()