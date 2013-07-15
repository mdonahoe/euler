#euler31

"""
##first attempt
coins = [1,2,5,10,20,50,100,200]
s=1
for a in range(201):
 print a
 for b in range(101):
  for c in range(41):
   for d in range(21):
    for e in range(11):
     for f in range(5):
      for g in range(3):
       if a+2*b+5*c+10*d+20*e+50*f+100*g==200:
        s+=1
 

print s


"""
coins = [1,2,5,10,20,50,100,200]
s = 0
def possibles(base,coin):
	global s
	for i in range(200/coins[coin]+1):
		x=base+coins[coin]*i
		if x==200:s+=1;	return
		elif x>200: return
		elif coin>0: possibles(x,coin-1)
		
possibles(0,7)
print s