#!/usr/bin/python3
if __name__ == "_main_":
	import hidden_4
	for i in dir(hidden_4):
		if not i.startswitch("_"):
			print("{:s}".format(i))
