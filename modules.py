# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Module Function:
import math
print(math.pi)
print(math.sqrt(81))
print(math.sin(60))

from math import *
print(pi)
import math as m
print(m.factorial(4))

from math import factorial as f,sqrt as s
print(s(6))
print(sqrt(36))

# Assignment:
# What is module?
# Module is a file that contains code to perform a specific task.
# A module may contain variables, functions, classes etc.
# Contents of this file can be made available to any other program.
# Python has the import keyword for this purpose.
# For ex.
import math
print("square root of 100:",math.sqrt(100))

# Difference between import math & from math import *
# import math:
# import math imports an entire code library.
# Use import math when you want to use multiple members of the module.

# for ex.
import math
x = 10
y = 4
d = math.sqrt(x**2 + y**2)
print(math.sqrt(x**2 + y**2))

r = 5
area = math.floor(math.pi*r**2)
print(math.floor(math.pi*r**2))

# from import math *
# from import imports a specific member or members of the library.
# Use from import when you want to save yourself from typing the module name over
# and over again. In other words, use from import when referring
# to a member of the module many times in the code.
# for ex.
from math import sqrt, floor
x = 5.2
y = 2.4
d = floor(sqrt(x ** 2 + y ** 2))
print(floor(sqrt(x ** 2 + y ** 2)))

# Aliasing:
# In python programming, the second name given to a piece of data is known as an alias.
# Aliasing happens when the value of one variable is assigned to another variable
# because variables are just names that store references to actual value.
# for ex.
from math import sqrt as s
print(s(625))

x = [10, 20, 30, 40, 50]
y = x
print(x)
print(y)

print(help('modules'))

# random module:
# Python has a built-in module that you can use to make random numbers.
# set the seed value to 10
import random
random.seed(10)
print(random.random())
import random
print(random.getstate())

# array module:
# This module defines an object type which can compactly represent an array of
# basic values: characters, integers, floating point numbers.
from array import *
array_num = array('i',[1,3,5,7,9])
array_num.typecode

array_num = array('i', [1,3,5,7,9,10,15])
array_num.itemsize

# collection module:
# The Python collection module is defined as a container that is used
# to store collections of data, for example - list, dict, set, and tuple, etc.
# It was introduced to improve the functionalities of the built-in collection containers.

V = ('Vijay',32,'M')
print(V)

# time module:
# The time module in Python provides functions for handling time-related tasks.
# The time-related tasks includes,
# reading the current time
# formatting time
# sleeping for a specified number of seconds and so on.

import time
seconds = time.time()
print("seconds since epoch=",seconds)

# id module:
# In Python, the “io” module supports several modules and functions for dealing
# with binary data, Unicode data, and string data.

import io
bs = io.BytesIO(b'Linuxhint\x0AGuide')
print(bs, '\n')
print(bs.getvalue())
bs.close()

# sys module:
# The python sys module provides functions and variables which are used
# to manipulate different parts of the Python Runtime Environment.
# It lets us access system-specific parameters and functions.

import sys
print(sys.version)

# re module:
# A regular expression (or RE) specifies a set of strings that matches it;
# the functions in this module let you check if a particular string matches
# a given regular expression (or if a given regular expression matches
# a particular string, which comes down to the same thing).

import re
p = "CNS: A python guide for all"
match = re.search(r'portal', p)
print('Start Index:', match.start())
print('End Index:', match.end())







