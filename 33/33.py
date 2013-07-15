#euler 33

"""
for i in range(1,10):
	for j in range(1,10):
		for k in range(1,10):
			if i==j:continue
			if float(str(i)+str(k)) / float(str(j)+str(k)) == i/float(j):
				print str(i)+str(k)+'/' +str(j)+str(k)
			if float(str(i)+str(k)) / float(str(k)+str(j)) == i/float(j):
				print str(i)+str(k)+'/' +str(k)+str(j)
				
"""

s = '123456789'

fracs = [i+k+'/'+k+j for i in s for j in s for k in s if float(i+k) / float(k+j) == float(i)/float(j) and i!=j]

num = 1
den = 1
for f in fracs:
	n,d = f.split('/')
	print n,d
	num*=int(n)
	den*=int(d)
print '%i/%i'%(num,den)

#dont know how to reduce it, but the answer is 100