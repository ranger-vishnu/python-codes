def add_expense(expenses, init_blns):
    category = input("Enter the Expense category: ")
    if category in expenses:
        amount = int(input("Enter the amount: "))
        already_spent = expenses[category]
        balance = init_blns - (already_spent + amount)
        if balance < 0:
            print("Recharge your Wallet:")
        else:
            init_blns -= amount
            expenses[category] += amount
    else:
        amount = int(input("Enter the amount: "))
        balance = init_blns - amount
        if balance < 0:
            print(f"Recharge your Wallet: your Current Wallet amount is {init_blns}")
        else:
            init_blns -= amount
            expenses[category] = amount
    print(f"Your current Balance after spending: {init_blns}")
    return init_blns

def add_balance(init_blns):
    amount = int(input("Enter the amount you wish to add to wallet: "))
    init_blns += amount
    print(f"Your current wallet Balance is {init_blns}")
    return init_blns


def view_expenses(expenses):
    print("Your Expenses are:")
    print(expenses)

# def main():
#     expenses = {}
#     init_blns = int(input("Enter the amount you can afford to spend: "))
#     while True:
#         print("\n1. Add Expenses")
#         print("2. Add Balance")
#         print("3. View Expenses")
#         print("4. Exit\n")
        
#         opt = int(input("Enter the option: "))
        
#         if opt == 1:
#             init_blns = add_expense(expenses, init_blns)
#         elif opt == 2:
#             init_blns = add_balance(init_blns)
#         elif opt == 3:
#             view_expenses(expenses)
#         elif opt == 4:
#             fileWrite()
#             break
#         else:
#             print("Invalid option")

# if __name__ == "__main__":
#     main()
