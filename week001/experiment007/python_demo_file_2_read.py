#!/usr/bin/env pyton3

# this program accept user input string as file name,
# then read the file
filename = input("Enter the file name: ")

with open(filename) as file:
	count = 0
	for line in file:
		count += 1
		print(line)
	print('Lines:', count)

