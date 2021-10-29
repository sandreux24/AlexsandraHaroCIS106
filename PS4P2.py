print("Enter part number")
partno = int(input())
print("Enter quantity")
quantity = float(input())
if partno == 10 or partno == 55:
    unitprice = 1.0
else:
    if partno == 99:
        unitprice = 2.0
    else:
        if partno == 80 or partno == 70:
            unitprice = 3.0
        else:
            unitprice = 5.0
total = unitprice * quantity
print("Part number: " + str(partno))
print("Quantity: " + str(quantity))
print("Price per Unit: " + str(unitprice))
print("Total price: " + str(total))
