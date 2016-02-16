import random
''' Trying to create a 21 or bust card game.
    I still need to go through the code, re-factor it and clean it up. 
    There are lots of room for improvement.'''

def getDeck():
    # This is a dict, keys are the card suits and each suit has 1-11 inside.
    deck = {'diamonds' : random.randint(1, 11),
        'hearts' : random.randint(1, 11), 
        'spades' : random.randint(1, 11), 
        'clubs' : random.randint(1, 11)}
    return deck

def getCards(deck):
    # The deck of cards is brought in, a random key is selected and a random number from that key.
    cardNumber = deck[random.choice(deck.keys())]
    cardSuit = random.choice(deck.keys())
    return cardNumber, cardSuit # Returns a tuple (two values)

def playerTwist(computerNumbers, computerCards, playerNumbers, playerCards):
    # This allows the player to keep twisting (taking cards), if the player 
    # busts while taking cards the loop stops and 'checkForWinner()' is called.
    while True:
        if sum(playerNumbers) < 21:
            hitOrStay = raw_input('Would you like to twist? (yes or no):').lower()
            if 'yes' in hitOrStay or hitOrStay.startswith('y'):
                drawNumber, drawSuit = getCards(getDeck())
                playerNumbers.append(drawNumber)
                playerCards.append(drawNumber)
                playerCards.append(drawSuit)
                print '{}'.format(playerCards)
                continue
        else:
            print checkForWinner(sum(playerNumbers), playerCards, 
                                         sum(computerNumbers), computerCards)
            break
        print checkForWinner(sum(playerNumbers), playerCards, sum(computerNumbers), 
                             computerCards)
        break

def computerAI(computerNumbers, deck):
    # This is a simple computer AI, it'll keep drawing cards, as long
    # as the total value of cards don't exeed 15, if it does exeed 15 (total card value)
    # it'll stop. Because the card draw is random, computer can also bust, keeping it at 15 
    # value seemed to stop it busting all the time.
    while True:
        if sum(computerNumbers) < 15:
        # This draws cards and unpacks the tuple in two variables.
        # The variables are then added to two lists, computerNumeber (to keep track of
        # computer's total card value) and computers cards (which is displayed).
            drawNumber, drawSuit = getCards(getDeck())
            computerNumbers.append(drawNumber) # this adds values to computer number list
            deck.append(drawNumber) # these two are added to the computers cards (for display)
            deck.append(drawSuit)
        else:
            break

def checkForWinner(player, playerCards, computer, computerCards):
# This checks to see who has won and prints the results..
    if player > 21 and computer > 21:
        return '{} you bust! \n {} computer busts too!'.format(playerCards, computerCards)
    elif player > 21:
        return '{} you bust!\n {} computer wins!'.format(playerCards, computerCards)
    elif computer > 21:
        return '{} computer busts! {} you win!'.format(playerCards, computerCards)
    elif player == 21 and computer == 21:
        return 'Your cards were {} \n computers cards were {} game is a draw!'.format(
                                                           playerCards, computerCards)
    elif player != 21 and computer == 21:
        return 'Your cards were {} \n computers cards were {} Computer wins!!'.format(
                                                           playerCards, computerCards)
    elif player == 21 and computer != 21:
        return 'Your cards were {} \n computers cards were {} you win!'.format(
                                                    playerCards, computerCards)
    elif player > computer:
        return 'Your cards were {} \n computers cards were {} you win!'.format(
                                                    playerCards, computerCards)
    elif player < computer:
        return 'Your cards were {} \n computers cards were {} Computer wins!'.format(
                                                          playerCards, computerCards)
    elif player == computer:
        return 'Your cards were {} \n computers cards were {} game is a draw!'.format(
                                                           playerCards, computerCards)
    playAgain()

def playAgain():
    # This allows the player to play again, or close the game out.
    while True:
        userIn = raw_input('Would you like to play? (yes or no): ').lower()
        if 'yes' in userIn or userIn.startswith('y'):
            startGame()
        else:
            exit()

def instructions():
    print '''
           Welcome to Daniel's 21 bust game!
           The object of the game is to get
           as close to 21 by drawing 'twisting' 
           without busting.The winner will be 
           whoever gets 21 or closest.

           Good Luck!
         '''
    playAgain()

def startGame():
    # This is the set-up.
    computerNumbers = [] # This list just keeps a count of all the computer card values.
    computerCards = [] # This holds the value of the computer's cards and the suit(for display purposes).

    computerAI(computerNumbers, computerCards) # This draws cards, and passes the two computer lists

    playerNumbers = []
    playerCards = []
    # Here I unpact the tuple and put the values in different lists.
    playerNumber, playerSuit = getCards(getDeck())  
    playerNumbers.append(playerNumber) # this is a player's card value.
    playerCards.append(playerNumber) # This and the next one are the players cards, for display.
    playerCards.append(playerSuit)
    print '{}'.format(playerCards) # Prints the first card on the screen.
    moreCards = playerTwist(computerNumbers, computerCards, playerNumbers, playerCards)
    playAgain()


instructions()
