from operator import index
from tkinter.font import ITALIC


mixed_data_types = ['kelvin',24,4.5,'single',2500]

it_companies = ['facebook','google','microsoft','apple','ibm','oracle','amazon']
print(it_companies)

print(len(it_companies))
# it_companies.append('safaricom')
print(it_companies)

# it_companies.insert(3,'moringa')

n = it_companies[4]
print(n.upper())

s = 'this are example of IT companie: '
print(' '.join(it_companies))

print('google' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)

print(it_companies[3::])
del it_companies[-1]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
#print(it_companies)

front_end = ["HTML",'CSS','JS','React','Redux']
back_end = ['Node','Express','MongoDB']

# print(front_end + back_end)
full_stack = front_end + back_end
print(full_stack)

full_stack.extend(['Python','SQL'])
print(full_stack)