#!/usr/bin/env python3

# how did we want to save a python object?

# the problem involves serialization.
# serialization refer to converting object in memery into format that can be stored.
# two ways to serilize in python:
# 	pickle model
# 	josn type

# pickle
# 
import pickle

pickle_demo = { 1:'Linux', 2:'Vim', 3:'Git'}
with open('./pickle_test.data', 'wb') as file:
	pickle.dump(pickle_demo, file)

with open('./pickle_test.data', 'rb') as file:
	new_pickle_demo = pickle.load(file)

print(new_pickle_demo)

print(type(new_pickle_demo))
# note that, open mode with 'b'.

# pickle.dumps(obj) serialize object into byte stream.
