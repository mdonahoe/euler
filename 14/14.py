##euler14

d={1:0}


def f(n):
 if n%2==0: return n/2
 return 3*n+1

def iterate(n):
 try: return d[n]
 except:
  d[n] = iterate(f(n)) + 1
  return d[n]
  
x = [(iterate(i),i) for i in xrange(1,1000000)]
x.sort()
print x[-1]