import time


def powerset(xs):
	ps = [[]]
	for x in xs:
		ps = ps + [y+[x] for y in ps]
	return ps


t = time.time()
N = 250
M = 10**16
d = [0]*N
for i in xrange(1,250251):
	x = pow(i,i,N)
	d2 = d[:]
	for j in xrange(N):
		y = (x+j)%N
		d2[y] = (d2[y]+d[j])%M
	d2[x]+=1
	d = d2[:]
	#if (i%1000==0): print i,d[0]

print d[0],time.time()-t

#print sum([1 for s in powerset([n**n for n in range(1,11)]) if s!=[] and (sum(s)%4)==0])
