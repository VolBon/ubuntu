new = []
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
    except:
        print ("Invalid input")
        continue
    new.append(num)
 
print "Maximum is", max(new)
print "Minimum is", min(new)