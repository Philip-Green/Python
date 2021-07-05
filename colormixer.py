# Philip Green
def main():
    p1= "red"
    p2="blue"
    p3="yellow"
    s1="purple"
    s2="orange"
    s3="green"

    user_input1= input("Enter a primary color(Red, Blue,or Yellow):")
    user_input2= input("Enter another primary(Red, Blue, or Yellow):")

    if user_input1.lower() == "red":
        if user_input2.lower() == "blue":
            print("Mixing", p1, "and", p2, "you get", s1)
        elif user_input2.lower() == "yellow":
            print("Mixing", p1, "and", p2, "you get", s2)
        elif user_input2== "red":
            print("Mixing", p1, "and", p1,"you get", p1)
        else:
            print("Invalid Input")

    elif user_input1.lower()== "blue":
        if user_input2.lower()== "red":
            print( "Mixing", p2,"and", p1, "you get", s1)
        elif user_input2.lower()== "yellow":
            print( "Mixing", p2, "and",p3, "you get", s3)
        elif user_input2.lower()== "blue":
            print( "Mixing", p2, "and", p2, "you get", p2)
        else:
            print("Invalid Input")

    elif user_input1.lower()== "yellow":
        if user_input2.lower()== "red":
            print("Mixing", p3, "and",p1, "you get", s2)
        elif user_input2.lower()== "yellow":
            print("Mixing", p3, "and",p3, "you get", p3)
        elif user_input2.lower()== "blue":
            print("Mixing", p3, "and",p2, "you get", s3)
        else:
            print("Invalid Input")
    else:
            print("Terminating")
            

main()
       

       
