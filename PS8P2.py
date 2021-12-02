def area(height, length, width):
    area = 2 * length * width + 2 * length * height + 2 * width * height
    
    return area

# Main
print("would you like to continue? (Yes or No)")
response = input()
while response == "Yes":
    print("Enter width of room")
    width = float(input())
    print("Enter length of room")
    length = float(input())
    print("Enter height of room")
    height = float(input())
    area(height, length, width)
    squarefoot = area(height, length, width)
    gallons = squarefoot / 50
    print("Gallons of paint needed: " + str(gallons))
    print("would you like to continue?")
    response = input()
