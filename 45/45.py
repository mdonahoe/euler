#euler45

fs = [lambda n:n*(n+1)/2,lambda n:n*(3*n-1)/2,lambda n:n*(2*n-1)]
ns = [1,1,1]

p=1

def equal(ls):
	if ls is None: return False
	p = ls[0]
	for i in ls:
		if i!=p: return False
		p=i
	return True

while p<40756:
	ys = [f(n) for f,n in zip(fs,ns)]
	if equal(ys):
		p=ys[0]
		print "T%i = P%i = H%i = %i"%tuple(ns+[p])
	xs = [(y,i) for i,y in enumerate(ys)]
	xs.sort()
	ns[xs[0][1]]+=1
	