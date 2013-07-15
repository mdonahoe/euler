from prime import primelist
primes  = set(primelist)
p2 = primelist[:50]
tried = set()
#print p2
def combo(items, n=None):
    if n is None: n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1: yield v
        else:
            rest = items[i+1:]
            for c in combo(rest, n-1):
                yield v + c


def catprime(xs): return int(str(xs[0])+str(xs[1])) in primes and int(str(xs[1])+str(xs[0])) in primes

def allpairs(ps): return not any(1 for c in combo(ps,2) if not catprime(c))
"""
x = [(sum(c),c) for c in combo(p2,3) if allpairs(c)]
x.sort()
print x[0]

"""
"""

def works(p,p2): return int(str(p)+str(p2)) in primes and int(str(p2)+str(p)) in primes
#find all the primes that work with the new number, then see which group of four all works together.
n = 5
workswith = {}
ps = []
while 1:
	p = primelist.pop(0)
	workswith[p] = []
	for p2 in ps:
		if works(p,p2):
			workswith[p].append(p2)
			workswith[p2].append(p)
	#print p,workswith[p]
	if workswith[p]<n-1: continue
	
	for c in combo(workswith[p],n-1):
		if allpairs([p]+c): print [p]+c, sum([p]+c)
	ps.append(p)

"""
"""
def fitin(x,xs): return not any([1 for y in xs if not catprime((x,y))])

primelist = primelist[4:]
print primelist[0]
#create sets of working numbers. try to add each new number to every set. sort in order
ones = [3,7]
twos = [(3,7)]
threes = []
fours = []
fives = []
while not fives:
	p = primelist.pop(0)
	for s in fours:
		if fitin(p,s): fives.append((p,)+s)
	for s in threes:
		if fitin(p,s): fours.append((p,)+s)
	for s in twos:
		if fitin(p,s): threes.append((p,)+s)
	for p2 in ones:
		if catprime((p,p2)): twos.append((p,p2))
	ones.append(p)
	print len(fours),len(threes),len(twos),len(ones)
print fives
"""
def fitin(x,xs): return not any([1 for y in xs if not catprime((x,y))])
"""
N = 10000
def primal(ps,i):
	if len(ps)==5: print ps
	p = primelist[i]
	if not fitin(p,ps): return
	for j in xrange(i+1,N): primal(ps+[p],j)
		
for i in xrange(N): primal([],i)
"""
N=100000
for i in xrange(N): 
	if fitin(primelist[i],(3,7,109,673)) and primelist[i] not in (3,7,109,673):
		print i