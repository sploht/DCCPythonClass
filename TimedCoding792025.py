print("Boudreaux & Thibodeaux's Po-Boy Shop")
print("------------------------------------")

itemSelected = 0
menu = {"1. Catfish Poboy: $": 14.95,
        "2. Roast Beef Poboy: $": 13.95,
        "3. Sausage Poboy: $": 12.95,
        "4. Gumbo: $": 4.95}

for key in menu.keys():
    print(key, menu[key])

print("------------------------------------")

print("What would you like to order?  Type the appropriate nummber of the menu item: ")
itemSelected = input()

while int(itemSelected) < 1 or int(itemSelected) > 4:
    print("That choice is not permitted. Please try again.")
    print("What would you like to order?  Type the appropriate nummber of the menu item: ")
    itemSelected = input()
    

for key in menu.keys():
    if itemSelected == key[0]:
        purchasePrice = menu[key]

salesTotal = purchasePrice * 1.0945
print("Your total is $ {:.2f}".format(salesTotal))
