from math import sin,cos,pi
from random import random
size(400,400)
S = 20
a = 0
stroke(0)
angles = set()
angles2 =set()
def robot(path,draw=True,q=5):
    #if not draw and sum(path)%q: return False
    a = 0
    dx = 0*random()*200+200
    dy = 0*random()*200+200
    x = dx
    y = dy
    ##if draw: print "sum = %i"%(sum(path))
    for p in path:
        ox,oy = x,y
        d = 360/float(q*2)
        if p=='l' or p==1 or p==True:d = -d
        angles.add((d+a)%360)
        x+=S*sin((d+a)*pi/180)
        y+=S*cos((d+a)*pi/180)
        a+=2*d
        angles2.add(a%360)
        if draw: line(ox,oy,x,y)
    return abs(x-dx)<.000001 and abs(y-dy)<.000001



def binary(x,d=0):
    ds = []
    while x:
        ds.append(x%2)
        x/=2
        d = max(d-1,0)
    return (0,)*d+tuple(ds[::-1])
    
def findclosed(n,q=5):
    n = int(n)
    N = 2**n
    L = len(binary(N-1))
    return sum([int(robot(binary(j,L),1,q)) for j in [i for i in range(N) if robot(binary(i,L),0,q)]])

	
var("teapots", NUMBER, 1, 5, 20)

findclosed(teapots)
