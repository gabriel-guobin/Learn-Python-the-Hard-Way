# cardinal number practice

list = [" $ 5"," $ 10"]

print("Which one do you like?")
print("1. orange juice")
print("2. coffee")
i = input('>')

if i == "1" or i == "2":
	i = int(i) - 1
	print(list[i])
