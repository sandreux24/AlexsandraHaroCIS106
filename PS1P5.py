print("Please enter the amount of the purchased item: ")
purchase = float(input())
tax = purchase * 0.07
total = purchase + tax
print("The purchase amount: " + str(purchase))
print("Tax: " + str(tax))
print("Total due: " + str(total))
