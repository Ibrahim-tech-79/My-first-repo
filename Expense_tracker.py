import json
import os


FILE_NAME = "expense.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_data(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ").title()

    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Please enter a valid amount.")

    expenses = load_data()

    new_expense = {
        "date": date,
        "category": category,
        "amount": amount
    }

    expenses.append(new_expense)
    save_data(expenses)

    print("\nExpense added successfully!\n")


def monthly_summary():
    month = input("Enter month (01-12): ")

    expenses = load_data()
    total = 0

    for expense in expenses:
        expense_month = expense["date"][5:7]

        if expense_month == month:
            total += expense["amount"]

    print(f"\nTotal spent in month {month}: ₹{total}\n")


def category_summary():
    expenses = load_data()

    totals = {}

    for expense in expenses:
        category = expense["category"]

        if category in totals:
            totals[category] += expense["amount"]
        else:
            totals[category] = expense["amount"]

    print("\nCategory-wise Summary")

    if not totals:
        print("No expenses found.")

    for category, amount in totals.items():
        print(f"{category}: ₹{amount}")

    print()


def main():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. Monthly Summary")
        print("3. Category-wise Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            monthly_summary()

        elif choice == "3":
            category_summary()

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice.\n")


main()