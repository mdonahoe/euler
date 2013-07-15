##euler35

notprime = set()
primes = []
m = 10**6
def compose(n,m):
	if n not in notprime: primes.append(n)
	for p in primes:
		newp = n*p
		if newp>m: break
		notprime.add(n*p)


for i in range(2,m): compose(i,m)


def rotate(n):
	s = str(n)
	return int(s[1:]+s[0])

def fullrot(n):
	r = str(n)
	for i in range(len(r)):
		r = rotate(r)
		if int(r) in notprime: return False
	return int(r)==n
	
print len([i for i in primes if fullrot(i)])

##55 primes below 10**6