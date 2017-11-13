"""
project euler #77
matt donahoe



i enjoyed thinking of this one. did some back of the envelope (literally)

discovered a dynamic programming solution
"""

from primes import Primes
p=Primes(5000)

ways = {} #ways.get((n,p),0) = number of ways to sum to n using only primes >= p
primes = []
n=1
while s<=50000000:
	n+=1
	s = 0
	if p.is_prime(n):
		s = 1
		primes.append(n)
	for x in primes[::-1]:
		s+=ways.get((n-x,x),0)
		ways[(n,x)] = s
	print n,s
