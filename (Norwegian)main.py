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
username = input("Hva er navnet ditt? ")
print("Hva vil du bestille",username,"?","her er menyen:", menu)
order = input()
price = 60
sure = input("Er du sikker på at du vil fortsette? ")
if sure=="Nei":
 sys.exit("User Stopped.")

print(chr(27) + "[2J")
quantity = input("Hvor mange vil du ha?\n")
total = price * int(quantity)
print("Du bestilte:", quantity, order)
print("Totalen blir:",total)
time.sleep(4)
print(chr(27) + "[2J")
print("Forbedrer din", order)
time.sleep(5)
print(chr(27) + "[2J")
print("Ferdig")
time.sleep(2)
print(chr(27) + "[2J")
choices = "Ansett Advokater mot stedet","Forlat stedet men du msiter",int(total) * 2
randomnumber = 5

if int(quantity) > 50:
  print("Å nei! Jeg sølte din kaffe. Her er dine valg:" ,choices)
  lawyerinput = input("Hva velger du å gjøre? ")
else:
   print("Hade! Kom tilbake senere.")
   sys.exit("User done")



if lawyerinput=="Advokat" or "advokat" or "ansett advokat" or "Ansett Advokat" or "Ansett Advokat" or "Advokater" or "advokater" or "ansett advokater":
  value1 = random.randint(0,10)
  if value1 < 4:
    print("Du tapte og mistet",total *2)
  if int(value1) > 4:
    print("Du forlot steted og du fikk",total,"tilbake.")
elif lawyerinput=="forlat" or "Forlat":
  print("Du forlot stedet og mistet",total * 2)


time.sleep(5)
print(chr(27) + "[2J")
