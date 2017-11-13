#euler53

def f(n,s=1): return 1*(n<=s) or n*f(n-1,s)

def ncr(n,r): return f(n,r)/f(n-r)

x = [ncr(i,j) for i in range(1,101) for j in range(1,101) if i>=j and ncr(i,j)>1000000]
print len(x)
