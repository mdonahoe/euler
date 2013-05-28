def read_primes():
    primes = [int(x) for x in file('10m_primes.txt').read().split()]
    return primes


def connections(x):
    # all numbers one digit away from X
    ret = set()
    ys = '123456789'
    s = str(x)
    for y in ys:
        ret.add(int(y + s))


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
    if left: ret.add(int(left))
    return ret


def e425(N):
    dists = dict((x,N) for x in read_primes())
    dists[2] = 0
    queue = [2]
    while queue:
        n = queue.pop(0)
        a = max(dists[n], n)
        for x in generate(n):
            if x > N:
                continue
            d = dists.get(x, None)
            if d <= a:
                # not prime (None < all things)
                # or there is already a better way
                continue
            dists[x] = a
            queue.append(x)
    return sum(k for k,v in dists.iteritems() if k < N and v > k)


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
rs = relative_primes(10**7)
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

