#Nested loops in python
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(0, i):
        print("*", end=' ')
    print()  # Move to the next line after each row


#Break, continue, and pass statements in python
for i in range(1, 6):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)

for i in range(1, 6):
    if i == 3:
        continue  # Skip the rest of the loop when i is 3
    print(i)        

for i in range(1, 6):
    if i == 3:
        pass  # Do nothing when i is 3
    print(i)