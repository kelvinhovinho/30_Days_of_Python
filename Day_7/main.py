#set are unordered items
# st = {}

fruits = {'banana','orange','mango','lemon'}
print(len(fruits))
print(type(fruits))

#we use loops to access items in a set 

#checking items in a set
print('banana' in fruits)

#adding item in a set 
fruits.add('passion')
print(fruits)

#update allows to take multiple agumets and it uses list arguments
fruits.update(['avocado','mapera','berries'])
print(fruits)


parents = {'Joash','Emily'}
children = ('Kelvin','Junior')
parents.update(children)
print(parents)
parents.update(['me','you'])
print(parents)

#we use remove method to remove items from a set. if an item is not present it will send an error however discard method does not raise an error
# pop method removes a random item and returns the removed item

county = {'Nairobi','Mombasa','Kisumu','Nakuru','Nandi'}
print(county.pop())
print(county)

#we use union to join sets 
city ={'Nairobi','Mombasa','Kisumu'}
county = {'Nandi','Machakos','Kilifi'}

kenya = city.union(county)
print(kenya)

kenya.add('Vihiga')
print(kenya)

#intersection returns items which are in both sets 
num1 = {1,2,3,4,5,6}
num2 = {4,5,6,7,8,9,0}

print(num1.intersection(num2))