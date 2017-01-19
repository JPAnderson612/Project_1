import random

class Deck():

    def __init__(self, deck):
        self.deck = deck #Initialize with the deck from the main function
        self.table = list()

    #This just shuffles the list of cards.
    def mix(self):
        random.shuffle(self.deck)
        print("Deck shuffled!")

    #This takes a card OUT of the list and gives it to what calls it.
    def deal(self):
        self.card = self.deck.pop()
        #print("Card popped!")
        return self.card

    #The first deal. Three cards are popped off the deck and put into a new list,
    #which acts as the table cards
    def theFlop(self):
        for card in range(0, 3):
            self.table.append(self.deck.pop())

    #This prints the cards on the table
    def printTableCards(self):
        self.fakeList = self.table
        for card in range(0, len(self.fakeList)):
            print(str(self.fakeList[card]))

    #Takes one more card and adds it to the table
    def theBurn(self):
        self.table.append(self.deck.pop())

    #get the table for whoever needs it
    def getTable(self):
        return self.table

    #Get the previously popped card for whoever needs it. 
    def getNextCard(self):
        return self.table[-1]
