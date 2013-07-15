#euler47
from prime import primelist as primes
#primes = [2,3,5,7,11,13,17]

class Memoize:
    """Memoize(fn) - an instance which acts like fn but memoizes its arguments
       Will only work on functions with non-mutable arguments
    """
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if not self.memo.has_key(args):
            self.memo[args] = self.fn(*args)
        return self.memo[args]


def primer(x):
	if x==1: return []
	factors = []
	for p in primes:
		if x%p==0:
			factors = [p]
			factors.extend(primer(x/p))
			return factors 
			
primer = Memoize(primer)

def count(ns):
	d = {}
	for n in ns:
		d[n] = d.get(n,0)+1
	return d

def newfactors(fs): return [k**v for k,v in count(fs).iteritems()]

n=10
s=[]
loop=1
nn=4
while loop:
	n+=1
	factors = newfactors(primer(n))
	if len(factors)!=nn:
		s = []
		continue
		
	s.append(factors)
	print n
	
	if len(s)==nn:
		nums=[]
		for x in s: nums.extend(x)
		print n-nn+1,n-nn+2,n,s,nums
		if len(set(nums)) == len(nums):
			print n-nn+1
			loop = False
		else: s = s[1:]
		
		#134043
