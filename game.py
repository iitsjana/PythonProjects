#Jana Batiya
#A Number Guessing Game
print("~~~~~~~~~~~~~~~~")

PlayerName= input('Enter your name')
print("welcome to the Number Guessing game" + PlayerName+ "!! ")
print("Try and guess the number I have in mind if you can ;)")
import random

condition = True
while condition:
    UpperboundNum = input('But first, Enter a number for an upper bound: ')

    if UpperboundNum.isdigit():
        print ("Now, let's play!")
        UpperboundNum = int(UpperboundNum)
        condition = False
    else:
        print('Invalid input! Try Again!')
        break 

secretNum = random. randint(1,UpperboundNum)

guess = None
count = 1

while guess != secretNum:
    guess = input('Enter a number between 1 and ' + str(UpperboundNum) + ": ")
    if guess. isdigit () :
        guess = int(guess)
    if guess == secretNum:
        print("You got it!")
        break 
    if guess > secretNum:
        print("Decrease the number!")
    if guess < secretNum:
        print("Increase the number!")
    else:
        print('Please try again!')
        count+=1
        
    
print('It took you', count, 'guess/guesses!')
    


