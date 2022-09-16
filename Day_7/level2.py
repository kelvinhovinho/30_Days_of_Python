A = {19,22,24,20,25,26}
B = {19,22,20,25,26,24,28,27}
age = [22,19,24,25,26,24,25,24]

#join A and B
c = A.union(B)
print(c)

print(A.issubset(B))

del A
print(A)