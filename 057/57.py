#e57

from fractions import Fraction
from math import log10
def root2(n):
	#generate the nth iteration
	x = '1'
	y = ''
	while n:
		n-=1
		x+='+1/(2'
		y+=')'
	return eval(x+'+Fraction(1,2)'+y)


def root22(n):
	x = Fraction(1,2)
	while n:
		x = 1/(2+x)
		n-=1
	return 1+x
#print root22(4),root2(4)	
#print sum([1 for i in range(1000) if str(root22(i).numerator)>str(root22(i).denominator)])



n = 1000
x = Fraction(1,2)
total = 0
while n:
	y = 1+x
	if len(str(y.numerator))>len(str(y.denominator)): total+=1; print y
	x = 1/(2+x)
	n-=1
print total
