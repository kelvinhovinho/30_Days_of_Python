#gictionary is an orderes mutable paired data type
# empty_dict = {}
from msilib import PID_TITLE


me ={
    'name':'kelvin',
    'age':27,
    'school':'UEAB',
    'country': 'Kenya',
    'is_married': True,
    'skills':['HTML','CSS','Python'],
    'address':{
        'street':'kayole',
        'town':'nairobi'
    }
 }

 #length
print(len(me))

#syntax
print(me['skills'][0])
print(me['address']['town'])

#we can use the get method. it does not raise an error if the key does not exist
print(me.get('address'))
print(me.get('city'))

#adding an item
me['works']='Naya Solutions'
print(me)

me['skills'].append('Django')
print(me.get('skills'))

#modifying items in a dict

me['name']='Adamba'
print(me['name'])

print('school' in me)

me.pop('school')
print(me)
me.popitem()
print(me)

#lititems changes dict into a list of items 

you = me.items()
print(type(you))

K = me.keys()
print(K)

V = me.values()
print(V)