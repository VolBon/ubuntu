filename = raw_input("Enter the filename:")
shout = open(filename, 'r')
total = 0
count = 0
for line in shout:
    if line.startswith("A"):
        n = line.find(" ")
        new = line[n:]
        total += float(new)
        count += 1
        print new
print count
print ("The average confidence is:", total/count)
