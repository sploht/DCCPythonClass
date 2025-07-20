
def main():
    menuChoice = 0
    qtyOrdered = 0
    runningTotal = 0
    singleCakeSlices = 0
    wholeCakes = 0

    while(str(menuChoice) != "DONE"):
        repeatMenu()
        print("\nWhat would you like to order? Type the appropriate number of the menu item or DONE when order is complete:")
        menuChoice = input()
        if(str(menuChoice)) == "DONE":
            computeOrderTotal(runningTotal)
        elif(int(menuChoice) < 1 or int(menuChoice) > 7):
             print("\nI'm sorry.  That is not an appropriate response.")
        else:
            print("Quantity")
            qtyOrdered = input()
            if int(menuChoice) == 3:
                if (int(qtyOrdered) >= 8 and int(qtyOrdered)%8 != 0):
                    singleCakeSlices = int(qtyOrdered)%8
                    print("\nItem Added:", int(qtyOrdered)%8, "X Crawfish Pie Slice(s) - ${:.2f}".format(float(3.65 * singleCakeSlices)))  
                elif int(qtyOrdered) < 8:
                    singleCakeSlices = int(qtyOrdered)
                    print("\nItem Added:", int(qtyOrdered), "X Crawfish Pie Slice(s) - ${:.2f}".format(singleCakeSlices*getPrices(int(menuChoice))))
                if int(qtyOrdered) > 7 or int(qtyOrdered)%8 == 0:
                    wholeCakes = int(qtyOrdered)//8    
                    print("Item Added:", int(qtyOrdered)//8, "X Whole Crawfish Pie(s) - ${:.2f}".format(22*wholeCakes))
               
            while(int(qtyOrdered) < 1):
                print("\nYou cannot order fewer than 1 of this item.  Please enter a new quantity.")
                print("How many of that item would you like to order?")
                qtyOrdered = input()
            if int(menuChoice) != 3: 
                print("\nItem Added:", qtyOrdered, "X", getItems(int(menuChoice)),"(s) - $", getPrices(int(menuChoice)), "each")
            if int(menuChoice) != 3:
                runningTotal += (float(qtyOrdered) * getPrices(int(menuChoice)))
            if int(menuChoice) == 3:
                runningTotal+= float(singleCakeSlices*3.65) + float(wholeCakes*22)

def getPrices(itemSelected):
    itemPrices = (3.95, 4.95, 3.65, 14.95, 13.95, 12.95, 5.95)
    return itemPrices[itemSelected-1]

def getItems(itemSelected):
    itemList = ("Croissant", "King Cake Slice", "Crawfish Pie (by the Slice)", "Catfish Poboy", "Roast Beef Poboy", "Sausage Poboy", "Gumbo")
    return itemList[itemSelected-1]

def computeOrderTotal(orderTotal):
        salesTax = orderTotal*.095
        totalWithTax = orderTotal+salesTax
        print("\n------------------------------")
        print("Your total is ${:.2f}".format(totalWithTax))

def repeatMenu():
    print("\nBoudreaux & Thibodeaux's Restaurant")
    print("------------------------------")
    print("1. Croissant: $3.95")
    print("2. King Cake Slice: $4.95")
    print("3. Crawfish Piece (by the Slice): $3.65")
    print("4. Catfish Poboy: $14.95")
    print("5. Roast Beef Poboy: $13.95")
    print("6. Sausage Poboy: $12.95")
    print("7. Gumbo: $5.95")
    print("------------------------------")


main()