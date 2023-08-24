import os
import time
import math
import operator

print("Welcome to my Python Calculator!")
time.sleep(.5)
print("Here are the operations you can perform: ")
time.sleep(.3)
print("1) Addition")
time.sleep(.1)
print("2) Subtraction")
time.sleep(.1)
print("3) Multiplication")
time.sleep(.1)
print("4) Division")

question = input("Select an option from above\n")

#Addition
if question == "addition" or question == "Addition" or question == "1" and "add" and "Add":
    os.system('cls' if os.name == 'nt' else 'clear') #clears the terminal, this checks if you're running windows(nt) or if your running anything else it will run cls
    print("Please enter the first number in your sum:")
    number1 = input()
    time.sleep(.1)
    print("Okay, " + number1 + " is your first number, what's the second number you want to add with?")
    number2 = input()
    userInputForYesOrNo = input(number1 + " + " + number2 + " - Calculate?\n")

    if userInputForYesOrNo == "y" or "yes" or "yeah":
        # int(number1)
        # int(number2)
        answerForAddition = int(number1) + int(number2)
        print("The answer is: ", answerForAddition, " - Thanks for using the Python Calculator, WaffleBell")

if question == "subtract" or question == "Subtraction" or question == "2" and "Subtract" and "subscribe and like the video":
        os.system('cls' if os.name == 'nt' else 'clear') #clears the terminal, this checks if you're running windows(nt) or if your running anything else it will run cls
        print("Please enter the first number in your sum:")
        number1 = input()
        time.sleep(.1)
        print("Okay, " + number1 + " is your first number, what's the second number you want to subtract with?")
        number2 = input()
        userInputForYesOrNo = input(number1 + " - " + number2 + " - Calculate?\n")

        if userInputForYesOrNo == "y" or "yes" or "yeah":
          # int(number1)
          # int(number2)
          answerForAddition = int(number1) - int(number2)
          print("The answer is: ", answerForAddition, " - Thanks for using the Python Calculator, WaffleBell")


else: print("Enter one of the options above you silly!")