#!/usr/bin/python3
def max_integer(my_list=[]):
	my_list = [12, 45, 78, 9]
maximum_number = my_list[0]
for num in my_list:
	if num > maximum_number:
	maximum_number = num
print(maximum_number)
