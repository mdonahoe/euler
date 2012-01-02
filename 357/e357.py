def sieve(N):
    s = [0] * N
    x = 1
    while x < N-1:
        x+=1
        if s[x]: continue
        y = x + x
        while y < N:
            s[y] = s[y] or x
            y += x
    return s

def powerset(xs):
    n = 2**(len(xs))
    for i in xrange(n):
        a = []
        j = 0
        while i:
            if i%2: a.append(xs[j])
            j+=1
            i/=2
        yield a

def product(xs):
    p = 1
    for x in xs: p *= x
    return p

def factors(n, s):
    x = s[n]
    if x == 0: return [n]
    return [x] + factors(n/x, s)

def divisors(n, s):
    fs = factors(n, s)
    return set([product(p) for p in powerset(fs)])

if __name__ == '__main__':
    import sys
    N = int(sys.argv[1])
    s = sieve(N+2)
    total = 1
    x = 2
    while x<=N:
        print x
        for d in divisors(x, s):
            if s[d+x/d]: break
        else:
            total += x
        x+=4
    print total
