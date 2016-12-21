file1 = open("1.txt"); data = file1.read()
file2 = open("2.txt",'w'); file2.write(data)
file1.close(); file2.close()