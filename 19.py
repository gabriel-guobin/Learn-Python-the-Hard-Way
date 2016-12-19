def cheese_and_butter(cheese_count, number_of_butter):
	print "You have %d cheess" % cheese_count
	print "You have %d butter" % number_of_butter
	print "Man that's enough for a party"
	print "Get the blanket. \n"

print "directly input value"
cheese_and_butter(20,30)

print "use the value in script"
amount_of_cheese = 30
amount_of_butter = 20

cheese_and_butter(amount_of_cheese, amount_of_butter)

print "calculate in the blankets"
cheese_and_butter(30*3, 20*2)

print "combine variable and math"
cheese_and_butter(amount_of_cheese + 30, amount_of_butter + 20)


