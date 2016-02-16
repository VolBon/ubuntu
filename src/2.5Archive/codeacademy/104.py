import re
filename = raw_input("Enter your file in your language:")
#try to open the file
d = dict()
try:
    filen = open(filename, 'r')
except:
    print "No file detected"
    quit()

for line in filen:
    line = re.sub(r'[^a-z]+', '', line)
    new = line.split()
    for x in new:
        for i in x:
            d[i] = d.get(i,0) + 1
print d

lst = list()
for k, v in d.items():
    lst.append((v, k))
    lst.sort(reverse=True)


