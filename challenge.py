# DailyProgrammer Challenge 39
import base64
import requests

def getinput () :
    return str(input("Input String: "))

def lettersum (intparam = 0) :
    def mainFunc (word):
        outputnum = 0
        for l in word:
            outputnum += (ord(l) - 96)
        return outputnum
    dictionary = requests.get("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt").text.splitlines()
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
        for word in dictionary:
            t = "bruh" # work on this
    else:
        x = getinput()
        print(mainFunc(x))

# Main Objective
# lettersum(0)
# 1.
# lettersum(1)
# 2.
lettersum(2)