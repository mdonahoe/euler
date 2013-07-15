q = 1700
N = 10
size(650,q)
s = 1
stroke(0)
q = 1700

from vector import *
from random import shuffle
def circle(p,r):oval(s*(p.x-r),s*(p.y-r),s*2*r,s*2*r)
R = 50


def test(v,c,n):
    if c:
        if v>n: return n
        return v
    else:
        if v<n: return n
        return v

def satisfy(a,b,m):
    dp = b-a
    dm = mag(dp)
    dist = (m-dm)*dp/dm
    b.y+=dist.y
    return (m-dm)
    



def drawpipe(rs,xx=q,draw=True):
    assert sum(rs)==840
    h=0
    prev = None
    for i,r in enumerate(rs):
        x = xx-R+r
        if i%2:x=xx+R-r
        p = vector(x,q-2*h-r)
        h+=r
        while prev:
            if abs(satisfy(prev[0],p,r+prev[1]))<.000001: break
        if draw:circle(p,r)
        prev = (p,r)
    H = p.y-r
    line(xx-R,q,xx-R,H)
    line(xx+R,q,xx+R,H)
    return H
        
print drawpipe(range(30,51),400)

sd = []
ad = []
for i in range(21):
    r = [50-i]
    if i%2: sd=sd+r
    else: ad=r+ad
print drawpipe(sd+ad,250)
qs  = range(30,51)
shuffle(qs)
print drawpipe(qs,100)
print drawpipe([((i+1)%2)*(30+i/2)+(i%2)*(50-i/2) for i in range(21)],550)

print sum(range(30,51)),sum([((i+1)%2)*(30+i/2)+(i%2)*(50-i/2) for i in range(21)])