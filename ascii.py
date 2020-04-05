#!/usr/bin/python3

data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ,. :1234567890()/\"&*"
datalwr = data.lower()

for x in range(len(data)):
	print(str(x+1) + ").", data[x], "=", ord(data[x]), " | ", datalwr[x], "=", ord(datalwr[x]))
