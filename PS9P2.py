print("Enter last name:")
lastname = input()
print("Enter exam 1 total points")
exam1 = float(input())
print("Enter exam 2 total points")
exam2 = float(input())
print("Enter exam 3 total points")
exam3 = float(input())
totalpoints = exam1 + exam2 + exam3
average = totalpoints / 300
percent = average * 100
print("Last name: " + lastname)
print("Total points: " + str(totalpoints))
print("Average exam score:% " + str(percent))
