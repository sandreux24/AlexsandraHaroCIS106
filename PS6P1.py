print("Do you want to calculate interest? (Yes or No)")
response = input()
while response == "Yes":
    print("Enter amount to invest: ")
    principal = float(input())
    print("Enter interest rate: ")
    intrate = float(input())
    totalint = 0.0
    print("Year-" + "Principal-" + "EndingBal.")
    for year in range(1, 5 + 1, 1):
        intamount = principal * intrate
        endingbalance = principal + intamount
        print(str(year) + "   " + str(principal) + "    " + str(endingbalance))
        totalint = totalint + intamount
        principal = endingbalance
    print("Total interest earned: " + str(totalint))
    print("Do you want to do another calculation? (Yes or No)")
    response = input()
