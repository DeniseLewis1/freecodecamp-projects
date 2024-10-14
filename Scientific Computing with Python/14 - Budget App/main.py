class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        output = self.name.center(30, "*") + "\n"

        for item in self.ledger:
            output += "{:<23}".format(item["description"])[:23] + "{:>7.2f}".format(item["amount"]) + "\n"
        output += "Total: {:.2f}".format(self.get_balance())
        return output
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({"amount": amount * -1, "description": description})
            return True
    
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, other):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, f"Transfer to {other.name}")
            other.deposit(amount, f"Transfer from {self.name}")
            return True

    def check_funds(self, amount):
            if amount > self.get_balance():
                return False
            else:
                return True

def create_spend_chart(categories):
    spent = {}

    for category in categories:
        category_spend = 0

        for item in category.ledger:
            if item["amount"] < 0:
                category_spend += abs(item["amount"])
        spent[category.name] = round(category_spend, 2)

    total_spent = sum(spent.values())

    spent_percentage = {}

    for category in spent:
        spent_percentage[category] = int(round(spent[category] / total_spent, 2) * 100)

    output = "Percentage spent by category\n"
    
    for i in range(100, -10, -10):
        output += str(i).rjust(3) + "|"

        for percent in spent_percentage.values():
            if percent >= i:
                output += " o "
            else:
                output += "   "
        output += " \n"

    output += " " * 4 + "-" * (3 * len(categories)) + "-\n"

    category_names = list(spent.keys())
    max_length = max([len(i) for i in category_names])
    
    for i in range(max_length):
        output += " " * 5

        for name in category_names:
            if len(name) > i:
                output += name[i] + "  "
            else:
                output += "   "
        output += "\n"
  
    return output.rstrip("\n")


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
clothing.withdraw(10, 'clothes')
print(clothing)
print(create_spend_chart([food, clothing]))