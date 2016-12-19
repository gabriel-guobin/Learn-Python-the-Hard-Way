def ready(va1,va2):
	print "we have two variables, they are %r and %r" % (va1, va2)
	

def none():
	print "when you hit this function, you will get nothing"
	
def new(*args):
	va1, va2, va3 = args
	print "this is a new way to receive variables, but usually not used."
	print "the three variable are: %r %r %r" % (va1, va2, va3)
	
ready("apples","oranges")
new("It is ", "very important ", "to have an icon")
none()