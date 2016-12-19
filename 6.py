x = "there are %d kinds of people" % 10
binary = "binary"
dont = "don't"
y = "those who know %s and those who %s" % (binary, dont)

print x
print y

print "I said: %r" % x
print "I also said: %s" % y

hilarious = False
joke_evaluation = "isn't this funny? %s"

print joke_evaluation % hilarious

w = "this is the left side of the string,"
q = "and this is the right side of the string"
print w + q
