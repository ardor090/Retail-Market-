# 1.	An inbuilt function for admin to change the price of any of the item.
# 2.	An inbuilt function for admins to add more items.
# 3.	An inbuilt function to compute goods purchased per customer and displays a receipt for printing.
#     a.	The function must be able to add 20% VAT for customers buying less than 5 items.
#     b.	30% VAT for customers buying more than 10 items.
#     c.	N800 bonus goods for customers purchasing more than 10 items with the least amount being N100.
# 4.	An inbuilt function that updates stock after an item has been purchased.
# 5.	An inbuilt function that takes record of total gain per day.


# Admin
# Create a main menu
data = open("Stock.txt", "r")
items = data.readlines()
store = []
for product in items:
    store.append(product.strip().split(","))

IDs = [x for x in range(len(items))]
items = [(item[1]).lower() for item in store]
quantities = [int(item[2]) for item in store]
prices = [float(item[3]) for item in store]
data.close()

basket = []
quans = []
total = []

def mainMenu():
    while True:
        print('''''
        -----------------------------
        Welcome to Adamu Retail Shop
        -----------------------------


        #### SHOPPING LIST ####

        1. Admin
        2. User
        3. Exit

        ''')
        #   Ask the Admin to make a selection
        selection = input("Please make your selection (Type 'quit' to end): ").lower()

        if selection == "1":
            admin()
        elif selection == "2":
            user()
        elif selection == "3":
            break
        elif selection == "quit":
            break
    else:
        print("You've entered a wrong selection")


def admin():

    while True:
        print('''''
        -----------------------------
        Welcome to Adamu Retail Shop
        -----------------------------


        #### SHOPPING LIST ####

        1. View shopping list
        2. Add item to shopping list
        3. Change item in shopping list
        4. Remove item from shopping list
        5. Check if item is in shopping list
        6. How many items on shopping list

        ''')
       # Ask the Admin to make a selection
        selection = input("Please make your selection (Type 'quit' to end): ").lower()


        if selection == "1":
            displayList()
        elif selection == "2":
            addItem()
        elif selection == "3":
            changeQuantity(1, 200)
        elif selection == "4":
            removeItem()
        elif selection == "5":
            update()
        elif selection == "6":
            checkItem()
        elif selection == "7":
            listLength()
        elif selection == "quit":
            break
    else:
        print("You've entered a wrong selection")

def user():

    while True:
        print('''''
        -----------------------------
        Welcome to Adamu Retail Shop
        -----------------------------


        #### SHOPPING LIST ####

        1. View shopping list
        2. Add item to cart
        3. Remove item from cart

        ''')
#   Ask the Admin to make a selection
        selection = input("Please make your selection (Type 'quit' to end): ").lower()

        if selection == "1":
            displayList()
        elif selection == "2":
            display_cart()
        # elif selection == "3":
        #     add_all_items(item_quant)
        elif selection == "quit":
            break
    else:
        print("You've entered a wrong selection")

# Displays all items in the item list
def displayList():
    for id, item, quantity, price in zip(IDs, items, quantities, prices):
        print("{:^10}{:<30}{:^10}{:>10}".format(id, item, quantity, price))

# Adds a new item with corresponding quantity and price to the item list
def addItem():

    newItem = input("Please Enter the item you wish to add: ")
    items.append(newItem)
    newQuantity = int(input("Please Enter the quantity of the item you added: "))
    quantities.append(newQuantity)
    newPrice = float(input("Please Enter the price of the item you added: "))
    prices.append(newPrice)
    print("item added successfully")

# Removes an item from the item list
def removeItem():
    user = int(input("enter Id of the item you'll like to remove: "))
    if user in IDs:
        item = items.pop(user)
        print("{} has been removed from list ".format(item))


# Checks if an item exists in the item list
def checkItem():
    itemCheck = input("what item would you like to check: ")
    if itemCheck in items:
        print("Yes," + itemCheck + " Item is on the item list")
    else:
        print("No, " + itemCheck + " on the item list")

# Checks if an item exists in the item list
def changeQuantity(id, new_quantity):
    if id in range(len(quantities)):
        quantities[id] = new_quantity
        print('%s quantity is changed to % d' % (items[id], new_quantity))
    else:
        print('No item with such Id')

    ids = input("what is the ID of the item you wish to change: ")
    quantity = input("what is the quantity of the item you wish to change: ")

# Shows the number of items in the item list
def listLength():
    print("There are", len(items), "items on the item list")

# Users
def display_cart():
    print('Hello Sir/Ma here is your basket please supply items to be added')
    basket.clear()
    quans.clear()
    done = 'no'
    while done == 'no':
        try:
            id = int(input('Enter item id: '))
            if id in range(len(items)):
                basket.append(id)
                quans.append(int(input('Enter the quantity u wish to buy: ')))
                print('perfect %s is added to your basket' %items[id])
            else:
                print('sorry no item with such id')
        except ValueError:
            print('Sorry IDs can only be numbers')
        finally:
            done = input('Are you done selecting items? (no to select again): ').lower()
    print('alright sir here are the items you selected with their prices\n')
    for i,it,p in zip(basket,map(items.__getitem__,basket),map(prices.__getitem__,basket)):
        print('{:<2d}{:<15}{:>4}'.format(i,it,p))
    #unit prices
    t_prices = list(map(prices.__getitem__, basket))
    #change unit to amount
    for i in range(len(t_prices)):
            t_prices[i] *= quans[i]
    vat = 0.0
    bonus = 0.0
    if sum(quans) < 5:
        vat = 0.2 * sum(t_prices)
    elif sum(quans)> 10:
        vat = 0.3* sum(t_prices)
        if min(t_prices) >= 100:
            bonus = 800.0
    print('your VAT is: #%.1f' %vat)
    print('your bonus is: #%.1f' %bonus)
    print('your total cost is: #%.1f' %(sum(t_prices) + vat - bonus))
    for I, q in zip(basket, quans):
        quantities[I] -= q
        update()

def update():
    sn = ''
    for i,q,p in zip(items,quantities,prices):
        sn += ','.join((i,str(q),str(p))) + '\n'
    with open('store.csv','w') as f:
        f.write(sn)
    f.close()


mainMenu()
