print("Enter name of appliance: ")
nameofappliance = input()
print("Enter the cost of the appliance: $")
costofappliance = float(input())
if costofappliance > 1000:
    over1000 = costofappliance * 0.1
    totalover1000 = costofappliance + over1000
    print("Name of appliance: " + nameofappliance)
    print("Cost of appliance: $" + str(costofappliance))
    print("Cost of warrantee: $" + str(over1000))
    print("Total amount due: $" + str(totalover1000))
else:
    under1000 = costofappliance * 0.05
    totalunder1000 = costofappliance + under1000
    print("Name of appliance: " + nameofappliance)
    print("Cost of appliance: $" + str(costofappliance))
    print("Cost of warrantee: $" + str(under1000))
    print("Total amount due: $" + str(totalunder1000))
