from math import *
W = 1000
size(W,W)
stroke(0)
fill(0)
COLORS = [color(0,.5+.5*random(),1-i/10.0) for i in range(10)]
class vector(object):
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y)
    def __mul__(self,scalar):
        return vector(self.x*scalar,self.y*scalar)
    __rmul__=__mul__
    def __div__(self,scalar):
        return vector(self.x/scalar,self.y/scalar)
    def __str__(self):
        return "<%.9f,%.9f>" %(self.x,self.y)

def mag(v):
    return sqrt(v.x*v.x+v.y*v.y)

def norm(v):
    return v/mag(v)

class Circle(object):
    def __init__(self,p,r,shell=False):
        self.p = p
        self.r = float(r)
        self.shell = shell
    def draw(self,N=0):
    	fill(N)
        if self.shell:nofill()
        oval(self.p.x-self.r,self.p.y-self.r,2*self.r,2*self.r)
    def area(self):
        return pi*self.r*self.r
        
def make_circle(x,y,r,shell=False):
    c = Circle(vector(x,y),r,shell)
    return c

def circle_gap(c1,c2):
    #returns the space between 2 circles
    dp = mag(c2.p-c1.p)
    if c1.shell or c2.shell:
        dr = abs(c1.r-c2.r)
    else:
        dr = c1.r+c2.r
    return dp-dr

def fill_gap(c1,c2,c3,n):
    c = Circle(c3.p,c3.r/10.0)
    dt = .1
    for i in range(500):
    	old = str(c.p)
        c.p-=dt*norm(c.p-c1.p)*circle_gap(c1,c)
        c.p-=dt*norm(c.p-c2.p)*circle_gap(c2,c)
        c.r+=dt*circle_gap(c3,c)
        if str(c.p)==old: break
    c.draw(COLORS[n+1])
    if n==0: return c.area()
    if n==5: print '.'
    return c.area()+fill_gap(c1,c2,c,n-1)+fill_gap(c1,c3,c,n-1)+fill_gap(c2,c3,c,n-1)
    
R = W/2
origin = vector(W/2,W/2)
outer = Circle(origin,R,1)
outer.draw()
rt3 = sqrt(3)
r = 3*R / (3+2*rt3)
dy = r*rt3 - 2*r/rt3
a = Circle(origin + vector(0,-r*2/rt3),r)
b = Circle(origin + vector(-r,dy),r)
c = Circle(origin + vector(r,dy),r)
s = 0
for cir in (a,b,c):
    cir.draw(COLORS[0])
    s+=cir.area()


N=4

s+=fill_gap(outer,a,b,N)
s+=fill_gap(outer,b,c,N)
s+=fill_gap(outer,c,a,N)
s+=fill_gap(a,b,c,N)

print (outer.area() - s) / outer.area()


