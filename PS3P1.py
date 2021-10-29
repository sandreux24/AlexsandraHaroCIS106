def computeExtentedPrice(unitPrice, quantity):
    extentedPrice = quantity * unitPrice
    
    return extentedPrice

def computeExtentedPrice2(quantity, unitPrice):
    extentedPrice = quantity * unitPrice
    
    return extentedPrice

# Main
print("Enter Quantity ordered ")
quantity = float(input())
print(" Enter Unit Price")
unitPrice = float(input())
extentedPrice = quantity * unitPrice
tax = extentedPrice * 0.07
if extentedPrice > 100:
    shipping = 0.0
else:
    shipping = extentedPrice * 0.1
total = extentedPrice + shipping + tax
print("ExQuantity Ordered:    " + str(quantity))
print("Unit Price:   $" + str(unitPrice))
print("Extented Price:    $" + str(extentedPrice))
print("Tax Amount:    $" + str(tax))
print("Shipping:   $" + str(shipping))
print("Total Orderd:   &" + str(total))
