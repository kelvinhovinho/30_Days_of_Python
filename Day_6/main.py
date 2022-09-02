#tuples are ordered and unchangable. they are writen in ()
#tuples have few methods: count, index, operator

fruits = ('banana','mango','lemon','orange')
print(len(fruits))

#accessing index
print(fruits[-1])

print(fruits[-3:-1])

#changing tuples t list
home = ('Vihiga','kakamega','Nandi','Kisumu')
print(type(home))
home_2 = list(home)
print(type(home_2))
home_2.append("Nairobi")
print(home_2)

backend = ('python','java')
print('java' in backend)