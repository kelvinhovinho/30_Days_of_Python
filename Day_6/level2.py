fruits = ('avocado','oranges','banana','lemon')
vegetables = ('kales','cabage','casava','beans')
animal_products = ('milk','meat')

food_stuff_tp = fruits+vegetables+animal_products

print(food_stuff_tp)
food_stuff_tp = list(food_stuff_tp)
print(type(food_stuff_tp))
print(food_stuff_tp)
del food_stuff_tp[4:5]
print(food_stuff_tp)

print(food_stuff_tp[0:3])

del food_stuff_tp
# print(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)