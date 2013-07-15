import sys,time
def equal(xs):
	v = xs[0]
	for x in xs:
		if x!=v: return False
	return True

def combolist(x):
	if not x: return []
	cs = combolist(x[1:])
	for c in cs[:]:
		cs.append([x[0]]+c)
	cs.append([x[0]])
	return cs

def remove(allpiles,frompiles,N):
	piles = []
	for i,p in enumerate(allpiles):
		if i in frompiles: piles.append(p-N)
		else: piles.append(p)
	for p in piles:
		if p<0:
			print piles,allpiles,frompiles,N
			sys.exit(0)
	return piles


games = {}
def game(piles):
	"""
		Can I force a win?
		
		try a bunch of moves, and if the 2nd player cant force a win, then I win.
		
	"""
	##sort the piles
	piles = list(piles)
	piles.sort()
	piles = [x for x in piles if x] #remove empties
	piles = tuple(piles)
	if piles in games: return games[piles]
	if not piles: return False #empty? already lost
	if equal(piles): return True
	
	for c in combolist(range(len(piles))):
		max_N = piles[c[0]]
		for i in range(max_N):
			newpiles = remove(piles,c,i+1)
			if not game(newpiles): 
				games[piles] = True
				return True
	games[piles] = False
	return False
	

N = 1001
start = time.time()
for a in range(N):
	if a>0: print (time.time()-start)/a*(N-a)
	for b in range(a,N):
		for c in range(b,N):
			game((a,b,c))

print sum([sum(k) for k,v in games.iteritems() if not v])