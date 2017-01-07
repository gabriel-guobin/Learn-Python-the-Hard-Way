numbers = [1, 2, 3, 4]
colors = ['red', 'green', 'yellow', 'blue', 'black']
fruits = [1, 'apple', 2, 'orange', 3, 'blueberry', 4, 'strawberry']

# this first kind of for-loop goes through a list
for number in numbers:
	print ("This is number %d" % number)
	
for color in colors:
	print("one of the seven is %s" % color)

for fruit in fruits:
	print("You got: %r" % fruit)
	
element = []

for k in range(0, 6):
	print("Adding %d to element..." % k)
	element.append(k)
	
for k in element:
	print("elements got: ", k)
