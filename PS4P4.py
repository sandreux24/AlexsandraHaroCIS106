print("Enter amount of ticket: ")
quantity = float(input())
if quantity >= 25:
    price = 50
else:
    if quantity > 10 and quantity < 24:
        price = 60
    else:
        if quantity > 5 and quantity < 9:
            price = 70
        else:
            price = 75
total = quantity * price
print("Number of Tickets: " + str(quantity))
print("Price per ticket: $" + str(price))
print("Total cost: $" + str(total))
