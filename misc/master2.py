import re
from random import choice
from time import time
code1 = """
70794 ;0 correct
34109 ;1 correct
12531 ;1 correct
90342 ;2 correct
39458 ;2 correct
51545 ;2 correct
"""

##39542

code2 = """
2321386104303845 ;0 correct
3847439647293047 ;1 correct
3174248439465858 ;1 correct
4895722652190306 ;1 correct
8157356344118483 ;1 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
2659862637316867 ;2 correct
4513559094146117 ;2 correct
5616185650518293 ;2 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
7890971548908067 ;3 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
1748270476758276 ;3 correct
"""




codes = re.findall(r'(\d+) ;',code1)
corrects = [int(c) for c in re.findall(r';(\d)',code1)]
N = len(codes)
L = len(codes[0])


	
def remover(c):
	for i in range(N):
		s=''
		for j in range(L):
			if codes[i][j]==c[j]: s+='_'
			else: s+=codes[i][j]
		codes[i]=s

def selector(cn,v):
	s = ''
	for i in range(L):
		if i==v:
			s+='_'
		else:
			s+=codes[cn][i]
	remover(s)
remover(codes[0])







for c in codes: print c
possibles = [[str(j) for j in range(10) if str(j)!=codes[0][i]] for i in range(L)]




	
def matches(a,b):
	m = 0
	for i in range(len(a)):
		if a[i]==b[i]:m+=1
	return m

def backtracker(x):
	if len(x)==L:
		for code,correct in zip(codes,corrects):
			if matches(x,code)!=correct: return None
		else: return x
	else:
		##check to see if it is good so far
		for code,correct in zip(codes,corrects):
			if matches(x,code)<=correct: continue
			else:
				return None		
		##try adding more
		for p in possibles[len(x)]:
			y = backtracker(x+p)
			if y is not None: return y
		return None
"""	
t = time()
print backtracker('')
print time()-t
"""
			

"""


possibles = [[str(j) for j in range(10) if str(j)!=codes[0][i]] for i in range(L)]

print possibles


def check(a,b,c):
	s=''
	matches = 0
	for i in range(L):
		s+=a[i]
		if a[i]==b[i]:matches+=1
		if matches>c:
			print s
			return i
	if matches==c:
		print s,'X'
		return None
	else: 
		print s,'O'
		return choice(range(L))
for m in range(10):
	a = [choice(p) for p in possibles]
	for n in range(10000):	
		for b,c in zip(codes[1:],corrects[1:]):
			x = check(a,b,int(c))	
			if x is None:continue
			else: 
				a[x] = choice(possibles[x])
				break
		else: print '-----',a
	
"""
		

					