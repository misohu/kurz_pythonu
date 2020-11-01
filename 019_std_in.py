import fileinput
import sys

# Citanie pomocou fileinput modulu v nekonecnom cykle
# Cyklus ukoncite klavesovou skratkou ctrl + c
for line in fileinput.input():
    print(line, end='')

# Citanie pomocou ss modulu jednorazovo 
def get_input():
    print("Zadaj retazec")
    input_string = sys.stdin.readline()
    return int(input_string)

while True:
    number= get_input()
    print("The number is", number)
    if number == 99:
        break