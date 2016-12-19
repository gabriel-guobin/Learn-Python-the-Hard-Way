# one hour practice
# I had too much tonight
# Do pay more time studying your major, and do this efficiently.

# now open a file 
input = raw_input("which file do you like to operate")
txt = open(input,'w')

# now truncate it
txt.truncate()

print "It's done."

line1 = raw_input("add something to it")
line2 = raw_input("try to add some more")

txt.write(line1 + "\n" +line2)

txt.close()
