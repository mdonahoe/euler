#euler75
def iterlen(x):
	n=0
	try:
		while x.next(): n+=1
	except StopIteration: pass
	return n

def rights(N):
	for c in range(N/2,2,-1):
		for b in range(N-c,1,-1):
			a = N-c-b
			if a<1: continue
			if a>b: break
			##print a,b,c
			if a*a+b*b==c*c: yield (a,b,c)
			
def summer(N,n,x=1):
	if n>1:
		while x<=(N/n):
			for y in summer(N-x,n-1,x): yield (x,)+y
			x+=1
	else: yield (N,)

def isright(tri):
	a,b,c = tri
	return a*a+b*b==c*c

def righter(N):
	x = summer(12,3)
	n=0
	for a,b,c in summer(12,3):
		if a*a+b*b==c*c: n+=1
		if n>1: return 0
	return n

"""			
12
6,5,1
6,4,2
6,3,

996
bigmac-2:Desktop Matt$ python rightangles.py 


(3, 4, 5),
(5, 12, 13), 
(8, 15, 17),
(7, 24, 25),
(20, 21, 29),
(12, 35, 37),
(9, 40, 41),

{96: (3, 4, 5),
80: (8, 15, 17),
36: (3, 4, 5),
70: (20, 21, 29),
72: (3, 4, 5),
12: (3, 4, 5),
48: (3, 4, 5),
40: (8, 15, 17),
56: (7, 24, 25),
24: (3, 4, 5),
30: (5, 12, 13)}








"""

def triple(u,v):
	a = 2*u*v
	b = u*u-v*v
	c = u*u+v*v
	if a>b: a,b=b,a
	return (a,b,c)

def gcd(a,b):
	while b:
		a,b = b,a%b
	return a
	
def gcd3(t):
	a,b,c = t
	return gcd(gcd(a,b),c)

if __name__=='__main__':
	lefts = dict()
	N = 1500000
	L = 0
	rights = dict()
	u = 2
	v = 0
	while 1:
		v = 1
		s = sum(triple(u,v))
		print s,L
		if s>N: break
		while v<u:
			t = triple(u,v)
			if gcd3(t)>1:
				v+=1
				continue
			s = sum(t)
			S = s
			while S<=N:
				if S in lefts: 
					S+=s
					continue
				if S in rights:
					del rights[S]
					lefts[S] = 1
					S+=s
					continue
				rights[S] = t
				S+=s
			v+=1	 
		u+=1
		#print a+b+c
	print len(rights.keys())
	print rights
	
	
	
	
	
	
	