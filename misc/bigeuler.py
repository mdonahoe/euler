>>> from math import sqrt
>>> sqrt(1929394959697989990)
1389026623.1062636
>>> b = _
>>> a = 319421985.8755939
>>> 
###
>>> from math import ceil
>>> b = ceil(b)
>>> a = int(a)
>>> for x in xrange(_,b,10):
...     if c.match(str(x*x)):
...             print x
...             break
...     else:
...             if x%1000000 == 0: print (x-a)/1000000,'and counting'
... 

1389019170
>>> 1389019170
1389019170
>>> _*_
1929374254627488900L
>>> 1389019170
1389019170



###
>>> dice4 = (1,2,3,4)
>>> 4**9
262144
>>> 6**6
46656
>>> 4**9*6**6
12230590464L
>>> 4*$
  File "<stdin>", line 1
    4*$
      ^
SyntaxError: invalid syntax
>>> 4*4
16
>>> s = [d for d in dice4]
>>> def rollNtimes(n,dice):
...     s = [d for d in dice]
...     for i in range(n-1):
... 
  File "<stdin>", line 4
    
    ^
IndentationError: expected an indented block
>>> 
>>> def sumroll(dice,n):
...     s = [0]
...     for i in range(n):
...             s = [a+b for a in dice for b in s]
...     return s
... 
>>> sumroll((1,2,3,4),2)
[2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8]
>>> def count(l):
...     d = {}
...     for x in l:
...             d[x] = d.get(x,0)+1
...     return d
... 
>>> count([1,2,3,2])
{1: 1, 2: 2, 3: 1}
>>> def roller(n,d): return count(sumroll(n,d))
... 
>>> roller((1,2,3,4),9)
{9: 1, 10: 9, 11: 45, 12: 165, 13: 486, 14: 1206, 15: 2598, 16: 4950, 17: 8451, 18: 13051, 19: 18351, 20: 23607, 21: 27876, 22: 30276, 23: 30276, 24: 27876, 25: 23607, 26: 18351, 27: 13051, 28: 8451, 29: 4950, 30: 2598, 31: 1206, 32: 486, 33: 165, 34: 45, 35: 9, 36: 1}
>>> s4 = _
>>> s4
{9: 1, 10: 9, 11: 45, 12: 165, 13: 486, 14: 1206, 15: 2598, 16: 4950, 17: 8451, 18: 13051, 19: 18351, 20: 23607, 21: 27876, 22: 30276, 23: 30276, 24: 27876, 25: 23607, 26: 18351, 27: 13051, 28: 8451, 29: 4950, 30: 2598, 31: 1206, 32: 486, 33: 165, 34: 45, 35: 9, 36: 1}
>>> s6 = roller((1,2,3,4,5,6),6)
>>> s6
{6: 1, 7: 6, 8: 21, 9: 56, 10: 126, 11: 252, 12: 456, 13: 756, 14: 1161, 15: 1666, 16: 2247, 17: 2856, 18: 3431, 19: 3906, 20: 4221, 21: 4332, 22: 4221, 23: 3906, 24: 3431, 25: 2856, 26: 2247, 27: 1666, 28: 1161, 29: 756, 30: 456, 31: 252, 32: 126, 33: 56, 34: 21, 35: 6, 36: 1}
>>> len(s6)
31
>>> len(s4)
28
>>> 31*28
868
>>> p = [b*y for a,b in s4.iteritems() for x,y in s6.iteritems()]
>>> sum(p)
12230590464L
>>> p = sum([b*y for a,b in s4.iteritems() for x,y in s6.iteritems() if a>x])
>>> p
7009890480L
>>> _/12230590464
0L
>>> _/12230590464.0
0.0
>>> p/12230590464.0
0.57314407678298007
>>> p
7009890480L
>>> t = sum([b*y for a,b in s4.iteritems() for x,y in s6.iteritems() if a>x])
>>> t = sum([b*y for a,b in s4.iteritems() for x,y in s6.iteritems()])
>>> t
12230590464L
>>> p/float(t)
0.57314407678298007
>>> round
<built-in function round>
>>> help(round)

>>> round(r/float(t),7)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: name 'r' is not define





