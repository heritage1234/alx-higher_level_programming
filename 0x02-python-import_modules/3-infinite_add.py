#!/usr/bin/python3

import sys

length = len (sys.argv)
summ = 0
if __name__ == "_main_":
	if length == 0:
		summ = 0
	else:
		for i in range(1, length):
			summ += int(sys.argv[i])
	print("{:d}")
