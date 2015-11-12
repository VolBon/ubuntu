import random


def name_to_num(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Not a good guess"

def num_to_name(comp):
    if comp == 0:
        return "rock"
    elif comp == 1:
        return "Spock"
    elif comp == 2:
        return "paper"
    elif comp == 3:
        return"lizard"
    elif comp == 4:
        return "scissors"
    else:
        print "Not in range"



def rpsls():
    comp = random.randrange(0,4)
    name = raw_input("Choose something:")
    you = name_to_num(name)
    if (comp - you)%5 == 0:
        print "Tie"
    elif (comp - you)%5 <= 2:
        print "Comp wins"
    elif (comp - you)%5 > 2:
        print "You win"
        
    print "Comp:", num_to_name(comp), "You:", name

while True:
    a = raw_input("wanna play? y/n")
    if a == "y":
        rpsls()
    elif a == "n":
        print "Bye"
        break
