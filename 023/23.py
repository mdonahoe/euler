#euler23 20161
from math import sqrt
def divisors(n):
	d = [i for i in range(2,int(sqrt(n))+1) if n%i==0]
	e = [n/i for i in d]
	return sum(set(d+e))+1
	
abundant = [i for i in range(1,20162) if divisors(i)>i]
sums = set([a+b for a in abundant for b in abundant])


print sum([i for i in range(20162) if i not in sums])