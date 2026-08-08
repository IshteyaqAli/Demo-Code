x = 3
y = 6
print(x >> 4)

import string

for ch in string.ascii_lowercase:  # lowercase a-z
    binary = format(ord(ch), '08b')
    print(ch, binary)

import string

for ch in string.ascii_uppercase:  # uppercase A-Z
    print(ch, format(ord(ch), '08b'))

import string

for ch in string.ascii_letters: # lowercase a-z and uppercase A-Z
    print(ch, format(ord(ch), '08b'))

#  How to get binary values by hand
# Each letter is stored as a number in ASCII. For example:

# a = 97
# b = 98
# c = 99
# ...
# z = 122
# Then convert that number to binary using repeated division by 2.

# Step 1: Know the letter’s number
# Use the ASCII table:

# lowercase a starts at 97
# lowercase z is 122
# uppercase A starts at 65
# uppercase Z is 90

# Quick pen-and-paper method
# For any letter:

# Find its ASCII number.
# Divide by 2 repeatedly.
# Record remainders.
# Read remainders from last to first.
# Add leading zeros to get 8 bits.
# That is the manual way to get each alphabet character’s binary value.