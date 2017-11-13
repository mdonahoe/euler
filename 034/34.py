##project euler 34

def factorial(x):
	if x<=1: return 1
	return x*factorial(x-1)

fs = [1,1]
ds = {'0':1,'1':1}
for i in range(2,10):
	fs.append(fs[-1]*i)
	ds[str(i)] = fs[-1]


def curious(x):
	y = sum([ds[i] for i in str(x)])
	if y<x: return -1
	if y==x: return 0
	return 1

s = 0
while curious(s)>0:
	s = s*10+9
print s
"""
def funk(x,t):
	if x>9999999: return 0
	r = 0
	if t==x:
		r = x
		print r
	return r + sum([funk(x*10+i,t+fs[i]) for i in range(10)])

print "sum = "+str(sum([funk(i,fs[i]) for i in range(1,10)]))

"""
x=3
nums = []
while x<s:
	if curious(x)==0: nums.append(x)
	x+=1
	if x%1000000==0: print x
print nums,sum(nums)



##145, 40585