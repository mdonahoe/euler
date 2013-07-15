from __future__ import division
combos = range(10**4)
unique = set()
for c in combos:
	s = list('%04d'%c)
	s.sort()
	unique.add(tuple(s))
print unique
print 10**4,len(unique)

ops = '+-*/'

nums = set()
def tryval(s):
	try: return eval(s)
	except ZeroDivisionError: return 10**10
	
for i in range(0):
	x,y,z = [int(j) for j in list('%03d'%i)]
	if z>3 or y>3 or x>3: continue
	x,y,z = ops[x],ops[y],ops[z]
	for a,b,c,d in unique:
		nums.add(tryval('(((%s%s%s)%s%s)%s%s)'%(a,x,b,y,c,z,d)))
		nums.add(tryval('((%s%s%s)%s(%s%s%s))'%(a,x,b,y,c,z,d)))
		
		
print 'wrong!'


def xcombinations(items, n):
    if n==0: yield []
    else
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xpermutations(items):
    return xcombinations(items, len(items))



def calcnums(ns):
	nums = set()
	for i in range(10**3):
		x,y,z = [int(j) for j in list('%03d'%i)]
		if z>3 or y>3 or x>3: continue
		x,y,z = ops[x],ops[y],ops[z]
		for a,b,c,d in xpermutations(ns):
			nums.add(tryval('(((%s%s%s)%s%s)%s%s)'%(a,x,b,y,c,z,d)))
			nums.add(tryval('((%s%s%s)%s(%s%s%s))'%(a,x,b,y,c,z,d)))
	nums = list([n for n in nums if n>0 and int(n)==n])
	nums.sort()
	prev = nums[0]
	chain = 1
	maxchain = 0
	for n in nums[1:]:
		if (n-1)!=prev: 
			maxchain = max(maxchain,chain)
			chain =0
		chain+=1
		#print n,chain
		prev = n
	return maxchain

chains = {}
for aa in range(10):
	for bb in range(aa+1,10):
		for cc in range(bb+1,10):
			for dd in range(cc+1,10):
				chains[(aa,bb,cc,dd)] = calcnums((aa,bb,cc,dd))

print ''.join([str(i) for i in max([(v,k) for k,v in chains.iteritems()])[1]])


