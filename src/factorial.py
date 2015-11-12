def factorial(x):
    total = 1
    for i in range(1, x):
        total = x
        total = total * factorial(x-1)
    return total
n = int(raw_input("Please enter any number and we will count it's factorial: "))
print "The answer to everything is ", factorial(n)
