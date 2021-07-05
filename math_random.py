#Philip Green
import random

MIN = 1
MAX = 50
def main():
#
    another_problem = True
    
# 
    while another_problem: 
        num1 = random.randint(MIN, MAX)
        num2 = random.randint(MIN, MAX)
        value = num1 + num2
        print('The problem is...\n',num1,"\n+",num2,"\n_____________")
        #print(random.randrange(1, 51))
        #print("+")
        #print(random.randrange(1, 51))
        User_input= int(input("What is the answer?:"))
        if User_input == value:
            print("You are correct!")
        else:
            print("You are wrong!")
        print("Answer is:", value)
# 
        response = input('Want another Problem (y = yes): ')
        if response == 'y' or response =='Y':
            another_problem = True
        else:
            another_problem = False
# 
main()
