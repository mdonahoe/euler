from prime import primelist
	
primes = set(primelist)
tried = set()
def comb(items, n=None):
    if n is None: n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1: yield v
        else:
            rest = items[i+1:]
            for c in comb(rest, n-1):
                yield v + c
                
def fullcomb(items):
	combos = []
	for i in range(1,len(items)+1): combos.extend(comb(items,i))
	return combos
	
fc={}
for i in range(10): fc[i] = fullcomb(range(i))

i=70000 ##ran it once and crashed at this high
loop=1
while loop:
	p = str(primelist[i])
	for c in fc[len(p)]:
		#try a particular pattern
		xx = []
		
		q = list(p)
		for k in c: q[k] = 'X'
		r = ''.join(q)
		if r in tried: continue
		
		for j in '1234567890':
			s = int(r.replace('X',j)) 
			if s in primes: xx.append(s)
		tried.add(r)
		
		if len(xx)==8: print 'xx',xx; ##cant find a good way to exit the loop
		
	i+=1
	
	
	##121313