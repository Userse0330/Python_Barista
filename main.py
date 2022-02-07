#Import Modules
import time
import sys

#Variables
name = "Test."

#Start Script
print(chr(27) + "[2J")
username = input("What is your name: ")
menu = "Espresso", "Cappuccino", "Mocha","Latte","Frappe"
print("What would you like to order",username,"?","Take a look at our menu:", menu)
order = input()
#Price Variable
price = 60

#Main Script
quantity = input("How many would you like:\n")
total = price * int(quantity)
print("your total is:", total)
time.sleep(3)
print(chr(27) + "[2J")
print("Preparing your", order)
time.sleep(10)
print(chr(27) + "[2J")
thankyou = "Thank you for shopping at Simple_Barista."
endmessage = "Made by se0330."

#End Script
time.sleep(3)
for char in thankyou:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

print(chr(27) + "[2J")
time.sleep(2)
time.sleep(3)
for char in endmessage:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

#Made by Sebastian
