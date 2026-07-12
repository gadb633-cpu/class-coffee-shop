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

# Extra 2. Loyalty Points
class Customer:
    def __init__(self,name, balance):
        self.name =name
        self.balance = balance
        self.points = 0
    def purchase(self,item_name, price):    
        if self.balance > price:
            self.points += 10 
            self.balance -= price
        else:
            print(f"Not enough balance for {item_name}.")
    def redeem(self):
        if self.points>=50:
            self.balance += 5.0
            self.points = 0 
    def status(self):
        print(f"Name: {self.name} | Balance: ${self.balance} | Points: {self.points}")       
noa = Customer("Noa", 15.0)
noa.purchase("coffee",10) 
noa.redeem()
noa.status()
print(noa.balance)

# Extra 3. Timed Order
class Order:
    def __init__(self,customer_name, items):
        self.customer_name=customer_name
        self.items = items
    def total_prep_time(self):
        self.sum =0
        for self.item in self.items:
            self.sum += self.item[1]
        return self.sum
    def ready_by(self,minutes):
        return True if self.total_prep_time()<=minutes else False
    def print_order(self):
        for self.item in self.items:
            print(self.item)
    def slowest_item(self):
        self.longest = ("",0)
        for self.item in self.items:
            if self.item[1] > self.longest[1]:
                self.longest = self.item
        return f"slowest is: {self.longest[0]}"
moshe = Order("Moshe", [("Latte", 3), ("Sandwich", 7), ("Smoothie", 5)])
print(f"total prep: {moshe.total_prep_time()}")
print(moshe.ready_by(10))
print(moshe.ready_by(20))
moshe.print_order()
print(moshe.slowest_item())

# Extra 4. Daily Revenue Tracker
class CoffeeShop:
    def __init__(self,name):
        self.name =name
        self.revenue = 0.0
    def sell(self,item_name, price):
        self.revenue += price
        print(f"{item_name} added to revenue ")
    def sell_discounted(self,item_name, price, discount):
        self.revenue += price*(1-discount)
        
    def daily_summary(self):
        print(f"{self.name} | Daily revenue: ${self.revenue:.2f}")
the_bean = CoffeeShop("The Bean")
the_bean.sell("cofffee",15)
the_bean.sell_discounted("cofffee",15,3)
the_bean.sell("capuchino",20)
the_bean.sell_discounted("capuchino",20,5)
the_bean.sell("latte",25)
the_bean.daily_summary()

# Extra 5. Size-Based Drink Pricing
class Drink:
    def __init__(self,name, base_price, size):
        self.name =name
        self.base_price = base_price
        self.size = size
    def final_price(self):
        if self.size == "small":
            self.price=self.base_price
            return self.price
        if self.size == "medium":
            self.price=self.base_price*1.3
            return self.price
        if self.size == "large":
            self.price=self.base_price*1.6
            return self.price
    def describe(self):
        print(f"{self.name} ({self.size}) → ${self.final_price():.2f}")
latte = Drink("Latte", 3.0, "small")
latte.describe()
latte = Drink("Latte", 3.0, "medium")
latte.describe()
latte = Drink("Latte", 3.0, "large")
latte.describe()

# Extra 6. Shift Planning
class Shift:
    def __init__(self,barista_name, start_hour, end_hour, drinks_target):
        self.barista_name = barista_name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.drinks_target =drinks_target
    def duration(self):
        return self.end_hour - self.start_hour
    def drinks_per_hour(self):
       return self.drinks_target // self.duration() 
    def is_long_shift(self):
        return True if self.duration() >6 else False
    def describe(self):
        print(f"Barista: {self.barista_name} | Hours: {self.duration()} | Target: {self.drinks_target} | Per hour: {self.drinks_per_hour()} | Long shift: {self.is_long_shift()}")
lior = Shift("Lior", 8, 16, 120)
lior.describe()

# Extra 7. Happy Hour Promotion
class MenuItem:
    def __init__(self,name,price):
        self.name =name
        self.price = price
class HappyHour:
    def __init__(self,start_hour, end_hour, discount_percent):
        self.start_hour =start_hour
        self.end_hour =end_hour
        self.discount_percent =discount_percent
    def is_active(self,current_hour):
        return True if self.start_hour<=current_hour<self.end_hour else False
    def discounted_price(self,item):
        return item*(1-self.discount_percent/100)
    
beer = MenuItem("Beer", 20.0)
discount = HappyHour(16, 18, 20)
print(discount.is_active(17))
print(discount.discounted_price(beer.price))
print(discount.is_active(20))

# Extra 8. Combo Deal
class MenuItem:
    def __init__(self,name, price):
        self.name = name
        self.price =price
class Combo:
    def __init__(self,name, items, discount):
        self.name =name
        self.items =items
        self.discount = discount
    def original_price(self):
        self.sum =0
        for self.item in self.items:
            self.sum += self.item.price
        return self.sum 
    def combo_price(self):
        return self.original_price()*(1-self.discount)
    def savings(self):
        return self.original_price()-self.combo_price()
    def describe(self):
        print(f"{self.name} | Original: ${self.original_price()} | Combo: ${self.combo_price()} | Savings: ${self.savings()}")

breakfast = Combo("Breakfast", [MenuItem("Espresso", 3.5), MenuItem("Croissant", 2.5)], 0.1)                     
breakfast.describe()

# Extra 9. Menu Search and Stats
class MenuItem:
    def __init__(self,name, price, category):
        self.name =name
        self.price =price
        self.category =category
class Menu:
    def __init__(self):
        self.items = []
    def add_item(self,item):
        self.items.append(item)
    def find_by_name(self,name):
        for self.item in self.items:
            if name == self.item.name:
                return name
        else:
            return
    def filter_by_category(self,category):
        self.list_of_cate = [] 
        for self.item in self.items:
            if category ==self.item.category:
                self.list_of_cate.append(category)
        return self.list_of_cate
    def cheapest(self):
        self.item_cheapest = self.items[0].price
        for self.item in self.items:
            if self.item.price< self.item_cheapest:
                self.item_cheapest = self.item.price
        return self.item_cheapest        
    def most_expensive(self):
        self.item_expensive = 0
        for self.item in self.items:
            if self.item.price> self.item_expensive:
                self.item_expensive = self.item.price
        return self.item_expensive        
    def average_price(self):
        self.item_avg = 0
        for self.item in self.items:
            self.item_avg += self.item.price
        return self.item_avg / len(self.items)
breakfast = Menu()    
breakfast.add_item(MenuItem("Espresso", 3.5,"drinks"))        
breakfast.add_item(MenuItem("Croissant", 9.5,"maffin"))
breakfast.add_item(MenuItem("coffee", 5.5,"drinks"))
breakfast.add_item(MenuItem("capuchino", 6.5,"drinks"))
breakfast.add_item(MenuItem("burecas", 11.5,"maffin"))
print(breakfast.find_by_name("Espresso"))
print(breakfast.filter_by_category("drinks"))
print(breakfast.cheapest())
print(breakfast.most_expensive())
print(breakfast.average_price())




            



















            
              







        






        
        




