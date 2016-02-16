
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
            y = new[1] # take the email, position 1
        except:
            continue
        d[y] = d.get(y,0) + 1 #this creates dictionary with tenants (or adds 1)
lst = list()
for k, v in d.items():
    lst.append((v, k))
    lst.sort(reverse=True)

print lst[0]

