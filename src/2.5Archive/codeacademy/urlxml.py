import urllib
import xml.etree.ElementTree as ET

while True:
    total = 0
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = address
    #serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    tree = ET.fromstring(data)

    results = tree.findall('.//name')
    other = tree.findall('.//comment')
    for item in other:
        total += int(item.find('count').text)
        
    print 'Count: ', len(results)
    print 'Sum: ', total
    #lat = results[0].find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text
