#used to iterate over a sequence

numbers = [0,1,2,3,4,5]

for number in numbers:
    print(number)

print("**********************")

language = 'python'

for lang in language:
    print(lang)


print("**********************")
#for loops will return keys in a dictionary 

mee ={
    'name':'Kelvin',
    'age':29,
    'skills':['HTML','CSS','JS']
}

for key in mee:
    print(key)

print("**********************")
for key, value in mee.items():
    print(key, value)


print("**********************")

it_company = {'Facebook','Twiter','Google','Microsoft','Apple'}
for company in it_company:
    print(company)


print("*********BREAK*************")

numberssss = (0,1,2,3,4,5)
for num in numberssss:
    if num == 3:
        break
    print(num)


numberssss = (0,1,2,3,4,5)
for num in numberssss:
    print(num)
    if num == 3:
        continue
    print('Next number should be ', num+1) if num != 5 else print("Loops end")
print('outside the loop')


print("*********RANGE*************")

lst = list(range(11))
print(lst)

st = set(range(1,11))
print(st)

for i in lst:
    print(i)

print('*******NESTED LOOPS****')

person = {
    'first_name': 'Kelvin',
    'last_name': 'Adamba',
    'age': 29,
    'country': 'Kenys',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    # print(key)
    if key == 'skills':
        for skill in person['skills']:
            print(skill)