#euler24

def all_perms(s):
    if len(s) <=1:
        yield s
    else:
        for perm in all_perms(s[1:]):
            print s,perm
            for i in range(len(perm)+1):
                yield perm[:i] + s[0:1] + perm[i:]

def permute(s):
	if len(s)==1:yield 1
	elif len(s)==2:
		yield s
		yield s[1]+s[0]
	else:
		for i in range(len(s)-1):
			for p in permute(s[:i]+s[i+1:]):yield s[i]+p
		for p in permute(s[:-1]):yield s[-1]+p

for i,p in zip(range(1000000),permute('0123456789')): pass
print i,p

