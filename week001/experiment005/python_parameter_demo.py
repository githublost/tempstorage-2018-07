#!/usr/bin/env python3

# python function paramter type.

# first type, required parameter.
# when we use function, 
# required parameter don't have to write parameter names.
# but, we must assign value to required parameter by order which function defined. 
# so, required parameter also be called as location parameter.
# if we don't want assignment ordered, 
# we must use parameter name to pass parameter.
# e.g. server connect program.
def connect(ipaddress, port):
	print("IP: ", ipaddress)
	print("Port: ", port)
# first time pass parameter, right order, true result.
connect('192.168.1.1', 22) 
# second time pass parameter, false order, true result. 
connect(22, '192.168.1.1')
# third time pass parameter, false order, pass parameter by par_name, true result.
connect(port=22, ipaddress='192.168.1.1')

# second type, default parameter.
# we can set parameter default value when function define.
# if we don't assign value to default parameter when function called,
# the default value will auto assign to parameter.
def connect(ipaddress, port=22):
	print("IP: ", ipaddress)
	print("Port: ", port)
connect('192.168.1.1', 2002)
connect('192.18.1.1')
# note that, 
# 1-required parameter can't after default parameter.
# e.g. function_name(a, b=10, c) # is false.
# 2-default parameter must set be immutable datatype value.
# if not default parameter will be modified when function called,
# we don't want that default parameter will be change bigger and bigger.
# e.g. wrong example 
def f(a, data=[]):
	data.append(a)
	return data
print(f(1))
print(f(2))
print(f(3))
# e.g. the solution 
def f(a, data=None):
	if data == None:
		data = []
	data.append(a)
	return data
print(f(1))
print(f(2))

# third type. variable parameter.
# if we don't sure the number of parameters be passed in function.
# maybe zero, maybe one, maybe more than one.
# such case, we need a variable parameter, 
# it's mean parameter number is variable.
# variable parameter can accept one tuple or any number of parameters.
# variable parameter define format is add '*' before parameter_name.
# we can define variable parameter by custom name.
# usually, define as '*args'.
# e.g. connect server multi ports.
def connect(ipaddress, *ports):
	print("IP: ", ipaddress)
	for port in ports:
		print("Port: ", port)
# pass zero or multi ports, or tuple of ports.
connect('192.168.1.1')
connect('192.168.1.1', 22, 23, 24)
connect('192.168.1.1', 22)
params = (25, 26, 27)
connect('192.168.1.1', *params)
# variable parameter only accept a tuple.
# if pass the parameter not tuple type to variable parameter location,
# these arguments will auto generate a tuple to pass in function.

# fourth type, keyword parameter
# required parmeter, default parameter, variable parameter 
# the three kinds parameter can assign value to function without parameter name.
# these parameters can define by custom name.
# keyword parameters will auto generate a dict inside function to extension function.
# define keyword parmeters format, add '**' before parmeter name,
# uaually, named as '**kw'
# note that, use the keyword parameter without '**', 
# when keyword parameter was used within function itself,
# 
# e.g. connect()
def connect(ipaddress, *ports, **kw):
	print("IP: ", ipaddress)
	for port in ports:
		print("Port: ", port)
	for key, value in kw.items():
		print('{}: {}'.format(key, value))
# as variable parameter, keyword parameter assign value can use dict,
# note that, dict key must be string datatype.
ipaddress = '192.168.1.1'
params = (25, 26, 27)
prop = {'device': 'eth0', 'proto': 'static'}
connect(ipaddress, *params, **prop)
# also can assign keyword parameter to function, as 'par_name=vaule' type.
# e.g. 
connect(ipaddress, *params, device='eth0', proto='static')

# fifth type, named keyword parameter.
# this kind parameter must use par_name to assign value.
# feature is defined by '*,' before parameter name.
# e.g. def test(m, *, a, b)
# 'm' is required parameter, 'a' and 'b' is named keyword parameter.
# but, ust use par_name to assign value when function called,
# if not will report error, TypeError.
# e.g. 
def hello(*, name):
 	print("Hello", name)
# hello('named keyword parameter')
hello(name='named keyword parameter')

# modified parameter value in function.
# in C/C++ language have pass value and pass references concept.
# 
# pass value, when function called, the parameter be used 
# just like local variable in function.
# the local variable will disposal when function execute finish.
# modification can't affect the parameter data.
# 
# pass references, when function called, function accpet outside parameter.
# if function execution modify the parameter, the modification will preserved.
# so, the parameter data is changed by function modification.

# python different C/C++ that parameter don't have type.
# python can use any object as parameter, and pass any object parameter.
# but, different parameter have different feature.
# so some parameter can be modified, some is not.
# if the parameter is mutable object, the parameter can be moditied,
# mutable object will affected in function, the result also can be affected.
# like list object parameter
# if not, the immutable object paramter can't modified.
# like string object parameter
# actually, immutable object as a local variable be created in function.
# when function execute finish, the modification can't affect parameter.
# e.g.
def connect(ipaddress, ports):
	print("IP: ", ipaddress)
	print("Ports: ", ports)
	# this position cread new local variable, 
	# and don't modified 'ipaddress' value.
	ipaddress = '10.10.10.1'
	# modify ports list values, use append() extend element to list.
	# will affect the value of 'prots' list.
	ports.append(8080)

if __name__ == "__main__":
	ipaddres = "192.168.1.1"
	ports = [22, 23, 24]
	print("Before connect:")
	print("IP: ", ipaddress)
	print("Ports: ", ports)
	print("In connect: ")
	connect(ipaddress, ports)
	print("After connect:")
	print("IP: ", ipaddress)
	print("Ports: ", ports)
# the reuslt will founc that 'ipaddress' value don't affected, 
# the 'ports' list value was changed.
