# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F


score = int(input('Enter your score\n'))
if score> 100:
    print('Enter a valid score')

elif score>=80 and score<=100:
    print('A')
elif score>=70 and score<=79:
    print('B')
elif score>=60 and score<=69:
    print('A')
elif score>=50 and score<=59:
    print('A')
else:
    print('F')