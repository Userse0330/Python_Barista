#Import Modules
import time
import sys

name = "Test."
print(chr(27) + "[2J")
username = input("What is your name: ")
menu = "Espresso", "Cappuccino", "Mocha","Latte","Frappe"
print("What would you like to order",username,"?","Take a look at our menu:", menu)
order = input()
price = 60
quantity = input("How many would you like:\n")
total = price * int(quantity)
print("your total is:", total)
time.sleep(3)
print(chr(27) + "[2J")
print("Preparing your", order)
time.sleep(10)
print(chr(27) + "[2J")
thankyou = "Thank you for shopping at Simple_Barista."
time.sleep(3)
for char in thankyou:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
print(chr(27) + "[2J")
#Made by sebastian
























#MIT License

#Copyright (c) 2022 SE0330

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom #the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
