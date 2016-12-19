from sys import argv
script, filename = argv

print "now we are going to clear %s" % filename
print "if you want to go on, hit RETURN"
print "if you don't want to, hit ^c."

raw_input("?")

print "opening the file"
file = open(filename, 'w')

print "now we truncate the file"
file.truncate()
print "It's done."

print "Now try to put some line in it:"
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "Now we are going to write"
file.write(line1)
file.write("\n")
file.write(line2)
file.write("\n")
file.write(line3)
file.write("\n")

print "OK, finished!"
print "Remember to close the file."
file.close()

