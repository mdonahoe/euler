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


n => [2.0*i/(2*n-i) for i in range(n)]

"""

def hexhidden(N):
	h = 0
	slopes = set()
	for n in xrange(N):
		for i in xrange(n):
			s = 2.0*i / (2*n-i)
			if s in slopes:
				h+=1
			else:
				slopes.add(s)
	print slopes
	return h

if __name__=='__main__':
	for i in range(5):
		print hexhidden(10),'---'
