print("Enter quantity of widgets: ")
quantity = float(input())
if quantity > 10000:
    price = 10
else:
    if quantity > 5000 and quantity < 10000:
        price = 20
    else:
        if quantity < 5000:
            price = 30
exprice = quantity * price
tax = exprice * 0.07
total = exprice + tax
print("Extended price: " + str(exprice))
print("Price per unit: " + str(price))
print("Tax: " + str(tax))
print("Total: " + str(total))
