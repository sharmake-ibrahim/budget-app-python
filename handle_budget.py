"""
    Personal Budget Management App
    1: Budget
    2: Balance: 
    3: Expenses

    Budget & Balance
    1: ask user his budget amount & display it and Balance is equal to Budget Valaue.

    Expenses
    1: user enters expenses amount & extenses Title and display it both.
    2: display that expenses amount on expenses variable then balance is equal balance - expenses.

"""


def handle_your_budget():
    
        budget = float(input("Enter Budget Amount: "))
       
        balance = 0

        while True: 
            if budget > 0:
                budgetAmount = budget
                balance = budgetAmount
                break
            else:
                print("Please enter budget")

        print(budgetAmount)


        def  handleExpenses():
            expenseTitle = input("Enter expense title: ")
            expenseAmount = 0
            expenseValue =  float(input(f"Enter the cost of the {expenseTitle}: "))
            while True:
                if expenseValue > 0 :
                    expenseAmount = expenseValue
                    balance = budgetAmount - expenseValue
                    print(f"Your balance is {balance}")
                    break
                else:
                    expenseValue =  float(input(f"Oops!, Enter the cost of the {expenseTitle}: "))




        handleExpenses()

handle_your_budget()



count = 0 

while count < 5:
     handle_your_budget()
     count += 1