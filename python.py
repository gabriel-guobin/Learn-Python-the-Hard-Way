# open a file


which = raw_input("which file do you want to open?")
apple = open(which)
print "this is your guess:"
print apple.read()

from sys import argv
script,file2 = argv
blue = open(file2)
print "and this is the right answer:"
print blue.read()

red = open("11.txt")
print red.read()




