"""
#429

step 1: print the unitary divisors of n!
"""
from prime_factorial import multiplicity

def powerset(xs):
    n = 2**(len(xs))
    x = 0
    while x < n:
        i = x
        a = []
        j = 0
        while i:
            if i%2: a.append(xs[j])
            j+=1
            i/=2
        yield a
        x += 1

def factorial_old(n):
    return n > 1 and n * factorial(n-1) or 1

def factors(n):
    fs = [1,n]
    for i in range(2, n):
        if n % i == 0: fs.append(i)
    return fs

def lazy_gcd(a,b):
    afs = set(factors(a))
    bfs = set(factors(b))
    return max(afs.intersection(bfs))

def unitary_divisors(n):
    fs = factors(n)
    us = []
    for f in fs:
        g = n / f
        if lazy_gcd(f, g) == 1: us.append(f)
    return list(sorted(us))

def product(xs, mod=None):
    p = 1

    if mod:
        f = lambda p, x: ((p*x) % mod)
    else:
        f = lambda p, x: p*x

    for x in xs:
        p = f(p,x)

    return p

def old_S(n):
    ds = [p**multiplicity(n, p) for p in primes(n)]
    return sum(product(s)**2 for s in powerset(ds))


def powmod(b, e, m):
    if e == 0: return 1
    p = b
    while e > 1:
        if e % 2:
            p *= b
        else:
            p *= p
        e = e >> 1
        p = p % m
    return p % m

def S(n, m):
    s = 1
    for p in primes(n):
        if p > n: break
        a = multiplicity(n, p)
        x = powmod(p, a * 2, m)
        s = (s * (x + 1)) % m
    return s

def old_S_mod(n,m):
    ps = [p for p in primes(n)]
    ms = [multiplicity(n, p) for p in ps]
    ds = [p**a for p,a in zip(ps, ms)]
    return sum((product(s, m)**2) % m for s in powerset(ds)) % m

def primes(n):
    with file('../primes.txt') as f:
        for line in f:
            try:
                p = int(line)
            except ValueError:
                raise StopIteration
            if p > n:
                raise StopIteration
            yield p

if __name__ == '__main__':
    M = 10**9 + 9
    N = 10**8
    print S(N, M)
    # >>> 96997076

