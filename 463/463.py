import time
"""

A: f(1) = 1
B: f(3) = 3
C: f(2*n) = f(n)
D: f(4*n + 1) = 2*f(2*n + 1) - f(n)
E: f(4*n + 3) = 3*f(2*n + 1) - 2*f(n)

S(n) = sum(f(i+1) for i in range(n))
S(8) = 22
S(100) = 3604

F = {}
F[1] = 1  # A
F[2] = F[1] = 1  # C
F[3] = 3  # B
F[4] = F[2] = 1  # C
F[5] = 2*f(3) - f(1) = 5  # D
F[6] = F[3] = 3  # C
F[7] = 3*f(3) - 2*f(1) = 7  # E
F[8] = F[4] = 1  # C

"""

from collections import Counter

def timeit(func):
    def g(*args):
        t = time.time()
        ret = func(*args)
        print 'time: {}'.format(time.time() - t)
        return ret
    return g

def memoized(func):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = int(func(x) % 1e9)
        return cache[x]
    return g


@memoized
def f(n):
    if n == 0:
        raise ValueError(0)
    if n == 1:
        return 1
    if n == 3:
        return 3
    if n % 2 == 0:
        return f(n / 2)
    if (n - 1) % 4 == 0:
        m = (n - 1) / 4
        return 2 * f(2 * m + 1) - f(m)
    if (n - 3) % 4 == 0:
        m = (n - 3) / 4
        return 3 * f(2 * m + 1) - 2 * f(m)
    raise ValueError('no rule for {}'.format(n))


def h(n):
    if n == 1:
        return 1
    if n == 3:
        return 3
    if n % 2 == 0:
        return 2
    if (n - 1) % 4 == 0:
        m = (n - 1) / 4
        return 5
    if (n - 3) % 4 == 0:
        m = (n - 3) / 4
        return 7
    raise ValueError('no rule for {}'.format(n))


@timeit
def S(n):
    return sum(f(i + 1) for i in xrange(n))


for i in range(1, 60):
    print i, f(i), h(i)
