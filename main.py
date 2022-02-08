#Import Modules
import time
import sys
import random

welcomemessage = "Welcome to Simple_Barista"

choices = "Hire lawyers against the company", "Say sorry and leave without getting a cup of coffee"

menu = "Espresso", "Cappuccino", "Mocha","Latte","Frappe"

name = "Test."
print(chr(27) + "[2J")
welcomemessage = "Welcome to Simple_Barista"
print(welcomemessage)
username = input("What is your name? ")
print("What would you like to order",username,"?","Take a look at our menu:", menu)
order = input()
price = 60
sure = input("Are you sure you want to continue? ")
if sure=="No":
 sys.exit("User Stopped.")

print(chr(27) + "[2J")
quantity = input("How many would you like?\n")
total = price * int(quantity)
print("You ordered:", quantity, order)
print("your total is:",total)
time.sleep(4)
print(chr(27) + "[2J")
print("Preparing your", order)
time.sleep(5)
print(chr(27) + "[2J")
print("done")
time.sleep(2)
print(chr(27) + "[2J")
choices = "Hire lawyers against the company","Leave the shop without any coffe altough you will loose",price
randomnumber = 5

if int(quantity) > 50:
  print("Oh no! I spilled your coffe. Here are your choices:" ,choices)
  asdasdasdgsdf = input("What do you choose to do? ")
else:
   print("Goodbye! Come back later.")
   sys.exit("User done")



if asdasdasdgsdf=="Hire lawyers" or "Hire Lawyers" or "hire lawyers" or "Hire Lawyers":
  value1 = random.randint(0,10)
  if value1== 4:
    print("You lost the case and need to pay",price *2)
  if int(value1) > 4:
    print("You won the case and you got the",price,"back.")
elif asdasdasdgsdf=="Leave" or "leave":
  print("You left the coffee shop and lost",price)

print("Goodbye! Come back later.")
time.sleep(5)
print(chr(27) + "[2J")
