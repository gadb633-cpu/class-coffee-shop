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

# 5. Track Item Stock
class MenuItem:
    def __init__(self,name, price, in_stock):
        self.name = name
        self.price =price
        self.in_stock = in_stock
    def sell(self):
        self.in_stock=False
    def restock(self):
        self.in_stock=True
    def status(self):
        print(f"{self.name} is in stock.") if self.in_stock== True else print(f"{self.name} is sold out.")

muffin = MenuItem("Muffin", 2.5, True)
muffin.status()
muffin.sell()
muffin.status()
muffin.restock()
muffin.status()

# 6. Coffee Shop Open and Close
class CoffeeShop:
    def __init__(self,name, city, capacity):
        self.name = name
        self.city = city
        self.capacity = capacity

    def open_shop(self):
        print(f"{self.name} is now open in {self.city}! Capacity: {self.capacity} seats.")
    def close_shop(self):
        print(f"{self.name} is now closed. See you tomorrow!")
Brew_House = CoffeeShop("Brew House", "Tel Aviv", 40)
Brew_House.open_shop()
Brew_House.close_shop()

# 7. Count Item Orders
class MenuItem:
    def __init__(self,name,price):
        self.order_count = 0
        self.name =name
        self.price = price

    def order(self):
        self.order_count += 1
        print(f"{self.name} ordered. Total orders: {self.order_count}")

cappuccino = MenuItem("cappuccino", 4.0)
cappuccino.order()
cappuccino.order()
cappuccino.order()




        






        
        




