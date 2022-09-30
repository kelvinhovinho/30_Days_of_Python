person = {
    'first_name' : 'Asabeneh', 
    'last_name' : 'Yetayeh',
    'age' : 250,
    'country' : 'Finland',
    'is_married' : True,
    'skills' : ['javascript', 'React','Node','MongoDB','Python'],
    'address':{
        'street': 'space Stream',
        'zipcode' : '02210'
    }
}

if person['skills']:
    print(person['skills'][len(person['skills'])//2])
    print('Python' in person['skills'],person['skills'])
    # print(person['skills'])

    # if person['skills'] in ['javascript','React']:
    #     print('Front End Developer')

    if 'javascript' in person['skills'] and 'React' in person['skills']:
         print('Front End Developer')
    
    elif 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('Full dtack Developer')

    # elif ['Node','MongoDB','React'] == person['skills']:
        # print('Full dtack Developer')
    
    else:
        print('Unknown title')
