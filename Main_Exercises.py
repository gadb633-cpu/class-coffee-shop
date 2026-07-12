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

# 8. Print an Order
class Order:
    def __init__(self,customer_name, items):
        self.customer_name = customer_name
        self.items = items
    def item_count(self):
        return len(self.items)
    def print_order(self):
        print(f"Order for: {self.customer_name} ,Items: {self.item_count()}")
        for self.item in self.items:
            print(f"-{self.item}")
dana = Order("Dana", ["Latte", "Croissant", "OJ"])
dana.print_order() 

# 9. Barista Shift Tracker
class Barista:
    def __init__(self,name, specialty):
        self.drinks_made = 0
        self.name = name
        self.specialty = specialty
    def make_drink(self,drink_name):
        self.drinks_made+=1
        print(f"{self.name} made a {drink_name}")
    def is_specialty(self,drink_name):
        return True if drink_name ==self.specialty else False
    def shift_summary(self):
        print(f"{self.name} made {self.drinks_made} drinks today.")
yossi = Barista("Yossi", "Espresso")
yossi.make_drink("Espresso")
yossi.make_drink("latte")
yossi.make_drink("cappuccino")
yossi.make_drink("coffee")
print(yossi.is_specialty("Espresso"))
yossi.shift_summary()

# 10. Receipt with Tax
class Receipt:
    def __init__(self,tax_rate):
        self.items = []
        self.tax_rate = tax_rate
    def add_item(self,name, price):
        
        self.items.append((name,price))
    def subtotal(self):
        self.sum = 0 
        for self.item in self.items:
            self.sum += self.item[1]
        return self.sum

    def tax_amount(self):
        return self.subtotal() *self.tax_rate
    def total(self):
        return self.subtotal() + self.tax_amount()
    def print_receipt(self):
        for self.item in self.items:
            print(f"-{self.item[0]}:,{self.item[1]}")
        print(f"Subtotal: ${self.subtotal()}")
        print(f"Tax (17%): ${self.tax_amount()}")
        print(f"Total: ${self.total()}")
receipt = Receipt(0.17)
receipt.add_item("Latte", 4.5)
receipt.add_item("Croissant", 2.0)
receipt.add_item("Water", 1.5)
receipt.print_receipt()

# Extra Exercises
# Extra 1. Category Filtering
class MenuItem:
    def __init__(self,name, price, category):
        self.name = name
        self.price =price
        self.category= category
    def is_drink(self):
        return True if "drink" in self.category else False
    def is_cheap(self,limit):
        return True if self.price<limit else False
espresso = MenuItem("Espresso", 3.5, "hot drink")        
muffin = MenuItem("Muffin", 2.0, "food")
print(espresso.is_drink())
print(espresso.is_cheap(3.0))
print(muffin.is_drink())
print(muffin.is_cheap(3.0))









            
              







        






        
        




