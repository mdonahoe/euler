"""
Project Euler problem #66
by Matt Donahoe and Doug Ellwanger
"""

from math import sqrt,floor

isqrt = lambda n: int(sqrt(n))


def f(S):
	
	m = 0
	d = 1
	a0 = isqrt(S)
	a = a0
	yield a
	while 1:
		m = d*a-m
		d = (S-m*m)/d
		a = int((a0+m)/d)
		yield a


def cfx(terms): #dougs first attempt
	if len(terms)==1: return terms[0]
	total = terms[-1]
	for i in range(len(terms)-2, -1, -1):
		total = 1.0/total+terms[i]
	return total


def cfr(terms): #matts first attempt (recursive!!!)
	if not terms: return (1,0)
	h,k = cfr(terms[1:])
	return terms[0]*h+k,h

def cf(terms): #final. unrolled recursion
	terms = terms[:] #make sure to copy the list. popping messes it up
	h,k = 1,0
	while terms:
		h,k = terms.pop()*h+k,h
	return h,k



def doN(n,N=1000):
	#print n
	g = f(n)
	xs = []
	while N:
		xs.append(g.next())
		h,k = cf(xs)
		#print n,h,k
		if h*h-k*k*n == 1: return h
		N-=1
	print 'loop out',n
	return -1

print max([(doN(n,100000),n) for n in range(1001) if sqrt(n)!=isqrt(n)])[1]


