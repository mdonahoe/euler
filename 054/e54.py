def nopal(x):
	b = str(x)
	d = str(b[::-1])
	return sum([1 for i,j in zip(b,d) if i!=j])
	
total = 0
for i in range(10000):
	x = i;j=0
	while nopal(x) and j<50: x+=int(str(x)[::-1]);j+=1
	if j<50: total+=1
	print x
print total
