import re
filename = raw_input("Enter your file in your language:")
#try to open the file
y = list()
try:
    filen = open(filename, 'r')
except:
    print "No file detected"
    quit()
regex = raw_input("Enter the regular expression:")
count = 0
for line in filen:
    y = re.findall(regex, line)
    if len(y) != 0:
        print y
        count += 1
print "There were %s expresions" % (count)
