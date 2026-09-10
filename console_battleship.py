import random #python standard libary
import sys
import time
import os
#! I messed with this a few days after the assignment accidently while showing my friends
#! Go to more > history > 12/6/25 @5:56 AM for the submitted version
#!
#!
#!
print("Welcome to Console Battleship!")

tutorial = str(input("Do you know how to play the game? (Y/N) "))
while not (tutorial == "Yes" or  tutorial == "yes" or  tutorial == "y" or tutorial == "Y" or tutorial == "No" or  tutorial == "no" or  tutorial == "n" or tutorial == "N"): #if the answer isn't valid
    print('That is not a valid input, please enter "Yes", "y", No", or "N"!') #keep looping until valid answer
    tutorial = str(input("Do you know how to play the game? (Y/N) "))
if tutorial == "No" or  tutorial == "no" or  tutorial == "n" or tutorial == "N":
    #printing tutorial line by line, with pauses in bewtween to help the player to read
    print("The goal is to guess where the enemy's ships are to destory them, you each get to fire at and check one grid square per turn!")
    time.sleep(3)
    print("Note that if you hit at a floating ship (represented by X) aim around it to destroy the rest!")
    time.sleep(3)
    print("The one who destroys all the opponent's ships first is the winner!")
    time.sleep(3)
    print("")
    time.sleep(2)
    print("To represent the game's various pieces on the map, symbols are used:")
    time.sleep(2)
    print('" " (space) is empty water on your side and unknown on the enemy map')
    time.sleep(2)
    print('"+" is empty water that has been shot at"')
    time.sleep(2)
    print('"▆ " is an floating boat piece (you can only see your own)')
    time.sleep(2)
    print('"X" is a hit ship that as a whole remains floating')
    time.sleep(2)
    print('"~" represents a sunken ship!')
elif tutorial == "Yes" or  tutorial == "yes" or  tutorial == "y" or tutorial == "Y":
    print("Great, good luck!")

rows = [] #creating the maps, currently empty
enemyRows = []
printableRows = []
emptyRow = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "] #row of 10 spaces
for i in range(0, 10): #gives each map 10 rows of 10 spaces
    rows.append(list(emptyRow))
    enemyRows.append(list(emptyRow))
    printableRows.append(list(emptyRow))

def printMap(): #defines printing the map including the numbers on the side and top
    print("Your Map:")
    print("")
    print("1 2 3 4 5 6 7 8 9 10")
    currentRow = rows[0] 
    for i in range(0, 10):
        currentRow = rows[i]
        print(currentRow[0],currentRow[1],currentRow[2],currentRow[3],currentRow[4],currentRow[5],currentRow[6],currentRow[7],currentRow[8],currentRow[9], i + 1)
def enemyPrintMap(): #defines printing the enemy map including the numbers on the side and top
    print("")
    print("Enemy Map:")
    print("")
    print("1 2 3 4 5 6 7 8 9 10")
    for i in range(0, 10):
        currentRow = printableRows[i]
        while printableRows[i].count("▆") > 0: #if an enemy gridpoint is a boat
            printableCol = printableRows[i].index("▆")  #find the gridpoint
            printableRows[i][printableCol] = " " #and convert to a " " for the printed enemy map to avoid leaking enemy boat locations
        print(printableRows[i][0],printableRows[i][1],printableRows[i][2],printableRows[i][3],printableRows[i][4],printableRows[i][5],printableRows[i][6],printableRows[i][7],printableRows[i][8],printableRows[i][9],i + 1)
    print("")

print("")
print("Difficulty Selection:")
print("Easy Mode: The bot fires entirely randomly")
print("Medium Mode: The bot fires randomly but will not hit the same gridpoint twice")
print("Hard Mode: The bot will not hit a gridpoint twice when firing randomly and after hitting a boat it will start shooting around and finishing it off")
print("")
level = str(input("Would you like to play on easy mode (1), medium mode (2), or hard mode (3) ")) #while loops to ensure the player picks a valid difficulty
while not (level == "easy mode" or level == "easy" or level == "1" or level == "medium mode" or level == "medium" or level == "2" or level == "hard mode" or level == "hard" or level == "3"):
    if level == "easy mode" or level == "easy" or level == "1":
        level = "1"
    elif level == "medium mode" or level == "medium" or level == "2":
        level = "2"
    elif level == "hard mode" or level == "hard" or level == "3":
        level = "3"
    else:
        print('That is not a valid input, please enter easy, medium, hard, 1, 2, or 3!')
        level = str(input("Would you like to play on easy mode (1), medium mode (2), or hard mode (3) "))
printMap()
#starts placing boats of length 2, 3, 4, and 5
#forces a valid direction of either ver or hor in the end
boatDirs = ["no 0", "no 1", "", "", "", ""] #declaring lists to hold all the player boat position values, no 0 and no 1 represent the lack of 0 and 1 boats
boatCols = ["no 0", "no 1", "", "", "", ""]
boatRows = ["no 0", "no 1", "", "", "", ""]
boatIsValid = False
for i in range(2, 6): #2 - 6 because i is used later for boat spawning mechanics
    while True:
        boatDirs[i] = str(input(f"Would you like the {i} length boat to be horizontal (1) or vertical (2)? ")) #gets direction and standardizes to either 1 or 2
        if boatDirs[i] == "horizontal" or boatDirs[i] == "1" or boatDirs[i] == "hor":
            boatDirs[i] = "hor"
            break
        elif boatDirs[i] == "vertical" or boatDirs[i] == "2" or boatDirs[i] == "ver":
            boatDirs[i] = "ver"
            break
    boatCols[i] = int(input(f"Which column would you like to place a {i} length boat in? ")) - 1 #gets placing position of boat from player
    boatRows[i] = int(input(f"Which row would you like to place a {i} length boat in? ")) - 1
    while not (boatCols[i] >= 0 and boatCols[i] <= 9 and boatRows[i] >= 0 and boatRows[i] <= 9): #while loop until the player enters a valid coordinate with 2 numbers 1 to 10
        print("")
        print("That is not a valid input, make sure to enter whole numbers from 1 - 10 for the rows and columns")
        boatCols[i] = int(input(f"Which column would you like to place a {i} length boat in? ")) - 1
        boatRows[i] = int(input(f"Which row would you like to place a {i} length boat in? ")) - 1
    while boatIsValid == False: #while loop around a series of checks to ensure the boats are placed properly
        boatIsValid = True
        # boatDirs[i] = str(input("Would you like the 3 length boat to be horizontal (1) or vertical (2)? "))
        while not (boatDirs[i] == "horizontal" or boatDirs[i] == "hor" or boatDirs[i] == "1" or boatDirs[i] == "vertical" or boatDirs[i] == "ver" or boatDirs[i] == "2"): #while direction is invalid
            boatDirs[i] = str(input(f"Would you like the {i} length boat to be horizontal (1) or vertical (2)? "))
            if boatDirs[i] == "horizontal" or boatDirs[i] == "1" or boatDirs[i] == "hor": #standardizes direction, needed here as part of the while loop that ensures correct placement
                boatDirs[i] = "hor"
                break
            elif boatDirs[i] == "vertical" or boatDirs[i] == "2" or boatDirs[i] == "ver":
                boatDirs[i] = "ver"
                break
            else:
                print('That is not a valid direction, please enter "horizontal", "vertical", "1", or "2"') #rejects answer and DOESNT break out of for loop
        #while loop to prevent the boat from spawning partially off the map
        while (boatDirs[i] == "hor" and int(boatCols[i]) > 8 and int(boatCols[i]) < 0) or (boatDirs[i] == "ver" and int(boatCols[i]) > 8 and int(boatCols[i]) < 0):
            print("It appears this boat extends to out of the confines of the map, please pick a new location")
            print("Note that the inputted row and column represent the top left corner of the boat")
            print("")
            boatCols[i] = int(input(f"Which column would you like to place a {i} length boat in? ")) - 1
            boatRows[i] = int(input(f"Which row would you like to place a {i} length boat in? ")) - 1
            boatIsValid = False
            break
        #prevents boat from overlapping with other boats
        for j in range(2, 6):
            for k in range(0, j
        
        
        
    
    \
    ):
                if boatDirs[i] == "hor" and rows[boatRows[i]][boatCols[i] + k] == "▆":
                    boatIsValid = False
                    break
                elif boatDirs[i] == "ver" and rows[boatRows[i] + k][boatCols[i]] == "▆":
                    boatIsValid = False
                    break
            for k in range(0, i): #begins placing boats, needed in the large while loop to ensure proper placement
                if boatDirs[i] == "hor" and boatIsValid:
                    rows[boatRows[i]][boatCols[i] + k] = "▆"
                elif boatDirs[i] == "ver" and boatIsValid:
                    rows[boatRows[i] + k][boatCols[i]] = "▆"
    for k in range(0, i): #second block to place boats independantly of the large while loop, preventning a boat being placed more than once
        if boatDirs[i] == "hor" and boatIsValid:
            rows[boatRows[i]][boatCols[i] + k] = "▆"
        elif boatDirs[i] == "ver" and boatIsValid:
            rows[boatRows[i] + k][boatCols[i]] = "▆"
    printMap()
print("")
#starts placing enemy boats of length 2, 3, 4, and 5
enemyBoatDirs = ["no 0", "no 1", "", "", "", ""] #declaring lists to hold all the player boat position values, no 0 and no 1 represent the lack of 0 and 1 boats
enemyBoatCols = ["no 0", "no 1", "", "", "", ""]
enemyBoatRows = ["no 0", "no 1", "", "", "", ""]
enemyBoatIsValid = False
for i in range(2, 6): #2 - 6 because i is used later for boat spawning mechanics
    enemyBoatDirs[i] = str(random.randint(1, 2))
    if enemyBoatDirs[i] == "horizontal" or enemyBoatDirs[i] == "1":  #gets direction and standardizes to either 1 or 2
        enemyBoatDirs[i] = "hor"
    elif enemyBoatDirs[i] == "vertical" or enemyBoatDirs[i] == "2":
        enemyBoatDirs[i] = "ver"
    enemyBoatCols[i] = random.randint(0, 10 - i)  #while loop until the enemy enters a valid coordinate with 2 numbers 1 to 10
    enemyBoatRows[i] = random.randint(0, 10 - i) 
    while enemyBoatIsValid == False:
        enemyBoatIsValid = True
        # enemyBoatDirs[i] = str(input("Would you like the 3 length enemyBoat to be horizontal (1) or vertical (2)? "))
        while not (enemyBoatDirs[i] == "horizontal" or enemyBoatDirs[i] == "hor" or enemyBoatDirs[i] == "1" or enemyBoatDirs[i] == "vertical" or enemyBoatDirs[i] == "ver" or enemyBoatDirs[i] == "2"): #while direction is invalid
            enemyBoatDirs[i] = str(random.randint(1, 2))
            if enemyBoatDirs[i] == "horizontal" or enemyBoatDirs[i] == "1": #standardizes direction, needed here as part of the while loop that ensures correct placement
                enemyBoatDirs[i] = "hor"
                break
            elif enemyBoatDirs[i] == "vertical" or enemyBoatDirs[i] == "2":
                enemyBoatDirs[i] = "ver"
                break
        #prevents enemy boat from hanging over edge of map
        while (enemyBoatDirs[i] == "hor" and int(enemyBoatCols[i]) > 8 and int(enemyBoatCols[i]) < 0) or (enemyBoatDirs[i] == "ver" and int(enemyBoatCols[i]) > 8 and int(enemyBoatCols[i]) < 0):
            enemyBoatCols[i] = random.randint(0, 10 - i)
            enemyBoatRows[i] = random.randint(0, 10 - i)
            enemyBoatIsValid = False
            break
        #prevents enemy boat from overlapping with other enemy boats and begins placing
        for i in range(2, 6):
            for k in range(0, i):
                if enemyBoatDirs[i] == "hor" and enemyRows[enemyBoatRows[i]][enemyBoatCols[i] + k] == "▆":
                    enemyBoatIsValid = False
                    break
                elif enemyBoatDirs[i] == "ver" and enemyRows[enemyBoatRows[i] + k][enemyBoatCols[i]] == "▆":
                    enemyBoatIsValid = False
                    break
            for k in range(0, i):
                if enemyBoatDirs[i] == "hor" and enemyBoatIsValid:
                    enemyRows[enemyBoatRows[i]][enemyBoatCols[i] + k] = "▆"
                elif enemyBoatDirs[i] == "ver" and enemyBoatIsValid:
                    enemyRows[enemyBoatRows[i] + k][enemyBoatCols[i]] = "▆"
    for k in range(0, i):  #second block to place boats independantly of the large while loop, preventning a boat being placed more than once
        if enemyBoatDirs[i] == "hor" and enemyBoatIsValid:
            enemyRows[enemyBoatRows[i]][enemyBoatCols[i] + k] = "▆"
        elif enemyBoatDirs[i] == "ver" and enemyBoatIsValid:
            enemyRows[enemyBoatRows[i] + k][enemyBoatCols[i]] = "▆"

findingBoat = False #declaring varibles for enemy shooting and hard mode bot 
findingBoatSwitchLeft = False
findingBoatSwitchDown = False
findingBoatColOffset = 0
findingBoatRowOffset = 0
firstHitRow = 0
firstHitCol = 0
ready = str(input("Are you ready to start the battle? (hit enter to continue) ")) #gives the player an otherwise pointless pause to read and ready up to the battle
os.system('clear')

#end of boat setup; naval warfare begins ⌄⌄⌄
while True:
    print("")
    targetCol = int(input(f"Which column are you firing at? (1-10) ")) - 1  #gets position to shoot at
    targetRow = int(input(f"Which row are you firing at? (1-10) ")) - 1
    while not (targetCol >= 0 and targetCol <= 9 and targetRow >= 0 and targetRow <= 9): #declines answer, until player gives two proper number from 1 - 10
        print("")
        print("That is not a valid input, make sure to enter whole numbers from 1 - 10 for the rows and columns")
        targetCol = int(input(f"Which column are you firing at? (1-10) ")) - 1
        targetRow = int(input(f"Which row are you firing at? (1-10) ")) - 1
    os.system('clear')  #clears console so that each turn it is refresh, rather than creating one long text
    
    if enemyRows[targetRow][targetCol] == " ": #finds what the grid point is and reacts to being hit, printable map also affected
        print("You missed the boats!")
        enemyRows[targetRow][targetCol] = "+"
        printableRows[targetRow][targetCol] = "+"
    elif enemyRows[targetRow][targetCol] == "▆":
        print("Hit! You destroyed a piece of the boat!")
        enemyRows[targetRow][targetCol] = "X"
        printableRows[targetRow][targetCol] = "X"
    elif enemyRows[targetRow][targetCol] == "X":
        print("You have already destroyed that boat square! ")
    elif enemyRows[targetRow][targetCol] == "+":
        print("You have already shot that empty water! ")
    # enemyPrintMap()
    if (rows[firstHitRow][firstHitCol + 1] == "X" or rows[firstHitRow][firstHitCol + 1] == " " or rows[firstHitRow][firstHitCol + 1] == "▆") and firstHitCol <= 8 and not findingBoatSwitchLeft: #rightwards firing at partially discovered boats
        findingBoatColOffset = 1 #resets adjustments to avoid work independantly 
        findingBoatRowOffset = 0
        while rows[firstHitRow][firstHitCol + findingBoatColOffset] == "X" and firstHitCol <= 8: #if the next square right is a damaged boat piece and if not on right edge
            # print("firing rightwards")
            enemyTargetCol += 1 #adjusts targeting and offset to match moving one rightwards
            findingBoatColOffset += 1
            enemyTargetRow = firstHitRow #resets target row to the first hit to continue finding next sections of the boat
            findingBoatRowOffset = 0    #resets other offset to prevent interference 
            if rows[firstHitRow][firstHitCol + findingBoatColOffset] != "X": #if the chain of following along the boat ends, resulting in a break and firing at that gridpoint
                break
    elif (rows[firstHitRow][firstHitCol - 1] == "X" or rows[firstHitRow][firstHitCol - 1] == " " or rows[firstHitRow][firstHitCol - 1] == "▆") and firstHitCol >= 0 and  findingBoatSwitchLeft: #leftwards firing at partially discovered boats
        findingBoatColOffset = 0
        findingBoatRowOffset = 0
        while rows[firstHitRow][firstHitCol + findingBoatColOffset] == "X" and firstHitCol >= 1: #if the next square left is a damaged boat piece and if not on left edge
            # print("firing leftwards")
            enemyTargetCol -= 1 #adjusts targeting and offset to match moving one leftwards
            findingBoatColOffset -= 1
            enemyTargetRow = firstHitRow #resets target row to the first hit to continue finding next sections of the boat
            findingBoatRowOffset = 0     #resets other offset to prevent interference 
            if rows[firstHitRow][firstHitCol + findingBoatColOffset] != "X": #if the chain of following along the boat ends, resulting in a break and firing at that gridpoint
                break
    elif (rows[firstHitRow - 1][firstHitCol] == "X" or rows[firstHitRow - 1][firstHitCol] == " " or rows[firstHitRow - 1][firstHitCol] == "▆") and firstHitRow >= 0 and not findingBoatSwitchDown: #downwards firing at partially discovered boats
        findingBoatColOffset = 0
        findingBoatRowOffset = 0
        while rows[firstHitRow + findingBoatRowOffset][firstHitCol] == "X" and firstHitRow >= 1: #if the next square up is a damaged boat piece and if not on upper edge
            # print("firing upwards")
            enemyTargetRow -= 1 #adjusts targetting and offset to match moving one upwards
            findingBoatRowOffset -= 1
            enemyTargetCol = firstHitCol #resets target row to the first hit to continue finding next sections of the boat
            findingBoatColOffset = 0     #resets other offset to prevent interference 
            if rows[firstHitRow + findingBoatRowOffset][firstHitCol] != "X": #if the chain of following along the boat ends, resulting in a break and firing at that gridpoint
                break
    elif (rows[firstHitRow + 1][firstHitCol] == "X" or rows[firstHitRow + 1][firstHitCol] == " " or rows[firstHitRow + 1][firstHitCol] == "▆") and firstHitRow <= 8 and findingBoatSwitchDown: #downwards firing at partially discovered boats
        findingBoatColOffset = 0
        findingBoatRowOffset = 1
        while rows[firstHitRow + findingBoatRowOffset][firstHitCol] == "X" and firstHitRow <= 8: #if the next square down is a damaged boat piece and if not on lower edge edge
            # print("firing downwards")
            enemyTargetRow += 1 #adjusts targeting and offset to match moving one downwards
            findingBoatRowOffset += 1
            enemyTargetCol = firstHitCol #resets target row to the first hit to continue finding next sections of the boat
            findingBoatColOffset = 0     #resets other offset to prevent interference 
            if rows[firstHitRow + findingBoatRowOffset][firstHitCol] != "X": #if the chain of following along the boat ends, resulting in a break and firing at that gridpoint
                break
            
    enemyTargetCol = firstHitCol + findingBoatColOffset #change enemy target to include determined offsets for left/right adjustments
    enemyTargetRow = firstHitRow + findingBoatRowOffset
    
    # print(findingBoatSwitchLeft, findingBoatSwitchDown) #handy debugging print statements
    # print(findingBoatColOffset, firstHitCol, enemyTargetCol)
    # print(findingBoatRowOffset, firstHitRow, enemyTargetRow)
    #enemy turn code starts below
    if level == "1":
        enemyTargetCol = random.randint(0, 9) #easy mode bot always shoots randomly
        enemyTargetRow = random.randint(0, 9)
    elif level == "2" or (level == "3" and findingBoat == False): #medium mode bot and hard mode bot when not finishing boats shoot randomly
        enemyTargetCol = random.randint(0, 9)
        enemyTargetRow = random.randint(0, 9)
        while not (rows[enemyTargetRow][enemyTargetCol] == " " or rows[enemyTargetRow][enemyTargetCol] == "▆"): #if the targeted position has been hit before
            enemyTargetCol = random.randint(0, 9) #rerolls medium/hard bot random shoot if they have shot there already
            enemyTargetRow = random.randint(0, 9)
    else:
        enemyTargetCol = firstHitCol + findingBoatColOffset #reset enemy target to include determined offsets for left/right adjustments
        enemyTargetRow = firstHitRow + findingBoatRowOffset #reset enemy target to include determined offsets for up/down adjustments
        
    enemyCurrentRow = rows[enemyTargetRow] #code for enemy firing and player map to response to being hit below
    if enemyCurrentRow[enemyTargetCol] == " ":
        print("The enemy missed the boats!")
        if findingBoatSwitchLeft == True and findingBoatSwitchDown == False: #if the bot was shooting left and missed
            findingBoatSwitchLeft = False #set up to attempt to shoot downwards to continue finishing boat
            findingBoatSwitchDown = True
            findingBoatColOffset = -1
            findingBoatRowOffset = 0
        elif findingBoatSwitchLeft == False and findingBoatSwitchDown == True: #if the bot was shooting down and missed
            findingBoatSwitchLeft = True #set up to attempt to shoot downwards to continue finishing boat
            findingBoatSwitchDown = False
            findingBoatRowOffset = -1
            findingBoatColOffset = 0
        else:
            findingBoatSwitchDown = True
            findingBoatColOffset = 0
            findingBoatRowOffset = 0
            
        enemyCurrentRow[enemyTargetCol] = "+" #replaces empty water with shot at empty water symbol
        
    elif enemyCurrentRow[enemyTargetCol] == "▆":
        print("Hit! The enemy destroyed a piece of your boat!")
        if findingBoat == False: #if the hard mode bot was shooting randomly
            firstHitCol = enemyTargetCol #defines first hit positions to assit in finishing the boat
            firstHitRow = enemyTargetRow
        findingBoat = True #cause the hard mode bot to stop shooting randomly and start finishing boat
        enemyCurrentRow[enemyTargetCol] = "X" #replaces gridsquare with damaged boat square symbol
        
    elif enemyCurrentRow[enemyTargetCol] == "X": #if already hit the damaged boat
        print("The enemy has already destroyed that boat section! ")
        
    elif enemyCurrentRow[enemyTargetCol] == "~": #if already hit the sunk boat
        print("The enemy has already sunk that boat! ")
        
    elif enemyCurrentRow[enemyTargetCol] == "+": #if already shot the empty water
        print("The enemy has already shot that empty water! ")
        if findingBoatSwitchLeft == True and findingBoatSwitchDown == False: #if the bot was shooting left and missed
            findingBoatSwitchLeft = False #set up to attempt to shoot downwards to continue finishing boat
            findingBoatSwitchDown = True
            findingBoatColOffset = -1
        elif findingBoatSwitchLeft == False and findingBoatSwitchDown == True: #if the bot was shooting down and missed
            findingBoatSwitchLeft = True #set up to attempt to shoot downwards to continue finishing boat
            findingBoatSwitchDown = False
            findingBoatRowOffset = -1
        else:
            findingBoatSwitchLeft = True
            findingBoatColOffset = -1
            findingBoatRowOffset = 0
    for i in range(2, 6):
        #detects if a player boat has been fully destroyed and sets points to ~ 
        if boatDirs[i] == "hor": 
            boatPotentiallyDestroyed = True
            for k in range(0, i): #once per length of the given boat, run for each boat
                if not rows[boatRows[i]][boatCols[i] + k] == "X": #using a for loop checks every boat if the boat has remaining pieces that are undamaged, horizontally
                    boatPotentiallyDestroyed = False #prevents conversion of X to ~ 
                    break
            if boatPotentiallyDestroyed == True: #if converting from X to ~
                for k in range(0, i): #runs once per given boat length
                    rows[boatRows[i]][boatCols[i] + k] = "~" 
                    findingBoat = False #the boat was destroyed so deactivate the hard mode bot finishing boat sequence
                print(f"Your {i} length boat has been destroyed! ")
                    
        if boatDirs[i] == "ver":  
            boatPotentiallyDestroyed = True
            for k in range(0, i): #once per length of the given boat, run for each boat
                if not rows[boatRows[i] + k][boatCols[i]] == "X": #using a for loop checks every boat if the boat has remaining pieces that are undamaged, vertically
                    boatPotentiallyDestroyed = False #prevents conversion of X to ~ 
                    break
            if boatPotentiallyDestroyed == True: #if converting from X to ~
                for k in range(0, i): #runs once per given boat length 
                    rows[boatRows[i] + k][boatCols[i]] = "~"
                    findingBoat = False #the boat was destroyed so deactivate the hard mode bot finishing boat sequence
                print(f"Your {i} length boat has been destroyed! ")

        #detects if an enemy boat has been fully destroyed and sets points to ~ 
        if enemyBoatDirs[i] == "hor": 
            boatPotentiallyDestroyed = True
            for k in range(0, i):
                if not enemyRows[enemyBoatRows[i]][enemyBoatCols[i] + k] == "X": #using a for loop checks every boat if the boat has remaining pieces that are undamaged, horizontally, for enemy boats
                    boatPotentiallyDestroyed = False #prevents conversion of X to ~ 
                    break
            if boatPotentiallyDestroyed == True: #if converting from X to ~
                for k in range(0, i): #runs once per given boat length
                    enemyRows[enemyBoatRows[i]][enemyBoatCols[i] + k] = "~"
                    printableRows[enemyBoatRows[i]][enemyBoatCols[i] + k] = "~"
                    #do NOT disable findingBoat as this code is for the enemy ships being sunk, not player ships
                print(f"The enemy {i} length boat has been destroyed! ")
                    
        if enemyBoatDirs[i] == "ver": 
            boatPotentiallyDestroyed = True
            for k in range(0, i):
                if not enemyRows[enemyBoatRows[i] + k][enemyBoatCols[i]] == "X": #using a for loop checks every boat if the boat has remaining pieces that are undamaged, vertically, for enemy boats
                    boatPotentiallyDestroyed = False #prevents conversion of X to ~ 
                    break
            if boatPotentiallyDestroyed == True: #if converting from X to ~
                for k in range(0, i): #runs once per given boat length
                    enemyRows[enemyBoatRows[i] + k][enemyBoatCols[i]] = "~"
                    printableRows[enemyBoatRows[i] + k][enemyBoatCols[i]] = "~"
                    #do NOT disable findingBoat as this code is for the enemy ships being sunk, not player ships                    
                print(f"The enemy {i} length boat has been destroyed! ")
    boatSquaresRemaining = 0 #resets win condition
    enemyBoatSquaresRemaining = 0 #resets enemy win condition
    for i in range(0, 10): 
        boatSquaresRemaining += rows[i].count("▆") #counts the floating boat pieces in the player map
        enemyBoatSquaresRemaining += enemyRows[i].count("▆") #counts the floating boat pieces in the enemy map
    if boatSquaresRemaining == 0: #if the player has no enemy ships left, game won
        print("Defeat! The enemy destroyed all your ships!")
        sys.exit #ends game
    if enemyBoatSquaresRemaining== 0: #if the enemy has no player ships left, game lost
        print("Victory! You destroyed all enemy ships!")
        sys.exit #ends game
        
    enemyPrintMap() #prints enemy printable map at the end of the turn
    printMap() #prints player map at the end of the turn
