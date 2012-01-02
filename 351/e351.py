"""hexagonal orchards"""

"""
The main idea here is that point obscure other points if
the slopes are the same.

Also there is rotational symmetry so just do a single triangle
and multiply by 6.

Slopes:
each point is an X,Y except just for the grid.

0:(0,0)
1:(2,0)
2:(3,2),(4,0)
3:(4,4),(5,2),(6,0)
4:(5,6),(6,4),(7,2),(8,0)
5:(6,8),(7,6),(8,4),(9,2),(10,0)
2*2
3*2

n => [2.0*i/(2*n-i) for i in range(n)]

"""
import sys
def hexhidden(N):
	h = 0
	slopes = set()
	for n in xrange(1,N+1):
		for i in xrange(n):
			s = 2.0*i / (2*n-i)
			xy = (2*n-i,2*i) # just for testing
			if s in slopes:
				h+=1
				#print xy # show me the coords of every blocked point
			else:
				slopes.add(s)
	return 6*h
print hexhidden(int(sys.argv[1]))