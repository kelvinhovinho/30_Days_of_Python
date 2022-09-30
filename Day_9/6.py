fruits = ['banana','orange','mango','lemon']

fruit = input('Enter your fruit\n')

if fruit in fruits:
    print('That fruit already exist in the list')

else:
    fruits.append(fruit)

print(fruits)

# print('that fruit already exists in the list' if fruit in fruits else fruits.append(fruit))
# print('That fruit already exists in the list' if fruit in fruits else fruits.append(fruit))
# prinbanat(fruits)

# if fruit in fruits:
#     print("that fruit already exists in the list")

# else:
#     fruits.append(fruit)

# print(fruits)
