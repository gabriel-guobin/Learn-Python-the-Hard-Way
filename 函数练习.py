a = 10
b = 10


def value(a, b):
	return a + b

print value(a, b)
c = value(a, b)
print c

print "the outcome is: %d" % value(a, b)
print 23 + value(a, b)