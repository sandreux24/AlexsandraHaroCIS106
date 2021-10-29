print("Enter principal amount: $")
principalamount = float(input())
print("Enter years to mature: ")
years = float(input())
if principalamount > 100000 and years == 5:
    rate = 0.06
else:
    if principalamount > 50000 and principalamount < 100000 and years == 10:
        rate = 0.05
    else:
        if principalamount > 50000 and principalamount < 100000 and years == 5:
            rate = 0.04
        else:
            rate = 0.02
percent = rate * 100
firstyear = principalamount * rate
print("Principal amount: $" + str(principalamount))
print("Interest rate:  %" + str(percent))
print("Interest amount for first year: $" + str(firstyear))
