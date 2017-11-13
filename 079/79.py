"""
Project Euler #79
by Matt Donahoe

My method was to find the first character in the code,
remove it from the logins
and recurse

but since no number is repeated,
it was easier just to sort the numbers by
average position in the 3char login code
"""

logins = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716""".split('\n')

keys= {}
for x in logins:
	for i,k in enumerate(x):
		keys[k] = keys.get(k,[])+[i]
code = [(1.0*sum(v)/len(v),k) for k,v in keys.iteritems()]
code.sort()
print ''.join([c[1] for c in code])
