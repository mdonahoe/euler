"""
project euler #71
by matt donahoe
"""

f = (0,1)
ff = 0
n,d = 0,1
while d<1000001:
	test = 1.0*n/d
	if test>=3.0/7: d+=1
	else:
		if test>ff:
			ff = test
			f = (n,d)
		n+=1
print f