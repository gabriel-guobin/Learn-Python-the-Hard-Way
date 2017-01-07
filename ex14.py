prompt = '>>>>>>>>>'

from sys import argv

script, username = argv



print "Hi %s, I'm the %s script" % (username, script)
print "I'd like to ask you a few questions"

print "do you like me %s?" % username
likes = raw_input(prompt)

print "where do you lives %s ?" % username
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
alright, so you said %r about liking me.
you live in %r. not sure where that is.
adn you have a %r computer. nice
""" % (likes,lives,computer)


# past we use this

print "Hi %s, I'm the %s script" % (username, script)
print "Now I will ask you some questions"
age = raw_input("how old are you %s ?" % username)
job = raw_input("what's your job %s ?"% username)
print "so you are %s years old, and your job is %s" % (age, job)


