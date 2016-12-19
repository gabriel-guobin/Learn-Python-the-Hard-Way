# We did two exercise yesterday.
# Now we try to repeat the first one

file = open("1.txt")
data = file.read()

file2 = open("2.txt", 'w')
file2.write(data)

# Well done, very good.
# Now try the second one.

def function1(*args):
	aaa, bbb, ccc = args
	print aaa, bbb, ccc
	
def function2(aa, bb, cc):
	print aa, bb, cc
	
def none():
	print "Nothing here."
	
function1("aaa","bbb","ccc")
function2("life","is","beautiful")
none()