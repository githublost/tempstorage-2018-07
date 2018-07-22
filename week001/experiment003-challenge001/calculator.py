#!/usr/bin/env python3

from collections import namedtuple
import sys

# constant
TAX_START_POINT = 3500

# use namedtuple make tax_query_table
quick_lookup_item = namedtuple('quick_lookup_item', [
	'pay_for_tax',
	'tax_rate',
	'quick_calculate_number'
])

tax_query_table = [ 
	quick_lookup_item(80000, 0.45, 13505),
	quick_lookup_item(55000, 0.35, 5505),
	quick_lookup_item(35000, 0.30, 2755),
	quick_lookup_item(9000, 0.25, 1005),
	quick_lookup_item(4500, 0.20, 555),
	quick_lookup_item(1500, 0.10, 105),
	quick_lookup_item(0, 0.03, 0)
]

def calculator(salary):
	# if salary equal or less than TAX_START_POINT 
	if salary <= 3500:  	
		return 0.00		

	# if salary greater than TAX_START_POINT
	pay_for_tax = salary - 3500
	for item in tax_query_table:
		if item.pay_for_tax < pay_for_tax:
			tax = pay_for_tax * item.tax_rate - item.quick_calculate_number
			return '{:.2f}'.format(tax)

def main():
	try: 
		# just only one parameter with script self.
		if len(sys.argv) != 2:
			raise SyntaxError
		# convert int datatype.
		salary = int(sys.argv[1])
	except Exception as e:
		print("Parameter Error")
		exit()
	print(calculator(salary))

if __name__ == '__main__':
	main()
