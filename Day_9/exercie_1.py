age = int(input("Enter your age \n"))
remaining = 18 -age

# sol one
print("You are old enough to drive") if remaining >0 else print(f'you need {remaining} years to drive')

# sol two
if age >= 18:
    print("You are ols enough to drive")

else:
    print('ypu need', remaining , 'year to learn to drive')


#number 2
my_age = 29 

your_age = int(input("Enter your age \n"))

diff = my_age - your_age

if diff >= 1:
    if diff ==1:
        print("I am a year older than you")
    else:
        print("I am ", diff, "years older than you")

else:
    if diff == -1:
        print("You are a year older than me")
    else:
        print(f'You are {diff * -1} years older than me')





