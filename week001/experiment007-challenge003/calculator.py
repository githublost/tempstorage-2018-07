#!/usr/bin/env python3

import sys
from collections import namedtuple
import csv

# constant 
tax_start_point = 3500

# make tax_quick_query_table by nametuple
fast_lookup_item = namedtuple('fast_lookup_item', 
	['pay_for_tax', 'rate', 'soon_calculate'])

tax_quick_query_table = (
	fast_lookup_item(80000, 0.45, 13505),
	fast_lookup_item(55000, 0.35, 5505),
	fast_lookup_item(35000, 0.30, 2755),
	fast_lookup_item(9000, 0.25, 1005),
	fast_lookup_item(4500, 0.20, 555),
	fast_lookup_item(1500, 0.10, 105),
	fast_lookup_item(0, 0.03, 0)
)

# dispose arg
class Args(object):
	def __init__(self):
		self._args = sys.argj[1:]
	def get_path(self, option):
		try:
			option_index = self_args.index(option)
			path = self_args[option_index+1]
		except IndexError, ValueError:
			print("Parameter Error")
			exit()
		return path

class Config(object):
	def __init__(self):
		pass

class Calculator(object):
	def __init__(self):
		pass

class Output(object):
	def __init__(self):
		pass

def main():
			

if __name__ == '__main__':
	if len(sys.argv):
		print("Parameter Error")
		exit()
	args = sys.argv[1:]
	main()
