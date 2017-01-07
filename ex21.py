def add(a, b):
	print "adding %d and %d" % (a, b)
	return a + b
	
def substract(a, b):
	print "substracting %d and %d" % (a, b)
	return a - b

def multiply(a, b):
	print "Multiplying %d and %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "Dividing %d and %d" % (a, b)
	return a / b

age = add(5, 10)
height = substract(190, 40)
weight = multiply(2, 20)
iq = divide(200, 2)

print "age: %d height: %d weight: %d iq: %d" % (
age, height,weight, iq)

# A puzzle

print "Here is a puzzle....."

what = add(age, substract(height, multiply(weight,divide(iq, 2))))

print "And the outcome is", what, "Can you find out?"


