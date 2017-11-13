import phi
def permuto(a,b):
	a = [i for i in str(a)]
	b = [i for i in str(b)]
	a.sort()
	b.sort()
	return a==b

j = 0
m = 100000000000
for i in xrange(2,10**7):
	p = phi.phi(i)
	if permuto(i,p):
		n = i/float(p)
		if n<m:
			j=i
			m=n
			print j