a = 3

if a > 0:
    print('A is a positive number')

else:
    print('A is a negative number')

#shot hand

b = -5

print('B is a positive') if b>0 else print('B is a negative number')

user = 'james'
access_level = 3

# if user == 'admin' or access_level >=4:
#     print('Access granted')

# else:
#     print('Access denied')

print('Access granted') if user =='admin' or access_level >=3 else print('Access denied')