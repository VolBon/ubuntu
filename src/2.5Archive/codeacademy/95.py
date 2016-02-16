
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
            x = new[1] # take the email, position 1
            y = x.split("@")[1] #takung only the tenant after @
        except:
            continue
        d[y] = d.get(y,0) + 1 #this creates dictionary with tenants (or adds 1)
print d

#now i write my own nice maximum function


def maxva(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]
print maxva(d), d[maxva(d)]
