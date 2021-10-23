print("Enter the price of the item: ")
price = float(input())
print("Enter the percent discounted: ")
discount = float(input())
percent = discount / 100
discamount = price * percent
discprice = price - discamount
print("Discount amount: " + str(discamount))
print("Discounted price: " + str(discprice))
