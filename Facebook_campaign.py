print("Enter your Budget\n1 Day of FB costs 100$\n1 Day of Instagram costs 50$")
budget = int(input("What is your Budget? \n"))
facebook = int(input("Enter how long is your facebook campagin: \n"))*100
instagram = int(input("How long is your instgram compagin: \n"))*50
sum=facebook+instagram
print("total cost: " + str(sum) + " $")
print("cost in NIS: " + str((sum)*3.5) + " NIS" )
print("cost in NIS + tax: " + str((sum) * 1.17*3.5)+ " NIS + Tax")

if(sum <= budget):
    print("Successfull " + str(budget-sum) + " $")
else:
    print("unsuccessfull, you need to add " + str(sum-budget) + " $, to the budget")