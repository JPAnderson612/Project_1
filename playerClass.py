import re

class Player():

    def __init__(self, card1, card2): #Player objects are have to be initialized with two cards
        self.card1 = card1
        self.card2 = card2
        self.hand = [card1, card2]
        self.table = list() #used later for card evaluation

    #This method just straight up prints the player's cards
    def printCards(self):
         print(self.card1)
         print(self.card2)

    #This method gets the 3 cards placed in the flop and puts them in a string.
    #This string gets evaluated in the findMe function.
    def getFlop(self, cardString):
        self.cardString = cardString

    #setNext just adds the 4th or 5th card to the already created evaluation string
    def setNext(self, newCard):
        self.newCard = newCard
        self.cardString = self.cardString + self.newCard

    #Here is the actual CPU's evaluation of it's hand: Using regular expressions, the CPU
    #looks at the suit and value of the cards in its hand. If ANY values match ANY of the
    #cards face up on the table (the evaluation string: cardString) Then the computer will
    #keep playing. Otherwise it just gives up.
    def findMe(self):
            if re.search(self.card1[0], self.cardString):
                return True
            elif re.search(self.card1[1], self.cardString):
                return True
            elif re.search(self.card2[0], self.cardString):
                return True
            elif re.search(self.card2[1], self.cardString):
                return True
            else:
                return False
    #These computers are not paticularly good poker players.
