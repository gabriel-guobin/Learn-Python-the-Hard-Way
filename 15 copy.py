# let's try again

from sys import argv

script, filename = argv

txt = open(filename)

print "the file you want to import is:", filename
print "and here is your file \n >>>>>>>>>>>"
print txt.read()
print ">>>>>>>>>>>>"

print "now try again"
again = raw_input("the file you want to import is:")
txt_again = open(again)
print "and here is your file \n >>>>>>>>>>>>"
print txt_again.read()

