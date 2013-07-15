import math

def isPrime(num):
    if type(num) != int: return False
    if num == 2: return True
    if num < 2 or num % 2 == 0: return False
    return not any(num % i == 0 for i in range(3, int(math.sqrt(num))+1, 2))

count = 1.0 # do not forget 1
pcount = 0 # 1 is not a prime
x = 1
dx = 0
ratio = 1
while ratio>=0.1:
	dx+=2
	for i in range(4):
		x+=dx
		count+=1
		if isPrime(x): pcount+=1
		ratio = pcount/count
print dx+1