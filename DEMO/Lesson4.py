# Range function in Python is used to generate a sequence of numbers.
#  It can take one, two, or three arguments:
range(5)          # Generates numbers from 0 to 4
range(1, 5)       # Generates numbers from 1 to 4
range(1, 10, 2)    # Generates numbers from 1 to 9 with a step of 2 (1, 3, 5, 7, 9)
print(list(range(5) ))          # [0, 1, 2, 3, 4]
print(list(range(1, 5)))       # [1, 2, 3, 4]
print(list(range(1, 10, 2)))


print("\n")    # [1, 3, 5, 7, 9]

for  i in range(1,10,2):
    print(i)

print("\n")

for i in "Hello":
    print(i)

