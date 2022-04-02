# German Dictionary (Conjuguemos-like), dict (dictionary) CX (Chapter X) S1 (Section 1)

## VARS ##

import random
import time
import math
from CLC_List import dictAll

germanToggle = 0
chooseChapter = 0
chooseSection = 0

showScore = 1 #toggle score
numCorrect = 0
numIncorrect = 0

showTime = 1 #toggle timer
timeLeftInternal = 0
timeLeft = "lol"

## FUNCTIONS ##

def FixInput(word, wordtype):
    """
    Fixes input type for less confusion
    """
    try:
        if wordtype == "int":
            x = int(word)
        elif wordtype == "float":
            x = float(word)
        elif wordtype == "str":
            x = str(word)
        return x
    except ValueError:
        if wordtype == "float":
            return 10
        else:
            return 0


def BuildRandomizerList(chapter, section):
    """
    Builds lists for better randomization
    """
    listrand = []
    for x in dictAll:
        if chapter != 0:
            x = chapter
        for y in dictAll[x]:
            if section != 0:
                y = section
            for z in dictAll[x][y]:
                v = dictAll[x][y][z]
                listrand.append(v)
            if section != 0:
                return listrand
                break
        if chapter != 0:
            return listrand
            break
    return listrand


def GiveTimer():
    """
    For timer function used later on in the while loop
    """
    n = math.floor(myEndTime - time.time())
    m = str(math.floor(n / 60))
    s = n - 60 * math.floor(n / 60)
    if s <= 9:
        s = "0" + str(s)
    else:
        s = str(s)
    timeLeftInternal = myEndTime - time.time()
    if timeLeftInternal <= 0:
        timeLeft = "0:00" # Turn this off for a fun surprise!
    else:
        timeLeft = m + ":" + s
    return timeLeft, timeLeftInternal


def UmlautInterpreter(word):
    """
    Umlaut intepreter for the input ("..a" = "ä")
    """
    word = word.replace('..a', 'ä')
    word = word.replace('..o', 'ö')
    word = word.replace('..u', 'ü')
    word = word.replace('..s', 'ß')
    word = word.replace('..A', 'Ä')
    word = word.replace('..O', 'Ö')
    word = word.replace('..U', 'Ü')
    return word

# Lists used to go here, now in clclist.py

## STARTUP ##

print("## Command-Line Conjuguemos ##\n\n# Zuletzt aktualisiert 11/15/2021 #\n# Hergestellt von Ethan Tock #\n")

chooseChapter = FixInput(input("Welche Kapitel?\n:"), "int")
# Put in 0 for all chapters
print()

if chooseChapter != 0:
    chooseSection = FixInput(input("Welche Lektion?\n:"), "int")
    # Put in "0" for all sections
    print()
else:
    chooseSection = 0

germanToggle = input("Vorsag englische Wörter? (j/n)\n:")
print()

if showTime == 1:
    myEndTime = 60 * FixInput(input("Wie viele Minuten?\n:"), "float") + time.time()
    print()

try:
    myChosenChapter = dictAll.get(chooseChapter)
    myChosenSection = myChosenChapter.get(chooseSection)
except AttributeError:
    chooseChapter = 0
    chooseSection = 0

randomizerList = BuildRandomizerList(chooseChapter, chooseSection)
print(f"{len(randomizerList)} Wörter.\n")

## CONJUGUEMOS LOOP ##

while True:

    # Setup and randomization

    myPracticeWord = randomizerList[random.randint(0, len(randomizerList) - 1)] #myChosenSection.get(random.randint(1, len(myChosenSection)))
    myGermanWord = myPracticeWord[0]
    myEnglishWord = myPracticeWord[1]

    # Prompt

    if germanToggle == "j":
        print(myEnglishWord)
    else:
        print(myGermanWord)

    # Input that translates "..a" into ä and such

    myGuessWord = input()
    myGuessWord = UmlautInterpreter(myGuessWord)

    # Check answer

    if germanToggle == "j":
        if myGuessWord == myGermanWord:
            print("Ja, genau!")
            numCorrect += 1
        else:
            print(f"Nein, man sagt '{myPracticeWord[0]}'.")
            numIncorrect += 1
    else:
        if myGuessWord == myEnglishWord:
            print("Ja, genau!")
            numCorrect += 1
        else:
            print(f"Nein, man sagt '{myPracticeWord[1]}'.")
            numIncorrect += 1

    # Show time and score

    if showTime == 1:
        timeLeft, timeLeftInternal = GiveTimer()

    if showScore == 1 or showTime == 1:
        print()
    if showScore == 1:
        print(f"{numCorrect} / {numIncorrect + numCorrect} richtig.")
    if showTime == 1:
        print(f"{timeLeft} übrig.")
    if timeLeftInternal <= 0 and showTime == 1:
        myScorePercentage = numCorrect/sum((numCorrect, numIncorrect)) # Must use a tuple for sum()
        print()
        print(f"{100 * round(myScorePercentage, 4)}% richtig! Mach weiter so!")
        break

    print()

# Ok so like this program should choose a random dict-key word, display it, ask me for input, and check if my answer is correct

# This program would be good for German study of the certain word lists, could use Conjuguemos if I really wanted to be boring.
