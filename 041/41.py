##euler41


comps = set()
comps.add(1)
primes = []
m = 10**7

def digits(n):
	n = int(n)
	ds = []
	while n:
		ds.append(n%10)
		n/=10
	return ds


def pandigital(n):
	ds = digits(n)
	ds.sort()
	for i,j in enumerate(ds):
		d = i+1
		if d!=j: return 0
	return d


panprimes = []

def compose(n,m):
	if n not in comps:
		primes.append(n)
		if pandigital(n): 
			print n
			panprimes.append((pandigital(n),n))
	for p in primes:
		newp = n*p
		if newp>m: break
		comps.add(n*p)


for i in xrange(2,m): compose(i,m)



panprimes.sort()
print panprimes[-1]

#7652413 (there could be bigger... but didnt try since this worked)