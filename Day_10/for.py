# for loop
# it is used to iterate over a sequence (list,tuple,dictionary,set or strinf)


numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)

language = 'python'
for lang in language:
    print(lang)


for i in range(len(language)):
    print(language [i])


person = {    
    'first_name':'kelvin',
    'last_name' : 'adamba',
    'age' : 20,
    'country' : 'kenya',
    'is_married' : False,
    'skills':['HTML','CSS','Python'],
    'address':{
        'street':'kayole',
        'xipcode': '30100'
    }
}

for key in person:
    print('first_name' in key)


for key,value in person.items():
    print(key,value)


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('next number should be ',number +1) if number !=5 else print('end of loop')