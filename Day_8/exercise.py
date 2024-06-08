dog ={
    'name':'skoby',
    'color':'white',
    'breed':'german shephered',
    'legs':4,
    'age':2,
}


student ={
    'first_name':'John',
    'last_name':'kambwala',
    'gender':'male',
    'age':20,
    'is_married':False,
    'skills':['grinding','welding'],
    'country':'Kenya',
    'city':'Kisumu',
    'address':{
        'code':10100,
        'street':'kondele'
    }
}

print(len(student))
print(student['skills'])
print(type(student['skills']))

student['skills'].append('crimping')
print(student['skills'])

print(student.keys())
print(student.values())

student_lst  = student.items()
print(student_lst)

student.pop('address')
print(student)

del student
print(student)