"""
Project Euler problem #64
by Matt Donahoe
"""

from math import sqrt

isqrt = lambda n: int(sqrt(n))


def period(S):
	a0 = isqrt(S)
	m = 0
	d = 1
	a = a0

	n = 0
	states = {(m,d,a):n}
	while 1:
		m = d*a-m
		d = (S-m*m)/d
		a = int((a0+m)/d)
		state = (m,d,a)
		if state in states: return n - states[state]
		states[state] = n
		n+=1

print sum([1 for n in range(10001) if sqrt(n)!=isqrt(n) and period(n)%2])