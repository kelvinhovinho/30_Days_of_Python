num = 0
while num <=10:
    print(num)
    num +=1

print('----for loop---')

for i in range(10+1):
    print(i)


print('----------')  

n = 10

while n >=0:
    print(n)
    n-=1

print('----for loop reverse---')
for n in range(10, -1,-1):
    print(n)

print('----Q3---')
for a in range(6+1):
    print(a*'#')

print('----Q4---')

for i in range(8+1):
    for j in range(8+1):
        print("#", end=' ')
    print()

print('----Q5---')
for a in range(10+1):
    print(f'{a} x {a} = {a*a}')


print('----Q6---')

lst = ['Python','numpy','Pandas','Django','Flask']

for ls in lst:
    print(ls)

print('----Q7---')
for i in range(100+1):
    if i%2 ==0:
        print(i)

print('----Q8---')
for i in range(100+1):
    if i%2 !=0:
        print(i)