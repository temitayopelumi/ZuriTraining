class Budget():
    db={}
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self, amount, bal):
        bal += amount
        return bal

    def withdraw(self, amount, bal):
        bal -= amount
        return bal

    def balance(self, db):
        for categ, bal in db.items():
            print(categ, bal)

    def transfer(self,db, option1, amount, option2):
        value1 = db[option1]
        valuue2 = db[option2]

        db[option1] = int(value1) - amount
        db[option2] = int(valuue2) + amount
        print('done')
        return db

budget1 = Budget("Food", 20000)
budget2=Budget('Clothe', 5000)

budget2.transfer('Food', 1000,  'Clothe')

print(budget2.category)