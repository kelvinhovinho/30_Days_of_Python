# function can pass different data types as parameters

# def function_name (parameter):
#     codes
#     codes
# print(function_name(argument))

from optparse import Values


def greetings(name):
    message = name + ', welcome to python for everyone!'
    return message
print(greetings('kelvin'))

def add_item(num):
    ten = 10
    return ten +num
print(add_item(90))

#square a number 
def square(x):
    return x*x
print(square(20))

#area of a circle
def area(y):
    return 3.14*y
print(area(10))

#sum of numbers

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(100))

#two parameters
#if your functon have parameters we should call it with with argumenta

# def function_name(para1, para2):
#     codes
#     codes
# print(function_name(arg1,arg2))


def gen_full_name (fname, lname):
    space = ' '
    full_name = fname + space + lname
    return full_name
print(gen_full_name('kelvin','adamba'))

def sum_two_number(num1,num2):
    sum = num1+num2
    return sum
print(sum_two_number(20,30))

def weight_of_gravity(mass,gravity):
    w = str(mass*gravity)+' N'
    return w
print(weight_of_gravity(30,20))


# passing arguments with key Values
def names(first_name, last_name):
    return f'my first name is {first_name} and my last name is {last_name}'

print(names(first_name='Kelvin',last_name='Adamba'))


#returning a boolean

def even(n):
    if n%2==0:
        print('Even')
        return True
    return False
print(even(10))
print(even(11))

#functon with default values
def me(name,nationality,age=27):
    return f'my name is {name}, i am a {nationality} citizen, i am {age} years old'
print(me('kelvin','kenyan',30))


#function as a parameter
def square(n):
    return n*n

def do_something(f,x):
    return f(x)

print(do_something(square,3))