print("enter name:")
name = input()
print("enter amount of credits: ")
credits = float(input())
print("enter district code:")
districtcode = input()
if districtcode == "I":
    percredit = 250
else:
    percredit = 550
tuition = credits * percredit
print("Students name: " + name)
print("Tuition owed: " + str(tuition))
