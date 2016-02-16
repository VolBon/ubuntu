import socket

site = raw_input("Enter you website:")
url = site.split('/')

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((url[2], 80))
except:
    quit()
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(3000)
    if ( len(data) < 1 ) :
        break
    print data;
    print len(data)

mysock.close()
