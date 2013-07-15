##euler208b

"""
def permute(a,b):
	if b:
		pass
		return reduce(lambda x,y:x+y,[permute(a+b[i],b[0:i]+b[i+1:]) for i in range(len(b))])
	else:
		#nums.append(a)
		return [a]
	
for n in range(5):
	p = permute('','rl'*n)

	

	p = set(p)
	p = list(p)
	p.sort()
	for a in p[:len(p)/2]: print a
	print n,len(p)/2
	print '-'*10
	
"""
"""
def shifter(R,L,s=''):
	if R<0 or L<0: return []
	if R==0 and L==0: return [s]
	
	return shifter(R-1,L,s+'r') + shifter(R,L-1,s+'l')


#print [len(shifter(i,i)) for i in range(10)]
print shifter(3,3)
print '-'*5
print shifter(3,2,'l')
"""
from math import sin,cos
import time

d2p = 3.1415926 / 180.0

def round(x): return int(x*10000)/10000.0
##def round(x): return x
def move(m=0,s=(0,0,0),p = 5):
	x,y,a = s
	d = 360/float(p*2)
	if m:d=-d
	t = (d+a)*d2p
	x+=round(sin(t))
	y+=round(cos(t))
	a+=2*d
	return (x,y,a)

err = .01
def robotwalk(R,L,state=(0,0,0)):
	if R<0 or L<0: return 0
	if R==0 and L==0: return 1*(abs(state[0])<err and abs(state[1])<err)
	return robotwalk(R-1,L,move(1,state)) + robotwalk(R,L-1,move(0,state))

def robotwalk2(R,L,state=(0,0,0)):
	if R<0 or L<0: return 0
	x,y,a = state
	if (x*x+y*y)>(2*min(R,L)+3)**2: return 0
	if R==0 and L==0: return 1*(abs(x)<err and abs(y)<err)
		
	return robotwalk2(R-1,L,move(1,state)) + robotwalk2(R,L-1,move(0,state))

print 'asdf',robotwalk(10,0)+robotwalk(5,5)+robotwalk(0,10)



##the purpose here is to have the robot go halfway and leave a reverse marker. Everytime the robot reaches a previously set marker, it knows it can get home.
## but i dont think i am representing all the possibles that way... maybe a counting dict instead of a set
deaths = set()
def rb(n,R,L,state=(0,0,0)):
	if R<0 or L<0: return 0
	print R+L,n/2
	if R+L < n/2:
		x,y,a = state
		x = int(x*1000)
		y = int(y*1000)
		a = int(a%360)
		#print deaths,(x,y,a),(x,y,a) in deaths
		deaths.add((x,y,a))
		#a  = (a-180)%360
		return 1.0*((x,y,a) in deaths)
	return rb(n,R-1,L,move(1,state)) + rb(n,R,L-1,move(0,state))
print deaths


for n in range(1,2):
	start = time.time()
	deaths = set()
	print 'results',n*10,sum([rb(n*10,10*(n-i),10*(i)) for i in range(n+1)]),int(time.time()-start)
	print deaths