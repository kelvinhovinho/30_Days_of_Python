'''
-Their are for collecting date type in python 
1. sets(collection in which unordered are immutable. does not allows duplicate meamber but we can add items to the sets.)
2. dictionary(collection which is unordered, chengibleand indexed. no duplicate member )
3. turples(collection which is ordered and immutable. allows duplicate)
4. list(collection which is ordered and changable)
-
'''
 #list 
 #they can be created using the build in function lst = list()
 #using the square bracket lst = []

fruits = ['banana','orange','lemon','mango']
vegetables = ['Tomato','Potato','Cabbage','Oniona']
web_tech = ['HTML','CSS','JS','React','Redux']

lst = ['asabeneh',250,True,{'country':'Finland','city':'Helsinki'}]

#we access list using their indes
print(fruits[0])
print(fruits[-1])

#unpacking a list 

country = ['kenya','uganda','somalia','djibouty','tanzania','sudan']

country_1,country_2, country_3, *rest = country

print(rest)
print(country_1)

print('kenya' in country)

#adding an item in alist we use the append method 

country.append('cameroon')

print(country)

#we use insert method to add an item ina a specific index

country.insert(1,'Rwanda')
print(country) 

#we use the remove method to remove an item. we can use po to remove a specific index. if it is not specified the last item is removed autimatically 

friends = ['paul','peter','mercy','joshua','kaibz']
friends.remove('mercy')
print(friends)
friends.pop()
print(friends)
friends.pop(1)
print(friends)

#del is used to delete a specific idex or the entire list

web_tech = ['html','css','js','mongo','sql','django']

del web_tech[3]
print(web_tech)
del web_tech
print(web_tech)