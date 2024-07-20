numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

print([num for num in numbers if num <=0])

#one dmensional
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_dimensions =[numbs for rows in list_of_lists for row in rows for numbs in row]
print(one_dimensions)

print("*"*10)
def gen_list_tuples():
    list_of_tuples =[]
    for i in range(11):
        list_of_tuples.append((i, i**0, i**1, i**2, i**3, i**4, i**5))
    return list_of_tuples

