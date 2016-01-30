import apachelog

def get_404(log):
    '''
    Find the set of all requests with status 404 in the given `log` sequence
    >>> get_404('access-log')
    []
    '''
    l = []
    for line in apachelog.lines_from_dir(log, 'www'):
        #print line
        for i in apachelog.apache_log(line):
            a = i['status']
            b = i['request']
            if a == '404':
                #print b
                if b not in l:
                    l.append(b)
    return l

def main():
    '''Main function'''
    # lines = apachelog.lines_from_dir('access-log*', 'www')
    # log = apachelog.apache_log(lines)
    for r in sorted(get_404('access-log')):
        print r

if __name__ == "__main__":
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()
