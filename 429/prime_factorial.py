# Copyright (c) 2013 the authors listed at the following URL, and/or
# the authors of referenced articles or incorporated external code:
# http://en.literateprograms.org/Factorials_with_prime_factorization_(Python)?action=history&offset=20100923154813
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Retrieved from: http://en.literateprograms.org/Factorials_with_prime_factorization_(Python)?oldid=16897

def multiplicity(n, p):
    """Return the power of the prime number p in the
    factorization of n!"""
    if p > n: return 0
    if p > n//2: return 1
    q, m = n, 0
    while q >= p:
        q //= p
        m += q
    return m

def primes(n):
    """Generate a list of the prime numbers [2, 3, ... m] where
    m is the largest prime <= n."""
    n = n + 1
    sieve = range(n)
    sieve[:2] = [0, 0]
    for i in xrange(2, int(n**0.5)+1):
        if sieve[i]:
            for j in xrange(i**2, n, i):
                sieve[j] = 0
    # Filter out the composites, which have been replaced by 0's
    return [p for p in sieve if p]

def powproduct(ns):
    """Compute the explicit value of a factored integer
    given as a list of (base, exponent) pairs."""
    if not ns:
        return 1
    units = 1
    multi = []
    for base, exp in ns:
        if exp == 0:
            continue
        elif exp == 1:
            units *= base
        else:
            if exp % 2:
                units *= base
            multi.append((base, exp//2))
    return units * powproduct(multi)**2

def factorial(n):
    return powproduct((p, multiplicity(n, p)) for p in primes(n))
