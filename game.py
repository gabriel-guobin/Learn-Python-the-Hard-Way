print("You entered a dark room. The door behind you closed.")
print("You were shot by a gun.")
print("1. Shoot back.")
print("2. Pretend to be dead.")
print("3. Shout back:'Who are you!?'")
print("4. Pick a jelly.")

choice = input(">")

if choice <= "3":
	blood = 10
	while blood > 0:
		blood -= 3
		print ("You' were shot again. Blood -3")
	print("You're dead. Good job.")
	
elif choice == "4":
	print ("You were sent back to the novice village. Let's try again.")
else:
	list = [30, 100]
	for i in list:
		i += 100
		print("your magic now is %d" % i)
	print("Level up! Congratulations!")
		