#!/usr/bin/python3
def no_c(my_string):
	no_c = 'abCcdddee'
print(no_c.translate({ord(i): None for i in 'Cc'}))
