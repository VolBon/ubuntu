import sys
import re


def word_search(filename):
    d = dict()
    with open(filename, 'r') as f:
        for line in f:
            line = line.lower()
            words = line.split()
            words = re.findall('\w+', str(words))
            #print words
            for word in words:
                #print word
                d[word] = d.get(word,0) + 1
    return d


def print_count(fname):
    '''
    Prints one per line '<word> <count>' sorted by word for the given file
    '''
    d = word_search(fname)
    lst = list()
    for key, value in d.items():
        lst.append((key, value))
    lst.sort()
    for key, val in lst:
        print key, val
    #print lst


def print_top(fname):
    '''
    Prints the top count listing for the given file
    '''
    d = word_search(fname)
    lst = list()
    for key, value in d.items():
        lst.append((value, key))
    lst.sort(reverse=True)
    for key, val in lst[:20]:
        print val, key
    #print lst


def main():
    if len(sys.argv) != 3:
        print 'Usage: ./wordcount.py {--count | --top} <file name>'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    print filename
    if option == '--count':
        print_count(filename)
    elif option == '--top':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()
