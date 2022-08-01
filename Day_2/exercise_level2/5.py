radius = 30

#area of a circle 
#pi r2
pi = 3.142
area_of_circle = pi * radius**2
print(area_of_circle)

# calculating circumfrence of a circle

# circumfrence = 2 pi r

circum_of_a_circle = 2*pi*radius

print(circum_of_a_circle)

# taking radius as input from user 

R = int(input('what si your radiues: \n'))

area = (R**2*pi)
print ('The area of the circle is ',area)

circumfence = (2*pi*R)
print('the circumfrence of the circle is ', circumfence)