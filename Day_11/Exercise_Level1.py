def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(10,20))
print(add_two_numbers(30,20))
print(add_two_numbers(80,20))

def area_of_circle(r, pi=22/7):
    calc = r*r*pi
    return f'The are of a circle with a radius of {r} is {calc}cm~'
print(area_of_circle(10))
print(area_of_circle(20))
print(area_of_circle(5))


def add_all_nums(*nums):
    total =0
    for num in nums:
        if isinstance(num, int):
            total+=num
        else:
            return("Input numbers")
    return total
print(add_all_nums(1,10))


def converts_celcius_to_fahrenheit(celsius):
    results =(celsius*9/5)+32
    return f'{celsius}°C is {results}°F'
print(converts_celcius_to_fahrenheit(230))


# season = input(" Which month do you want to check the season?\n").lower()

# def check_season(season):
#     if season in ['october','november''september']:
#         return 'Autumn'
#     else:
#         return "I dont get it"
# print(check_season(season))

def check_season(month):
    if month in ["September", "October", "November"]:
        print("Autumn")
    if month in ["December", "January", "February"]:
        print("Winter")
    if month in ["March", "April", "May"]:
        print("Spring")
    else:
        print("Summer")
print(check_season('September'))
print(check_season('December'))

# print(reverse_list())
# [5, 4, 3, 2, 1]
def reverse_list():
    a= [1, 2, 3, 4, 5]
    return a[::-1]
print(reverse_list())


# print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]