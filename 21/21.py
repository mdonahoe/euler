#euler21

from math import sqrt
from time import time

def divisors(n):
	d = [i for i in range(2,int(sqrt(n))+1) if n%i==0]
	e = [n/i for i in d]
	return sum(set(d+e))+1
	

dic = {}

for i in range(10000):
	dic[i] = divisors(i)
	
s = 0

for k,v in dic.iteritems():
	try:
		if dic[v]==k and k!=v:print k;s+=k
		
	except: pass

print s
