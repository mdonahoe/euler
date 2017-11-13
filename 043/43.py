#euler43

def pandigital(x):
	x = str(x)
	for n in '0987654321':
		if n in x: continue
		else: return False
	return True
	
	
def pandig(x='',d='1234567890'):
	if not d: return [x]
	nums = []
	for i in range(len(d)):
		ds = d[:i]+d[i+1:]
		nums.append(pandig(x+d[i],ds))
	return reduce(lambda x,y:x+y,nums)
	
	##reduce(lambda x,y:x+y,[pandig(x+d[i],d[:i]+d[i+1:]) for i in range(len(d))])

def digpan(ds,x=''): return (not ds)*[x] or reduce(lambda x,y:x+y,[digpan(ds[:i]+ds[i+1:],x+ds[i]) for i in range(len(ds))])

primes = [2,3,5,7,11,13,17]

def divisibility(x):
	x = str(x)
	for i in range(7):
		if int(x[i+1:i+4])%primes[i] == 0: continue
		else: return False
	return True

##print sum([x for x in xrange(1023456789,9876543211) if pandigital(x) and divisibility(x)])
print pandigital(1406357289)
print divisibility(1406357289)
def doit(): print sum([int(x) for x in digpan('1234567890') if divisibility(x)])
doit()
