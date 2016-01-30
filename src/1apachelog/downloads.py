import apachelog

def get_downloads_count(log, fpath):
    """
    Find the number of download for the file
    >>> get_downloads_count('access-log', '/ply/ply-2.3.tar.gz')
    690
    """
    total = 0
    for line in apachelog.lines_from_dir(log, 'www'):
        #print line
        for i in apachelog.apache_log(line):
            if i["request"] == fpath:
                total += 1
    return total

def main():
    # lines = apachelog.lines_from_dir('access-log*', 'www')
    # log = apachelog.apache_log(lines)
    #
    print 'Total: %d' % get_downloads_count('access-log', '/ply/ply-2.3.tar.gz')


if __name__ == "__main__":
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()
