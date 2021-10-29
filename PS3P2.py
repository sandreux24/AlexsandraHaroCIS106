def iTEM(a, b):
    
    return iTEM

# Main
itemA = "A"
itemB = "B"
unitPriceA = 10
unitPriceB = 20
print("Enter Quantity Ordered: ")
quantity = int(input())
print("What is the price per unit: ")
priceperUnit = int(input())
if priceperUnit == 10:
    extentedPrice = unitPriceA * quantity
    print("Item choosen: " + itemA)
else:
    extentedPrice = unitPriceB * quantity
    print("Item choosen: " + itemB)
print("Extented Price:  $" + str(extentedPrice))
