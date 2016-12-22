def one_ring_to_rule_them_all(a):
	words = a.split(' ')
	b = sorted(words)
	print words.pop(0)
	print words.pop(-1)
	print b.pop(0)
	print b.pop(-1)
	
a = "an apple a day, keep the doctors away"
one_ring_to_rule_them_all(a)

