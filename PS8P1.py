def percent(month, rate):
    month = rate
    if month == "Jan":
        rate = 0.1
    else:
        if month == "Feb":
            rate = 0.1
        else:
            if month == "Mar":
                rate = 0.1
            else:
                if month == "Apr":
                    rate = 0.15
                else:
                    if month == "May":
                        rate = 0.15
                    else:
                        if month == "Jun":
                            rate = 0.15
                        else:
                            if month == "Jul":
                                rate = 0.2
                            else:
                                if month == "Aug":
                                    rate = 0.2
                                else:
                                    if month == "Sep":
                                        rate = 0.2
                                    else:
                                        if month == "Oct":
                                            rate = 0.25
                                        else:
                                            if month == "Nov":
                                                rate = 0.25
                                            else:
                                                if month == "Dec":
                                                    rate = 0.25
    
    return rate

# Main
print("Enter last name:")
lastname = input()
print("enter month")
month = input()
percent(month, rate)
rate = percent(month, rate)
print("enter sales:")
sales = float(input())
forecast = sales * (1 + rate)
print("Next months forecast: " + str(forecast))
