print("Enter last name: ")
lastname = input()
print("Enter number of dependents: ")
numberofdependents = float(input())
print("Enter gross income: $")
grossincome = float(input())
dependents = numberofdependents * 12000
adjustedgrossincome = grossincome - dependents
if adjustedgrossincome > 50000:
    overtaxrate = adjustedgrossincome * 0.2
    if overtaxrate < 0:
        incometaxrate = 100
        print("Last name: " + lastname)
        print("Gross income: $" + str(grossincome))
        print("Number of dependents: " + str(numberofdependents))
        print("Adjusted gross income: $" + str(adjustedgrossincome))
        print("Income tax: $" + str(incometaxrate))
    else:
        print("Last name: " + lastname)
        print("Gross income: $" + str(grossincome))
        print("Number of dependents: " + str(numberofdependents))
        print("Adjusted gross income: $" + str(adjustedgrossincome))
        print("Income tax: $" + str(overtaxrate))
else:
    undertaxrate = adjustedgrossincome * 0.1
    if undertaxrate < 0:
        incometaxrate = 100
        print("Last name: " + lastname)
        print("Gross income: $" + str(grossincome))
        print("Number of dependents: " + str(numberofdependents))
        print("Adjusted gross income: $" + str(adjustedgrossincome))
        print("Income tax: $" + str(incometaxrate))
    else:
        print("Last name: " + lastname)
        print("Gross income: $" + str(grossincome))
        print("Number of dependents: " + str(numberofdependents))
        print("Adjusted gross income: $" + str(adjustedgrossincome))
        print("Income tax: $" + str(undertaxrate))
