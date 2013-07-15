"""evaluates poker hands given in the file poker.txt



pair checking could be done better. right now it is very redundant."""

from combos import combo,combo_and_cruft
def any(xs):
	for x in xs:
		if x: return x
	return False

def all(xs):
	if not xs: return False
	for x in xs:
		if not x: return False
	return xs[-1]

def allequal(xs):
	if (not any(1 for a in xs for b in xs if a!=b)): return xs[0]
	return False

ranks = '23456789TJQKA'
rank_map = dict([(c,i+2) for i,c in enumerate(ranks)])
print rank_map

class card:
	def __init__(self,s):
		self.c = s
		self.rank = rank_map[s[0]]
		self.suit = s[1]
	def __cmp__(self,other):
		return cmp(self.rank,other.rank)
	def __str__(self):
		return self.c
	def __repr__(self): return str(self)

def straight_check(cards):
	cs = [c.rank for c in cards]
	cs.sort()
	
	if cs[0]==2 and cs[-1]==14: cs = [1]+cs[:-1]
	low = cs[0]
	for c in cs:
		if c!=low: return False
		low+=1
	
	return cs[-1]

def flush_check(cards):
	if not any(c.suit!=d.suit for c in cards for d in cards):
		cs = [c.rank for c in cards]
		cs.sort()
		return cs[-1]
	return False
	

	
def four(cards):
	cs = [c.rank for c in cards]
	return any(allequal(d) for d in combo(cs,4))

def fullhouse(cards):
	cs = [c.rank for c in cards]
	return any((a[0],b[0]) for a,b in combo_and_cruft(cs,3) if allequal(a) and allequal(b))

def three(cards):
	cs = [c.rank for c in cards]
	return any(allequal(d) for d in combo(cs,3))


def twopair(cards):
	cs = [c.rank for c in cards]
	##cs = cards[:]
	p = any(allequal(d) for d in combo(cs,2))
	if not p: return False
	cs = [c for c in cs if c!=p]
	p2 = any(allequal(d) for d in combo(cs,2))
	if not p2: return False
	if p>p2: return (p,p2)
	return (p2,p)
	

def pair(cards):
	cs = [c.rank for c in cards]
	return any(allequal(d) for d in combo(cs,2))
	
def highcard(cards):
	cs = [c.rank for c in cards]
	cs.sort()
	cs.reverse()
	return cs
		
def bestfirst(x,lst): lst.append(not any(lst) and x)

class hand:
	def __init__(self,cards):
		self.cards = cards
		self.cards.sort()
		scores = []
		fl = flush_check(cards)
		st = straight_check(cards)
		
		#straight flush?
		#if fl==st: scores.append(fl)
		#else: scores.append(False)
		scores.append(fl and st)
		
		#four of a kind?
		bestfirst(four(cards),scores)
		
		#fullhouse
		bestfirst(fullhouse(cards),scores)
		
		#flush
		bestfirst(fl,scores)
		
		#straight
		bestfirst(st,scores)
		
		#three of a kind
		bestfirst(three(cards),scores)
		
		#Two Pair
		bestfirst(twopair(cards),scores)
		
		#pair
		bestfirst(pair(cards),scores)
		
		#highcards
		scores.append(highcard(cards))
		self.scores=scores
	def __cmp__(self,other):
		return cmp(self.scores,other.scores)

f = file('poker.txt')
games = f.read().split('\n')
f.close()

p1 = 0
for game in games:
	
	hand1 = hand([card(game[i:i+2]) for i in range(0,15,3)])
	hand2 = hand([card(game[i:i+2]) for i in range(15,30,3)])
	print hand1.cards,hand1.scores
	print hand2.cards,hand2.scores
	print hand1>hand2
	p1+=hand1>hand2
print p1



