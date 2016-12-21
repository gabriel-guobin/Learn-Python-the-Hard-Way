from sys import argv
script, file_name = argv

def print_all(a):
    print a.read()

def rewind(a):
    a.seek(0)

def print_line(count,a):
    print count
    print a.readline()

file = open(file_name)

print_all(file)
rewind(file)

line = 1
print_line(line, file)

line = line + 1
print_line(line, file)

line = line + 1
print_line(line, file)




