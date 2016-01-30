import os
import gzip
import bz2
import re

def get_files(dirname):
    for root, dirs, files in os.walk(dirname):
        for i in files:
            yield os.path.join(root, i)
            
def lines_from_dir(filepat, dirname):
    for filename in get_files(dirname):
        if filepat in filename:
            if os.path.splitext(filename)[1] == '.gz':
                with gzip.open(filename, 'r') as f:
                    for line in f:
                        yield line
            if os.path.splitext(filename)[1] == '.bz2':
                with bz2.BZ2File(filename, 'r') as f:
                    for line in f:
                        yield line
            else:
                with open(filename, 'r') as f:
                    for line in f:
                        yield line
'''
Return sequence of lines from all files for the given `filepat`
in directory `dirname '''

def apache_log(lines):
    host = re.match("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", lines)
    host = host.group(1) if host else ""
    referrer = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.{1}(\S*)\s", lines)
    referrer = referrer.group(1) if host else ""
    user = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.{1}\S*\s(\S*)", lines)
    user = user.group(1) if host else ""
    dat = re.search("\[(.*)\]", lines)
    dat = dat.group(1) if host else ""
    method = re.search("\s\"([a-zA-Z]*)\s", lines)
    method = method.group(1) if host else ""
    request = re.search("\s\"[a-zA-Z]*\s(\S*)\s", lines)
    request = request.group(1) if host else ""
    proto = re.search("\s\"[a-zA-Z]*\s\S*\s(\S*)\"\s", lines)
    proto = proto.group(1) if host else ""
    status = re.search("\s\"[a-zA-Z]*\s\S*\s\S*\"\s([0-9]*)\s", lines)
    status = status.group(1) if host else ""
    bytes = re.search("\s([0-9]*)$", lines)
    bytes = bytes.group(1) if host else ""
    yield  {'status' : status,
            'proto' : proto,
            'referrer': referrer,
            'request' : request,
            'bytes' : bytes,
            'datetime': dat,
            'host' : host,
            'user' : user,
            'method' : method}
    '''
    Parse log and map fields to dictionary key/value pairs'''

def main():
    # for i in apache_log('62.161.167.222 - - [28/Feb/2008:03:27:10 -0600] "GET /favicon.ico HTTP/1.1" 404 133'):
    # print i
    for line in lines_from_dir('access-log', 'www'):
        print line
        for i in apache_log(line):
            print i

if __name__ == '__main__':
    main()