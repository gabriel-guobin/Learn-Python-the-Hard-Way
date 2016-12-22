print "Let's practice everything."
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \nthe need of love
nor comprehend passion from intuition
and requires an explanation
\n \t \t where there is none.
"""

print "---------------"
print poem
print "---------------"

five = 10 + 3 - 2 - 6
print "This should be five: %s " % five

def color(shine):
	star = shine * 5
	moon = star / 10
	sky = moon / 10
	return star, moon, sky
	
shine = 100
star, moon, sky = color(shine)

print "with shine as %d " % shine
print "we got %d stars, %d moon and %d sky." % (star, moon, sky)

shine = shine / 10
print "We can also do this:"
print "%d stars, %d moon and %d sky." % color(shine)
	 