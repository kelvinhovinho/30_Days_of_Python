#function for adding two numbers

def add_two_numbers(num1,num2):
    return num1+num2
print('the sum of the two numbers is:',add_two_numbers(10,20))

def area_of_circle(pi,radius):
    return pi * radius**2
print(area_of_circle(3.142,7))


def add_all_numbers(*numbers):
    total = 0
    for i in (numbers):
        total +=i
    return total
print(add_all_numbers(10,20,50,20))


def convert_celsius_to_fahrenheit(c):
    return str((c*9/5)+32)+'F'
print(convert_celsius_to_fahrenheit(20))

def check_season():
    month = input("write the month of the year\n").lower()
    if month in['december','february','january']:
        return('WINTER')
    elif month in ['march','may','april']:
        return('SPRING')
    elif month in['june','july','august']:
        return 'SUMMER'
    elif month in['september','october','november']:
        return "AUTUMN"
    else:
        return 'write a proper month'
print(check_season())


def reverse_list(a):
    return a[::-1]
print(reverse_list(['me','yo']))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total=total+i
    return total
print(sum_of_numbers(15))

# def sum_of_numbers(high):
#     sum_of_numbers = 0
#     for i in range(high + 1):
#         sum_of_numbers += i
#     return sum_of_numbers
# print(sum_of_numbers(5))