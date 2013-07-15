#euler30

print sum([i for i in range(2,200000,) if i==sum([int(c)**5 for c in str(i)])])