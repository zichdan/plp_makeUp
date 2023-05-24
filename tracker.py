import json

# Initialize variables

income = 0.0
expenses = []
savings  = 0.0

# Load transaction data from file

def load_data():
    global income, expenses, savings    # global function
    try:
        with open('transactions.json', 'r') as file:
            data = json.load(file)
            income = data.get('income', 0.0)
            expenses = data.get('expenses', [])
            savings = data.get('savings', 0.0)
    except FileNotFoundError:  
        pass
    

# Save Transaction data to file
def save_data():
    data = {
        'income': income,
        'expenses': expenses,
        'savings': savings
    }
    with open('transactions.json', "w") as file:
        json.dump(data, file) 
        
    
# Add that income
def add_income():
    global income
    amount = float(input("Enter Income Amount"))
    income += amount
    print(f"income of {amount} added successfully!!!!")
    
# Add the expenses
def add_expense():
    global expenses
    description = input("Enter Expenses description")
    amount = float(input("Enter Expenses amount"))
    category = input("Enter Expenses category")
    expense = {
        'description': description,
        'amount': amount,
        'category': category
    }    
    expenses.append(expense)  
    print("Expenses added successfully!!!!")
    
# calculate Savings
def calculate_savings():
    global  savings
    savings = income - sum(expense['amount'] for expense in expenses)
    print(f'Total savings: {savings}')
    
 
#   
def generate_expense_report_by_category():
    category = input("Enter your")   
    total_amount = sum(expense["amount"] for expense in expenses if expense["category"] == category)
    print(f'Total for {category} is: {total_amount}')
    
    
def main():
    load_data()
    
    while True:
        print('====== Welcome Personal Finance Tracker =====')
        print("1. Add Income ") 
        print("2. Add Expense") 
        print("3. Calculate savings") 
        print("4. Generate Report") 
        print("5. Exist") 
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            calculate_savings()
        elif choice == '4':
            generate_expense_report_by_category()
        elif choice == '5':
            save_data()
            print("Thank You for using PFT but you need to save more")
            break
        else:
            (print("Invalid choice, Please call again or try Again"))
            
if __name__ == "main":
    main()



    
