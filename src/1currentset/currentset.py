import sys
sys.path.insert(0, '../lib')

# Wrapper for ElementTree
# api: http://docs.python.org/2/library/xml.etree.elementtree.html
import ElementSoup as ES
from itertools import groupby
from operator import itemgetter


def parse(fobj):
    '''
    Parse HTML file and extract targets data
    '''
    d = list()
    
    root = ES.parse(fobj)
    tbllst = root.findall('.//table')
    for elem in tbllst[0][0]:  # iterating over table/tbody/tr elements
        if elem.tag == 'tr':
            lst = list()
            # elem is 'tr' tag with a few children 'td'
            # iterating over children might look as follows:
            for td in elem:
                lst.append(td.text)
            #print lst
            d.append(lst)
    return d


def report(targets):
    '''
    Generate targets report to standard output in the form:
    <HW type>

    <Target name> <Target IP>
    <Target name> <Target IP>
    ...
    <Target name> <Target IP>

    <HW type>

    <Target name> <Target IP>
    <Target name> <Target IP>
    ...
    <Target name> <Target IP>
    ...

    '''
    lst = parse(targets)
    del lst[0]
    lst = sorted(lst, key=itemgetter(9))
    for key, group in groupby(lst, lambda x: x[9]):
        if key is not None: 
            print "\n======= %s ======\n" % (key)
        else:
            continue
        for thing in group:
            print " %s  %s." % (thing[0], thing[2])
        print "\n==================="
    

def main():
    with open('currentsets.html') as f:
        report(f)


if __name__ == '__main__':
    main()
