# DailyProgrammer Challenge 39
import requests

# simple input function
def getinput () :
    return str(input("Input String: "))

# The main calculator
def mainFunc (word):
    outputnum = 0
    for l in word:
        outputnum += (ord(l) - 96)
    return outputnum

#Given dictionary
dictionary = requests.get("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt").text.splitlines()

def lettersum (intparam = 0) :
    if (intparam == 1):
        for word in dictionary:
            if (mainFunc(word) == 319):
                print(word)
    elif (intparam == 2):
        counter = 0
        for word in dictionary:
            if(mainFunc(word) % 2 != 0):
                counter += 1
        print(counter)
    elif (intparam == 3):
        maxlen = 0
        for word in dictionary:
            if (mainFunc(word) > maxlen):
                maxlen = mainFunc(word)
        lengthylist = [0] * (maxlen + 1)
        for word in dictionary:
            lengthylist[mainFunc(word)] += 1
        print(max(lengthylist))
    else:
        x = getinput()
        print(mainFunc(x))

# Main Objective
# lettersum(0)
# 1.
# lettersum(1)
# 2.
# lettersum(2)
# 3.
# lettersum(3)