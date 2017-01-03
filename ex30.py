people = 10
cars = 5
buses = 10

if cars > people:
	print("We should take the cars.")

elif cars < people:
	print("We should not take the cars.")
	
else:
	print("We could not decide.")
	
if buses > cars:
	print("That's too many buses.")

elif buses < cars:
	print("Maybe we could take the buses.")
	
else :
	print("We still can't decide.")
	
if people > buses:
	print("All right, let's just take the bus.")
else:
	print("Fine, just stay at home.")