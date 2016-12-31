def amount(start):
	beans = start + 1
	star = start + 2
	moon = start + 3
	return beans, star, moon
	
start = 3
a,c,b =  amount(start)

print "We have %d, %d, and %d." % amount(start)
print a, b, c
 