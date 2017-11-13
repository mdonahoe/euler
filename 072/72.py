def calc_less_than(x, n):
  #a[q] - number irreducible fractions less than x whith denominator equal to q
  #finds all the fractions at 1/2, and then gets rid of 2/4, 4/8 .. n/2*n etc
  # then does the same for 1/3 and 2/3, and 1/4 and 3/4 etc
  #dynamic programming ftw
  a = [int(q*x) for q in xrange(0,n+1)]
  for q in xrange(1, n+1):
    m = 2
    while(m*q<=n):
      a[m*q] -= a[q]
      m += 1
      #print a
  return sum(a)-1
 
if __name__=='__main__':
    #print calc_less_than(0.5,10000)-calc_less_than(1./3,10000)-1\
    print calc_less_than(1,10**6)
    
    
