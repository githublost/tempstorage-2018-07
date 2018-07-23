#!/usr/bin/evn python3

# set is unordered collection of unique elements.
# the first feature is unordered, so set don't have index.
# you can't use index to visit set.
# and second feature is unique, so set every element is unique in set.
# if you want to define more than one same elements, not report error,
# but, set will just keep one unique element and auto remove same elements.
# yes, you can't define and find two of same elements in set.
# even if you want to manipulate same elements to set, not work.
# the elements of set, all unique, and always keep unique.

# set usual use to keep data elemnt unique and test element exists.
# set also support mathematical operations. 
# e.g. union, intersection, difference, symmentric difference.

# define set, use brace or set function to create set.
# but empty set, only create by set function.
# because {} is dictionary type, not set.
set_demo=set() # empty set.
print(type(set_demo))
set_demo={} # not set
print(type(set_demo))
# create set by {}
set_demo={'linux', 'C++', 'Vim', 'Linux'} # set elements wil be unique.
# set work to keep uniqe elements.
print(set_demo)
# set() can create set with a character string arguments, 
# and set() arguments just need one.
# if set() get more than one args, will report error, TypeError.
set_demo=set('set_demo')
# if set() get one character string arguments, not a single character.
# set() will split character string to single character, keep unique.
# so set elements will be unique single character from character string.
print(set_demo)

# set operation.
# set work to test elements is exists.
# 'in' or 'not in', result return boolean type, True or False.
print('Linux' in set_demo)
print('Python' in set_demo)
print('Python' not set_demo)
# add() add elements.
print(set_demo)
set_demo.add('Python')
print(set_demo)
# remove() delete elements.
set_demo.remove('Python')
print('Python' in set_demo)
# if element is not in set, use remove() will report error, KeyError.
# set_demo.remove('Pthon')

# set support mathematical operations.
set1={1, 2, 3, 4}
set2={3, 4, 5, 6}
# '|' operations equivalent union(),
# will return the elements which in set1 or set2.
print(set1 | set2)
print(set1.union(set2))
# '&' operations equivalent ,
# will return the elements which both in set1 and set2.
print(set1 & set2)
# '-' operations equivalent ,
# will return the elements which in set1 and not in set2.
print(set1 - set2) 
# '-' operations equivalent ,
# will return the elements which union elements without intersecion elements.
print(set1 ^ set2) 

