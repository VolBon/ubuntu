number = "start"
count = 0
total = 0
average = 0

while number != "done":
    number = raw_input("Enter number or done to finish:")
    if number == "done":
        break
    try:
        number = float(number)
    except:
        print ("Invalid input")
        continue
    print "Number =", number
    count = count + 1
    total = total + number
    average = total/count
    
print "Total is %s, count to %s and average is %s" % (total, count, average)