"""
s=0
for i in range(200000):
	s+=sum([1 for x in str(i) if int(x)==9])
	print i,s
	
"""
from math import *
from random import random
def sign(x):
	if x<0: return -1
	return 1
	


def f(n,d):
	ns = [int(i) for i in reversed(str(n))]
	s = sum([10**i*(n/(10**(i+1)))+(ns[i]==d)*(n%10**i+1)+(ns[i]>d)*10**i for i in range(len(ns))])
	return s


def g(n,d): return n-f(n,d)


def h(x): return 5<=x
	
def ssearch(func,min,max,n):
	if n==0: return 'fail'
	if min==max: return min
	x = int(round((min+max)/2.0))
	print min,x,max,func(x)
	if func(x): return search(func,min,x,n-1)
	return search(func,x,max,n-1)
	
def search(func,low,high):
	while high-low>1:
		probe = (high+low)/2
		if func(probe): high = probe
		else: low = probe
	
	if func(low): return low
	return high
	
	

def find(x):
	return 0>=g(x,1)


def doit1():
	low = 0
	high = 1
	s=0
	while s<22786974071:
		guess = search(find,low,high)
		if g(guess,1)==0: 
			s+=guess
			print s-22786974071
			low = guess+1
			high = high+2
		else:
			low = high
			high = 2*high

def doit2():
	n = 0
	step = 1
	ns =[]
	value = 0
	for i in range(1000):
		value,old = g(n,1),value
		if sign(value)!=sign(old):
			n = search(find,n-step,n)
			step=1
		if value==0: 
			ns.append(n)
		n = n+step
		step+=abs(value)
		
	print ns,sum(ns)
	

def findem(d):
	n = 0
	ns=[]
	prev = 1
	r=1.0
	for i in range(1000):
		n = int(round(n))
		print n,g(n,d),prev,r
		if n in ns:
			r=sign(r)*-1
			n+=prev*r
		elif g(n,d)==0:
			ns.append(n)
			n+=r*prev
		else:
			if sign(prev)!=sign(g(n,d)): r*=.9
			prev = sign(g(n,d))
			n+=r*g(n,d)
			
	return ns
	
	

def findem2(d):
	n = 0
	ns=[]
	up=0
	old = 0
	mx = 10**20
	while n<mx:
		print n, g(n,d)
		if g(n,d)==0:
			ns.append(n)
			n,old = n+1,n
		else:
			up = (abs(g(n,d))-abs(g(old,d)))
			if up>0:
				dx = abs(g(n,d))/2
			else:
				dx = abs(g(n,d))/10
			n,old = n+max((1,dx)),n
	return ns

s=0
for i in range(1,10):
	s+=sum(findem2(i))
print s


##21295121502550