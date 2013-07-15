def crackmaker(row,width,bricks):
	if len(row)>=width: return [row]
	return reduce(lambda x,y:x+y,[crackmaker(row+[b],width,bricks) for b in bricks])
	
print crackmaker([],5,[2,3])