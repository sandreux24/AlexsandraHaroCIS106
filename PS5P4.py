sum = 0
numberofemployee = 0
print("Do you want to continue? (Yes or No)")
response = input()
while response == "Yes":
    print("Employee Last Name: ")
    lastname = input()
    print("Hours worked: ")
    hoursworked = float(input())
    print("Rate of pay: ")
    rate = float(input())
    if hoursworked > 40:
        ot = (hoursworked - 40) * (rate / 2)
    else:
        ot = 0
    grosspay = hoursworked * rate + ot
    numberofemployee = numberofemployee + 1
    print("Employee last name: " + lastname)
    print("Gross Pay: " + str(grosspay))
    print("Do you want to continue? (Yes or No)")
    sum = sum + grosspay
    response = input()
print("Sum: " + str(sum))
averagepay = sum / numberofemployee
print("Average pay: " + str(averagepay))
print("Number of Employess: " + str(numberofemployee))
