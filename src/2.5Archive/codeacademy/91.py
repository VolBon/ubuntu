filename = raw_input("Enter the filename:")
d = dict()
try:
    shout = open(filename, 'r')
except:
    print "File does not exist"
    quit()
for line in shout:
    new = line.split()
    for i in new:
        d[i] = "in"

print d
