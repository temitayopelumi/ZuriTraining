class Budget:
    bal = 0

    def __init__(self, category):
        self.category = category

    def deposit(self, amount):
        self.bal += amount
        return self.bal

    def withdraw(self, amount):
        self.bal -= amount
        return self.bal

    def balance(self):
        return self.bal


def transfer(cat1, amount, cat2):
    cat1.withdraw (amount)
    cat2.deposit (amount)
    print('The current balance of', cat1.category, 'is', cat1.balance(), 'and The new balance for', cat2.category,  'is',  cat2.balance())


budget1 = Budget ("Food")
budget2 = Budget ('Clothe')
budget2.deposit (1000)
budget1.deposit(3000)


transfer (budget1, 500, budget2)
