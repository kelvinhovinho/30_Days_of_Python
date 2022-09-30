# season = input('which month do you want to know the seaso? \n').capitalize()

# if season == 'September':
#     print('Autumn')
# elif season =='October':
#     print('Autumn')
# elif season == 'November':
#     print('Autumn')
# elif season == 'December':
#     print('Winter')
# elif season == 'January':
#     print('Winter')
# elif season == 'February':
#     print('Winter')
# elif season == 'March':
#     print('Spring')
# elif season == 'April':
#     print('Spring')
# elif season == 'May':
#     print('Spring')
# elif season == 'June':
#     print('Summer')
# elif season == 'July':
#     print('Summer')
# elif season == 'August':
#     print('Summer')
# else:
#     print('Thants not the month of the year')

# if season == ['September','October','November']:
#     print('Autum')

# else:
#     print('OOps')


month = input('Enter month: ').title()
if month in ["September", "October", "November"]:
    print("Autumn")
elif month in ["December", "January", "February"]:
    print("Winter")
elif month in ["March", "April", "May"]:
    print("Spring")
else:
    print("Summer")