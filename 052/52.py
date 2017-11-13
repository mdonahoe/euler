def d(x,y): #different digits?
	a = list(str(x))
	b = list(str(y))
	if len(a)!=len(b): return 1
	a.sort();b.sort()
	return sum([1 for aa,bb in zip(a,b) if aa!=bb])
	
x = 1
while sum([d(x,i*x) for i in range(2,7)]): x+=1
print x