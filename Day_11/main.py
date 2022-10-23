# a function is a block of code or a programming statement designed to perfom a certain task
# it uses the def key word. the function is executed only when the fuction is called or invoked.

import code
from pyexpat.errors import codes


def function_name():
    codes
    codes
function_name()

# function without parameters

def generate_full_name():
    fname = 'kelvin'
    lname = 'adamba'
    full_name = fname+' ' + lname
    print(full_name)
generate_full_name()

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one+num_two
    print(total)
add_two_numbers()

def add_number():
    one = 10
    two = 5
    total = one + two
    return total
print(add_number())

def fname():
    firstname = 'kelvin'
    lastname = 'adamba'
    space = ' '
    name = firstname +space + lastname
    return name
print(fname())