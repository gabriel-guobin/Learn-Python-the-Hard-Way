from sys import argv
script, filename = argv

def print_all(a):
	print a.read()

def rewind(a):
	a.seek(0)

def print_line(b, a):
	print b
	print a.readline()
	
a = open(filename)
	
print_all(a)
print "now we rewind"
rewind(a)


b = 1
print_line(b, a)
b = b + 1
print_line(b, a)



