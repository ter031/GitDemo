file = open('test.txt')
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readlines())



# print line by line using readline method
#line = file.readline()
#while line!= "":
 #   print(line)
 #   line = file.readline()

line = file.readlines()
for x in line:
    print(x)






file.close()