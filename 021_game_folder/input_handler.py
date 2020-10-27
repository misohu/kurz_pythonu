import sys 

def get_input():
    try:
        x = int(sys.stdin.readline())
    except ValueError as e:
        print("Please insert only numbers as position")
        return get_input()
    return x 