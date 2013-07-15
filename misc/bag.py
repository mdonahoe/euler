##generate the state space
def pluck(bag):
	"""
	Given a bag of items, return all possible combinations of (item, rest of items)"	
	
	>>> pluck('abc')
	[('a', 'bc'), ('b', 'ac'), ('c', 'ab')]
	
	"""
	return [(x,bag[0:i]+bag[i+1:]) for i,x in enumerate(bag)]
	
def pulls(bag,N,s=''):
	"""
	return all possible combinations of N pulls from a bag of strings
	
	>>>pulls('abcd',2)
	['ab', 'ac', 'ad', 'ba', 'bc', 'bd', 'ca', 'cb', 'cd', 'da', 'db', 'dc']
	
	"""
	if len(s)==N: return [s]
	return reduce(lambda x,y: x+y,[pulls(newbag,N,s+x) for x,newbag in pluck(bag)])


def combo1(grow,shrink):
	if not shrink: return grow
	growing = [combo(tuple(grow+(s,)),hrink) for s,hrink in pluck(shrink)]
	return growing
	
def permute(bag,box=tuple()):
	box = tuple(box)
	if not bag: return box
	boxes = []
	for b,ag in pluck(bag):
		new = combo(ag,box+(b,))
		if type(new)==list: boxes.extend(new)
		else: boxes.append(new)
	return boxes
	
def combo(items, n=None):
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[i+1:]
            for c in combo(rest, n-1):
                yield v + c

