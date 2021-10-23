discsum = 0
print("Do you want to continue (Yes or No)")
response = input()
while response == "Yes":
    print("Please enter quantity")
    quantity = float(input())
    print("Please enter price")
    price = float(input())
    extprice = quantity * price
    if extprice > 10000.0:
        discount = extprice * 0.25
    else:
        discount = extprice * 0.1
    total = extprice - discount
    discsum = discsum + discount
    print("Extented price: " + str(extprice))
    print("Discount amount: " + str(discount))
    print("Total: " + str(total))
    print("Do you want to continue? (Yes or No)")
    response = input()
print("Total discounts given: " + str(discsum))
