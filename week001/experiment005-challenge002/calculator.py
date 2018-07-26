#!/usr/bin/env python3

from collections import namedtuple
import sys

# constant
tax_start_point = 3500
shebao_rate = {
	'yanglao':0.08,
	'yiliao':0.02,
	'shiye':0.005,
	'gongshang':0,
	'shengyu':0,
	'gongjijin':0.06,
}

# make tax_quick_query_table by namedtuple
fast_lookup_item = namedtuple('fast_lookup_item', ['pay_for_tax', 'rate', 'soon_calculate'])

tax_quick_query_table = [
	fast_lookup_item(80000, 0.45, 13505),
	fast_lookup_item(55000, 0.35, 5505),
	fast_lookup_item(35000, 0.30, 2755),
	fast_lookup_item(9000, 0.25, 1005),
	fast_lookup_item(4500, 0.20, 555),
	fast_lookup_item(1500, 0.10, 105),
	fast_lookup_item(0, 0.03, 0)
]

def calculator(salary):
	shebao = salary*sum(shebao_rate.values())
	salary_part_for_tax = salary - shebao - tax_start_point
	if salary <= tax_start_point:
		income = salary - shebao
		return '{:.2f}'.format(income)
	for item in tax_quick_query_table:
		if salary_part_for_tax > item.pay_for_tax:
			tax = salary_part_for_tax*item.rate - item.soon_calculate
			income = salary - shebao - tax
			return '{:.2f}'.format(income)

def main():
	# check arguments
	if len(sys.argv) < 2:
		print("Parameter Error")
		exit()
	for arg in sys.argv[1:]:
		try:
			employee_id, salary = arg.split(':')
			employee_id = int(employee_id)
			salary = int(salary)
		except Exception as e:
			print("Parameter Error")
			exit()
		print('{}:{}'.format(employee_id, calculator(salary)))

if __name__ == "__main__":
	main()
