numbers = raw_input("Throw a  list of numbers:")
maks = float(numbers[0])
mini = float(numbers[0])
for i in numbers:
    try:
        i = float(i)
        print i
    except:
        print "Xujovo"
        continue
    if i < mini:
        mini = i
    elif i > maks:
        maks = i
        
print ("Maximum %s, minimum %s") % (maks, mini)