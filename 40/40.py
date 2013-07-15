#euler40
from math import log

def digiter(max):
	p=1
	L=0
	d = 1
	n=0
	while 1:
		n+=1
		s = str(n)
		for j in range(len(s)):
			L+=1
			if L==d:
				print L,n,s[j]
				p*=int(s[j])
				d*=10
				if d>max: return p
print digiter(10**6)
#210