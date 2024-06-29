# import mymodule
from mymodule import generate_full_name, sum_two_numbers

print(generate_full_name('Kelvin','Adamba'))
print(sum_two_numbers(10,20))

#renaming imported functions from a module

from mymodule import sum_two_numbers as add_two_numbers
print(add_two_numbers(40,50))

#importing buid in modules 
#math, datetime, os, sys, random, statistics, collection, json, re

import os
# os.

from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

print(mean(ages))
print(mode(ages))
print(stdev(ages))

import math 
print(math.pi)
print(math.sqrt(9))

#importing strings 
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)


#importing random
from random import randint
print(randint(1,5))