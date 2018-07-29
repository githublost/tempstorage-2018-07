#!/usr/bin/env python3

# python language have manry advanced featrue usages,
# the usages not easy to understanded,
# but, ad_features can improved programming efficiency and code quality.

# lambda
# lambda support for anonymous functions.
double = lambda x: x * 2
print(double(5))
# the example above, 'double' variable actually is a anonymous function.
# will get the result when execute 'double(x)' as functions run.
# 
# lambda define a anonymous function, get return value without 'return' keyword.
# usually, lambda function used as parameter for the common function need passed in.
# and, the lambda function only used in one place, 
# anonymous function generally passed as a parameter .
# the benefit is easy defined and quick used.
# remeber! the scenario is simple, used at one place where 
# we just need a simple method work here to provide value,
# without method name and the process of standard define and call,
# even no 'return' keyword.

# slice
# slice used to get a sequence (list or tuple) or part of a string, 
# return a new sequence or string.
# the usage is specifying start and end of subscript in parentheses,
# sparated by a colon. 
# used for list or tuple very common.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
print(letters[1:3])
# remeber! splice range get elements without the last one of end of subscript.
# the end_subscript, it's meaning end here, not get last one here.
# 
# the subscript can be positive, also can be nagative.
# the mapping relation of letters and subscripts.
# positive subscript:   0  1  2  3  4  5  6
# letters	    :   a  b  c  d  e  f  g
# negative subscript:  -7 -6 -5 -4 -3 -2 -1
#
# also, we use positive subscript and negatvie subscript together.
# but, you must be sure the range of subscript marked is true and exists.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:-4])
# if start subscript is omited, default set start to '0'.
# if end of subscript is omited, default slice to the end of sequence.
print(letters[:4])
print(letters[4:])
#
# slice all elements of sequence. slice like '[:]'.
# use the slice feature what slice will retrun a new list, to copy a list.
copy = letters[:]
print(copy)
 
# list comprehension
# list comprehension provide a elegant pattern to operating list.
# since python2.0
unmbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# get even numbers of list.
print([x for x in numbers if x % 2 ==0]
# every number squared.
print([x * x for x in numbers])
# 
# python provide few higher-order functions, like 'map', 'filter', and 'lambda'.
# the higher-order functions mean that 
# can pass in a function as a parameter, 
# the incoming function used to process data.
# the example above, finish by higher-order function.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = filter[lambda x: x % 2 ==0, numbers]
m = map(lambda x: x * x, numbers]
# 
# compare the two realization.
# list comprehension will be more readable.
# in addition, higher-order function increases the overhead of calling a function.
# so that its space-time efficiency is not as efficient as list comprehension.
# no wonder even the author of python also recommend using list comprehension.

# dict comprehension
# once understand the list comprehension, dict comprehension will be easy.
# 'list' changed 'dict', process objec is key and value of dict.
d = {'a':1, 'b':2, 'c':3}
print({k:v*v for k,v in d.items()})
# note that dict cannot be iterated, 
# need to use dict method items() to turn dict into an iterable object.

# iterator
# if you have studied iterator pattern in design patterns, 
# it's easy to understand the concept of iterator.
# to understand iterator, 
# first understand the difference between iterator and iterable object.
# one by one to read and process object called iterate.
# in python, the iterable object what can use 'for...in' to iterate itself elements.
# like list is iterable.
letters = ['a', 'b', 'c']
for letter in letters:
	print(letter)
# the iterator is that you can use next() to keep get next value, 
# util iterator return StopIteraion exception. 
# all the iterable object can through iter() to get its iterator.
# such as the 'letters' above is an iterable object, so iterate it.
letter = ['a', 'b', 'c']
it = iter(letters)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))
# when iterator touch StopIteration, iterate will stop and report error.
#
# all iterable object actually implementing two magic methods of '__iter__()' and '__next__()',
# iter() and next() actually call the two magic method, too. 
# actually the case behind the above example. such as:
letter = ['a', 'b', 'c']
it = letters.__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
# until touch StopIteration, iterate will stop and report error.
# print(it.__next__())
# 
# summarize
# can accessed by for loop that all iterable objects.
# can be get next value by netxt() that all iterator.

# generator
# first generator is a iterator, difference that generator only can be iterated once.
# because the element in each iteration is not already in memory like list,
# it's that you iterate once, then generator generate a element.
# create a generator and iterate:
g = (x**x for x in range(1,4))
print(g)
# a little bit like list comprehension, except using parentheses intead.
# difference that list can iterate over and over again,
# iterate a generator after iterate finish once, don't print element and report error.
#
# the benefit of use generator, 
# because generator does not store all elements in memory,
# generator will dynamically generate one element in memory at once.
# so when you iterate the object has a large number of elements, 
# use generator to save a lot of memory, it's the feature memory-frendly.

# yield
# yield usage like 'return'
# difference that is 'return' return a effective python object, 
# yield return a generator.
# usually, function touch 'return' will return directly, 
# when function use yield, will cotinue execute agter yield,
# until meet next yield or function finish exit.
# the example :
def fib(n):
	current = 0
	a, b = 1, 1
	while current <n:
		yield a
		a, b = b, a+b
		current += 1
# the example above, use yield return a generator.
f5 = fib(5)
print(f5)
# iterate
for x in f5:
	print(x)

# decorator
# decorator can add addiational functionality to function without effecting main body of function.
# in python, function is first citizens, that is so say,
# a function can be passed as a parameter to another function,
# a function can be another function as a return value,
# this is the foundation of decorator to realized.
# the decorator is essentially a function,
# it accept a function as a parameter.
#
# e.g.
# a simple example, also a decorator classic use scenarios, record function call log.
from datatime import datatime
def log(func):
	def decorator(*args, **kwargs):
		print("Function " + func.__name__ + 'has been called at ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		return func(*args, **kwargs)
	return decorator
@log
def add(x, y):
	return x + y

add(1, 2)
#
# '@' is a syntactic sugar provide by Python, 
# syntactic sugar refers to a kind of grammar added in compute language,
# which has no influence on the function of compute language,
# but it is more convenient for programmer to use.
#
# the code above, '*arg' and '**kwargs' are both variable arguments to functoin of Python.
# '*args' represent any number of unknow parameter, it's a tuple,
# '**kwargs' represent keyword parameter, it's a dict,
# these two combination represent all parameters of function.
# when used together, '*args' parameters listed in front of '**kwargs'.
#
# it's equivalent to doing the following:
def add(x, y):
	return x + y
add = log(add)
add(1, 2)
#
# that is, called log(), the add() as a parameter, pass to go in the log().
# log() return a another function 'decorator',
# in the function 'decorator', first print log information, 
# then callback the incoming function 'func', namely 'add' function.
#
# you may noticed that, after executed 'add = log(add)', or after dechking 
# 'add' by '@log',  'add' is no longer the original 'add' function,
# it has become the decorator function of 'log' function returns.
print(add.__name__)
# 'decorator' # the result
# this is also a side effect of decorators, 
# and python provide a way to solve this problem.
# the soluation code.
from functools import wraps
def log(func):
	@wraps
	def decorator(*args, **kwargs):
		print('Function: ' + func.__name__ + ' has been called at ' + datatime.datatime.now().strftime('%Y-%m-%d %H:%M:%S'))
		return func(*args, **kwargs)
	return decorator

@log
def add(x, y):
	return x + y

print(add.__name__)
# 'add' # the result
# there are many application scenarios for decorator,
# when we lean about Flask Web development in the future.
# we will use decorators in a large unmber to realize the routing of Web page and otherfunctions.
 

