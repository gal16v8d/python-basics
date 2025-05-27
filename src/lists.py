import functools

numbers = [1, 2, 3, 4, 5, 6]
# add item to end
numbers.append(7)
print(numbers)
# add item at certain position
numbers.insert(3, 3.5)
print(numbers)
# extract and delete an item (default last)
numbers.pop()
print(numbers)
# remove first occurence of
numbers.remove(3.5)
print(numbers)
# reverse list
numbers.reverse()
print(numbers)
# sort list
numbers.sort()
print(numbers)
# find pos of element
print(numbers.index(3))
# append lists
numbers2 = [10, 11, 12]
all_nums = numbers + numbers2
print(all_nums)
# append lists
numbers.extend(numbers2)
print(numbers)
# update index
numbers[0] = 0
print(numbers)
# count occurrences (how many 0's on list)
print(numbers.count(0))
# list size
print(len(numbers))
# empty list
numbers.clear()
print(numbers)
# list of many types
types_list = [1, True, "lol"]
# python custom substract syntax
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
print(primos[3:10:2])
# fill elements
numbers3 = [x for x in range(1, 10)]
print(numbers3)

# yield tuples (union)
union = list(zip(numbers3, types_list))
print(union)

# mapping / transform
numbers4 = [1, 2, 3, 4]
numbers4 = list(map(lambda x: x * 2, numbers4))
print(numbers4)

# filtering
numbers5 = [1, 2, 3, 4, 5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers5))
print(new_numbers)

# reduce
result = functools.reduce(lambda c, item: c + item, [1, 2, 3, 4])
print(result)

# sort will not work on it
types_list.sort()
