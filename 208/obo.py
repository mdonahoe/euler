from math import sin,cos
import time
timestart = time.time()
d2p = 3.1415926 / 180.0
rr = 4
def solid(x): return int((10**rr)*round(x,rr))
def move(m=0,s=(0,0,0),p = 5):
	x,y,a = s
	d = 360/float(p*2)
	if m:d=-d
	t = (d+a)*d2p
	x += solid(sin(t))
	y += solid(cos(t))
	a = int((a+2*d))%360
	return (x,y,a)
	
def mv(s,d):
	x,y,a = s
	x1,y1,a1 = d
	return (x+x1,y+y1,a1)

def adder(d,k,n=1): d[k] = d.get(k,0)+n
def addup(ls):
	d = {}
	for l in ls: adder(d,l)
	return d
	
def sumd(a,b):
	d = dict(a)
	for k,n in b.iteritems():
		adder(d,k,n)
	return d

def travel(steps_left,state):
	if steps_left==0: return {state:1}
	ss = []
	for d in (0,1):
		s = move(d,state)
		t = travel(steps_left-1,s)
		ss.append(t)
	return reduce(sumd,ss)

angles = [360/5*i for i in range(5)]

state5 = dict([(a,travel(5,(0,0,a))) for a in angles])

def makemore(g_start,g_end):
	more = {}
	for angle,countstate in g_start.iteritems():
		d = {}
		for start,count1 in countstate.iteritems():
			mid = start[2]
			for end,count2 in g_end[mid].iteritems(): adder(d,mv(start,end),count1*count2)
		more[angle] = d
	return more

latest = state5
for i in range(6):
	latest = makemore(state5,latest)
	print latest[0][(0,0,0)]

halfway = latest[0]

counter = 0
for half,count1 in halfway.iteritems():
	x,y,a = half
	counter+=count1*latest[a].get((-x,-y,0),0)
print 'count',counter
print time.time()-timestart