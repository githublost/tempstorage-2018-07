#!/usr/bin/env python3

from collections import namedtuple
import sys

tax = 0.00

TAX_START_POINT = 3500

# use namedtuple make tax_quick_query_table
TAX_QUICK_QUERY_TABLE = namedtuple('TAX_QUICK_QUERY_TABLE', [
	'PAY_FOR_TAX',
	'TAX_RATE',
	'QUICK_CALCULATE_NUMBER'
])

qqtat = TAX_QUICK_QUERY_TABLE(
	PAY_FOR_TAX=[80000, 55000, 35000, 9000, 4500, 1500, 0],
	TAX_RATE=[0.45, 0.35, 0.30, 0.25, 0.20, 0.10, 0.03],
	QUICK_CALCULATE_NUMBER=[13505, 5505, 2755, 1005, 555, 105, 0]
)

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

for shuld_pay in qqtat.PAY_FOR_TAX:
	if shuld_pay < pay_for_tax:
		tax = pay_for_tax*qqtat.TAX_RATE[qqtat.PAY_FOR_TAX.index(shuld_pay)] - qqtat.QUICK_CALCULATE_NUMBER[qqtat.PAY_FOR_TAX.index(shuld_pay)]
		break;	
print('{:.2f}'.format(tax))
