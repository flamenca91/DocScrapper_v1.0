docFile = {}
f = open("DocTagsList.txt")
for line in f:
    line = line.split()
    docFile[line[0]] = line[1]

print(docFile)
    
