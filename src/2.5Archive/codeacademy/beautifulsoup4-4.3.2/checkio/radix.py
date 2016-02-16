def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except:
        return -1
print checkio("AFC", 10)
