q = 1700
N = 10
size(650,q)
stroke(0)

from random import shuffle
from math import sqrt
def circle(x,y,r):oval((x-r),(y-r),2*r,2*r)
R = 50
    



def drawpipe(rs,xx=q,draw=True):
    assert sum(rs)==840
    pr = 0
    h = 0
    for i,r in enumerate(rs):
        x = xx-R+r
        if i%2:x=xx+R-r
        if pr==0:y = r
        else: y = sqrt((r+pr)**2 - (2*R-r-pr)**2)
        h+=y
        y = q-h
        if draw:circle(x,y,r)
        pr = r
    H = y-r
    
    line(xx-R,q,xx-R,H)
    line(xx+R,q,xx+R,H)
    return q-H
        
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