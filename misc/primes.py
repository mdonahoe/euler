#primes.py
import math


class Primes:
	def __init__(self,limit):
		self.limit = limit
		self.nums = sieve(limit)
	def get_list(self):
		return [i for i,n in enumerate(self.nums) if not n]
	def is_prime(self,n):
		assert n<self.limit, "prime too large: %s > %s"%(n,self.limit)
		return self.nums[n]==0
	
def sieve(N):
	#do the sieve
	nums = [0]*N;nums[0:2]=[1,1]
	n=2
	stop = math.sqrt(N)
	while n<stop:
		m = n*n
		while m<N:
			nums[m]+=1
			m+=n
		n+=1
		while nums[n]>0: n+=1
	return nums

if __name__=="__main__": print Primes(100).get_list()
