# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Once a set is created, you cannot change its items, but you can remove items and add new items.
# removes duplicates.
myset = {'apple', 'banana', 'cherry'}
print(myset)

set_from_string = set('hello')
# set with every char as element
print(set_from_string)

numbers = [1,2,3,4,4,3,2,1]
set_numbers = set(numbers)
# remove all repeated elements
print(set_numbers)

myset.add('orange')
print(myset)

myset.update(['kiwi'])
print(myset)

# remove element if exists
myset.discard('kiwi')
print(myset)
# remove element if exists, raise error if not
myset.remove('orange')
print(myset)
# get and remove one element, raise error if empty set
myset.pop()
print(myset)
# set size
print(len(myset))
# empty set
myset.clear()
print(myset)