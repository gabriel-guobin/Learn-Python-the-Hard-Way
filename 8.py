formatter = "%r %r %r %r"

print formatter % ('one', 'two', 'three', 'four')
print formatter % (1, 2, 3, 4)
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"i had this right",
	"and i know you will make it",
	"but it can't sing",
	"so i said good night")