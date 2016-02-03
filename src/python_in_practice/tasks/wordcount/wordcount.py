import sys


def print_count(fname):
    '''
    Prints one per line '<word> <count>' sorted by word for the given file
    '''
    # !!!Your code here!!!


def print_top(fname):
    '''
    Prints the top count listing for the given file
    '''
    # !!!Your code here!!!


def main():
    if len(sys.argv) != 3:
        print 'Usage: ./wordcount.py {--count | --top} <file name>'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_count(filename)
    elif option == '--top':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()
