"""
X2 = AX1+BY1+C

A = (X2-BY1-C)/X1

X3 = +BY2+C

"""
from random import randint

def main():
    ns = [21, 120, 697, 4060]
    xs = [15, 85.0, 493.0, 2871.0]

    def fx(x, y, c):
        return x * c[0] + y* c[1] + c[2]

    def test(c, a):
        score = 0
        for i in range(len(ns)-1):
            x = fx(xs[i], ns[i], c)
            score += x - a[i + 1]
        return score


    genes = [(0, 0, 0)]
    def mutate(x):
        if abs(sum(x))>10:
            x = (0, 0, 0)
        return tuple([a + randint(-1, 1) for a in x])

    def evolve(a):
        genes = [(0, 0, 0)]
        y = 1
        while genes and abs(y)>0:
            x = genes.pop()
            y = test(x, a)
            genes.append(mutate(x))
            genes.append(mutate(x))
        return x

    cx = evolve(xs)
    cn =  evolve(ns)
    n = 21
    x = 15
    while n < 10 ** 12:
        x, n = fx(x, n, cx), fx(x, n, cn)

    print x, n

main()
