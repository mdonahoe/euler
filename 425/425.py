

def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]


def read_primes():
    primes = [int(x) for x in file('10m_primes.txt').read().split()]
    return primes


def generate(x):
    # all numbers one digit away from X
    ret = set()
    ys = '123456789'
    s = str(x)
    for y in ys:
        ret.add(int(y + s))
        #ret.add(int(s + y))


    # replace a single digit with another
    # add a digit on the left
    ys += '0'
    for i,x in enumerate(s):
        for y in ys:
            z = ''.join(s[:i] + y + s[i+1:])
            if z and z[0] != '0' and z[-1] != '0':
                ret.add(int(z))

    # remove edges
    left = s[1:]
    right = s[:-1]
    if left: ret.add(int(left))
    if right: ret.add(int(right))
    return ret


def relative_primes(N):
    primes = set(read_primes())
    print len(primes)
    def not_prime(x):
        return x > N or x not in primes

    dists = { 2 : 0 }
    queue = [ 2 ]
    while queue:
        n = queue.pop(0)
        a = max(dists[n], n)

        for x in generate(n):
            if not_prime(x):
                # this also deals with numbers > N
                continue

            # what is the current best distance?
            d = dists.get(x, N)

            # can we beat it?
            if d <= a:
                # there is a better way to reach this number already
                continue

            dists[x] = a
            queue.append(x)

    nots = [p for p in primes if p < N and dists.get(p, N) > p]

    return nots

def path(x, prev):
    p = []
    c = x
    while prev[c]:
        p.append(c)
        c = prev[c]
    p.append(2)
    return p

import time
t = time.time()
rs = relative_primes(10**6)
print sum(rs)
print time.time() -t

def test(n):
    ls = list(generate(n))
    ls.sort()
    print ls

def possibles():
    primes = read_primes()
    smalls = set([p for p in primes if p < 10000 and p > 1000])
    print [(a,b,17553-a-b) for a in smalls for b in smalls if a < b and (17553-a-b) in smalls]

