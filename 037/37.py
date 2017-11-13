#euler37

comps = set()
comps.add(1)
primes = []
m = 10**6

def truncate_left(n):
	if n in comps: return False
	if n<10: return True
	return truncate_left(int(str(n)[1:]))

def truncate_right(n):
	if n in comps: return False
	if n<10: return True
	return truncate_right(int(str(n)[:-1]))

def trunk(n): return n>10 and truncate_left(n) and truncate_right(n)

trunks = []

def compose(n,m):
	if n not in comps:
		primes.append(n)
		if trunk(n): trunks.append(n)
	for p in primes:
		newp = n*p
		if newp>m: break
		comps.add(n*p)


for i in range(2,m): compose(i,m)



print trunks
print sum(trunks)