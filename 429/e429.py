"""
429

Find the sum of the squares of "unitary" divisors of N!

"Unitary divisors" are just relatively prime,
so we can take the prime factorization of X and compute the powerset.
The product of each subset is a unitary divisor.

However, since we are just summing the squares,
we dont need to compute the powerset, which is 2^N log(N)
Instead we can use s = s * (1 + P_i^2),
where P_i is a power of a prime which divides X.


Also, since X is just N!, we can more easily compute the prime factorization,
since we know all primes <= N are included
"""
from prime_factorial import multiplicity

def S(n, m):
    s = 1
    for p in primes(n):
        a = multiplicity(n, p)
        x = pow(p, a * 2, m)
        s = (s * (x + 1)) % m
    return s


def primes(n):
    """yield primes from file"""
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
    # >>> 98792821

