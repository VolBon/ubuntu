
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
        new = line.split() #split the line into words
        try:
            y = new[5].split(":")[0]
            # take only the HOUR from time, from line
        except:
            continue #if there is nothing, just continues
        d[y] = d.get(y,0) + 1 #this creates dictionary with tenants (or adds 1)

#now sort and print
for k, v in sorted(d.items()):
    print k, v
