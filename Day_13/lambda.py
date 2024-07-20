#lambda are anonymous functions without a name and can take any number of arguments but can only have one expression 

add_two_numbers = lambda a,b: a+b

print(add_two_numbers(10,10))

#self invoking lambda function 

print((lambda a,b: a+b)(2,3))

squre = lambda a : a**2
print(squre(10))

print((lambda a:a**2)(5))

#cube
print((lambda b: b**3)(3))

# lambda function inside a another function

def power(x):
    return lambda n:x**n

print(power(2)(3))