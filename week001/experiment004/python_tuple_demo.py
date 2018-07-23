#!/usr/bin/env python3

# tuple is special list. if tuple is created, then it can't be modified.
# so tuple cant use sort(), append() ... as list. it's a more secure datatype.

# define tuple.
tuple_demo=('C++', 'Cloud', 'Linux', 'PHP')
print(tuple_demo)
# tuple is sequential, so it's also have index as list.
# tuple element subscript, it's also tuple index.
# we can get element value by index.
# tuple index is start from zero as list.
# get first element value by index. 
print(tuple_demo[0] 

# tuple can't modified when it's created,
# if we want to use sort() to sort tuple as list, will report error.
# error information is AttrbuteError, tuple has no attribute 'foo'.
# tuple_demo.sort()

# tuple is more secure datatype, it's usual allow user only to read.
# tuple is special, it's immutable. remeber it!
# but tuple can contain modifiable type element, e.g list.
# and this kind of element can be modified in tuple.
new_tuple_demo=('Linux', ['BigData1', 'BigData2', 'BigData1'], 'Vim')
print(new_tuple_demo[1])
new_tuple_demo[1].append('BigData4')
print(new_tuple_demo)

# notic that, when you define a single element tuple,
# you must add a dot after element value in brackets,
# because if not do it, the datatype is str, not tuple.
# e.g. tuple_demo=(foo,)
tuple_single_element_demo=('foo',)
print(tuple_single_element_demo)
print(type(tuple_single_element_demo))
tuple_single_element_without_dot_demo=('foo')
print(tuple_single_element_without_dot_demo)
print(type(tuple_single_element_without_dot))
