#Philip Green
import random
#import randit 
def main():
    again= 'y'

    while again== 'y' or again== 'y':
        MAX= 6
        MIN= 1
        print('Rolling the dice...')
        print('Their values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        again= input('Roll them again( y = yes:')

main()
