#list comprehension is creating a list from a sequence 

# sntax [i for i in iterable if expression]

#example changing a string to a list of characters

languange = 'python'

lst = list(languange)
print(lst)

# second way using list comprehension 

lst_2 = [lang for lang in languange]

print(type(lst_2))

print(lst_2)


#generating a listof numbers 

numbers = [num for num in range(0,10)]
print(numbers)

print('-'*16)
#mathematical operations during iterations
squre = [i * i for i in range(0,10+1)]
print(squre)


#making tuples
squre_2 = [(i,i*i) for i in range(10+1)]
print(squre_2)


print('@'*16)
#example 2

#combining LC wth if expression 
even_numbers = [i for i in range(20+1) if i%2==0]
print(even_numbers)

odd_numbers = [i for i in range(20+1) if i%2!=0]
print(odd_numbers)

#filter numbers
numberss = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]

numbb = [n for n in numberss if n> 0 and n%2==0] 
print(numbb)

print('#'*16)
#flatterning 3 dimension array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)