file = open("11.txt",'w+')

print file.read()
file.truncate()

line1 = "sdfsdfd"
line2 = "sdfsdf"
line3 = "ererererer"



print file.write(line1+"\n"+line2+line3)
print file.read()
