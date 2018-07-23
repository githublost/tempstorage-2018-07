#!/usr/bin/env python3

# usaully, the same code will be used many times in program.
# such case, we will use function resolve code redundancy.
# function help us do same thing over and over again.
# define function,  put the same code into the function. 
# when we need, we call the function.

# function simple working principle.
# function will accept parameters when be called.
# and processing data within the function itself, 
# get value of result, maybe the result is True or False.
# maybe the result is an exception. it's all normal.
# finally, return the value back to caller. 

# usually, function must be defined before we call it.
# note that, some special functions, named built-in functions.
# built-in functions can be used without defined.
# because these functions are used frequently, and practical.
# so pytho3 have 68 built-in functions, when python launched, 
# the built-in functions are already defined by default. 
  
# define a python function.
# created by 
# 	keyword 'def', top of line.
# 	spacing, after 'def'.
# 	function_name, after 'spacing'.
# 	round brackets, after function_name.
#	parameter is selectable, insert the parentheses, as function input.
#	colon, after parentheses.
#	code block, new lines after first line and indentation.
#	keyword 'return' is selectable.
#	usually, keyword 'return' will insert the code block.
# 	'return' will terminate code execution,
#	and return result to the caller as function output.
# e.g. 
# def function_anme(params):
#	statement1
# 		return foo_result # 'return' in the middle. 
#	statement2
# 	return foo_result # 'return' in the end.
# 

# char_count(), accept two parameters, retrun result.
# accept a character_string and a single character.
# count(), count the single character number from character_string.
# return count_result, numeric type.
def char_count(str, char):
	return str.count(char)

# call funtion on condition that function is defined.
# e.g.  
# function_name(parameter1, parameter2, ...)
print(char_count('banana', 'a')) # print the result.
# also, call function and assign return_result to variable.
# e.g.
# result_variable = function_name(params)
result = char_count('banana', 'a')
print(result)
# but, if function is not defined, call function not work.
# will report error, NameError.
# e.g.
# function_name_not_defined(params)
