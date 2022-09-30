# for i in range(7+1):
#     print(i*'#')


# for i in range(1, 9):
#     for j in range(1, 9):
#         print(i, end=' ')
#     print(i)


for i in range(9+1):
    for j in range(9+1):
        print('#',end=' ')
    print(' ')

for i in range(10+1):
    print(f'{i} * {i} = {i*i}')


languages = ['Python', 'Numpy','Pandas','Django', 'Flask']

for lang in languages:
    print(lang)

for i in range(100+1):
    if i%2==0:
        print(i)

for i in range(100+1):
    if i%2!=0:
        print(i)