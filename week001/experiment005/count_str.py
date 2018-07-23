#!/usr/bin/env python3
# explain need python3 interpreter to execute current script.

def char_count(str):
	char_list = set(str)
	for char in char_list:
		print(char, str.count(char))

# equivalent C language main function.
# judge the code block where under 'if' statement whether be executed.
# when the script run by itself, the code block will be executed.
# when the script was called, like 'import count_str' somewhere else,
# then the code block will not be exectued.
if __name__ == '__main__': 
	s = input("Enter a string: ")
	char_count(s)
