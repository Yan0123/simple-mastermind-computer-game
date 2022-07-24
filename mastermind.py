#import random library
import random

# function for checking users input
def checking(list1,list2):
    # correct fruit in correct place
    # [Explaination] :
    # x as index of list
    # check whether the same index element of list1 and list2  are same
    # count = counting the quantity of element which is correct and also in same location
    count=0    # note: was put this counter under for loop, so that always got bug(infinity loop/ counter counld't work)
    for x in range(0,4):     
        if list1[x] == list2[x]:     
            count += 1    
            
        elif list1[x] != list2[x]:
            count= count + 0
    print()
    print('Correct fruits in the correct place: ', count)
    
    # correct fruit but wrong place   
    # [Explaination] :
    #  y as element of list 1, z as element of list2, let y (an element) compare with every element od list 2
    #  if y is match with z, then there has an element same with y in list 2 ---> the input of 'correct but may in wrong place'
    #  minus the quantity of input which is 'correct and in correct location' to get the quantity of input which correct but not in correct indec location
    counter = 0
    for y in list1:    
        for z in list2:    
            if y==z:    
                counter = counter + 1
    print()
    print('Correct fruits but in wrong place:', counter - count)
    

# use random to generate the answer list
fruit_list= ["apple","banana",'kiwi','lemon','peach','orange']
fruit = random.sample(fruit_list,4)

# Interface Design
print()
print()
print ('                                                                    WELCOME TO MASTER MIND                                                                 ')
print()
print ('-----------------------------------------------------------------------------------------------------------------------------------------------------------')
print()
print(' HOW TO PLAY ?                                                                                                                                                     ')
print(' Once you start the game, the system will choose four fruit name from the fruit list provided below.      ')
print(' Player need to guess what fruit the system chosen and enter the fruit name sequentially ')
print()
print(' ATTENTION ')
print(' - The game will keep running until you guess the name and sequence correctly')
print(' - Enter the fruits name with lower case letters')
print()
print()
print('FRUIT: apple, banana, kiwi, lemon, peach, orange')
print()
print()
print ('-------------------------------------------------------------------        GAME START      ----------------------------------------------------------------')
print()
print()
print()
# using while loop to run main part of game to get user guess time
guess_count=0
correct = 0
while correct < 1:
    print()
    print('-----------------------------------------------------------')
    print()
    # make users input as a list, simplify the program code
    usersguess=[]
    usersguess.append(str(input("Enter your first fruit name:")))
    usersguess.append(str(input("Enter your second fruit name:")))
    usersguess.append(str(input("Enter your third fruit name:")))
    usersguess.append(str(input("Enter your fourth fruit name :")))
    
    # use 'correct' as a button to stop program if user input are correct
    if usersguess == fruit :
        correct = correct + 1
        guess_count = guess_count + 1
        print()
        print('Congratulation ! you took only',guess_count, 'guess !')
    
    else:
        guess_count = guess_count + 1
        checking(usersguess,fruit)
        
    
    
    
    

#testing part

#comparison program
# correct fruits in the correct place: and correct fruit but in the wrong place:
#compare elements in usersguess and fruit list                 

##problem is in the count part, become infinity loop now, need to adjust it to normal, normal means while element in usersguess and fruit list are equal then plus 1        
    
