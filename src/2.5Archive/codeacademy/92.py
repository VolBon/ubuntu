filename = raw_input("Enter the filename:")
d = dict()
try:
    shout = open(filename, 'r')
except:
    print "File does not exist"
    quit()
for line in shout:
    if line.startswith("From"):
        new = line.split()
        try:
            x = new[2]
        except:
            continue
        d[x] = d.get(x,0) + 1
print d
