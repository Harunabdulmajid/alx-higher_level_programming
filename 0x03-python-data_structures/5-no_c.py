#!/usr/bin/python3
def no_c(my_string):
	s = 'abCcdddee'
print(s.translate({ord(i): None for i in 'Cc'}))
