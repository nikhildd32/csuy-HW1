"""
Author: [Nikhil Diddee]
Assignment / Part: HW1 - Q1 (etc.)
Date due: September 21, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

quarters = int(input('Number of quarters: '))
dimes = int(input('Number of dimes: '))  
nickels = int(input('Number of nickels: '))
pennies = int(input('Number of pennies: '))

total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
dollars = int(total)
cents = round(total * 100) % 100

print('The total is', dollars, 'dollar(s) and', cents, 'cent(s)')