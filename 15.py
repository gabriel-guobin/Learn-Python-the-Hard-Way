from sys import argv

script, filename = argv

txt = open(filename)

print "this is your file ", filename
print txt.read()

print "type the filename again"
filename2 = raw_input(">>")

txt_again = open(filename2)

print txt_again.read()




