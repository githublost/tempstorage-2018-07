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

class Args(object):
	def __init__(self):
		self._args = sys.argv[1:]
		self._check_args()
	def _check_args(self):
		if len(self._args) != 6:
			print("Parameter Error")
			exit()
	def _get_path(self, option):
		try:
			option_index = self._args.index(option)
			path = self._args[option_index+1]
		except (IndexError, ValueError):
			print("Parameter Error")
			exit()
		return path
	@property
	def userdata_path(self):
		return self._get_path('-d')
	@property
	def config_path(self):
		return self._get_path('-c')
	@property
	def output_path(self):
		return self._get_path('-o')

args = Args()

class Config(object):
	def __init__(self):
		self.config = self._get_config_data()
	def _get_config_data(self):
		config = {}
		with open(args.config_path, 'r') as file:
			for line in file.readlines():
				key, value = line.split('=')
				try:
					key = key.strip()
					value = float(value.strip())
				except ValueError:
					print("Config Error")
					exit()
				config[key] = value
		return config

config = Config()

class UserData(object):
	def __init__(self):
		self.userdata = self._get_userdata()
	def _get_userdata(self):
		userdata = []
		with open(args.userdata_path, 'r') as file:
			for line in file.readlines():
				id, salary = line.split(',')
				try:
					id = int(id.strip())
					salary = int(salary.strip())
				except ValueError:
					print("UserData Error")
					exit()
				userdata.append((id, salary))
		return userdata

userdata = UserData()

class Calculator(object):
	def __init__(self):
		self.config = config.config
		self.userdata = userdata.userdata
	def _check_jishu(self, salary):
		if salary < self.config['JiShuL']:
			return self.config['JiShuL']
		elif salary > self.config['JiShuH']:
			return self.config['JiShuH']
		return salary
	def _get_shebao(self, salary):
		shebao_rate = sum(self.config.values()) - self.config['JiShuH'] - self.config['JiShuL']
		shebao = self._check_jishu(salary)*shebao_rate
		return shebao
	def calculate(self, salary):
		shebao = self._get_shebao(salary)
		part_for_tax = salary - shebao - tax_start_point
		if part_for_tax <= 0:
			tax = 0.00
			income = salary - shebao
			return '{:.2f}'.format(shebao), '{:.2f}'.format(tax), '{:.2f}'.format(income)
		for item in tax_quick_query_table:
			if part_for_tax > item.pay_for_tax:
				tax = part_for_tax*item.rate  - item.soon_calculate
				income = salary - shebao - tax
				return '{:.2f}'.format(shebao), '{:.2f}'.format(tax), '{:.2f}'.format(income)
	def calcu_all(self):
		result = []
		for userdata_item in self.userdata:
			id = userdata_item[0]
			salary = userdata_item[1]
			shebao, tax, income = self.calculate(salary)
			result_item = [id, salary, shebao, tax, income]
			result.append(result_item)
		return result
	def export(self, default='csv'):
		result = self.calcu_all()
		with open(args.output_path, 'w', newline='' ) as file:
			writer = csv.writer(file)
			writer.writerows(result)

def main():
	calcu = Calculator()
	calcu.export()

if __name__ == '__main__':
	main()
