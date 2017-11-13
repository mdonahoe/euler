def f(n):
	if n<=1: return 1
	return n*f(n-1)
	
def factdigits(n):
	s=0
	while n:
		s+=f(n%10)
		n = n/10
	return s
	
def chain(n):
	s = set([n])
	while 1:
		n = factdigits(n)
		if n in s: return len(s)-1
		s.add(n)


def test():
	ns = []
	for i in range(10**6):
		c = chain(i)
		#print i,c
		if c==59: ns.append(i)
	print len(ns)
	print ns
	
print chain(69)