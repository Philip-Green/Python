#Philip Green
import random

HEADS=1
TAILS=2
TOSSES=10

def main():
    heads=0
    tails=0
    for t in range(TOSSES):
        num= random.randint(HEADS, TAILS)
        if num== HEADS:
            print("Heads")
            heads = heads +1
        else:
            print("Tails")
            tails= tails +1
    print(heads,"Heads and", tails, "tails")
main()
