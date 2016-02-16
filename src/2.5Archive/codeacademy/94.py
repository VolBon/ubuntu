
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

def keymax(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     print k[v.index(max(v))], max(v)
keymax(d)
