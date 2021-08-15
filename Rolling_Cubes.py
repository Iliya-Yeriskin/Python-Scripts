'''
Cube project:
receive an input of player money
every game costs 3₪
every round we will roll 2 cubes,
1.if cubes are the same player wins 100₪
2.if the cubes are the same and both are "6" player wins 1000₪
3.if the cubes different but cube 2 = 2 player wins 40₪
4.if the cubes different but cube 1 = 1 player wins 20₪
in the end we'll print how much money the player won.
'''
from random import randint
from time import sleep
print("Welcome to the Rolling Cube Game\n--------------------------------\nEach round costs 3₪\n")
money = input("How much money do you have?: \n")
start_money = money
turns = int(money)//3
change = int(money) % 3
print("Your Change is: "+str(change)+"₪")
print("Prepare to play: "+str(turns)+" Rounds\n-----------------------")
money = int(turns)*3
cube1 = 0
cube2 = 0
for i in range(turns):
    start_money = int(int(start_money)-3)
    money = int(int(money)-3)
    print("Round: "+str(i+1)+" Rolling...")
    sleep(2)
    cube1 = randint(1, 6)
    cube2 = randint(1, 6)
    if cube1 == cube2 & cube1 == 6:
        print("You Rolled ("+str(cube1)+","+str(cube2)+") And Won 1000₪!!\n-----------------------")
        money = money+1000
    elif cube1 == cube2:
        if cube1 == 1:
            print("You Rolled ("+str(cube1)+","+str(cube2)+") And Won 120₪\n-----------------------")
            money = money+120
        elif cube2 == 2:
            print("You Rolled ("+str(cube1)+","+str(cube2)+") And Won 140₪\n-----------------------")
            money = money+140
        else:
            print("You Rolled ("+str(cube1)+","+str(cube2)+") And Won 100₪\n-----------------------")
            money = money+100
    elif cube1 == 1:
        if cube2 == 2:
            print("You Rolled ("+str(cube1)+","+str(cube2)+") And Won 60₪\n-----------------------")
            money = money+60
        else:
            print("You Rolled ("+str(cube1)+","+str(cube2)+") And Won 20₪\n-----------------------")
            money = money+20
    elif cube2 == 2:
        print("You Rolled (" + str(cube1) + "," + str(cube2) + ") And Won 40₪\n-----------------------")
        money = money+40
    else:
        print("You Rolled ("+str(cube1)+","+str(cube2)+") Sorry you didn't win\n-----------------------")
print("Calculating your Prize....\n")
sleep(3)
print("Your Total winning are: ["+str(money)+"₪]\nNow you have: ["+str(int(start_money)+int(money))+"₪]" +
      "\nHope to see you again :-)")
