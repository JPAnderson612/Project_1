import sys
from deckClass import Deck
from playerClass import Player

def newGame():
    #Deck is a list of strings representing each of the 52 cards
    deck = ["ac", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c",
    "jc", "qc", "kc", "ah", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h",
    "jh", "qh", "kh", "as", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "10s",
    "js", "qs", "ks", "ad", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "10d",
    "jd", "qd", "kd"]
    quiklst = list()
    mainDeck = Deck(deck) #This will serve as our game's deck

    mainDeck.mix() #Shuffle the deck

    #This is just dealing two cards to each player
    humVar0 = mainDeck.deal()
    humVar1 = mainDeck.deal()
    cpVar2 = mainDeck.deal()
    cpVar3 = mainDeck.deal()
    cpVar4 = mainDeck.deal()
    cpVar5 = mainDeck.deal()
    cpVar6 = mainDeck.deal()
    cpVar7 = mainDeck.deal()

    #Now we're creating new player objects with their freshly dealt hands
    player0 = Player(humVar0, humVar1)
    player1 = Player(cpVar2, cpVar3)
    player2 = Player(cpVar4, cpVar5)
    player3 = Player(cpVar6, cpVar7)
# Fully aware that lines 17-29 could be programmed much better, just can't figure it out and time is limited

    print("----------\nHere's the flop...\n----------")
    mainDeck.theFlop() #Put the first cards on the table and...
    mainDeck.printTableCards()#...print them

    flopToCPUs = mainDeck.getTable() #The deck sends us the value of the cards on the table...
    string = ""
    string = string.join(flopToCPUs)#We pass those values on to the CPUs for evaluation

    player1.getFlop(string)
    player2.getFlop(string)
    player3.getFlop(string)

    #These CPU check vars are determining if the computer is going to keep playing
    cpuOneCheck = player1.findMe()
    cpuTwoCheck = player2.findMe()
    cpuThreeCheck = player3.findMe()

    #This sets up for the future removal of the CPUs
    markCpu0 = False
    markCpu1 = False
    markCpu2 = False

    cpuList = [cpuOneCheck, cpuTwoCheck, cpuThreeCheck]

    #Summarized, this next bit is: If the CPU is going to play, print that it's checking,
    #but if it's not playing, have it fold AND remove it from play.
    #Spoiler alert: Not exactly functional
    for cpu in range(0, len(cpuList)):
        if cpuList[cpu]:
            print("CPU " + str(cpu) + " checks")
        else:
            if cpu == 0:
                markCpu0 = True
                print("CPU " + str(cpu) + " folds")
            elif cpu == 1:
                markCpu1 = True
                print("CPU " + str(cpu) + " folds")
            elif cpu == 2:
                markCpu2 = True
                print("CPU " + str(cpu) + " folds")

    #Lines 77 through 90 are taking and CPUs that are marked for removal and
    #actually removing them from their "master list" so they don't play anymore
    if markCpu0:
        cpuList.remove(cpuOneCheck)
        markCpu0 = False

    if markCpu1:
        cpuList.remove(cpuTwoCheck)
        markCpu1 = False

    if markCpu2:
        cpuList.remove(cpuThreeCheck)
        markCpu2 = False

    #give the Human their cards here, then they can choose if they want to fold or check.
    #As is probably obvious, if they fold they lose, and if they check they continue
    print("Here are YOUR cards:")
    player0.printCards()
    print("Press 'c' to check and 'f' to fold")
    playerPick = input(">")


    if playerPick == "c":
        mainDeck.theBurn() #add one card to the table
        nextC = mainDeck.getNextCard() #This var gets passed to the CPUs as an additional card to
                                       #evaluate their hands to

        player1.setNext(nextC) #Add the new card to the evaluation string
        player2.setNext(nextC)
        player3.setNext(nextC)

        #Once again check to see if the CPU will keep playing
        cpuOneCheck = player1.findMe()
        cpuTwoCheck = player2.findMe()
        cpuThreeCheck = player3.findMe()

#-------------------------------------
#At this point, a lot of the code is repasted from earlier, as the same formulas
#need to run another time. Obviously pasting the same thing over and over is stupid
#when you can automate it, but I underestimated how in depth this project would be,
#and now it's 6am.
#Copy paste = little brain power = better at 6am
        for cpu in range(0, len(cpuList)):
            if cpuList[cpu]:
                print("CPU " + str(cpu) + " checks")
            else:
                if cpu == 0:
                    cpuList.remove(cpuOneCheck)
                    print("CPU " + str(cpu) + " folds")
                elif cpu == 1:
                    cpuList.remove(cpuTwoCheck)
                    print("CPU " + str(cpu) + " folds")
                elif cpu == 2:
                    cpuList.remove(cpuThreeCheck)
                    print("CPU " + str(cpu) + " folds")

        if markCpu0:
            cpuList.remove(cpuOneCheck)
            blacklist.append("cpu1")

        if markCpu1:
            cpuList.remove(cpuTwoCheck)
            blacklist.append("cpu2")

        if markCpu2:
            cpuList.remove(cpuThreeCheck)
            blacklist.append("cpu3")

        print("Here are YOUR cards:")
        player0.printCards()
        print("Press 'c' to check and 'f' to fold")
        playerPick2 = input(">")

        if playerPick2 == "c":
            mainDeck.theBurn()
            nextC = mainDeck.getNextCard()

            player1.setNext(nextC)
            player2.setNext(nextC)
            player3.setNext(nextC)

            cpuOneCheck = player1.findMe()
            cpuTwoCheck = player2.findMe()
            cpuThreeCheck = player3.findMe()

            for cpu in range(0, len(cpuList)):
                if cpuList[cpu]:
                    print("CPU " + str(cpu) + " checks")
                else:
                    if cpu == 0:
                        cpuList.remove(cpuOneCheck)
                        print("CPU " + str(cpu) + " folds")
                    elif cpu == 1:
                        cpuList.remove(cpuTwoCheck)
                        print("CPU " + str(cpu) + " folds")
                    elif cpu == 2:
                        cpuList.remove(cpuThreeCheck)
                        print("CPU " + str(cpu) + " folds")

            #I didn't finish, so I just copped out the ending by
            #showing all the player's cards and the table cards.
            print("\nCPU 1s cards:")
            player1.printCards()

            print("\nCPU 2s cards:")
            player2.printCards()

            print("\nCPU 3s cards:")
            player3.printCards()

            print("\nAnd your cards:")
            player0.printCards()

            print("\nCards up are:")
            mainDeck.printTableCards()

        elif playerPick == "f": #If the player folds they lose (duh)
            print("You lost!")
            sys.exit()

    elif playerPick == "f":
        print("You lost!")
        sys.exit()

#And here's the menu, quite straightforward if you read it.
print("-" * 10)
print("Poker")
print("-" * 10)
print("Main Menu\n1. Start game\n2. EXIT")
userSelect = int(input("Pick a number >"))
# Don't forget exception handling

if(userSelect == 1):
    print("Starting new game!")
    newGame()
#elif(userSelect == 2):
    #print("Resuming game")
elif(userSelect == 3):
    print("Farewell")
    sys.exit()
