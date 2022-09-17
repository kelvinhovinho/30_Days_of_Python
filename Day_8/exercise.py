dog = {
    'name':'skubidu',
    'color':'white',
    'breed':'german shephered',
    'legs':4,
    'age': 7
}

student = {
    'first_name' :'kelvin',
    'last_name' : 'adamba',
    'gender': 'Male',
    'age' :27,
    'is_mariade': False,
    'skills' : ['HTML',"css"],
    'country': 'kenya',
    'city': 'Nairobi',
    'address': 'kayole'
}

print(len(student))
print(len(student['skills']))
print(type(student['skills']))

student['skills'].append('Flask')
print(student['skills'])

m = student.keys()
print(type(m))