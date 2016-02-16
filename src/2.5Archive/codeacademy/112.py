import re
filename = raw_input("Enter your file in your language:")
#try to open the file
try:
    filen = open(filename, 'r')
except:
    print "No file detected"
    quit()
count = 0
total = 0
for lin in filen:
    y = re.findall('New Revision: ([0-9.]+)' ,lin)
    if len(y) != 0:
        print y
        total += float(y[0])
        count += 1
print total/count
