
def f(n,d):
	##figures it out without having to look at all the numbers before n
	ns = [int(i) for i in reversed(str(n))]
	s = sum([10**i*(n/(10**(i+1)))+(ns[i]==d)*(n%10**i+1)+(ns[i]>d)*10**i for i in range(len(ns))])
	return s

def g(n,d): 
	##useful function so I can search for zeros.
	return n-f(n,d)
	
def s(d):
	##this function moves forward looking for g(n,d)==0
	##it tries to search the space efficiently by skipping ahead without overshooting
	n = 0
	s = 0
	old = 0
	while n<10**20:
		if g(n,d)==0:
			s+=n
			n,old = n+1,n
		else:
			if (abs(g(n,d))-abs(g(old,d)))>0: ##if we are moving away from zero
				dx = abs(g(n,d))/2## take larger steps
			else:
				dx = abs(g(n,d))/10 ##otherwise take smaller steps
			n,old = n+max((1,dx)),n
	return s

print sum([s(i) for i in range(1,10)])

##21295121502550