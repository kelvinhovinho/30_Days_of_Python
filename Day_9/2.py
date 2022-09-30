age = int(input('Enter your age\n'))
y = 25

if age < y:
    if y-age ==1:
        print('I am a year older than you')
    else:
        print(f'you are {y-age} younger than me')
else:
    if age - y ==1:
        print('you are a year older than me')
    else:
        print(f'you are {age- y} years old than me')
