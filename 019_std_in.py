import fileinput
import sys

# Citanie pomocou fileinput modulu v nekonecnom cykle
# Cyklus ukoncite klavesovou skratkou ctrl + c
for line in fileinput.input():
    print(line, end='')

# Citanie pomocou ss modulu jednorazovo 
def get_input():
    print("Please insert your number")
    x = int(sys.stdin.readline())
    return x 

# Citanie do vtedy kym nezadam 99
while True:
    number=get_input()
    print(f"Your number is: {number}")
    if number == 99:
        print("Number is 99 ending the loop")
        break 