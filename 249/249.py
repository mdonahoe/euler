from primes import Primes

N = int(1.6*(10**6))
p = Primes(N)
sums = {}
M = 10**16





xs = [i for i in range(5000) if p.is_prime(i)]

for i,x in enumerate(xs):
	
	temp = sums.copy()
	#print len(sums),max(sums.values()+[0])
	for s,c in sums.iteritems():
		y = (x+s)
		temp[y]=(temp.get(y,0)+c)%M
	temp[x]=temp.get(x,0)+1
	sums = temp.copy()
	print x
	#if (i%100==0): print i

print sum([c for s,c in sums.iteritems() if p.is_prime(s)])%M

#print sum([1 for s in powerset([n**n for n in range(1,11)]) if s!=[] and (sum(s)%4)==0])
