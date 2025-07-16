
def main():
    
    menuChoice = 0
    qtyOrdered = 0
    runningTotal = 0

    while(str(menuChoice) != "DONE"):
        print("\nWhat would you like to order? \nType the appropriate number of the menu item or DONE when order is complete:")
        menuChoice = input()
        if(str(menuChoice)) == "DONE":
            computeOrderTotal(runningTotal)
        elif(int(menuChoice) < 1 or int(menuChoice) > 4):
             print("\nI'm sorry.  That is not an appropriate response.")
        else:
            print("How many of that item would you like to order?")
            qtyOrdered = input()
            while(int(qtyOrdered) < 1):
                print("\nYou cannot order fewer than 1 of this item.  Please enter a new quantity.")
                print("How many of that item would you like to order?")
                qtyOrdered = input()
            print("You have ordered", qtyOrdered, getItems(int(menuChoice)),"(s) for $", getPrices(int(menuChoice)), "each.")
            runningTotal += (float(qtyOrdered) * getPrices(int(menuChoice)))
            #print("The running total for your order is:", runningTotal)

def getPrices(itemSelected):
    itemPrices = (5.95, 4.95, 3.95, 3.75)
    return itemPrices[itemSelected-1]

def getItems(itemSelected):
    itemList = ("Muffin", "King Cake Slice", "Croissant", "Scone")
    return itemList[itemSelected-1]

def computeOrderTotal(orderTotal):
        salesTax = orderTotal*.095
        totalWithTax = orderTotal+salesTax
        print("\n------------------------------")
        print("Your total is ${:.2f}".format(totalWithTax))


print("Boudreaux & Thibodeaux's Bakery")
print("------------------------------")
print("1. Muffin: $5.95")
print("2. King Cake Slice: $4.95")
print("3. Croissant: $3.95")
print("4. Scone: $3.75")
print("------------------------------")


main()
