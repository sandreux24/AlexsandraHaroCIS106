totalstudents = 0
print("Do you want to continue? (Yes or No)")
response = input()
while response == "Yes":
    print("Please enter last name: ")
    lastname = input()
    print("Enter exam score 1: ")
    exam1 = float(input())
    print("Enter exam score 2: ")
    exam2 = float(input())
    average = (exam1 + exam2) / 2
    totalstudents = totalstudents + 1
    print("Last Name: " + lastname)
    print("Average score: " + str(average))
    print("Do you want to continue? (Yes or No)")
    response = input()
print("Total number of students: " + str(totalstudents))
