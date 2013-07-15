#euler49

from prime import primelist as primes
from bag import combo

p=0
i=0
digits4=[]
while p<10000:
	p = primes[i]
	if p>1000: digits4.append(p)
	i+=1
	
#now we have all the 4 digit primes

def isperm(x,y):
	x = list(str(x))
	y = list(str(y))
	x.sort()
	y.sort()
	return sum([1 for a,b in zip(x,y) if a!=b])==0


#split the list into lists of permuted primes with at least 3 primes
def permoot(ps):
	x = list(ps)[0]
	xs = [p for p in ps if isperm(p,x)]
	ps = set(ps).difference(set(xs))
	return xs,ps
ps = digits4	
ms = []
while ps:
	xs,ps = permoot(ps)
	if len(xs)>2: ms.append(xs)

#convert all groups of 4+ into multiple groups of 3

ns = []
for m in ms:
	if len(m)==3: ns.append(m); continue
	ns.extend(combo(m,3))

for n in ns:
	n.sort()
	if n[1]-n[0]==n[2]-n[1]: print n
	
	
