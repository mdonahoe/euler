import math

def isPrime(num):
    if type(num) != int: return False
    if num == 2: return True
    if num < 2 or num % 2 == 0: return False
    return not any(num % i == 0 for i in range(3, int(math.sqrt(num))+1, 2))

count = 1 # do not forget 1
pcount = 0 # 1 is not a prime
z = 1
a = 1
b = 1
c = 1
d = 1
i = 1
ratio = 1

while ratio >= 0.1:
    aa = a + 4 * z
    a = aa
    if isPrime(aa):
        pcount +=1
    bb = b + 4 * z - 2
    b = bb
    if isPrime(bb):
        pcount +=1
    cc = c + 8 * i
    c = cc
    if isPrime(cc):
        pcount +=1
    dd = d + 8 * i - 2
    d = dd
    if isPrime(dd):
        pcount +=1
    z += 2
    i += 1
    count += 4
    ratio = 1.0 * pcount / count

print "Found:",(i-1)*2+1,ratio,dd