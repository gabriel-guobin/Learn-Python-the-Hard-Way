from sys import argv
script, cc, dd = argv

def dream(practice, goal):
	print "You need %s" % practice
	print "And %s" % goal

# 1
dream("reading","practicing")

# 2
aa = raw_input("?")
bb = raw_input("?")
dream(aa, bb)

# 3
dream("reading %s" % aa,
"practicing %s" % bb)

# 4
dream(50,60)

# 5
dream(50+100,60*3)

# 6
dream(cc, dd)

# 7
dream(aa+cc, bb+dd)





