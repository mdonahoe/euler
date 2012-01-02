from math import sqrt
N=30
size(2.1*N,1.8*N)
slopes = {}
allsum =0
sq3 = sqrt(3)/2
stroke(0,.5,1,1)
strokewidth(0)
f = lambda y: HEIGHT-1-y*sq3
for n in xrange(1,N+1):
    linesum = 0
    for i in xrange(1,n):
        strokewidth(0)
        x,y = 2*n-i,2*i
        s = 1.0*y/x
        fill(.5,.5,.5)
        if s in slopes:
            x2,y2 = slopes[s]
            fill(0,.5,1)
            linesum+=1
            if n==30: oval(x,f(y),1,1)
            strokewidth(.1)
            if n==30:
                line(x+.5,f(y)+.5,x2+.5,f(y2)+.5)
                fill(0,0,0)
                oval(x2,f(y2),1,1)
        else:
            slopes[s]=(x,y)
            oval(x,HEIGHT-1-(y*sqrt(3)/2),1,1)
    allsum+=linesum
print 6*(allsum+N-1)