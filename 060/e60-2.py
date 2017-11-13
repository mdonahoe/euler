#! /usr/bin/python
# -*- mode:python; coding:utf-8 -*-
#
# problem60.py -
#
# Copyright(C) 2008 by mzp
# Author: MIZUNO Hiroki / mzpppp at gmail dot com
# http://howdyworld.org
#
# Timestamp: 2008/07/17 23:04:02
#
# This program is free software; you can redistribute it and/or
# modify it under MIT Lincence.
#
from prime import primelist
def delete(x,xs):
    return [y for y in xs if y != x]

def shift(xs):
    x = xs[0]
    del xs[0]
    return x

def join(x,y):
    return int("%d%d" % (x,y))

def next(x,xs):
    return delete(x,xs) + [max(xs)+1]



prime = primelist
theprimes = set(primelist)
q = []
q.append(range(5))

while len(q) > 0:
    cancel = False
    p = shift(q)
    print "target: ",p
    for x in p:
        for y in p:
            if x == y:
                continue
            px = prime[x]
            py = prime[y]
            if not (join(px,py) in theprimes and join(px,py) in theprimes):
                a = next(x,p)
                b = next(y,p)
                print "push:",a," del:",x
                print "push:",b," del:",y
                if a not in q:
                    q.append(a)
                if b not in q:
                    q.append(b)
                cancel = True
                break
        if cancel:
            print ""
            break
    else:
        print "answer:",[prime[i] for i in p]
        break