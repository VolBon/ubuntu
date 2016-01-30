import apachelog

def get_largest(log):
    '''
    Find the largest data transfer in the given `log` sequence
    >>> get_largest('access-log')
    (4919642, '/dynamic/ffcache.zip')
    '''
    size = 0
    f = 0
    for line in apachelog.lines_from_dir(log, 'www'):
        for i in apachelog.apache_log(line):
            try:
                a = int(i["bytes"])
                b = i["request"]
            except:
                continue
            if a > size:
                size = a
                f = b
    return size, f

def main():
    '''Main function'''
    # lines = apachelog.lines_from_dir('access-log*', 'www')
    # log = apachelog.apache_log(lines)
    print '%d %s' % get_largest('access-log')

if __name__ == "__main__":
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()
