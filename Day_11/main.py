# A function is a reusable block of code or a statent designed to perfom a certain task 
# when we make a functon we call it declairing a function, wehn we use it we call it calling or invoking a function 

# syntax

# def name(parameters):
    # Code
    # pass
#function name
# name()


def full_name():
    fname = 'Kelvin'
    lname = 'Adamba'
    space = ' '
    name = fname + space + lname
    return name
print(full_name())


def add_two_numbers():
    num1 = 10
    num2 = 20
    sum = num1 + num2
    print(sum)
add_two_numbers()

# using the return value

def fullname():
    fname = 'Kelvin'
    lname = "Odiaga"
    space = " "
    full_name = fname+space+lname

    return full_name

print(fullname())

def addtwonumbers():
    num1 = 10
    num2 = 25
    total = num1+num2
    return total
print(addtwonumbers())


#function with parameters
#if our function takes in a parameter, we should call our functon with an argument 

#def functon_name(parameter):
    #codes

#print(function_name(arguments))


def greetings(name): #name is the parameter
    message = name + ', welcome to 30 days of python'
    return message
print(greetings('kelvin')) #kelvin is the argument

def square_number(number):
    return number*number
print(square_number(10))

def area_of_circle(radius):
    pi = 3.142
    return pi*radius**2
print(area_of_circle(20))


def total_sum(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(total_sum(100))


#function with two parameters 
#syntax
# def functio_name(para1,para2):
    #codes
#print(function_name(arg1,arg2))

def full_name (f_name,l_name):
    space= ' '
    return f_name + space + l_name
print('the upcoming full stack developer,',full_name('kelvin','Adamba'))


def sum_of_two_numbers(num1,num2):
    return num1+num2
print('the sum of the two numbers is:',sum_of_two_numbers(20,30))

def weight_of_an_object(mass,gravity):
    weight = str(mass*gravity)+" N"
    return weight
print(weight_of_an_object(50,10))

#passing arguments with key values
def name(par1,par2):
    pass
print(name(par1='Kelvin',par2='Adamba'))


def my_name(fname,lname):
    space=' '
    return fname+space+lname
print('My full name is',my_name(fname='kelvin',lname='Adamba'))


def sum(num1,num2):
    return num1+num2
print(sum(num1=10,num2=30)) 


def calculate_age(current_year, date_of_birth):
    return current_year-date_of_birth
print(calculate_age(2022,2003))


def even(n):
    if n%2==0:
        return True
    return False
print(even(7))
print(even(6))


def evens(n):
    even = []
    for i in range(n+1):
        if i%2==0:
            even.append(i)
    return even
print(evens(10))


#function with default parameters
def name(my_name='kelvin'):
    return f'{my_name} in an upcoming programmer'
print(name())
print(name('nehema'))


def area_of_circle(radius,pi=3.142):
    return pi*radius**2
print(f'the are of a circle is:',area_of_circle(22))

#arbitrary number os arguments. we add * before the parameters

def sum_of_all_numbers(*numbers):
    sum = 0
    for i in numbers:
        sum+=i
    return sum
print(sum_of_all_numbers(2,5,10,15))


def mimi(team,*arg):
    print(team)
    for i in arg:
        print(i)
mimi('team1','boo','joo','kii')


#function as a parameter of another function 

def sq(n):
    return n*n
def s(f,x):
    return f(x)
print(s(sq,3))