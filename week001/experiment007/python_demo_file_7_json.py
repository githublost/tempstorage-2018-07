#!/usr/bin/env python3

# JSON(JavaScript Object Notation, JS object markup language)
# a kind of lightweight data interchange format.
# json is popular work on internet application development
# as data transmission format between difference server components communicate.
# they are almost json format what the return value of internet application offered API interfaces. 
import json

json_demo = {1:'Linux', 2:'Vim', 3:'Git'}

print(json.dumps(json_demo))

with open('json_demo.json', 'w') as file:
	file.write(json.dumps(json_demo))

with open('json_demo.json', 'r') as file:
	new_json_demo = json.loads(file.read())

print(new_json_demo)

print(type(new_json_demo))

# 'dumps' is serialize operation.
# 'loads' is deserialize operation.



