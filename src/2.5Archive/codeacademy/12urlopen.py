import urllib
counts = dict()
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt').read(3000)
print fhand
print len(fhand)
