class Category:
    def __init__(self, cat):
        self.cat = cat
        self.ledger = []

    def deposit(self, amount, descr=''):
        # append an object to the ledger list
        self.ledger.append({'amount': amount, 'description': descr})  # append the object to the ledger list

    def withdraw(self, amount, descr=''):
        # negative amount, add object to the ledger (True) if the fund is sufficient, else False
        if self.check_funds(amount):
            self.ledger.append({'amount': -(amount), 'description': descr})
            return True
        else:
            return False

    def get_balance(self):
        # return current balance based on occured deposits and withdrawals
        fund = 0
        for i in range(len(self.ledger)):
            fund += self.ledger[i]['amount']
        return fund

    def transfer(self, amount, other_cat):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_cat.cat}')  # withdraw from this budget
            other_cat.deposit(amount, f'Transfer from {self.cat}')  # deposit to another budget
            return True
        else:
            return False

    def check_funds(self, amount):
        # return False if the amount > balance and True o.t.w
        return True if amount <= self.get_balance() else False
        # if amount <= self.get_balance():
        #     return True
        # else:
        #     return False

    def __str__(self):
        output = self.cat.center(30, '*') + '\n'
        for i in range(len(self.ledger)):
            output += f"{self.ledger[i]['description'][:23].ljust(23)}\
{format(self.ledger[i]['amount'], '.2f').rjust(7)}\n"

        output += f"Total: {format(self.get_balance(), '.2f')}"
        return output


def create_spend_chart(categories):
    # return a bar chart, calculating the percentage spent in each cat,
    # only with withdrawals, not with deposits
    title = 'Percentage spent by category\n'
    cat_names = []
    spent = []
    spent_percent = []

    for item in categories:
        tot = 0
        for i in item.ledger:
            if i['amount'] < 0:
                tot -= i['amount']
        spent.append(round(tot, 2))
        cat_names.append(item.cat)

    for amount in spent:
        spent_percent.append(round(amount / sum(spent), 2) * 100)

    labels = range(100, -10, -10)
    graph = title

    for label in labels:
        graph += str(label).rjust(3) + '| '
        for percent in spent_percent:
            if percent >= label:
                graph += 'o  '
            else:
                graph += '   '
        graph += '\n'

    graph += '    ----' + ('---' * (len(cat_names) - 1)) + '\n     '

    longest_name = max(len(name) for name in cat_names)

    for i in range(longest_name):  # print horizontally
        for name in cat_names:
            if len(name) > i:
                graph += name[i] + '  '
            else:
                graph += '   '

        if i < longest_name - 1:
            graph += '\n     '

    return graph

# ## Test Case:
# 
# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)
# 
# print(food)
# print(clothing)
# 
# print(create_spend_chart([food, clothing, auto]))
# entertainment = Category('Entertainment')
# business = Category('Business')
# food.deposit(900, 'deposit')
# entertainment.deposit(900, 'deposit')
# food.withdraw(105.55)
# entertainment.withdraw(33.40)
# business.withdraw(10.99)
# res = create_spend_chart([business, food, entertainment])
# print(res)
