# your code goes here!
import time

def countdown(i):
    while i > 0:
        print(f"{i} SECOND(S)!")
        
        i -= 1
    else:
        print("HAPPY NEW YEAR!")

countdown(5)

def countdown_with_sleep(i):
    while i > 0:
        print(f"{i} SECOND(S)!")
        time.sleep(1)
        i -= 1
    else:
        print("HAPPY NEW YEAR!")

    pass

countdown_with_sleep(5)