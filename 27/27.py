##euler27
from math import sqrt
primes=[2]

for i in range(3,1000,2):
	for p in primes:
		prime = True
		if i%p==0:prime = False;break
	if prime:primes.append(i)
	
def primal(n):
	if n==2: return True
	if n<2:return False
	if n%2==0:return False
	for i in range(3,int(sqrt(n))+1,2): 
		if n%i==0: return False
	return True

for i in range(-10,10):print i,primal(i)
	
counts = {}
for i in range(-1000,1000):
	print i
	for p in primes:
		n=0
		counts[i*p] = 0
		while primal(n*n+i*n+p):
			counts[i*p]+=1
			n+=1
		
		
x = [(v,k) for k,v in counts.iteritems()]
x.sort()
print 'v,k'
print x[0]
print x[-1]