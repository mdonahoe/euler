#euler39

from math import sqrt


d = dict()

def integral(n): return int(n)==n

for a in range(1000):
	for b in range(1000):
		c = sqrt(a*a+b*b)
		s = int(a+b+c)
		if s>1000: continue
		if integral(c): d[s] = d.get(s,0)+1

s = [(b,a) for a,b in d.iteritems()]
s.sort()
print s[-1]
		
#max p = 840