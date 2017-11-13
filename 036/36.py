#euler36

def palindrome(n): return int(n)==int(str(n)[::-1])

def binary(n):
	s=''
	while n:
		s = str(n%2)+s
		n/=2
	if s is None: s='0'
	return s

print sum([i for i in range(1,10**6) if palindrome(i) and palindrome(binary(i))])
##872187
