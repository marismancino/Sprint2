#Maris Mancino
#First, you go to play minigolf with your friends
#Afterwards, you enter a bakery looking to buy some pastries
#import time and time.sleep() are used to delay the next time of code; the user has time to read
#https://www.geeksforgeeks.org/python-time-module/

import time
# allows for the predefined function 'time.sleep()' to be used
def greeting():
# function definition
    print("Hello and welcome to the Putt Palace Mini Golf!")
    time.sleep(1.5)
    print("How many players are on your team?")
    time.sleep(1)

def main():
# function defintion
    greeting()
    players = int(input("number of players: "))
    print(players,", great! What are the names of your players?")
    for x in range(players):
# for is used as a loop with a definite set of outputs
# range() defines the amount of times the loop will run
        name = input("Player's name: ")
    print("Alright, here are your clubs and balls. There are", players, " of each.")
    time.sleep(1.5)

main()
# function call to main

print("Hello and welcome to the Maris' Munchies Bakery!")
time.sleep(2)
print("Our menu today features cake, cookies, and macaroons.")
time.sleep(1.5)
cake = "red velvet cakes"
cookies = "chocolate chip cookies"
macaroons1 = "strawberry macaroons"
print("How many of each would you like?")
time.sleep(2)
cake = int(input("number of " + cake + ": "))
# + concatenates two strings
cookies = input("number of " + cookies + ": ")
macaroons1 = input("number of " + macaroons1 + ": ")
print("I will package those right up for you.")
time.sleep(1.5)
num1 = int(cake)
num2 = int(cookies)
num3 = int(macaroons1)
cost1 = (num1 * 15.99)
# * multiplies the two values
cost2 = (num2 * 1.99)
cost3 = (num3 * 0.99)
print("Okay, your prices today break down like this:")
time.sleep(1.5)
print("The cakes cost $", format(cost1,'0.2f'), sep='')
time.sleep(0.5)
print("The cookies cost $", format(cost2,'0.2f'), sep='')
time.sleep(0.5)
print("The macaroons cost $", format(cost3,'0.2f'), sep='')
time.sleep(0.5)
total1 = (cost1 + cost2 + cost3)
# + adds the values
time.sleep(1)
print("Your total will be $", format(total1,'0.2f'), sep='')
total2 = (total1 - cost3)
# - removes the value
time.sleep(2)
print("I see, you don't want the macaroons anymore? ", end='')
print("Sure thing. Your new total is $", format(total2, '0.2f'), sep='')
time.sleep(3.5)
print("Can I offer you a different macaroon flavor? ", end='')
# end= ends the output with a space
print("We also have pistachio and vanilla.")
time.sleep(2)
macaroons2 = "pistachio macaroons"
macaroons3 = "vanilla macaroons"
macaroons2 = input("number of " + macaroons2 + ": ")
macaroons3 = input("number of " + macaroons3 + ": ")
num4 = int(macaroons2)
num5 = int(macaroons3)
cost4 = (num4 * 0.99)
cost5 = (num5 * 0.99)
total3 = (total2 + cost4 + cost5)

if total3 > 100:
# if stament allows for a conditonal output based on the value of an expression
# > greater than conditional operator
    total6 = (total3 * 0.85)
    print("It's your lucky day! ", end='')
    time.sleep(1)
    print("Since you are spending more than $100, we will give you 15% off your order.")
    time.sleep(2)
    print("Your final total will be $", format(total6, '0.2f'), sep='')
elif total3 <= 100 or total3 > 30:
# elif is a python keyword to test multiple options
# <= less than or equal to conditional operator
# or operator is a disjunction
    total5 = (total3 * 0.90)
    print("It's your lucky day! ", end='')
    time.sleep(1)
    print("Since you are spending between $30-$100, we will give you 10% off your order.")
    time.sleep(2)
    print("Your final total will be $", format(total5, '0.2f'), sep='')
elif total3 > 30:
    total4 = (total3 * 0.95)
    print("It's your lucky day! ", end='')
    time.sleep(1)
    print("Since you are spending more than $30, we will give you 5% off your order.")
    time.sleep(2)
    print("Your final total will be $", format(total4, '0.2f'), sep='')
else:
#else output if all other conditions fail
    print("Your final total will be $", format(total3,'0.2f'), sep='')

time.sleep(2)
print("Cash or card?")
time.sleep(1)
print("Alright, you're all set! Have a great day!")
time.sleep(1.5)

#extra operations
firstNumber = input("Enter a number: ")
secondNumber = input("Enter another number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
division = num1 / num2
# / division operator
power = num1 ** num2
# ** power operator
num1 *= num2
# *= power shortcut operator
floor = num1 // num2
# // floor division rounds to a whole number
modulus = num1 % num2
# % modulus operation returns the remainder
num1 += num2
# += addition shortcut operator
num1 -= num2
# -= subtraction shortcut operator
num1 == num2
# == equal to shortcut operator
num1 != num2
# != not equal to shortcut operator

print("First, divide the two numbers: ",division)
print("Then, put the first number to the power of the second number: ",power)
print("Next, floor divide the first number to the second number: ",floor)
print("Finally, modulus the first number to the second number: ",modulus)
print("Puppy" * 5)
# * in a string prints the word that many times

number = 11
while number <= 10:
    print(number)
    number = number + 1
# while loop allows for a block of code to be repeated multiple times

(age>=18) and (can_vote)
# and operator is a conjunction
not(credits>120)
# not operator is a negation