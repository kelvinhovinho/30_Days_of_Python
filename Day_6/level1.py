from lib2to3.pytree import type_repr


empty_tuple = ()
print(type(empty_tuple))

brothers = ('kenneth','mambo','joash')
sisters = ('joy','mercy','elizabeeth')

siblings = list(brothers+sisters)
print(type(siblings))

parents= ['joash','emily']
# family_members = parents+siblings
parents.extend(siblings)
print(parents)

# family_members = parents.extend(siblings)
# print(family_members)
# parents = ['joash','emily']




# print(family_members)