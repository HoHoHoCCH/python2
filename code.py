#First We import time for waiting, random for selecting the 3 numbers, and the 3 globals for use of other functions
import time
import random
import sys
global ca2
global ca1
global ca3
global guesses
global correctNumbers
global correctOrder
global ifa
guesses = 0








def game2():




    #entering numbers
    correctNumbers = 0
    ca1 = 0
    ca2 = 0
    ca3 = 0
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    ca1 = random.choice(numbers)
    ca2 = random.choice(numbers)
    ca3 = random.choice(numbers)
    ifa = [ca1, ca2, ca3]
    correctOrder = 0
    print(ifa)
    input1 = input()
    input2 = input()
    input3 = input()
    correctNumbers = 0
    if input1 == ca1: #here we are testinf for input1 of all 3 numbers.
        print("The First Number Is 100% Correct. Number and Order.")
        correctNumbers += 1
        correctOrder += 1
    if input1 == ifa:
        correctNumbers += 1
    if input2 == ca2:  #over here we are doing the same thing but for 2
        print("The Second number Is 100% Correct. Number and Order.")
        correctOrder += 1
        correctNumbers += 1
    if input2 == ifa:
        correctNumbers += 1
    if input3 == ca3:  #same here, but for 3
        print("The Third number Is 100% Correct. Number and Order.")
        correctOrder += 1
        correctNumbers += 1
    if input3 == ifa:
        correctNumbers += 1
    if correctNumbers == 3:
        win()
    else:
        lose()
        guesses += 1

def game3():
    print(ifa)
    input1 = input(1)
    input2 = input(2)
    input3 = input(3)
    correctNumbers = 0
    if input1 == ca1: #here we are testinf for input1 of all 3 numbers.
        print("The First Number Is 100% Correct. Number and Order.")
        correctNumbers += 1
        correctOrder += 1
    if input1 == ifa:
        correctNumbers += 1
    if input2 == ca2:  #over here we are doing the same thing but for 2
        print("The Second number Is 100% Correct. Number and Order.")
        correctOrder += 1
        correctNumbers += 1
    if input2 == ifa:
        correctNumbers += 1
    if input3 == ca3:  #same here, but for 3
        print("The Third number Is 100% Correct. Number and Order.")
        correctOrder += 1
        correctNumbers += 1
    if input3 == ifa:
        correctNumbers += 1
    if correctNumbers == 3:
        win()
    else:
        lose()
        guesses += 1



def lose():
    print("You have ", "Numbers Correct")
    print("And", "Numbers That are correct in order.")
    game3()

def win():
    print("Congratulations!")
    print("It took you", guesses, "guesses to Win.")
    q2 = input()
    if q2 == "yes":
        startGame()


def startLevel1():
    #chooses the numbers
    wait1sec()
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    ca1 = random.choice(numbers)
    ca2 = random.choice(numbers)
    ca3 = random.choice(numbers)
    game2()



#The game starts here
def startGame():
    guesses = 0
    print("Welecome To Mastermind!")
    print("How To Play:")
    wait1sec()
    print("1. The Computer will select 3 numbers from 1 to 10, you must guess all 3 numbers in the right order.")
    wait1sec()
    print("2. Each time you guess, the computer will tell you how much numbers did you guess right, and tell you if those numbers were in the correct order.")
    wait1sec()
    print("3.There is no limit to how much guesses you can use.")
    wait1sec()
    print("You win by guessing all the correct numbers in the right order")
    startLevel1()



























def wait1sec():
    time.sleep(1)

startGame()

