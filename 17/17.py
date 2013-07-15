#euler17


ones = ['zero','one','two','three','four','five','six','seven','eight','nine']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['none','none','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def sayit(n):
	word = ''
	s = "%.3d"%n
	if int(s[0])>0:
		word+=ones[int(s[0])]+'hundred'
		if s[1]=='0' and s[2]=='0': return word
		word+='and'
	if int(s[1])>1:
		word+=tens[int(s[1])]
		if s[2]=='0':return word
		word+=''
	if int(s[1])==1:
		word+=teens[int(s[2])]
		return word
	word+=ones[int(s[2])]
	return word
	
print sum([len(sayit(i)) for i in range(1,1000)])+len('onethousand')
	