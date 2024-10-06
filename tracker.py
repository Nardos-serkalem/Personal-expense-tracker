import csv
from datetime import datetime

FILE_NAME = 'expenses.csv'

def load_expenses():
    expenses = []
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append({
                    'date': row[0],
                    'category': row[1],
                    'description': row[2],
                    'amount': float(row[3])
                })
    except FileNotFoundError:
        pass
    return expenses

def save_expenses(expenses):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for expense in expenses:
            writer.writerow([expense['date'], expense['category'], expense['description'], expense['amount']])

def add_expense(expenses):
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Entertainment, transporation, personal care, housing,  Education and Learning): ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))
    expenses.append({
        'date': date,
        'category': category,
        'description': description,
        'amount': amount
    })
    
    save_expenses(expenses)
    print("Expense added!")

def view_expenses(expenses):
    print("\nAll Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['date']} - {expense['category']}: {expense['description']} - ${expense['amount']}")

def edit_expense(expenses):
    view_expenses(expenses)
    index = int(input("Enter the index of the expense to edit: ")) - 1
    if 0 <= index < len(expenses):
        expenses[index]['date'] = input(f"Enter the new date (YYYY-MM-DD) [{expenses[index]['date']}]: ") or expenses[index]['date']
        expenses[index]['category'] = input(f"Enter the new category [{expenses[index]['category']}]: ") or expenses[index]['category']
        expenses[index]['description'] = input(f"Enter the new description [{expenses[index]['description']}]: ") or expenses[index]['description']
        expenses[index]['amount'] = float(input(f"Enter the new amount [{expenses[index]['amount']}]: ") or expenses[index]['amount'])
        save_expenses(expenses)
        print("Expense updated!")
    else:
        print("Invalid index")

def delete_expense(expenses):
    view_expenses(expenses)
    index = int(input("Enter the index of the expense to delete: ")) - 1
    if 0 <= index < len(expenses):
        deleted = expenses.pop(index)
        save_expenses(expenses)
        print(f"Deleted: {deleted['description']} - ${deleted['amount']}")
    else:
        print("Invalid index")

def search_expenses(expenses):
    keyword = input("Enter a keyword to search (in description or category): ").lower()
    results = [expense for expense in expenses if keyword in expense['description'].lower() or keyword in expense['category'].lower()]
    
    if results:
        print("\nSearch Results:")
        for expense in results:
            print(f"{expense['date']} - {expense['category']}: {expense['description']} - ${expense['amount']}")
    else:
        print("No matching expenses found.")

def filter_expenses_by_date(expenses):
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    filtered = [expense for expense in expenses if start_date <= expense['date'] <= end_date]
    
    if filtered:
        print(f"\nExpenses from {start_date} to {end_date}:")
        for expense in filtered:
            print(f"{expense['date']} - {expense['category']}: {expense['description']} - ${expense['amount']}")
    else:
        print("No expenses found for the given date range.")

def generate_summary_report(expenses):
    total_expense = sum(expense['amount'] for expense in expenses)
    avg_expense = total_expense / len(expenses) if expenses else 0
    category_totals = {}
    
    for expense in expenses:
        category_totals[expense['category']] = category_totals.get(expense['category'], 0) + expense['amount']
    
    print("\nSummary Report:")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Average Expense: ${avg_expense:.2f}")
    print("\nExpenses by Category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

def set_budget_alert(expenses):
    budget_limit = float(input("Set your monthly budget limit: "))
    total_expense = sum(expense['amount'] for expense in expenses)
    
    if total_expense > budget_limit:
        print(f"Warning: You have exceeded your budget by ${total_expense - budget_limit:.2f}!")
    else:
        print(f"You are within budget. You have ${budget_limit - total_expense:.2f} remaining.")

def main():
    expenses = load_expenses()
    while True:
        print("\nOptions: 1. Add Expense  2. View Expenses  3. Edit Expense  4. Delete Expense  5. Search Expenses  6. Filter by Date  7. Generate Summary Report  8. Set Budget Alert  9. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            edit_expense(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            search_expenses(expenses)
        elif choice == "6":
            filter_expenses_by_date(expenses)
        elif choice == "7":
            generate_summary_report(expenses)
        elif choice == "8":
            set_budget_alert(expenses)
        elif choice == "9":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
