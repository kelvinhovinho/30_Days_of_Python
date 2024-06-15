#while loop

count = 0

while count <=5:
    print(count)
    count+=1
else:
    print(count)

print("-------------")


#break
counts = 0

while counts <=10:
    print(counts)
    counts+=1
    if counts == 3:
        break

print("-------------")

counts = 0
while counts <=10:
    if counts == 3:
        counts+=1
        print("continue")
        continue
    print(counts)
    counts+=1