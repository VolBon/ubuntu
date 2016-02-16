import urllib
fhand = urllib.urlopen('http://www.google.com')
for line in fhand:
    print line.strip()
