#!/usr/bin/env python3

from collections import namedtuple
import sys

tax = 0.00

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

# dispose exceptions
try: 
	if len(sys.argv) != 2:
		raise SyntaxError
	salary = int(sys.argv[1])
except Exception as e:
	print("Parameter Error")
	exit()

# if salary less than TAX_START_POINT 
if salary < 3500:  	
	print(tax)
	exit()

# if salary equal or greater than TAX_START_POINT
pay_for_tax = salary - 3500

for item in tax_query_table:
	if item.pay_for_tax < pay_for_tax:
		tax = pay_for_tax * item.tax_rate - item.quick_calculate_number
		break;	
print('{:.2f}'.format(tax))
