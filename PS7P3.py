def cost(gallons, unit):
    unit = 2.5
    cost = gallons * unit
    
    return cost

def milespergallon(miles, gallon):
    milespergallon = miles / gallon
    
    return milespergallon

# Main
unit = 2.5
print("Enter Destination: ")
city = input()
print("Enter miles travelled: ")
miles = float(input())
print("Enter gallons used: ")
gallons = float(input())
milespergallon(miles, gallons)
cost(gallons, unit)
print("Destination: " + city)
print("Miles travelled: " + str(miles))
print("Cost of gas: $" + str(cost))
