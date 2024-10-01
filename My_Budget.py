import json
import os
import matplotlib.pyplot as plt

def load_data(filename):
    # Load data from file if it exists
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {"income": [], "expenses": []}

def save_data(filename, data):
    # Save data to file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def add_income(data):
    source = input("Enter income source (e.g., Salary, Freelancing): ")
    amount = float(input("Enter amount: "))
    data['income'].append({"source": source, "amount": amount})

def add_expense(data):
    category = input("Enter expense category (e.g., Rent, Food, Utilities): ")
    amount = float(input("Enter amount: "))
    data['expenses'].append({"category": category, "amount": amount})

def view_summary(data):
    total_income = sum(item['amount'] for item in data['income'])
    total_expenses = sum(item['amount'] for item in data['expenses'])
    savings = total_income - total_expenses

    print("\n--- Financial Summary ---")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Savings: ${savings}\n")

def view_category_expenses(data):
    print("\n--- Expenses by Category ---")
    categories = {}
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    for category, amount in categories.items():
        print(f"{category}: ${amount}")

    return categories

def plot_expenses(categories):
    # Plot expenses as a pie chart
    labels = categories.keys()
    sizes = categories.values()
    
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Expenses Distribution")
    plt.show()

def main():
    filename = "budget_data.json"
    data = load_data(filename)

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View Expenses by Category")
        print("5. Visualize Expenses (Pie Chart)")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            view_summary(data)
        elif choice == '4':
            categories = view_category_expenses(data)
        elif choice == '5':
            categories = view_category_expenses(data)
            plot_expenses(categories)
        elif choice == '6':
            save_data(filename, data)
            print("Data saved. Exiting.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
