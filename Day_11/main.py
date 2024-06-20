#Functions 

#A functon is a reusable block of code 
def generate_full_name():
    first_name = 'kelvin'
    last_name = 'Adamba'
    space = ' '
    full_name = first_name+space+last_name
    print(full_name)
generate_full_name()

def adding_two_numbers():
    num1=10
    num2 = 20
    total = num1+num2
    print(total)
adding_two_numbers()

print('*********')

#return statement 
def full_name():
    fname = 'Kelvin'
    lname = 'Adamba'
    space = ' '
    return fname+space+lname
print(full_name())

def addition():
    num1 = 20
    num2 = 20
    return num1+num2
print(addition())

# function with parameters
def greeting(name):
    return name + " welcome to python for everyone"
print(greeting("Kelvn"))

print("**************")

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#Two parameters 

def full_name(fName, lName):
    return (f'My name is {fName} {lName}')
print(full_name('Kelvin','Adamba'))
print(full_name('John','Kenneth'))
print(full_name('Joash','Adamba'))
print(full_name('Emily','Adamba'))


#passing arguments with keys and values 
def company(name, activity):
    return name + " "+ activity
print(company(name="NAYA", activity="Solution"))


#returning boolean 
def is_even(n):
    if n%2==0:
        print (n, " is Even")
        return True
    return False
print(is_even(20))
print(is_even(21))

#returning list 
def find_even_numbers(n):
    even = []
    for i in range(n+1):
        if i%2==0:
            even.append(i)
    return even
print(find_even_numbers(20))

#Arbitrary number of arguments 
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total+=num
    return total
print(sum_all_nums(1,1,4,6))



