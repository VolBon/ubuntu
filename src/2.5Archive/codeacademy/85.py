fopen = open("box", "r")
count = 0
for line in fopen:
    if line.startswith("From"):
        newline = line.split()
        count += 1
        print newline[1]
        

print "There were %s lines with From" % (count)
