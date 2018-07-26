#!/usr/bin/env python3

# file processing is the primary means of 
# data persistence and configuration in development.1
# python support process a lot of file type in work.

# open and close file
#
# open()
# open() will open file, and return a file object,
# read and write file with the file object used.
# 
# open() require two parameters,
# first parameter is file name or file path.
# second parameter is open mode with 'r' 'w' 'a' 'b'
# 'r' open with only read mode. default
# 'w' open with write mode.
# 'a' open with append mode.
# 'b' open with binary mode.
#
file = open('/etc/protocols')
print(type(file))
print(file)
file.close()
# need close file after program execution finish.
# if not, system resources will be occupied, even lost data.
# close() close for open(), and repeate close no problem.

# actually, we should use 'with' statement to dispose file object.
# it will auto closed after file used finish.
# even occur exceptions, it's ok. it's sort for try-finally block.
with open('/etc/protocols') as file:
	count = 0
	for line in file:
		count += 1
	print(count)

# read file content
# read() 
# read() read all file content to string at once.
file_name = '/etc/protocols'
file = open(filename)
file.read()
file.close()
# note that, read() used carefully.
# maybe dangerous that memery size can't enough for load file content.
# read() will running once, then repeate it can't output anything.
# 
# readline() 
# readline() will process file one by one line.
# readline() read content of line from file every time.
# 
# readlines()
# readlines() read content of all line form file 
# different readline() that readlines() return a list what contain all line.
# the list every element is string of every line content.
filename = '/etc/protocols'
file = open(filename)
print(file.readline())
print(file.readline())
file.close
# readline() will mark the start point of fine read.
# so, close file, and open again.
file = open(filename)
print(file.readlines())
file.close()
# traveral file object to read every line from line.
file = open(fileanme)
for x in file:
	print(x, end=' ' )

file.close()

