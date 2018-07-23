#!/usr/bin/env python3

a = 9
def change():
	global a
	print(a)
print("Before the function call  ", a)
print("inside change function", end=' ')
change()
print("After the function call ", a)
