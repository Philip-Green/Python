#Philip Green
def checkspeed(acceleration):
    if acceleration <= 70:
        print(acceleration, "mph is okay,")
    else:
        decrement = (acceleration - 70) // 5
        if decrement > 12:
            print ("# of points lost:", decrement, "license suspended.")
        else:
            print("current number of points lost:", decrement)
def main():
    acceleration= int(input("Enter speed in mph:"))
    print("Accelerating at:", acceleration,"mph")
    checkspeed(acceleration)
main()
    
    
