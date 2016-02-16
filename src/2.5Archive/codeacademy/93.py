filename = raw_input("Enter the filename:")
d = dict()
#if open fails program shuts down
try:
    shout = open(filename, 'r')
except:
    print "File does not exist"
    quit()
#loop thru doc and find lines that starts from 'From' and take emails

for line in shout:
    if line.startswith("From"):
        new = line.split()
        try:
            x = new[1]
        except:
            continue
        d[x] = d.get(x,0) + 1 #this creates dictionary with emails (or adds 1)
print d

#looking for the maximum value and corresponding key

mak = None
maki = None
for i in d:
    if mak is None:
        mak = d[i]
    elif mak < d[i]:
        mak = d[i]
        maki = i
print maki, d[maki]
        

