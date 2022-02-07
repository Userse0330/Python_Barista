#Import Modules
import time
import sys

#Variables
name = "Test."
username = input("What is your name? ")
menu = "Espresso", "Cappuccino", "Mocha",""
print(username,"What would you like to order? Take a look at our menu.", menu)
order = input()
#Price Variable
price = 60

#Main Script
quantity = input("How many would you like?\n")
total = price * int(quantity)
print("your total is", total)
time.sleep(3)
print("Preparing your", order)
time.sleep(10)
print("Here is your", quantity,order)
time.sleep(3)

thankyou = "Thank you for shopping at Testshop"
ewasdf = "#####################"
sadfasdf = "Made by sebastian"


time.sleep(3)

for char in thankyou:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

print(chr(27) + "[2J")

for char in ewasdf:
    time.sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()

print(chr(27) + "[2J")

for char in sadfasdf:
    time.sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()

print(chr(27) + "[2J")



#Made by Sebastian
