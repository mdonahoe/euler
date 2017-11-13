from time import time
import sys
sys.setrecursionlimit(100000)


def h(n,r=0):
	if n<=1: return 1
	m = min(n,r)
	return h(n-1,r+1)+h(m,r-m)

def p(n,r=0):
	#print (n,r)
	if n<=1:
		#print '1',(n,r)
		return 1
	m = min(n,r)
	return (p(n-1,r+1)+p(m,r-m))%1000000

class memo:
	def __init__(self,f):
		self.f = f
		self.d = {}
	def __call__(self,*args):
		if not args in self.d:
			self.d[args] = self.f(*args)
		#else: print 'huge cache savings!' #lol, puns

		return self.d[args]
"""
p = memo(p)

n = 1
while p(n): n+=1; print n
print n
"""


def theway(n,m=1000000):
	ws = [0]*n
	ws[0] = 1
	for i in range(1,n):
		print 'i',i
		for j in range(i,n):
			ws[j] = (ws[j]+ws[j-i])%m
		if ws[i]==0: return j
	return 0
print theway(100000)

	

