print("Enter quantity")
quantity = float(input())
print("Enter price per unit")
price = float(input())
total = quantity * price
tax = total * 0.07
finaltotal = tax + total
print("Total: " + str(total))
print("Tax: " + str(tax))
print("Final Total: " + str(finaltotal))
