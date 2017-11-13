##project euler
##problem 32


def permute(a,b):
	if b:
		return reduce(lambda x,y:x+y,[permute(a+b[i],b[0:i]+b[i+1:]) for i in range(len(b))])
	else:
		#nums.append(a)
		return [a]

nums = []
def f(x):
	n = int(x[5:])
	if int(x[0])*int(x[1:5])==n or int(x[0:2])*int(x[2:5])==n and n not in nums: nums.append(n)
	
	


for a in permute('','123456789'): f(a)
print nums, sum(nums)
##[5796, 5346, 4396, 7254, 6952, 7852, 7632] 45228


