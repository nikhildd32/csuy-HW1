"""
Author: [Nikhil Diddee]
Assignment / Part: HW1 - Q1 (etc.)
Date due: September 21, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

dollars = int(input("Enter amount of dollars:"))  
cents = int(input("Enter amount of cents:"))
amount = dollars + cents/100

quarters = amount // 0.25
amount -= quarters * 0.25  
dimes = amount // 0.1
amount -= dimes * 0.1
nickels = amount // 0.05 
amount -= nickels * 0.05
pennies = int(amount*100)

print(dollars, "dollars and", cents, "cents are:" ,int(quarters), "quarters", int(dimes), "dimes,", int(nickels), "nickels and", pennies, "pennies")