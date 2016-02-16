filename = raw_input("Enter the filename:")
if filename == "honey":
    print "You honey boo boo fat bitch"
    quit()
try:
    shout = open(filename, 'r')
except:
    print "File does not exist"
    quit()
total = 0
count = 0
for line in shout:
    if line.startswith("X-DSPAM-Confidence:"):
        n = line.find(" ")
        new = line[n:]
        total += float(new)
        count += 1
        print new
print count
print ("The average confidence is:", total/count)
