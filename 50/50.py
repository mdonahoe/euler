from prime import primelist as primes

i=0
while primes[i]<1000000:
	i+=1

primes = primes[:i-1]
sprimes = set(primes)
L = len(primes)
print L, L*L
runsum = []
total = 0
for p in primes:
	total+=p
	runsum.append(total)


def subset(i,j):
	if i==0: a = 0
	else: a = runsum[i-1]
	return runsum[j-1]-a



i=1
while subset(0,i)<1000000: i+=1
print i



#find the max diff
diff = i
i=0
while 1:
	p = subset(i,i+diff)
	if p in primes: print 'p = ',p; break
	i+=1
	if p>1000000:
		diff-=1
		i = 0
		print p, diff
		
		
		#997651