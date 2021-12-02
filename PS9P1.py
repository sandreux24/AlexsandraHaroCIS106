print("Enter price")
price = float(input())
print("Enter quantity")
quantity = float(input())
print("Enter discount rate: %")
discountrate = float(input())
sum = price * quantity
rate = discountrate / 100
discountedamount = sum * rate
discountedprice = sum - discountedamount
print("Quantity: " + str(quantity))
print("Price per unit: " + str(price))
print("Amount due before discount:$ " + str(sum))
print("Discounted amount:$ " + str(discountedamount))
print("Final amount:$ " + str(discountedprice))
