#e61

def gen(f):
	xs = []
	n = 0
	x = 0
	while x<10000:
		n+=1
		x = f(n)
		if x>999: xs.append(x)
	return xs

tris = gen(lambda n:n*(n+1)/2)
sqrs = gen(lambda n:n*n)
pents= gen(lambda n:n*(3*n-1)/2)
sexs = gen(lambda n:n*(2*n-1))
septs= gen(lambda n:n*(5*n-3)/2)
octs = gen(lambda n:n*(3*n-2))

shapes=[ tris,sqrs,pents,sexs,septs,octs]
p=1
for s in shapes: print len(s);p*=len(s)
print 'p',p

