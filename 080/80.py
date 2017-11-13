lr = lambda N:((N+'00')[:2],N[2:])
from math import sqrt

isqrt = lambda x: int(sqrt(x))

def up2(p,c):
	x = 10
	while 1:
		q = (20*p+x)*x
		#print q
		if q<=c: return x,c-q
		x-=1

def spacin(n):
	if n==0: return ''
	n = str(n)
	if len(n)==2: return n
	return '0'+n

def root(n,M=100):
	m = -1
	L,R = str(float(n)).split('.')
	if len(L)%2: L='0'+L
	dp = len(L)/2
	R = L+R
	L = ''
	p = 0
	while 1:
		m+=1
		#if m==dp: yield '.'
		if m>=M: break
		L,R = L+(R+'00')[:2],R[2:]
		d,r = up2(p,int(L))
		#print L,R,d,r
		yield d
		if r==0: L = ''
		else: L = str(r)
		p = 10*p+d

print sum([sum([d for d in root(n,100)]) for n in range(1,101) if sqrt(n)!=isqrt(n)])		