"""
project euler #68
by matt donahoe and doug ellwanger
"""
def test(outer,inner):
	#assuming len(inner)==2
	total = outer[0]+sum(inner)
	all = outer+inner
	inner2 = inner[:]
	for o in outer[1:-1]:
		next = total - o - inner2[-1]
		if next in all or next<1 or next>10: 
			#print all,next, 'already used'
			return False
		inner2.append(next)
		all.append(next)
	
	if inner2[0]!=(total - outer[-1] - inner2[-1]): return False
	s = ''
	L = len(outer)
	for i in range(L):
		s+=str(outer[i])+str(inner2[i])+str(inner2[(i+1)%L])
	return int(s)


def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xpermutations(items):
    return xcombinations(items, len(items))

m = 0
for outer in xpermutations([7,8,9,10]):
	outer = [6]+outer
	#print outer
	for inner in xcombinations([1,2,3,4,5],2):
		n = test(outer,inner)
		if n>m: m = n
print m