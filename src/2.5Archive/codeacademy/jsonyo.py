import json
import urllib

while True:
    total = 0
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = address
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    info = json.loads(data)
    print 'User count:', len(info)

    print info['comments'][3]['name']

    for item in info['comments']:
        '''print 'Name', item['name']
        print 'Id', item['count']'''
        total += int(item['count'])
        
    print 'Count: ', len(info['comments'])
    print 'Sum: ', total
