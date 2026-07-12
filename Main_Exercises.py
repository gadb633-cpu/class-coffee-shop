# 1. Describe a Menu Item
class MenuItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def describe(self):
        print( f"Item: {self.name} | Price: ${self.price}")

Espresso = MenuItem("Espresso",3.5)
Espresso.describe() 

# 2. Customer Greeting
class Customer:
    def __init__(self,name,favorite_drink):
        self.name = name
        self.favorite_drink= favorite_drink
    def greet(self):
        print(f"Hi! I am {self.name} and I would like a {self.favorite_drink}.")

alice = Customer("alice","latte")
alice.greet()

# 3. Multiple Items with a Constructor
class MenuItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def describe(self):
        print(f"Item: {self.name} | Price: ${self.price}")

latte = MenuItem("latte",4.5)
Croissant = MenuItem("Croissant",2.0)
Cold_Brew = MenuItem("Cold Brew",5.0)
latte.describe()
Croissant.describe()
Cold_Brew.describe()

# 4. Can the Customer Afford It?
class Customer:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def can_afford(self,price):
        self.price = price
        return True if self.price<= self.balance else False
bob = Customer("bob",10.0)
print(bob.can_afford(8.0))
print(bob.can_afford(12.0))

    
        
        




