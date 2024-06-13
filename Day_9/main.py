#conditions
a = 0

if a>0:
    print("a is positive number")

elif a==0:
    print("A is a zero")
else:
    print('a is a negative number')


#short hand code
#code if condition else code

b=0
print("B is a positive number") if b>0 else print("b is a negative number")

#we use logical operators instead of nested if statements

username = 'admin'
access_level = 5

print("Access granted") if username =='admin' and access_level >=4 else print("Access denied")