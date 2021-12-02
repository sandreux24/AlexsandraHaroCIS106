print("Would you like to continue? (Yes or No)")
response = input()
while response == "Yes":
    print("Please enter last name: ")
    lastname = input()
    print("Please enter miles from downtown Chicago: ")
    miles = float(input())
    if miles >= 30:
        ticket = 12
    else:
        if miles >= 20 and miles <= 29:
            ticket = 10
        else:
            if miles >= 10 and miles <= 19:
                ticket = 8
            else:
                if miles < 10:
                    ticket = 5
    print("How many tickets?")
    howmany = float(input())
    sum = ticket * howmany
    print("This is the rate of one ticket: " + str(ticket))
    print("Amount due: " + str(sum))
    print("Would you like to continue?(Yes or No)")
    response = input()
