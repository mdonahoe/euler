


def differ(old,next):
	ns,prev = old
	if prev==None: return ([],next)
	ns.append(prev-next)
	return (ns,next)

def numlist(n):
	return [int(i) for i in str(n)]
	
def pipeline(f,seq):
	return [f(a,b) for a,b in zip(seq[:-1],seq[1:])]

	

def bouncey(n):
	##s = reduce(differ,numlist(n),(None,None))[0]
	s = pipeline(lambda x,y:int(y)-int(x),numlist(n))
	return sum([abs(i) for i in s])>abs(sum(s))
	
	
	
def bouncy(n):
	"""returns True if n is a 'bouncy' number."""
	diffs = [int(b)-int(a) for a,b in zip(str(n)[:-1],str(n)[1:])]
	return sum([abs(x) for x in diffs])>abs(sum(diffs))
	
n=1
b=0
while float(b)/n<.99:
	if bouncy(n):b+=1
	n+=1

print "answer:",n
	

	