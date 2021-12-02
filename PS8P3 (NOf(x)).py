print("Would you like to continue? (Yes or No)")
response = input()
while response == "Yes":
    print("Enter make of car")
    make = input()
    if make == "Honda":
        print("is it a Honda Accord? (Y or N)")
        response = input()
        if response == "Y":
            print("is car electric? (Y or N)")
            response = input()
            if response == "Y":
                rateoff = 0.04
            else:
                rateoff = 0.001
        else:
            print("is car electric? (Y or N)")
            response = input()
            if response == "Y":
                rateoff = 0.003
            else:
                rateoff = 0.0005
    else:
        if make == "Toyota":
            print("Is it a Toyota Rav4? (Y or N)")
            response = input()
            if response == "Y":
                print("is car electric? (Y or N)")
                response = input()
                if response == "Y":
                    rateoff = 0.045
                else:
                    rateoff = 0.015
            else:
                print("is car electric? (Y or N)")
                response = input()
                if response == "Y":
                    rateoff = 0.003
                else:
                    rateoff = 0.0005
        else:
            print("is car electric? (Y or N)")
            response = input()
            if response == "Y":
                rateoff = 0.003
            else:
                rateoff = 0.0005
    print("enter msrp:")
    msrp = float(input())
    newmsrp = msrp * rateoff
    outthedoormsrp = msrp - newmsrp
    total = outthedoormsrp * 0.07 + outthedoormsrp
    print("total: " + str(total))
