sum = 0
for i in range (100+1):
    sum+=i
    print(sum)


sum_even = 0

for j in range (100+1):
    if j % 2 ==0:
        sum_even+=j
        print(sum_even)

print('*'*10)
sum_odd = 0
for j in range (100+1):
    if j % 2 !=0:
        sum_odd+=j
        print(sum_odd)
    