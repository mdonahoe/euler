#euler 213
import time
start = time.time()
N = 30
jumps = []
for i in range(N*N):
	jump = []
	if i%N>0: jump.append(i-1)
	if i%N<N-1: jump.append(i+1)
	#else: jump.append(i)
	if i>=N: jump.append(i-N)
	if i<N*(N-1): jump.append(i+N)
	#else: jump.append(i)
	jumps.append(jump)

fleas = []
for i in range(N*N):
	flea = [0]*N*N
	flea[i] = 1.0
	fleas.append(flea)

def boxp(N,fleas):
	boxes = [1.0]*N*N
	for flea in fleas:
		for i in range(N*N):
			boxes[i]*=(1-flea[i])
	return boxes


for bell in range(50):
	print bell
	#start = time.time()
	newfleas = []
	for flea in fleas:
		newflea = [0]*N*N
		for box,jump in enumerate(jumps):
			x = flea[box]/float(len(jump))
			for j in jump:
				newflea[j]+=x
		newfleas.append(newflea)
	fleas = newfleas
	
	#print "time = %.2f"%(time.time()-start)
print "answer = %f"%(4*round(sum(boxp(N,fleas)),6))
print "time = %.2f"%(time.time()-start)