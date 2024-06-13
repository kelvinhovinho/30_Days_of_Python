score = int(input("Enter you score \n"))

if score >=80:
    if score >100:
        print('Score can not exceed 100%')
    else:
        print("A")
elif score >=70:
    print("B")
elif score >=60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")


#seasons

month = input("Enter a month to know the season: ").capitalize()

if month in ['September','October','November']:
    print('Autumn')

elif month in ['December','January','February']:
    print('Winter') 

elif month in ['March','April','May']:
    print("Spring")
elif month in ['June','July','August']:
    print("Summer")
else:
    print("Write a valid month")



#question 3
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('write your favourite fruit\n').lower()

if fruit in fruits:
    print('Fruit already exist')
else:
    fruits.append(fruit)
    print(fruits)
