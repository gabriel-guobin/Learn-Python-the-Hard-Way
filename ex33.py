# exercise of while

list = []
i = 0

while i < 6:
	print("At the top of the list is %d" % i)
	list.append(i)
	
	i += 1
	print("list now is", list)
	print("At the bottom of the list is", i)

	
	
print("list:")
for a in list:
	print(a)