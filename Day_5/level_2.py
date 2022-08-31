from unittest.util import three_way_cmp


age = [19,22,19,24,20,25,26,24,25,24]

age.sort()
print(age)

print(max(age))
a,b,c,d,e,f,g,h,i,j = age

print((a+b+c+d+e+f+g+h+i+j)/10)

print(max(age)-min(age))


country = ['China','Russia','USA','Finland','Sweden','Denmark']

country1,country2,country3,*rest = country
three =country1,country2,country3 
print(three)

print(rest)