from math import sin,cos
import time

d2p = 3.1415926 / 180.0
rr = 4
##def round(x): return int(x*rr)
##def unround(x): return x/float(rr)

##def round(x): return x

def fuck(x): return int((10**rr)*round(x,rr))
def move(m=0,s=(0,0,0),p = 5):
	x,y,a = s
	d = 360/float(p*2)
	if m:d=-d
	t = (d+a)*d2p
	x += fuck(sin(t))
	y += fuck(cos(t))
	a = int((a+2*d))%360
	return (x,y,a)

states = set()
for i in range(5):
	a = 360/5*i
	for m in (0,1):
		states.add((a,)+move(m,(0,0,a)))
	

starts = {}

for s in states:

	starts[s[0]] = starts.get(s[0],[])+[s[1:]]


def mv(s,d):
	x,y,a = s
	x1,y1,a1 = d
	return (x+x1,y+y1,a1)

def grow(n,s):
	if n==0: return (s,)
	stops = []
	for d in starts[s[2]]:
		ns = mv(s,d)
		stops.extend(grow(n-1,ns))
	return stops

def count(n,s=(0,0,0)):
	if n==0: return 1*(s[0]==s[1]==0)
	return sum([count(n-1,mv(s,d)) for d in starts[s[2]]])

pts = {(0,0,0):[]}
q = [(0,0,0)]
start = time.time()
N = 20
for i in range(N):
	newq = []
	for s in q:
		for d in starts[s[2]]:
			ns  = mv(s,d)
			if ns in pts:
				pts[ns].append(s)
			else:
				newq.append(ns)
				pts[ns]=[s]
		q = newq
	print "len %i in %.2f"%(len(pts),time.time()-start)

def backtrace(n,p):
	if n==0: return 1*(p==(0,0,0))
	return sum([backtrace(n-1,b) for b in pts[p]])
print "tracing...."
start = time.time()	
print "num %i in %.2f"%(backtrace(N,(0,0,0)),time.time()-start)