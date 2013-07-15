#euler28

def f(n):
	if n==1:return 1
	if n%2==0:return 0 #even numbers not allowed
	#sum of the corners at level n
	return 4*n*n-6*n+6
	
def g(n):
 return sum([f(i) for i in range(1,n+1,2)])

print g(5),g(1001)
	
