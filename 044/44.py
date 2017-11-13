#euler 44
def pent(n): return  n*(3*n-1) / 2

pents = set()
n=1
loop=True
while loop:
	x = pent(n)
	for y in pents:
		if x-y in pents and x-2*y in pents: print x-2*y;loop=0
	pents.add(x)
	n+=1

	
