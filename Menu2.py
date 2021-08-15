'''
Menu:
1.Printing 100 Numbers
2.Check Fibonacci
3.randint numbers until we get 12 or count to 10 times
'''
from time import sleep
from random import randint
while True:
    choise = input("Menu:\n1.Printing 100 Numbers\n2.Check Fibonacci\n3.randint numbers until we get 12 or count "
                       "to 10 times\nPlease enter your choise: ")
    if choise == "1":
        print("Choose 1")
        counter = 100
        for i in range(1, 101):
            print(i, '.', randint(0, 100))
            counter = counter - 1
        print("------------------------\n")
        sleep(1)
    elif choise == "2":
        print("Choose 2")
        print("Please Enter a list of numbers: ")
        counter = 7
        fibo2 = []
        while counter > 0:
            fibo2.append(int(input("Enter a number: ")))
            counter = counter - 1
            print(fibo2)
        boolean = "True"
        for i in range(2, len(fibo2)):
            print(fibo2[i])
            print(fibo2[i - 1])
            print(fibo2[i - 2], "\n")
            if fibo2[i - 2] + fibo2[i - 1] == fibo2[i]:
                print(fibo2)
                continue
            else:
                boolean = "False"
                break
        if boolean == "True":
            print("--------------\nIts Fibonacci series\n--------------\n")
        else:
            print("--------------\nIts not Fibonacci series\n--------------\n")
        sleep(1)
    elif choise == "3":
        print("Choose 3")
        counter = 1
        num = 0
        while counter < 11 and num != 12:
            print("Counter:" + str(counter) +"   "+"Number: "+str(num))
            counter = counter+1
            num = (randint(1, 12))
        if num == 12:
            print("Your num is: "+str(num))
    else:
        print("Enter ONLY 1-3!!")
    exit = input("Do you want to exit? (y/n): ")
    if exit != "y" and exit != "yes":
        print("\n-------------------\n")
        continue
    else:
        break
print("-------------------\nThank you Byebye.....\n-------------------")