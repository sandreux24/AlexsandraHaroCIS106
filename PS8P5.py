print("Woud you like to continue? (Yes or No)")
response = input()
while response == "Yes":
    print("Enter county:")
    county = input()
    if county == "Cook":
        percent = 0.009
    else:
        if county == "DuPage":
            percent = 0.008
        else:
            if county == "McHenry":
                percent = 0.0075
            else:
                if county == "Kane":
                    percent = 0.006
                else:
                    percent = 0.007
    print("Please enter the value of the home: ")
    valueofhome = float(input())
    sum = percent * valueofhome + valueofhome
    notdecimal = percent * 100
    print("Market value of the home:$ " + str(valueofhome))
    print("Percent qualified for:% " + str(notdecimal))
    print("Final price: " + str(sum))
    print("Would you like to contiue? (Yes or No) ")
    response = input()
