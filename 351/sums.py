import sys
import array

def hexsum(N):
	sums = array.array('L', (0 for _ in xrange(N+1)))
	print 'init'
	for n in range(2,N):
		s = n-1-sums[n]
		x = 2*n
		while x<=N:
			sums[x]+=s
			x+=n
	return 6*(sum(sums)+N-1)

if __name__=='__main__':
	print hexsum(int(sys.argv[1]))