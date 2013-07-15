import time
def unisort(x,list,i=0):
	while i<len(list) and x>list[i]:i+=1
	if i>=len(list) or x<list[i]: list.insert(i,x)


def hamming(seeds,limit,f):
	i=0
	while i<len(seeds):
		x = seeds[i]
		j=0
		while 1:
			y = x*seeds[j]
			if y>limit: break
			f(y,seeds,j) ##add to list
			j+=1
		print i,len(seeds)
		i+=1


def hammer(x,seeds,limit): return x<=limit and 1+sum([hammer(x*s,seeds[i:],limit) for i,s in enumerate(seeds)])
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

t = time.time()
#print (lambda a,b,c: a(a,b,c))(lambda f,x,skip: x<=1000000000 and 1+sum([f(f,x*(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)[i],i) for i in xrange(skip,25)]),1,0)
hammer(1,primes,10**9)
print time.time()-t


