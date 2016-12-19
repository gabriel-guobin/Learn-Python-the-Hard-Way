# Actually I think this is still an easy job.

# Now we are going to flirt with functions.
# More over, we are going to make our own functions. Use def?

def function_two(*args):
	variable1, variable2 = args
	print "first one is %r, second one is %r" % (variable1, variable2)

def function_two_again(va1, va2):
	print "first is %r, second is %r" % (va1, va2)

def function_one(va1):
	print "this only variable is %r" % va1

def function_none():
	print "I got nothing"
	

function_two("sdf","sdf")
function_two_again("sdf","sdf")
function_one("sdf")
function_none()
