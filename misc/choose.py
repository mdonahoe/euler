def choose(n,k):
	if k==0: 
		n=-1
		yield None
	x = range(k)
	while n>=k:
		i=k-1
		yield tuple(x)
		x[i]+=1
		while x[i]>=n:
			i-=1
			if i==-1: break
			x[i]+=1
			for j in range(i+1,k):
				x[j] = x[j-1]+1
				if x[j]==n:x[i]=n
		if i== -1: break

##if __name__=="__main__":
##	for i in choose(10,2):print i