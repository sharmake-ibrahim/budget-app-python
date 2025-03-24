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
        budgetDetials = {
             "Budget": "",
             "Balance": "",
             "Expenses":0,
             "Expenses Title": "",
             "Spent": ""
        }
        budget = float(input("Enter Budget Amount: "))
       
        balance = 0

        while True: 
            if budget > 0:
                budgetAmount = budget
                balance = budgetAmount
                budgetDetials["Budget"] = budgetAmount
              
                break
            else:
                print("Please enter budget")

        


        def  handleExpenses():
            expenseTitle = input("Enter expense title: ")
            budgetDetials["Expenses Title"] = expenseTitle
            expenseAmount = 0
            expenseValue =  float(input(f"Enter the cost of the {expenseTitle}: "))
            while True:
                if expenseValue > 0 :
                    expenseAmount = expenseValue
                    balance = budgetAmount - expenseAmount
                    budgetDetials["Balance"] = balance
                    budgetDetials["Spent"] = expenseAmount


                    # print(f"Your balance is {balance}")
                    # print(f"Detials about your Budget: {budgetDetials}")
                    break
                else:
                    expenseValue =  float(input(f"Oops!, Enter the cost of the {expenseTitle}: "))




        handleExpenses()
        print(f"Your Bubget is {budgetDetials['Budget']}")
        print(f"Your Balance is {budgetDetials['Balance']}")
        print(f"Your Expenses Title is {budgetDetials['Expenses Title']}")
        print(f"Your Expenses Cost is {budgetDetials['Spent']}")
        print(f"Your Spent {budgetDetials['Spent']}")

        

handle_your_budget()



count = 0 

while count < 1:
     handle_your_budget()
     count += 1
