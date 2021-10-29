print("Please enter last name: ")
lastname = input()
print("Please enter salary: ")
salary = float(input())
print("Please enter job level: ")
joblevel = float(input())
if joblevel >= 10:
    bonus = 0.25
else:
    if joblevel > 5 and 9 > joblevel:
        bonus = 0.2
    else:
        bonus = 0.1
total = salary * bonus
print("Last name: " + lastname)
print("Bonus: " + str(total))
