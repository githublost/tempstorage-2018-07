#!/usr/bin/env python3

# python list is a kind of sequential map.

# define list.
list_demo = ['Linux','Python', 'Vim', 'C++']
print(list_demo)

# list.append()
list_demo.append('PHP') 
print(list_demo)

# list index
# every element have a subscript,it's index of element.
# we can get the element by subscript.
# the first element of list, subscript is zero.
# if you use positive number expression, index start from zero.
print(list_demo[0])
print(list_demo[1]) # subscript '1' is second element.
# the last element of list, subscript is '-1'. 
# you can use positive number expression, but we usual use '-1'.
# if you use negative expreesion, index is start from '-1', not zero.
print(list_demo[-1])
print(list_demo[-2]) # subsrcpt '-2' is last but one.
# if subscript is out of index range, will report an error, IndexError.
# print(list_demo[9])

# use len(), get length of list
print(len(list_demo))

# operating list.
# list is sequential, so we can operating list by index. 
# also python can match element value to operating list.
# append(), append new element at end of list.
# but sometime we need add new element anywhere in the list,
# at this time, use insert(), add new elemnet by index.
list_demo.insert(0, 'Java') # '0' is position of index, 'Java' is object of element.
print(list_demo)
# count(),  count number of elements.
print(list_demo.count('Java'))
# remove(), delete first matched element of list by element value.
list_demo.remove('Java')
print(list_demo)
# dell(), delet elment of list by index.
# list is sequential, we can reverse position of element in list.
# reverse(), reverse position of element in list.
print(list_demo)
list_demo.reverse()
print(list_demo)
# extend(), merge the other list elements to the end. 
new_list_demo=['Bigdata', 'Cloud']
print(new_list_demo)
print(list_demo)
list_demo.exend(new_list_demo)
print(list_demo)
# if list element_values is comparable by number, alphabet, whatever. 
# sort(), sort list element by value. default sort by alphabet.
print(list_demo)
list_demo.sort()
print(list_demo)
# pop(), popup element by index, default popup last one.
# pop() will delete element from list and return it.
# pop(i), 'i' is index.
print(list_demo)
pop_element=list_demo.pop() # return pop_element value.
print(pop_element)
print(list_demo)  
list_demo.pop() # popup last element.
print(list_demo)
list_demo.pop(0) # popup first element.
print(list_demo)
