
>>> def twoxmody(x,y):
...     s = 1
...     while x:
...             s = (s*2)%y
...             x-=1
...     return s
...
>>> twoxmody(4,10)
6
>>> twoxmody(4,100)
16
>>> twoxmody(8,100)
56
>>> twoxmody(1000,100)
76
>>> twoxmody(1234123,100)
8
>>> twoxmody(1234123,10**10)
6503876608
>>> twoxmody(7830457,10**10)
9700303872
>>> _*28433
275808739992576
>>> _+1
275808739992577
>>> _%10**10
8739992577