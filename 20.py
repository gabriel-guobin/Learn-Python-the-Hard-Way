from sys import argv
script, file_name = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	print f.seek(0)
	
def print_line(which_line, f):
	print which_line, f.readline()
	
file = open(file_name)

print "First, print the file.\n"
print_all(file)

print "Second, rewind."
rewind(file)

print "Finally, print a line."
which_line = 1
print_line(which_line, file)

which_line = which_line + 1
print_line(which_line, file)

which_line = which_line + 1
print_line(which_line, file)
	


