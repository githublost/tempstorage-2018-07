#!/usr/bin/env python3

# dict is unordered and key-value type set.
# yes, dict is special set, have set features.
# like, set don't have index, set element is unique.

# dict special feature is element composed by key and value.
# the key is unique in dict as set elements.
# key and value is one-to-one correspondence.
# because key is unique, so the element is unique, too.
# usaully use key to get value, this usage is usefully.

# define dictionary.
# define empty dictionary
dict_demo = {}
# dict elements must be key-value type.
dict_demo = {1:'Linux', 2:'Vim'}
print(dict_demo)
# also dict created by dict()
# the parameter is a tuple that contain several sub_tuple.
# sub_tuple composed by key and value, it's dict elemnt. 
dict_demo = dict(((1,'Linux'), (2,'Vim')))
print(dict_demo)

# note that, dict element, key can be a lot of type.
dict_demo={1:2, 'Linux':'Vim', 3:[1,2,3]}
print(dict_demo)
# but, the key can't be mutable type, like list.
# dict_dem={[1,2,3]:'Linux'}
# will report error, TypeError: unhashable type: 'list'.
# remeber! key must be immutable type.

# use key to get value.
dict_demo = {1:'Linux', 2:'Vim'}
print(dict_demo)
print(dict_demo[1])
# but, if key is not exists,
# will report error, KeyError.
# print(dict_demo[5])
# such case, we have a solution, get().
# get(), also use key to get value,
# different is get() will return None when key absent, not error.
print(dict_demo.get(5))
# and get() can set default value, if key absent.
# get() will return default value, not None.
print(dict_demo.get(5, 'default')
# so get() is frendly for user, prvent program interruption.

# dict operation.
# dict add elements. 
# e.g. dict_name[key]=value
print(dict_demo)
dict_demo[5] = 'Bash'
dict_demo[6] = 'Python'
print(dict_demo)
# note that, when dict adding element,
# if key is exists, it's just update the value.
# if not, dict augment elements.

# dict delete elements.
# e.g. del dict_name[key]
del dict_demo[1]
print(dict_demo)
# but, if key is not exists.
# will report error, KeyError.
# del dict_demo[1]

# also dict can delete element by pop().
# delette single element from dict.
# pop() popup element from dict. 
# delete element from dict and return it.
# yes, delete both key and value what composed the element.
# e.g. dict_name.pop(key)
dict_demo.pop(2)
print(dict_demo)

# get all the elements from dict.
# items() get a lot of dict elements, 
# return dict_items type objects,
# dict_items is a binary tuple.
# get dict_items, also get both the key and the value.
# usually, loop through dict elements by for. 
for key, value in dict_demo.items():
	print(key, value)

# get key list from all dict elements.
# keys() get all keys, return a list type.
print(dict_demo.keys())
# get value list from all dict elements.
# keys() get all values, return a list type.
print(dict_demo.values())
# remeber! keys() and values() return type can be loop by for.

