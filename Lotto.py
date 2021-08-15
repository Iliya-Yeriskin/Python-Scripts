from time import sleep
from random import randint

print("Hello, Welcome to our Lotto Game!\nEach Row in game costs 3 NIS")
user_money = int(input("Please enter your budget: "))
tries = user_money//3
print("You can play: "+str(tries)+" Rows")
# Generating the winning numbers #
Z = 0
X = 0
big_money = 0
prize_nums = []
p_count = 0
while p_count <= 5:
    Z = randint(1, 37)
    if Z not in prize_nums:
        prize_nums.append(Z)
        p_count = p_count+1
print("_______________________\nThe Winning numbers:\n"+str(prize_nums)+"\n________________________")
# Generating player numbers #
for i in range(tries):
    print("Row: "+str(i+1)+" Drum Roll...")
    sleep(2)
    my_nums = []
    nums_count = 0
    prize_count = 0
    while nums_count <= 5:
        X = randint(1, 37)
        if X not in my_nums:
            my_nums.append(X)
            nums_count = nums_count+1
        if X in prize_nums:
            prize_count = prize_count+1
    print("Your numbers are: "+str(my_nums))
# Calculating prize #
    print("Calculating your prize.....\n___________________________")
    if prize_count == 3:
        print("You won 10 NIS\n")
        big_money = big_money + 10
    elif prize_count == 4:
        print("You won 100 NIS\n")
        big_money = big_money + 100
    elif prize_count == 5:
        print("You won 5000 NIS\n")
        big_money = big_money + 5000
    elif prize_count == 6:
        print("You won 1,000,000 NIS\n")
        big_money = big_money + 1000000
    else:
        sleep(2)
        print("No Winnings, Try next time...\n")

print("###### You Won "+str(big_money)+" NIS ######")
input("To Exit Press Enter")