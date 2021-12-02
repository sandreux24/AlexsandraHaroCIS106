print("Enter last name:")
lastname = input()
print("Enter sales:")
sales = float(input())
if sales > 100000:
    commissionrate = 0.1
else:
    commissionrate = 0.05
commission = commissionrate * sales
target = sales * 0.05 + sales
print("Last name: " + lastname)
print("Commission amount: " + str(commission))
print("Next years target sales: " + str(target))
