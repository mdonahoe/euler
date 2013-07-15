#euler38

def pandigital(n):
	s = str(n)
	if len(s)!=9: return False
	x = set([str(i) for i in range(1,10)])
	for i in s:
		if i in x:
			x.remove(i)
		else: return False
	return True

def pit(n):
	s = ''
	i=0
	while len(s)<9:
		i+=1
		s+=str(i*n)
	return int(s)

ps = [pit(i) for i in range(10000) if pandigital(pit(i))]
ps.sort()
ps.reverse()
print ps[0]

#932718654