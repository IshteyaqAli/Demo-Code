# Built in modules in python
#help('modules') # It's output will be the list of all the modules available in python

import math # this module provides access to the mathematical functions defined by the C standard
math.e # This is aan example and It's output will be 2.718281828459045
print(math.e) # It's output will be 2.718281828459045

import random # this module implements pseudo-random number generators for various distributions
random.randrange(1, 10) # It's output will be a random number between 1 and 10
print(random.randrange(1, 10)) # It's output will be a random number between 1 and 10
#OR
random.shuffle([1, 2, 3, 4, 5]) # It's output will be a shuffled list of [1, 2, 3, 4, 5]
print(random.shuffle([1, 2, 3, 4, 5])) # It's output will be a shuffled list of [1, 2, 3, 4, 5]

import time # this module provides various time-related functions
print("hello")
time.sleep(5) # It's output will be a delay of 5 seconds
print("World") # It's output will be World after a delay of 5 seconds
print(time.time()) # It's output will be the current time in seconds since the epoch

import os # this module provides a portable way of using operating system dependent functionality
print(os.getcwd()) # It's output will be the current working directory
#OR
print(os.listdir()) # It's output will be the list of files and directories in the current working directory