#Dictionaries
#collection of unordered, mutables, paired key value data type

empty_dict ={}

dict = {'key1':'value1', 'key2':'value2'}

person ={
    'fName':'Kelvin',
    'lName':'Adamba',
    'age':29,
    'is_married':False,
    'skills':['javaScript','Python','Node'],
    'address':{
        'street':'Kitengela',
        'zipcode':30100,
    }
}

#length

print(len(person))

#accessing items using key
print(person['address'])
print(person['fName'])
print(person['skills'][0:2])

#we use get method it will return None if a key does not exist
print(person.get('lName'))
print(person.get('school'))

#adding key value to a dictionary
person['school']='UEAB'
print(person)
person['skills'].append('HTML')
print(person['skills'])
print(person.get('school'))

#checkin keys
print('fName' in person)

#pop(key) ==> removes the item with specified name
#popitem() ==> removes the last item
#del: removes and item with specified key name

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct)
dct.pop('key2')
print(dct)

dct.popitem()
print(dct)

del dct['key1']
print(dct)

#changing a dict to a list
dct1 = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
#item method changes dict to lst
print(type(dct1))
dct2 = dct1.items()
print(dct2)

#clearing
print(dct1.clear())

dct3 = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct3.keys()
print(keys)

print(dct3.values())