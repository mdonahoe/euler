from math import sqrt
from time import time

def nthprime(n):
	ps = [2]
	next = 1
	while len(ps)<n:
		next+=2
		sq = int(sqrt(next))
		tests=[p for p in ps if p<=sq]
		for t in tests:
			if not next%t: break
		else:
			ps.append(next)
	return ps[-1]
	



t = time()		
print sum(primesbelow(2000000))
print time()-t