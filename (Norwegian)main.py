#Import Modules
import time
import sys
import random

welcomemessage = "Welcome to Simple_Barista"

choices = "Hire lawyers against the company", "Say sorry and leave without getting a cup of coffee"

menu = "Espresso", "Cappuccino", "Mocha","Latte","Frappe"

name = "Test."
print(chr(27) + "[2J")
welcomemessage = "Velkommen til Simple_Barista"
print(welcomemessage)
username = input("Hva er navnet ditt? ")
print("Hva vil du bestille",username,"?","Her er menyen våres:", menu)
order = input()
price = 60
sure = input("Er du sikker på at du vil fortsette? ")
if sure=="nei" or "Nei" or "stop" or "Stop":
 sys.exit("User Stopped.")

print(chr(27) + "[2J")
quantity = input("Hvor mange\n",order,"vil du ha?")
total = price * int(quantity)
print("Du bestilte:", quantity, order)
print("totalen blir:",total)
time.sleep(4)
print(chr(27) + "[2J")
print("Forbedrer din", order)
time.sleep(5)
print(chr(27) + "[2J")
print("Ferdig")
time.sleep(2)
print(chr(27) + "[2J")
choices = "Ansette advokater mot selskapet","Forlat stedet men du mister",int(total) * 2
randomnumber = 5

if int(quantity) > 50:
  print("Å nei! Jeg sølte din kaffe. Her er valgene dine:" ,choices)
  lawyerinput = input("Hva velger du å gjøre? ")
else:
   print("Hade! Kom tilbake senere.")
   sys.exit("User done")



if lawyerinput=="Ansett advokater" or "ansett advokater" or "advokat" or "Advokat" or "Advokater" or "advokater" or "ansett advokat" or "Ansett advokat" or "Ansett Advokat":
  value1 = random.randint(0,10)
  if value1 < 4:
    print("Du tapte og mistet",total *2)
  if int(value1) > 4:
    print("Du forlot stedet og fikk",total,"tilbake.")
elif lawyerinput=="Leave" or "leave":
  print("Du forlot stedet og mistet",price)


time.sleep(5)
print(chr(27) + "[2J")
