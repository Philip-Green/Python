#Philip Green
import random

HEADS=1
TAILS=2
TOSSES=10

def main():
    for t in range(TOSSES):
        num= random.randint(HEADS, TAILS)
        if num== HEADS:
            print("Heads")
        else:
            print("Tails")
main()
