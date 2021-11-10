def gross():
    rate()
    grosspay = rate * hoursworked
    
    return grosspay

def rate():
    print("Enter job code: ")
    code = input()
    if code == "L":
        rate = 25
    else:
        if code == "A":
            rate = 30
        else:
            if code == "J":
                rate = 50
    
    return rate

# Main
print("Enter last name: ")
lastname = input()
print("Enter hours worked: ")
hoursworked = float(input())
if hoursworked > 40:
    hoursworked = (hoursworked - 40) * 1.5 + 40
else:
    hoursworked = hoursworked
print("Enter job code: ")
code = input()
if code == "L":
    ratepay = 25
else:
    if code == "A":
        ratepay = 30
    else:
        if code == "J":
            ratepay = 50
grosspay = ratepay * hoursworked
print("Last name:" + lastname)
print("Gross pay:$ " + str(grosspay))
