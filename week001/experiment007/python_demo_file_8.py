#!/usr/bin/env python3

# os.path very common standard libraries
# main use to get and process file, folder property.

# common method 
# os.path.abspath(path) # return the absolute path of file.
# os.path.basename(path) # return file name.
# os.path.dirname(path) # retrun folder name.
# os.path.isfile(path) # determine whether the path is a file.
# os.path.isdir(path) # determine whether the path is a folder.
# os.path.exists(path) # determine whether the path is exists.
# os.path.join(path1[, path2[, ..]) join pathname components with separator '/', become a  path.
# get more information with official documents.

import os

filename = './test.txt'
os.path.abspath(filename)
os.path.basename(filename)
os.path.dirname(filename)
os.path.isfile(filename)
os.path.exists(filename)
os.path.join('/.../', 'test.txt')
