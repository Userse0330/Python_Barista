#Import Modules
import time
import sys
import random

welcomemessage = "Welcome to Simple_Barista"

choices = "Hire lawyers against the company", "Say sorry and leave without getting a cup of coffee"

menu = "Espresso", "Cappuccino", "Mocha","Latte","Frappe"

name = "Test."
print(chr(27) + "[2J")

print("Anmeldelsene plassen har fått:")

print("Nydelig, koselig og fin plass å dra til etter en hard og lang arbeidsdag 5/5.")

print("Kjempe trang, gammel og skitten plass. Bestilte en kaffe som de sølte overalt og jeg måtte betale 20 kroner ekstra, anbefales ikke. 2/5")

print("Man kan ikke bestille mere en 10 kaffekopper før de søler overalt og du må betale 20 kroner ekstra! Ikke dra hit. 1/5")

print("Veldig koselig og trivelig sted du kan dra til når som helst :) 5/5")

print("God Cappuccino 4/5")

 

username = input("Hva er navnet ditt? ")
print("Hva vil du ha",username,"?","Ta en titt på menyen:", menu)
order = input()
price = 60

print(chr(27) + "[2J")
quantity = input("Hvor mange vil du ha?\n")
total = price * int(quantity)
print("Du bestilte:", quantity, order)
print("total sum:",total)
time.sleep(4)
print(chr(27) + "[2J")
print("Forbedrer din", order)
time.sleep(5)
print(chr(27) + "[2J")
print("done")
time.sleep(2)
print(chr(27) + "[2J")
choices = "Ansett advokater mot bedriften","Forlat butikken og miste",price
randomnumber = 5

if int(quantity) > 50:
  print("Å nei! Jeg sølte din kaffe. Her er dine valg:" ,choices)
  asdasdasdgsdf = input("Hva vil du gjøre? ")
else:
   print("Hade! Kom tilbake når du vil.")
   sys.exit("User done")



if asdasdasdgsdf=="Ansett advokater" or "Ansett Advokater" or "advokat" or "Advokat":
  value1 = random.randint(0,10)
  if value1== 4:
    print("Du tapte og må betale",price *2)
  if int(value1) > 4:
    print("Du vant og fikk tilbake",price)
elif asdasdasdgsdf=="Forlat" or "forlat":
  print("Du forlot stedet og mistet",price)

print("Hade, kom tilbake når du vil!")
time.sleep(5)
print(chr(27) + "[2J")
